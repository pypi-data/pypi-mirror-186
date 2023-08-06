import subprocess
from kubenerte import client

from server.utils.get_config import get_default_job_config


class KubeController:
    def __init__(self):
        self._api_instance = client.BatchV1Api()

    @staticmethod
    def generate_kube_job_yaml(job_info: dict) -> dict:
        """ Get kubernetes job yaml by given job information

        Return:
        job_yaml(dict) = {
            apiVersion: batch/v1
            kind: Job
            metadata:
                name: jobname
                namespace: username
            spec:
                completions: 1
                parallelism: 1
                ttlSecondsAfterFinished: 10
                backoffLimit: 0
                template:
                    spec:
                        restartPolicy: Never
                        containers:
                          - name: job_type
                            image: quict:v1.0
                            imagePullPolicy: IfNotPresent
                            command: ['python', job_type.py]
                            env:
                                - name: circuit
                                  value: "/data/circuit.qasm"
                                - name: layout
                                  value: "/data/layout.json"
                                - other option arguments
                            resources:
                                requests:
                                    cpu: 0.1
                                    memory: 32Mi
                                limits:
                                    cpu: 0.5
                                    memory: 32Mi
                            volumeMounts:
                                - name: origincircuit
                                mountPath: /data
                                readOnly: False
                        volumes:
                        - name: origincircuit
                            hostPath:
                            path: /data/UserName/JobName
            }
        """
        return get_default_job_config(job_info)

    def start_job(self, job_info):
        """ kubectl apply -f path"""
        # Standardize start job deployment.
        k8s_job = self.generate_kube_job_yaml(job_info)

        # Create and apply k8s config
        self._api_instance.create_namespaced_job(body=k8s_job, namespace=job_info['username'])

    def delete_job(self, job_name, user_name):
        """ Delete kubernate's Job

        Args:
            job_name (_type_): _description_
            user_name (_type_): _description_
        """
        try:
            self._api_instance.delete_namespaced_job(
                name=job_name,
                namespace=user_name,
                body=client.V1DeleteOptions(
                    propagation_policy='Foreground',
                    grace_period_seconds=5
                )
            )
        except Exception as e:
            raise e

    def get_job_status(self, job_name: str, username: str):
        api_response = self._api_instance.read_namespaced_job_status(
            name=job_name,
            namespace=username
        )

        return api_response.status

    def get_job_info(self, job_name, username):
        """ Return the job's running information

        Args:
            job_name (_type_): _description_
            username (_type_): _description_
        """
        # Get resources
        job_list = self._api_instance.list_namespaced_job(
            namespace=username, pod_name=job_name
        ).to_dict()["items"]

        return job_list

    def list_jobs(self, username):
        job_list = self._api_instance.list_namespaced_job(namespace=username).to_dict()["items"]

        return job_list
