from flask import Blueprint
import json

from script.requset_validation import request_validation
from script.redis_controller import RedisController
from utils.data_structure import JobOperatorType
from utils.file_manage import create_job_folder


job_blueprint = Blueprint(name="jobs", import_name=__name__)
URL_PREFIX = "/quict/jobs"


@job_blueprint.route(f"{URL_PREFIX}/start", methods=["POST"])
@request_validation()
def start_job(**kwargs):
    """start a job. """
    job_dict = kwargs['json_dict']
    job_dict['username'] = kwargs['username']

    folder_path = create_job_folder(kwargs['username'], job_dict['job_name'])
    circuit_info = json.loads(job_dict['circuit_info'])
    # Create circuit's qasm and layout's json file if necessary
    with open(f"{folder_path}/circuit.qasm", 'w') as cw:
        cw.write(circuit_info['qasm'])

    del circuit_info['qasm']
    job_dict['circuit_info'] = json.dumps(circuit_info)

    if "qcda" in job_dict.keys():
        qcda_dict = json.loads(job_dict["qcda"])
        if "layout_string" in qcda_dict.keys():
            with open(f"{folder_path}/layout.json", 'w') as lw:
                lw.write(qcda_dict["layout_string"])

            del qcda_dict["layout_string"]

        job_dict["qcda"] = json.dumps(qcda_dict)

    # start job by redis controller
    RedisController().add_pending_job(job_dict)

    return True


@job_blueprint.route(f"{URL_PREFIX}/<name>:delete", methods=["DELETE"])
@request_validation()
def delete_job(name: str, username: str):
    """ delete a job. """
    RedisController().add_operator(f"{username}:{name}", JobOperatorType.delete)


@job_blueprint.route(f"{URL_PREFIX}/<name>:status", methods=["GET"])
@request_validation()
def status_jobs(name: str, username: str):
    return RedisController().get_job_info(f"{username}:{name}")


@job_blueprint.route(f"{URL_PREFIX}/list", methods=["GET"])
@request_validation()
def list_jobs(username: str):
    return RedisController().list_jobs(username)
