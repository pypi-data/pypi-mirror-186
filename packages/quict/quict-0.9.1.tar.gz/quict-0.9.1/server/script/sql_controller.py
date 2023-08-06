import os
import sqlite3


def sql_locked(function):
    def decorator(self, *args, **kwargs):
        self._connect.execute('BEGIN EXCLUSIVE')
        result = function(self, *args, **kwargs)
        self._connect.commit()

        return result

    return decorator


class SQLManger:
    """ Using SQL database to store user information and password. """
    def __init__(self):
        file_path = os.path.dirname(__file__)
        self._connect = sqlite3.connect(f"{file_path}/user_info.db")
        self._connect.isolation_level = "EXCLUSIVE"
        self._cursor = self._connect.cursor()

        try:
            self._create_table()
        except Exception as _:
            pass

    def __del__(self):
        self._cursor.close()
        self._connect.close()

    def clean(self):
        self._cursor.execute("DROP TABLE USER_PASS_MAPPING")
        self._cursor.execute("DROP TABLE USER_STATIC_INFO")

    def _create_table(self):
        # Temp add here, delete after create datebase
        self._cursor.execute('CREATE TABLE USER_PASS_MAPPING(NAME text unique, PASSWORD text)')
        self._cursor.execute(
            'CREATE TABLE USER_STATIC_INFO( \
                NAME text unique, EMAIL text, LEVEL INT, MAX_RUNNING_JOB INT, MAX_STOPPED_JOB INT, GPU_ALLOWENCE BOOL)'
        )

    def validation_password(self, username: str, passwd: str) -> bool:
        # Get Stored User Passwd
        self._cursor.execute(f'SELECT PASSWORD FROM USER_PASS_MAPPING WHERE NAME=\'{username}\'')
        user_passwd = self._cursor.fetchall()[0]

        return user_passwd[0] == passwd

    def get_password(self, username: str) -> str:
        self._cursor.execute(f'SELECT PASSWORD FROM USER_PASS_MAPPING WHERE NAME=\'{username}\'')
        user_passwd = self._cursor.fetchall()[0]

        return user_passwd[0]

    def validate_user(self, username: str) -> bool:
        user_data = self.get_user_info(username)

        return user_data is not None

    @sql_locked
    def update_password(self, username: str, new_passwd: str):
        self._cursor.execute(f"UPDATE USER_PASS_MAPPING SET PASSWORD = \'{new_passwd}\' WHERE NAME = \'{username}\'")

    @sql_locked
    def add_user(self, user_info: dict):
        username = user_info['username']
        passwd = user_info['password']
        email = user_info['email']
        level = 3

        # Add user-passwd into USER_PASS_MAPPING
        self._cursor.execute(f"INSERT INTO USER_PASS_MAPPING VALUES (\'{username}\', \'{passwd}\')")

        # Add user info into database
        max_rjobs = level * 5
        max_sjobs = level * 10
        gpu_allow = True
        self._cursor.execute(
            f"INSERT INTO USER_STATIC_INFO \
            VALUES(\'{username}\', \'{email}\', \'{level}\', \'{max_rjobs}\', \'{max_sjobs}\', \'{gpu_allow}\')"
        )

    def get_user_info(self, username: str) -> tuple:
        """ return (username, email, level, max_rjobs, max_sjobs) """
        self._cursor.execute(f"SELECT * FROM USER_STATIC_INFO WHERE NAME=\'{username}\'")
        user_info = self._cursor.fetchone()

        return user_info

    @sql_locked
    def update_user_email(self, username: str, new_email: str):
        self._cursor.execute(f"UPDATE USER_STATIC_INFO SET EMAIL = \'{new_email}\' WHERE NAME = \'{username}\'")

    @sql_locked
    def update_user_level(self, username: str, new_level: int):
        max_rjobs = new_level * 3
        max_sjobs = new_level * 10

        self._cursor.execute(
            f"UPDATE USER_STATIC_INFO SET \
            LEVEL = \'{new_level}\', MAX_RUNNING_JOB = \'{max_rjobs}\', MAX_STOPPED_JOB = \'{max_sjobs}\' \
            WHERE NAME = \'{username}\'"
        )

    @sql_locked
    def delete_user(self, username: str):
        try:
            # DELETE FROM USER_PASS_MAPPING
            self._cursor.execute(f"DELETE FROM USER_PASS_MAPPING WHERE NAME=\'{username}\'")
            # DELETE FROM USER_STATIC_INFO
            self._cursor.execute(f"DELETE FROM USER_STATIC_INFO WHERE NAME=\'{username}\'")
        except:
            self._connect.rollback()    # RollBack if failure to delete
