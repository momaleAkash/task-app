from sqlalchemy.orm import declarative_base

Base = declarative_base()

# IMPORT ALL MODELS HERE
from app.models.task import Task
