# Copyright 2022-2023 Lawrence Livermore National Security, LLC and other
# This is part of Flux Framework. See the COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
import shutil

import fluxcloud.utils as utils
from fluxcloud.logger import logger
from fluxcloud.main.decorator import save_meta, timed

here = os.path.dirname(os.path.abspath(__file__))


class ExperimentClient:
    """
    A base experiment client
    """

    def __init__(self, *args, **kwargs):
        import fluxcloud.main.settings as settings

        self.settings = settings.Settings
        self.times = {}

        # Job prefix is used for organizing time entries
        self.job_prefix = "minicluster-run"

    def __repr__(self):
        return str(self)

    @timed
    def run_timed(self, name, cmd, cleanup_func=None):
        """
        Run a timed command, and handle nonzero exit codes.
        """
        logger.debug("\nRunning Timed Command:" + " ".join(cmd))
        res = utils.run_command(cmd)

        # An optional cleanup function (also can run if not successful)
        if cleanup_func is not None:
            cleanup_func()

        if res.returncode != 0:
            raise ValueError("nonzero exit code, exiting.")

    def run_command(self, cmd, cleanup_func=None):
        """
        Run a timed command, and handle nonzero exit codes.
        """
        logger.debug("\nRunning Command:" + " ".join(cmd))
        res = utils.run_command(cmd)

        # An optional cleanup function (also can run if not successful)
        if cleanup_func is not None:
            cleanup_func()

        if res.returncode != 0:
            raise ValueError("nonzero exit code, exiting.")

    def __str__(self):
        return "[flux-cloud-client]"

    def get_script(self, name, cloud=None):
        """
        Get a named script from the cloud's script folder
        """
        cloud = cloud or self.name
        script = os.path.join(here, "clouds", cloud, "scripts", name)
        if os.path.exists(script):
            logger.debug(f"Found template script {script}")
            return script

    def get_shared_script(self, name):
        """
        Get a named shared script
        """
        return self.get_script(name, cloud="shared")

    def experiment_is_run(self, setup, experiment):
        """
        Determine if all jobs are already run in an experiment
        """
        # The experiment is defined by the machine type and size
        experiment_dir = setup.get_experiment_directory(experiment)
        minicluster = setup.get_minicluster(experiment)

        # One run per job (command)
        jobs = experiment.get("jobs", [])
        if not jobs:
            logger.warning(
                f"Experiment {experiment['id']} has no jobs, nothing to run."
            )
            return True

        # If all job output files exist, experiment is considered run
        for size in minicluster["size"]:

            # We can't run if the minicluster > the experiment size
            if size > experiment["size"]:
                logger.warning(
                    f"Cluster of size {experiment['size']} cannot handle a MiniCluster of size {size}, not considering."
                )
                continue

            # Jobname is used for output
            for jobname, job in jobs.items():

                # Do we want to run this job for this size and machine?
                if not self.check_job_run(job, size, experiment):
                    logger.debug(
                        f"Skipping job {jobname} as does not match inclusion criteria."
                    )
                    continue

                # Add the size
                jobname = f"{jobname}-minicluster-size-{size}"
                job_output = os.path.join(experiment_dir, jobname)
                logfile = os.path.join(job_output, "log.out")

                # Do we have output?
                if not os.path.exists(logfile):
                    return False
        return True

    @save_meta
    def run(self, setup):
        """
        Run Flux Operator experiments in GKE

        1. create the cluster
        2. run each command and save output
        3. bring down the cluster
        """
        # Each experiment has its own cluster size and machine type
        for experiment in setup.matrices:

            # Don't bring up a cluster if experiments already run!
            if not setup.force and self.experiment_is_run(setup, experiment):
                logger.info(
                    f"Experiment on machine {experiment['id']} was already run and force is False, skipping."
                )
                continue

            self.up(setup, experiment=experiment)
            self.apply(setup, experiment=experiment)
            self.down(setup, experiment=experiment)

    @save_meta
    def down(self, *args, **kwargs):
        """
        Destroy a cluster implemented by underlying cloud.
        """
        raise NotImplementedError

    def check_job_run(self, job, size, experiment):
        """
        Determine if a job is marked for a MiniCluster size.
        """
        if "sizes" in job and size not in job["sizes"]:
            return False
        if "size" in job and job["size"] != size:
            return False
        if (
            "machine" in job
            and "machine" in experiment
            and job["machine"] != experiment["machine"]
        ):
            return False
        if (
            "machines" in job
            and "machine" in experiment
            and experiment["machine"] not in job["machines"]
        ):
            return False
        return True

    @save_meta
    def apply(self, setup, experiment):
        """
        Apply a CRD to run the experiment and wait for output.

        This is really just running the setup!
        """
        # Here is where we need a template!
        if setup.template is None or not os.path.exists(setup.template):
            raise ValueError(
                "You cannot run experiments without a minicluster-template.yaml"
            )
        apply_script = self.get_shared_script("minicluster-run")

        jobs = experiment.get("jobs", [])

        # The MiniCluster can vary on size
        minicluster = setup.get_minicluster(experiment)
        if not jobs:
            logger.warning(f"Experiment {experiment} has no jobs, nothing to run.")
            return

        # The experiment is defined by the machine type and size
        experiment_dir = setup.get_experiment_directory(experiment)

        # Iterate through all the cluster sizes
        # NOTE if this changes here, also check self.experiment_is_run
        for size in minicluster["size"]:

            # We can't run if the minicluster > the experiment size
            if size > experiment["size"]:
                logger.warning(
                    f"Cluster of size {experiment['size']} cannot handle a MiniCluster of size {size}, skipping."
                )
                continue

            # Jobname is used for output
            for jobname, job in jobs.items():

                # Do we want to run this job for this size and machine?
                if not self.check_job_run(job, size, experiment):
                    logger.debug(
                        f"Skipping job {jobname} as does not match inclusion criteria."
                    )
                    continue

                # Add the size
                jobname = f"{jobname}-minicluster-size-{size}"
                job_output = os.path.join(experiment_dir, jobname)
                logfile = os.path.join(job_output, "log.out")

                # Any custom commands to run first?
                if hasattr(self, "pre_apply"):
                    self.pre_apply(experiment, jobname, job)

                # Do we have output?
                if os.path.exists(logfile) and not setup.force:
                    logger.warning(
                        f"{logfile} already exists and force is False, skipping."
                    )
                    continue
                elif os.path.exists(logfile) and setup.force:
                    logger.warning(f"Cleaning up previous run in {job_output}.")
                    shutil.rmtree(job_output)

                # Create job directory anew
                utils.mkdir_p(job_output)

                # Generate the populated crd from the template
                template = setup.generate_crd(experiment, job, size)

                # Write to a temporary file
                crd = utils.get_tmpfile(prefix="minicluster-", suffix=".yaml")
                utils.write_file(template, crd)

                # Apply the job, and save to output directory
                cmd = [
                    apply_script,
                    "--apply",
                    crd,
                    "--logfile",
                    logfile,
                    "--namespace",
                    minicluster["namespace"],
                    "--job",
                    minicluster["name"],
                ]
                self.run_timed(f"{self.job_prefix}-{jobname}", cmd)

                # Clean up temporary crd if we get here
                if os.path.exists(crd):
                    os.remove(crd)

    def save_experiment_metadata(self, setup, experiment):
        """
        Save experiment metadata, loading an existing meta.json, if present.
        """
        # The experiment is defined by the machine type and size
        experiment_dir = setup.get_experiment_directory(experiment)
        if not os.path.exists(experiment_dir):
            utils.mkdir_p(experiment_dir)
        meta_file = os.path.join(experiment_dir, "meta.json")

        # Load existing metadata, if we have it
        meta = {"times": self.times}
        if os.path.exists(meta_file):
            meta = utils.read_json(meta_file)

            # Don't update cluster-up/down if already here
            frozen_keys = ["create-cluster", "destroy-cluster"]
            for timekey, timevalue in self.times.items():
                if timekey in meta and timekey in frozen_keys:
                    continue
                meta["times"][timekey] = timevalue

        # TODO we could add cost estimation here - data from cloud select
        for key, value in experiment.items():
            meta[key] = value
        utils.write_json(meta, meta_file)
        self.clear_minicluster_times()
        return meta

    def clear_minicluster_times(self):
        """
        Update times to not include jobs
        """
        times = {}
        for key, value in self.times.items():

            # Don't add back a job that was already saved
            if key.startswith(self.job_prefix):
                continue
            times[key] = value
        self.times = times

    @save_meta
    def up(self, *args, **kwargs):
        """
        Bring up a cluster implemented by underlying cloud.
        """
        raise NotImplementedError
