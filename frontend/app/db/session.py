from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("postgresql://postgres:RFLfZRhuhauJlrwpFzIBZfcJywUxSqEl@maglev.proxy.rlwy.net:45225/railway")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
