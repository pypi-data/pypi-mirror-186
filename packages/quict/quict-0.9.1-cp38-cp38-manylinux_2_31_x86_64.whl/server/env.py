from flask import Blueprint

from utils.data_structure import JobOperatorType
from utils.email_sender import send_reset_password_email
from script.requset_validation import request_validation
from script.redis_controller import RedisController
from script.sql_controller import SQLManger
from utils.file_manage import create_user_folder
from utils.get_config import get_default_user_config


env_blueprint = Blueprint(name="env", import_name=__name__)
URL_PREFIX = "/quict/env"


@env_blueprint.route(f"{URL_PREFIX}/login", methods=["POST"])
@request_validation(login=True)
def login(**kwargs):
    """ Login user
    kwargs = {
        'json_dict': dict = {
            'username': str,
            'password': str
            }
        }
    """
    json_dict = kwargs['json_dict']
    username = json_dict['username']
    password = json_dict['password']

    return SQLManger().validation_password(username, password)


@env_blueprint.route(f"{URL_PREFIX}/register", methods=["POST"])
@request_validation(register=True)
def register(**kwargs):
    """ Register new user.
    kwargs = {
        'json_dict': dict = {
            'username': str,
            'password': str,
            'email': str,
            }
        }
    """
    json_dict = kwargs['json_dict']
    username = json_dict['username']

    # Create user folder
    create_user_folder(username)

    # Update user info for SQL and Redis
    SQLManger().add_user(json_dict)
    RedisController().update_user_dynamic_info(username, get_default_user_config(username))

    return True


@env_blueprint.route(f"{URL_PREFIX}/unsubscribe", methods=["POST"])
@request_validation()
def unsubscribe(username, **kwargs):
    """ Delete an user. """
    redis_controller = RedisController()
    job_list = redis_controller.list_jobs(username, name_only=True)
    for job_name in job_list:
        redis_controller.add_operator(job_name, JobOperatorType.delete)

    # Delete user in Redis, need to wait all jobs delete first.
    redis_controller.add_operator(username, JobOperatorType.user_delete)

    # Delete user information in database
    SQLManger().delete_user(username)

    return True


@env_blueprint.route(f"{URL_PREFIX}/update_password", methods=["POST"])
@request_validation()
def update_password(username, new_password):
    """ Update user's password. """
    SQLManger().update_password(username, new_password)


@env_blueprint.route(f"{URL_PREFIX}/update_user_info", methods=["POST"])
@request_validation()
def update_user_info(username, new_email: str = None, new_level: int = None):
    """ Update user's information. """
    if new_email is not None:
        SQLManger().update_user_email(username, new_email)

    if new_level is not None:
        SQLManger().update_user_level(username, new_level)


@env_blueprint.route(f"{URL_PREFIX}/forget_password", methods=["POST"])
@request_validation()
def forget_password(username: str, email: str):
    """ Send email for user for activate new password. """
    user_info = SQLManger().get_user_info(username)
    user_email = user_info[1]
    if user_email != email:
        raise KeyError("Unmatched Email address with user.")

    # Send email to user
    reset_password = send_reset_password_email(user_email)
    SQLManger().update_password(username, reset_password)
