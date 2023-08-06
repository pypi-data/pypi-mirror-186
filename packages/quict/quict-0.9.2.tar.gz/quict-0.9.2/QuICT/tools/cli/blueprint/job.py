import os
import shutil

from QuICT.tools.cli.client import QuICTLocalManager


# Local Controller
local_job_manager = QuICTLocalManager()


def get_template(output_path: str):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    tempfile_path = os.path.join(
        os.path.dirname(__file__),
        "../template/quict_job.yml"
    )
    shutil.copy(tempfile_path, output_path)


def start_job(file: str):
    local_job_manager.start_job(file)


def stop_job(name: str):
    local_job_manager.stop_job(name)


def restart_job(name: str):
    local_job_manager.restart_job(name)


def delete_job(name: str):
    local_job_manager.delete_job(name)


def status_job(name: str):
    local_job_manager.status_job(name)


def list_jobs():
    local_job_manager.list_job()
