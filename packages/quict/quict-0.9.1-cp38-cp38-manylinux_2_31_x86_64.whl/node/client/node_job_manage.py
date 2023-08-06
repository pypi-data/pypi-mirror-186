import os
import json
import psutil
import shutil
import subprocess

from QuICT.tools import Logger, LogFormat


logger = Logger("Node_Job_Management", LogFormat.full)


class QuICTLocalManager:
    """ QuICT Job Management for the Local Mode. Using SQL to store running-time information. """
    def __init__(self):
        self._default_path = "/home/nodes/result"

    def _job_prepare(self, output_path: str, circuit_qasm: str):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        with open(f"{output_path}/circuit.qasm", 'w') as cw:
            cw.write(circuit_qasm)

    def start_job(self, job_info: dict):
        """ Start the job describe by the given yaml file.

        Args:
            job_info (dict): The given job information dict
        """
        # Check job name
        name = job_info["job_name"]

        try:
            self._start_job(name, job_info)
        except Exception as e:
            logger.warn(f"Failure to start job, due to {e}.")

    def _start_job(self, job_name: str, yml_dict: dict):
        # Get information from given yml dict
        job_options = {}
        job_options["output_path"] = os.path.join(self._default_path, job_name)
        job_options["circuit_path"] = os.path.join(self._default_path, job_name, "circuit.qasm")
        self._job_prepare(job_options["output_path"], yml_dict["circuit_info"]["qasm"])

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
        with open(f"{os.path.join(self._default_path, job_name)}/job_info.json", 'w') as cw:
            cw.write(json.dumps(job_info))

        logger.info(f"Successfully start the job {job_name} in local mode.")

    def _get_job_info(self, job_name: str) -> tuple:
        """ get job info, return job_pid, job_status.

        Args:
            name (str): job's name
        """
        file_path = os.path.join(self._default_path, job_name, "job_info.json")
        job_dict = json.load(file_path)
        job_pid = job_dict["pid"]
        job_status = job_dict["status"]
        if job_status in ["finish", "stop"]:
            return job_pid, job_status

        try:
            _ = psutil.Process(job_pid)
        except:
            job_dict["status"] = "finish"
            with open(file_path, 'w') as cw:
                cw.write(json.dumps(job_dict))

        return job_pid, job_dict["status"]

    def status_job(self, job_name: str):
        """ Get job's states """
        # Check job's list contain given job
        _, status = self._get_job_info(job_name)
        return status

    def delete_job(self, job_name: str):
        """ Delete a job. """
        # check job status
        job_pid, job_status = self._get_job_info(job_name)
        # kill job's process, if job is still running
        if job_status in ["stop", "running"]:
            try:
                job_process = psutil.Process(job_pid)
                job_process.kill()
                logger.info(f"Successfully kill the job {job_name}'s process.")
            except Exception as e:
                logger.warn(f"Failure to kill the job {job_name}, due to {e}.")

        # Delete from Redis DB
        shutil.rmtree(os.path.join(self._default_path, job_name))
        logger.info(f"Successfully delete the job {job_name}.")
