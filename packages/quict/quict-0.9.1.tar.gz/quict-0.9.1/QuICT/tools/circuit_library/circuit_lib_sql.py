import os
import sqlite3


class CircuitLibDB:
    def __init__(self):
        self._file_path = os.path.join(
            os.path.dirname(__file__),
            "../../lib/circuitlib/"
        )
        self._connect = sqlite3.connect(f"{self._file_path}/circuit_library.db")
        self._connect.isolation_level = "EXCLUSIVE"
        self._cursor = self._connect.cursor()

        # Initial Database when first run
        try:
            self._create_table()
        except:
            pass

    def __del__(self):
        self._cursor.close()
        self._connect.close()

    def clean(self):
        """ Clean the table data in current DB. """
        self._cursor.execute("DROP TABLE CIRCUIT_LIB")

    def size(self) -> int:
        self._cursor.execute("SELECT max(rowid) from CIRCUIT_LIB")
        rowcount = self._cursor.fetchone()

        return rowcount[0]

    def circuit_filter(
        self,
        type: str,
        classify: str,
        max_width=None, max_size=None, max_depth=None
    ) -> list:
        """ Get list of qasm file's name which satisfied the condition. """
        based_sql_cmd = "SELECT NAME FROM CIRCUIT_LIB WHERE "
        condition_cmd = f"TYPE=\'{type}\' AND CLASSIFY=\'{classify}\'"
        if isinstance(max_width, int):
            condition_cmd += f" AND WIDTH<=\'{max_width}\'"
        elif isinstance(max_width, list):
            width_str = ", ".join([str(w) for w in max_width])
            condition_cmd += " AND WIDTH IN (%s)" % width_str

        if max_size is not None:
            condition_cmd += f" AND SIZE<=\'{max_size}\'"

        if max_depth is not None:
            condition_cmd += f" AND DEPTH<=\'{max_depth}\'"

        sql_cmd = based_sql_cmd + condition_cmd
        self._cursor.execute(sql_cmd)

        return self._cursor.fetchall()

    def _create_table(self):
        # Temp add here, delete after create datebase
        self._cursor.execute(
            'CREATE TABLE CIRCUIT_LIB(' +
            'ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME text, TYPE text, CLASSIFY text, ' +
            'WIDTH INT, SIZE INT, DEPTH INT)'
        )

    def circuit_exist(self, file_name: str):
        self._cursor.execute(f"SELECT * FROM CIRCUIT_LIB WHERE NAME=\'{file_name}\'")
        file_info = self._cursor.fetchone()

        return file_info is not None

    def add_template_circuit(self):
        file_path = os.path.join(
            self._file_path,
            "template"
        )

        for file in filter(lambda x: x.endswith('.qasm'), os.listdir(file_path)):
            _, width, size, depth, _ = file.split("_")
            width = int(width[1:])
            size = int(size[1:])
            depth = int(depth[1:])

            self._cursor.execute(
                "INSERT INTO CIRCUIT_LIB(NAME, TYPE, CLASSIFY, WIDTH, SIZE, DEPTH)" +
                f"VALUES (\'{file}\', \'template\', \'template\', " +
                f"\'{width}\', \'{size}\', \'{depth}\')"
            )

        self._connect.commit()

    def add_circuit(self, type_: str):
        file_path = os.path.join(
            self._file_path,
            type_
        )

        for classify in os.listdir(file_path):
            if classify == ".keep":
                continue

            folder = os.path.join(file_path, classify)
            for file in filter(lambda x: x.endswith('.qasm'), os.listdir(folder)):
                width, size, depth = file.split("_")[:3]
                width = int(width[1:])
                size = int(size[1:])
                if ".qasm" not in depth:
                    depth = int(depth[1:])
                else:
                    depth = int(depth[1:-5])

                self._cursor.execute(
                    "INSERT INTO CIRCUIT_LIB(NAME, TYPE, CLASSIFY, WIDTH, SIZE, DEPTH)" +
                    f"VALUES (\'{file}\', \'{type_}\', \'{classify}\', " +
                    f"\'{width}\', \'{size}\', \'{depth}\')"
                )

        self._connect.commit()
