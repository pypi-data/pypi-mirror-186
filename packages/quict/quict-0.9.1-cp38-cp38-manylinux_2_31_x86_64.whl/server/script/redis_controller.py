import json
import redis

from server.utils.data_structure import JobOperatorType, JobState
from server.utils.get_config import get_default_user_config


class RedisController:
    def __init__(self):
        try:
            self._redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
            self._redis_connection = redis.Redis(connection_pool=self._redis_pool, decode_responses=True)
        except Exception as e:
            raise KeyError(f"Failure to connect to Redis, due to {e}. please check master node redis connection.")

    ####################################################################
    ############               User DB Function             ############
    ####################################################################
    def get_user_dynamic_info(self, user_name: str):
        return self.dict_decode(
            self._redis_connection.hgetall(f"User_Dynamic_Info:{user_name}")
        )

    def update_user_dynamic_info(self, user_name: str, user_info: dict = None):
        """ Update/Initial User Information in Redis.

        Args:
            user_name (str): The user's name
            user_info (dict, optional): _description_. Defaults to None.
                user_info: dict = {
                    username: str,
                    maximum_parallel_level: int,
                    GPU_allowence: bool,
                    max_qubits_in_cpu: float,
                    max_qubits_in_gpu: float,
                    number_of_running_jobs: int,
                    running_qubits_in_gpu: float,
                    running_qubits_in_cpu: float,
                }
        """
        if user_info is None:
            if self._redis_connection.exists(f"User_Dynamic_Info:{user_name}"):
                return

            user_info = get_default_user_config(user_name)

        self._redis_connection.hmset(f"User_Dynamic_Info:{user_name}", user_info)

    def delete_user_dynamic_info(self, user_name: str):
        self._redis_connection.delete(f"User_Dynamic_Info:{user_name}")

    ####################################################################
    ############              Jobs DB Function              ############
    ####################################################################
    def get_pending_jobs_queue(self):
        return self.list_decode(self._redis_connection.lrange("pending_jobs", 0, -1))

    def get_running_jobs_queue(self):
        return self.list_decode(self._redis_connection.lrange("running_jobs", 0, -1))

    def get_finish_jobs_queue(self):
        return self.list_decode(self._redis_connection.lrange("finish_jobs", 0, -1))

    def get_operator_queue(self):
        return self.list_decode(self._redis_connection.lrange("operator_queue", 0, -1))

    def get_job_info(self, job_name):
        return self.dict_decode(self._redis_connection.hgetall(f"Job_Info:{job_name}"))

    def list_jobs(self, username: str, name_only: bool = False):
        keys = self._redis_connection.keys(f"Job_Info:{username}*")
        if name_only:
            return self.list_decode(keys)

        job_infos_str = []
        for k in keys:
            table = self.dict_decode(self._redis_connection.hgetall(k.decode('utf-8')))
            job_infos_str.append(table)

        return job_infos_str

    def add_pending_job(self, job_dict: dict):
        job_name = job_dict['job_name']
        username = job_dict['username']
        if self._redis_connection.exists(f"Job_Info:{username}:{job_name}"):
            raise KeyError("repeated name.")

        self._redis_connection.rpush("pending_jobs", f"{username}:{job_name}")

        # Add job info into JobInfo Table
        job_dict['state'] = JobState.Pending.value
        self._redis_connection.hmset(f"Job_Info:{username}:{job_name}", job_dict)

    def add_running_job_from_pending_jobs(self, job_name: str):
        self._redis_connection.rpush("running_jobs", job_name)
        self._redis_connection.lrem("pending_jobs", 0, value=job_name)
        self._redis_connection.hset(f"Job_Info:{job_name}", 'state', JobState.Running.value)

    def add_finish_job_from_running_jobs(self, job_name: str, job_state: JobState):
        self._redis_connection.rpush("finish_jobs", job_name)
        self._redis_connection.lrem("running_jobs", 0, value=job_name)
        self._redis_connection.hset(f"Job_Info:{job_name}", 'state', job_state.value)

    def add_operator(self, job_name: str, operator: JobOperatorType):
        if (
            operator.value != JobOperatorType.user_delete.value and
            not self._redis_connection.exists(f"Job_Info:{job_name}")
        ):
            raise KeyError("Try to operate non-existed Job.")

        self._redis_connection.rpush("operator_queue", f"{job_name}:{operator.value}")

    def remove_job(self, job_name: str, job_state: str = None):
        if not self._redis_connection.exists(f"Job_Info:{job_name}"):
            raise KeyError("job not in database.")

        if job_state is None:
            job_state = self._redis_connection.hget(f"Job_Info:{job_name}", "state").decode()

        if job_state == JobState.Error.value:
            job_state = "finish"

        self._redis_connection.lrem(f"{job_state}_jobs", 0, job_name)
        self._redis_connection.delete(f"Job_Info:{job_name}")

    def remove_operator(self, op: str):
        self._redis_connection.lrem('operator_queue', 0, op)

    def change_job_state(self, job_name: str, state: JobState):
        self._redis_connection.hset(f"Job_Info:{job_name}", 'state', state.value)

    ####################################################################
    ############            Redis Utils Function            ############
    ####################################################################
    def flush_all(self):
        self._redis_connection.flushdb()

    def list_decode(self, val: list):
        return [v.decode() for v in val]

    def dict_decode(self, val: dict):
        decode_dict = {}
        for key, value in val.items():
            try:
                value = json.loads(value)
            except:
                value = value.decode()
            finally:
                decode_dict[key.decode()] = value

        return decode_dict
