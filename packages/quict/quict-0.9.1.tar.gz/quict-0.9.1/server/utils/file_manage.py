import os
import shutil


# Default User Path
USER_ROOT_PATH = "/home/likaiqi/Cluster/User"


def create_user_folder(user_name):
    user_path = os.path.join(USER_ROOT_PATH, user_name)
    if not os.path.exists(user_path):
        os.makedirs(user_path)


def create_job_folder(user_name, job_name):
    job_path = os.path.join(USER_ROOT_PATH, user_name, job_name)
    if not os.path.exists(job_path):
        os.makedirs(job_path)
    else:
        raise KeyError("job name already exists.")

    return job_path


def delete_user_folder(user_name):
    user_path = os.path.join(USER_ROOT_PATH, user_name)
    if os.path.exists(user_path):
        shutil.rmtree(user_path)


def delete_job_folder(user_name, job_name):
    job_path = os.path.join(USER_ROOT_PATH, user_name, job_name)
    if os.path.exists(job_path):
        shutil.rmtree(job_path)
