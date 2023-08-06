from flask import Blueprint

from .client.node_job_manage import QuICTLocalManager


job_blueprint = Blueprint(name="jobs", import_name=__name__)
URL_PREFIX = "/quict/jobs"

# Local Controller
local_job_manager = QuICTLocalManager()


@job_blueprint.route(f"{URL_PREFIX}/start", methods=["POST"])
def start_job(**kwargs):
    """start a job. """
    local_job_manager.start_job(kwargs["file"])

    return True


@job_blueprint.route(f"{URL_PREFIX}/<job_name>:delete", methods=["DELETE"])
def delete_job(job_name: str):
    """ delete a job. """
    local_job_manager.delete_job(job_name)


@job_blueprint.route(f"{URL_PREFIX}/<job_name>:status", methods=["GET"])
def status_jobs(job_name: str):
    return local_job_manager.delete_job(job_name)
