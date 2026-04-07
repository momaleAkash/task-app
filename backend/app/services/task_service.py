from app.core.cache import get_cache, set_cache

class TaskService:
    def __init__(self, repo):
        self.repo = repo

    def get_tasks(self):
        cached = get_cache("tasks")
        if cached:
            return cached

        tasks = self.repo.get_all()
        result = [t.__dict__ for t in tasks]

        set_cache("tasks", result)
        return result
