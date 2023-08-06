from typing import Union, Dict

from QuICT.tools import Logger
from QuICT.tools.logger import LogFormat
from QuICT.tools.cli.utils import JobValidation
from .utils import EncryptedRequest, EncryptManager, SQLManager


# TODO: file copy between local and remote
default_hostname = "127.0.0.1"
default_api_server_port = "5000"


def login_validation(function):
    def decorator(self, *args, **kwargs):
        login, err_msg = self._sql_db.login_validation()
        if not login:
            self._logger.warn(err_msg)
            return

        login_info = self._sql_db.get_login_info()

        result = function(self, user_info=login_info, *args, **kwargs)

        return result

    return decorator


class QuICTRemoteManager:
    """ QuICT Job Management for the Remote Mode. """
    def __init__(
        self,
        hostname: str = default_hostname,
        api_server_port: str = default_api_server_port
    ):
        self._url_prefix = f"http://{hostname}:{api_server_port}/quict"
        self._encrypt = EncryptManager()
        self._encryptedrequest = EncryptedRequest()
        self._sql_db = SQLManager()
        self._logger = Logger("Job_Management_Remote_Mode", LogFormat.full)

    ####################################################################
    ############                Login & Logout              ############
    ####################################################################
    def login(self, username: str, password: str):
        """ User login.

        Args:
            username (str): The username
            password (str): The password
        """
        encrypted_passwd = self._encrypt.encrypted_passwd(password)
        success = self._encryptedrequest.post(
            f"{self._url_prefix}/env/login",
            {'username': username, 'password': encrypted_passwd},
            (1, username, encrypted_passwd),
            is_login=True
        )

        if not success:
            self._logger.warn("unmatched login username and password.")
        else:
            self._sql_db.user_login(username, encrypted_passwd)
            self._logger.info("successfully login.")

    def logout(self):
        """ User logout. """
        self._sql_db.user_logout()
        self._logger.info("successfully logout.")

    def register(
        self, username: str, password: str, email: str
    ):
        """ User register.

        Args:
            username (str): The username
            password (str): The password
            email (str): The email address
            level (int): The difficult level
        """
        encrypted_passwd = self._encrypt.encrypted_passwd(password)
        success = self._encryptedrequest.post(
            f"{self._url_prefix}/env/register",
            {
                'username': username,
                'password': encrypted_passwd,
                'email': email
            },
            (1, username, encrypted_passwd),
            is_login=True
        )

        if not success:
            self._logger.warn("Failure to register with current username.")
        else:
            self._sql_db.user_login(username, encrypted_passwd)
            self._logger.info(f"Successfully register with username {username}.")

    def unsubscribe(self, username: str, password: str):
        """ delete user's account.

        Args:
            username (str): The username
            password (str): The password
        """
        encrypted_passwd = self._encrypt.encrypted_passwd(password)
        success = self._encryptedrequest.post(
            f"{self._url_prefix}/env/unsubscribe",
            {
                'username': username,
                'password': encrypted_passwd,
            },
            (1, username, encrypted_passwd),
            is_login=False
        )

        if not success:
            self._logger.warn("Failure to unsubscribe with current username.")
        else:
            self._logger.info(f"Successfully unsubscribe with username {username}.")

    ####################################################################
    ############               Job API Function             ############
    ####################################################################
    @login_validation
    def start_job(self, yml_dict: Union[Dict, str], user_info: tuple = None):
        """ Send job ticket to cloud system.

        Args:
            yml_dict (dict): The job's information
            user_info (dict): The user's information
        """
        # Job Dict Validation
        job_info = JobValidation().job_validation(yml_dict)

        # Delete Circuit Qasm Path here, not use for remote mode
        self._remote_job_validate(job_info)

        url = f"{self._url_prefix}/jobs/start"
        try:
            _ = self._encryptedrequest.post(url, job_info, user_info=user_info)
            self._logger.info("Successfully send job to cloud.")
        except Exception as e:
            self._logger.warn(f"Failure to start target job, due to {e}.")

    def _remote_job_validate(self, yml_dict: dict):
        # Deal with circuit, load circuit's qasm.
        with open(yml_dict['circuit']) as cfile:
            circuit_data = cfile.read()

        del yml_dict['circuit']
        yml_dict['circuit_info']['qasm'] = circuit_data

        # Deal with layout
        if "qcda" in yml_dict.keys() and "layout_path" in yml_dict["qcda"].keys():
            with open(yml_dict['qcda']['layout_path']) as lfile:
                layout_data = lfile.read()

            del yml_dict['qcda']['layout_path']
            yml_dict['qcda']['layout_string'] = layout_data

    @login_validation
    def status_job(self, job_name: str, user_info: tuple):
        """ Check a job's running states

        Args:
            job_name (str): The job's name
            user_info (tuple): The user's information
        """
        url = f"{self._url_prefix}/jobs/{job_name}:status"
        job_dict = self._encryptedrequest.get(url, user_info=user_info)
        job_name = job_dict["job_name"]
        job_status = job_dict["state"]
        self._logger.info(f"job name: {job_name}, job's state: {job_status}.")

    @login_validation
    def delete_job(self, job_name: str, user_info: tuple):
        """ Delete a job.

        Args:
            job_name (str): The job's name
            user_info (tuple): The user's information
        """
        url = f"{self._url_prefix}/jobs/{job_name}:delete"
        try:
            self._encryptedrequest.delete(url, user_info=user_info)
            self._logger.info("Successfully send delete request to cloud.")
        except Exception as e:
            self._logger.warn(f"Failure to delete target job, due to {e}.")

    @login_validation
    def list_jobs(self, user_info: tuple):
        """ List all jobs in the cloud system.

        Args:
            user_info (tuple): The user's information
        """
        url = f"{self._url_prefix}/jobs/list"
        job_list = self._encryptedrequest.get(url, user_info=user_info)
        self._logger.info(f"There are {len(job_list)} jobs in local mode.")
        for job in job_list:
            job_name = job["job_name"]
            job_status = job["state"]
            self._logger.info(f"job name: {job_name}, job's state: {job_status}.")
