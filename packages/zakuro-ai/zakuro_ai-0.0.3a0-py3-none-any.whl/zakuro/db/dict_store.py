import os

class DictStore:
    def __init__(self, tasks_db='tasks_db'):
        self.store = dict()
        self.pid = f"(pid {os.getpid()})"
        self.tasks_db = tasks_db
        self.verbose = False

    def select_all(self):
        return self.store

    def select(self, id):
        return self.store[id]

    def insert(self, _id, d):
        self.store[_id] = d

    def update(self, _id, d1):
        self.store[_id].update(d1)

