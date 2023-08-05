# Copyright 2022 Lawrence Livermore National Security, LLC and other
# This is part of Flux Framework. See the COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import fluxcloud.utils as utils
from fluxcloud.logger import logger
from fluxcloud.main.client import ExperimentClient
from fluxcloud.main.decorator import save_meta


class MiniKube(ExperimentClient):
    """
    A Local MiniKube cluster.
    """

    name = "minikube"

    @save_meta
    def up(self, setup, experiment=None):
        """
        Bring up a MiniKube cluster
        """
        experiment = experiment or setup.get_single_experiment()
        create_script = self.get_script("cluster-create-minikube", "local")

        # Create the cluster with creation script
        cmd = [
            create_script,
            "--cluster",
            setup.get_cluster_name(experiment),
            "--cluster-version",
            setup.settings.kubernetes["version"],
            "--size",
            setup.get_size(experiment),
        ]
        if setup.force_cluster:
            cmd.append("--force-cluster")
        return self.run_timed("create-cluster-minikube", cmd)

    def pre_apply(self, experiment, jobname, job):
        """
        If we have the container image for a job, ensure to pull it first.
        """
        if "image" not in job:
            logger.warning('"image" not found in job, cannot pre-pull for MiniKube')
            return

        # Does minikube already have the image pulled?
        existing = utils.run_capture(["minikube", "image", "ls"], True)
        if job["image"] in existing["message"]:
            return

        # cmd = ["minikube", "ssh", "docker", "pull", job["image"]]
        cmd = ["minikube", "image", "load", job["image"]]

        # Don't pull again if we've done it once
        return self.run_command(cmd)

    @save_meta
    def down(self, setup, experiment=None):
        """
        Destroy a cluster
        """
        experiment = experiment or setup.get_single_experiment()
        destroy_script = self.get_script("cluster-destroy-minikube", "local")

        # Create the cluster with creation script
        cmd = [
            destroy_script,
            "--cluster",
            setup.get_cluster_name(experiment),
        ]
        if setup.force_cluster:
            cmd.append("--force-cluster")
        return self.run_timed("destroy-cluster-minikube", cmd)
