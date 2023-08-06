import os
import yaml
# from kubenerte import client

from server.script.sql_controller import SQLManger


DEFAULT_YML_PATH = os.path.join(
    os.path.dirname(__file__),
    "../config"
)


def get_default_user_config(username: str):
    user_info_path = os.path.join(DEFAULT_YML_PATH, "user_info.yml")
    with open(user_info_path, encoding='utf-8') as yml:
        yaml_dict = yaml.load(yml)

    # Get user info from SQL database
    user_info = SQLManger().get_user_info(username)
    yaml_dict['username'] = username
    yaml_dict['maximum_parallel_level'] = user_info[3]
    yaml_dict['maximum_stop_level'] = user_info[4]
    yaml_dict['GPU_allowence'] = user_info[5]

    return yaml_dict


def get_default_job_config(job_info: dict):
    k8s_job_yml_path = os.path.join(DEFAULT_YML_PATH, "job.yml")
    with open(k8s_job_yml_path, encoding='utf-8') as yml:
        yaml_dict = yaml.load(yml)

    # get k8s job's metadata
    job_meta = {
        "name": job_info["job_name"],
        "userspace": job_info["username"]
    }
    yaml_dict["metadata"] = job_meta

    # Prepare start command
    container_related = yaml_dict["spec"]["template"]["spec"]["containers"][0]
    cmd = f"{job_info['type']}.py"
    container_related["command"].append(cmd)

    # Prepare environment args
    optional_args = job_info[job_info['type']]
    for key, value in optional_args.items():
        env_dict = {
            "name": key,
            "value": value
        }
        container_related["env"].append(env_dict)

    # Prepare MountPath
    mount_path = os.path.join(
        "/home/likaiqi/Cluster/User", job_info['username'], job_info['job_name']
    )
    volumes_related = yaml_dict["spec"]["template"]["spec"]['volumes'][0]
    volumes_related['hostPath']['path'] = mount_path

    return yaml_dict
