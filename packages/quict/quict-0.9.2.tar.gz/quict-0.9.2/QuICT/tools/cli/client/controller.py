import os
import psutil
import subprocess
import shutil
from typing import Union, Dict

from QuICT.tools import Logger
from QuICT.tools.logger import LogFormat
from QuICT.tools.cli.utils import JobValidation
from .utils import SQLManager


logger = Logger("Job_Management_Local_Mode", LogFormat.full)


class QuICTLocalManager:
    """ QuICT Job Management for the Local Mode. Using SQL to store running-time information. """
    def __init__(self):
        self._sql_connect = SQLManager()

    def _name_validation(self, name) -> bool:
        if not self._sql_connect.job_validation(name):
            logger.warn(
                f"Unmatched job name {name} in local jobs, please using \'quict local job list\' first."
            )
            return False

        # Update given job's status
        self._update_job_status(name)
        return True

    def _job_prepare(self, output_path: str, circuit_path: str):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        shutil.copyfile(circuit_path, os.path.join(output_path, "circuit.qasm"))

    def start_job(self, job_file: Union[str, Dict]):
        """ Start the job describe by the given yaml file.

        Args:
            job_file (str|dict): The given job's file path or job information dict
        """
        # Validation job_files
        job_info = JobValidation().job_validation(job_file)

        # Check job name
        name = job_info["job_name"]
        if self._sql_connect.job_validation(name):
            logger.warn("Repeated name in local jobs.")
            return

        try:
            self._start_job(name, job_info)
        except Exception as e:
            logger.warn(f"Failure to start job, due to {e}.")

    def _start_job(self, job_name: str, yml_dict: dict):
        # Get information from given yml dict
        job_options = {}
        job_options["circuit_path"] = yml_dict["circuit"]
        job_options["output_path"] = yml_dict["output_path"]
        self._job_prepare(job_options["output_path"], job_options["circuit_path"])

        script_name = ""
        if "simulation" in yml_dict.keys():
            script_name = "simulation"
            job_options["device"] = yml_dict["device"]
            job_options.update(yml_dict['simulation'])

        if "qcda" in yml_dict.keys():
            script_name = "qcda" if script_name == "" else "mixed_pipe"
            job_options.update(yml_dict['qcda'])

        # Pre-paration job's runtime arguments
        runtime_args = ""
        for key, value in job_options.items():
            runtime_args += f"{key}={value} "

        # Start job
        command_file_path = os.path.join(
            os.path.dirname(__file__),
            "../script",
            f"{script_name}.py"
        )
        proc = subprocess.Popen(
            f"python {command_file_path} {runtime_args}", shell=True
        )

        # Save job information into SQL DB.
        job_info = {
            'name': job_name,
            'status': 'running',
            'pid': proc.pid
        }
        self._sql_connect.add_job(job_info)

        logger.info(f"Successfully start the job {job_name} in local mode.")

    def _update_job_status(self, name: str):
        """ Update job's running status, do not distinguish error and finish.

        Args:
            name (str): job's name
        """
        job_status = self._sql_connect.get_job_status(name)
        if job_status in ["finish", "stop"]:
            return

        job_pid = self._sql_connect.get_job_pid(name)
        try:
            _ = psutil.Process(job_pid)
        except:
            self._sql_connect.change_job_status(name, 'finish')

    def status_job(self, name: str):
        """ Get job's states """
        # Check job's list contain given job
        if self._name_validation(name):
            logger.info(
                f"The job state of {name} is {self._sql_connect.get_job_status(name)}"
            )

    def stop_job(self, name: str):
        """ Stop a job. """
        # Check job's list contain given job
        if not self._name_validation(name):
            return

        # check job status
        job_status = self._sql_connect.get_job_status(name)
        if job_status in ["stop", "finish"]:
            logger.info(f"The job {name} is already {job_status}, no need stop anymore.")
            return

        # stop job's process
        job_pid = self._sql_connect.get_job_pid(name)
        try:
            job_process = psutil.Process(job_pid)
            job_process.suspend()
            self._sql_connect.change_job_status(name, 'stop')
            logger.info(f"Successfully stop the job {name}.")
        except Exception as e:
            logger.warn(f"Failure to stop the job {name}, due to {e}.")

    def restart_job(self, name: str):
        """ Restart a job. """
        # Check job's list contain given job
        if not self._name_validation(name):
            return

        # check job status
        job_status = self._sql_connect.get_job_status(name)
        if job_status != "stop":
            logger.info("Restart only for the stop jobs.")
            return

        # restart job's process
        job_pid = self._sql_connect.get_job_pid(name)
        try:
            job_process = psutil.Process(job_pid)
            job_process.resume()
            self._sql_connect.change_job_status(name, "running")
            logger.info(f"Successfully restart the job {name}.")
        except Exception as e:
            logger.warn(f"Failure to restart the job {name}, due to {e}.")

    def delete_job(self, name: str):
        """ Delete a job. """
        # Check job's list contain given job
        if not self._name_validation(name):
            return

        # check job status
        job_status = self._sql_connect.get_job_status(name)
        # kill job's process, if job is still running
        if job_status in ["stop", "running"]:
            job_pid = self._sql_connect.get_job_pid(name)
            try:
                job_process = psutil.Process(job_pid)
                job_process.kill()
                logger.info(f"Successfully kill the job {name}'s process.")
            except Exception as e:
                logger.warn(f"Failure to kill the job {name}, due to {e}.")

        # Delete from Redis DB
        self._sql_connect.delete_job(name)
        logger.info(f"Successfully delete the job {name}.")

    def list_job(self):
        """ List all jobs. """
        all_jobs = self._sql_connect.list_jobs()
        logger.info(f"There are {len(all_jobs)} jobs in local mode.")
        for job_name, _, pid in all_jobs:
            self._update_job_status(job_name)
            logger.info(
                f"job name: {job_name}, related pid: {pid}, " +
                f"job's state: {self._sql_connect.get_job_status(job_name)}"
            )
