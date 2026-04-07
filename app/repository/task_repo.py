class TaskRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.query(Task).all()
