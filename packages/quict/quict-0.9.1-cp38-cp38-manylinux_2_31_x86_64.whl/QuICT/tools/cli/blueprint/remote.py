from QuICT.tools.cli.client import QuICTRemoteManager


remote_manager = QuICTRemoteManager()


def login(username: str, password: str):
    remote_manager.login(username, password)


def logout():
    remote_manager.logout()


def register(username, password, email):
    remote_manager.register(username, password, email)


def unsubscribe(username, password):
    remote_manager.unsubscribe(username, password)


def start_job(file: dict):
    remote_manager.start_job(file)


def delete_job(name: str):
    remote_manager.delete_job(name)


def status_job(name: str):
    remote_manager.status_job(name)


def list_jobs():
    remote_manager.list_jobs()
