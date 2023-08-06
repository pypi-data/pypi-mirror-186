import time

import sqlite3

import os
from tqdm import tqdm
import json
from gnutools.utils import id_generator


from datetime import datetime
class SQLiteStore:
    def __init__(self, tasks_db='tasks_db'):
        self.schema = dict([
            ("_id", "text NOT NULL PRIMARY KEY"),
            ("status", "text"),
            ("requested_by", "text"),
            ("executed_by", "text"),
            ("module", "text"),
            ("function", "text"),
            ("args", "text"),
            ("kwargs", "text"),
            ("result", "text")
        ])
        self.pid = f"(pid {os.getpid()})"
        self.tasks_db = tasks_db
        self.init_table()
        self.verbose = False



    def select_all(self):
        with sqlite3.connect(self.tasks_db, timeout=-1) as conn:
            c = conn.cursor()
            results = list(c.execute('''SELECT * from tasks'''))
            if len(results)==0:
                return []
            results = dict([(r[0], r[1:]) for r in results])
        return results
    def init_table(self):
        with sqlite3.connect(self.tasks_db, timeout=-1) as conn:
            c = conn.cursor()
            # Create table
            try:
                kv =[f"{k} {v}" for k, v in self.schema.items()]
                command = f"CREATE TABLE tasks ({','.join(kv)}) "
                c.execute(f'''{command}''')
            except sqlite3.OperationalError as e:
                if e.args[0] == 'table tasks already exists':
                    pass
            except Exception as e:
                    raise e

    def select(self, id):
        with sqlite3.connect(self.tasks_db, timeout=-1) as conn:
            command = f"SELECT * FROM tasks WHERE _id='{id}'"
            result = list(conn.execute(command))
            if len(result)==0:
                return None
            assert len(result)==1
            task = result[0]
            return dict([(k, v) for k, v in zip(self.schema.keys(), task)])

    def __update_from_id(self, conn, _id, d0, d1=None, wait=True, return_result=True):
        assert d1 is not None
        assert d0 is not None
        while True:
            try:
                condition1 = ", ".join(["=".join([k, f"'{v}'"]) for k, v in d1.items()])
                if d0 is not None:
                    condition0 = "AND ".join(["=".join([k, f"'{v}'"]) for k, v in d0.items()])
                    command = f"UPDATE tasks SET {condition1} WHERE _id='{_id}' AND {condition0}"
                else:
                    command = f"UPDATE tasks SET {condition1} WHERE _id='{_id}'"
                conn.execute(command)
                conn.commit()
                task = self.select(_id)
                print(f"{self.pid} | {datetime.now()} >> Locking") if self.verbose else None
                return task if return_result else None
            except sqlite3.OperationalError as e:
                if e.args[0] == 'database is locked':
                    # print(f"{pid} | {datetime.now()} >> {e}")
                    if wait:
                        time.sleep(0.01)
                    else:
                        break
                else:
                    raise e
            except Exception as e:
                print(_id)
                raise e

    def __insert(self, conn, d, wait=True):
        """
        Wait until the insert operation is done

        :param conn:
        :param d:
        :param wait:
        :return:
        """
        while True:
            try:
                columns = ', '.join(list(d.keys()))
                alloc = ', '.join(['?'] * len(list(d.values())))
                command = f"INSERT INTO tasks({columns}) VALUES({alloc})"
                conn.execute(command, list(d.values()))
                print(f"{self.pid} | {datetime.now()} >> Locking") if self.verbose else None
                conn.commit()
                print(f"{self.pid} | {datetime.now()} >> Unlocking") if self.verbose else None
                # print("++", d)
                break

            except sqlite3.OperationalError as e:
                if e.args[0] == 'database is locked':
                    # print(f"{pid} | {datetime.now()} >> {e}")
                    if wait:
                        time.sleep(0.01)
                    else:
                        break
                else:
                    raise e
            except Exception as e:
                raise e

    def insert(self, _id, d, wait=True):
        with sqlite3.connect(self.tasks_db, timeout=-1) as conn:
            # _id = "_id" # f"x{id_generator(12)}.{datetime.now()}"
            d.update({"status": "todo", "requested_by": self.pid, "_id": _id})
            try:
                self.__insert(conn, d, wait)
                # self.select(_id)
                return _id
            except Exception as e:
                del d["requested_by"]
                del d["_id"]
                raise e


    def update(self, _id, d1):
        with sqlite3.connect(self.tasks_db, timeout=-1) as conn:
            task = self.__update_from_id(conn=conn, _id=_id, d0={"_id": _id}, d1=d1)


    def execute(self, _id, wait=True):
        pass
        # with sqlite3.connect(self.tasks_db, timeout=-1) as conn:
        #     task = self.__update_from_id(conn=conn, _id=_id, d0={"status": "todo"}, d1={"status": "doing", "executed_by": self.pid})
        # with sqlite3.connect(self.tasks_db, timeout=-1) as conn:
        #     task = self.__update_from_id(conn=conn, _id=_id, d0={"status": "doing"}, d1={"status": "done", "result": "result"})
        #     a=1


