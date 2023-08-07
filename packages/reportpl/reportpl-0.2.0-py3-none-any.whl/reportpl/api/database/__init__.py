from reportpl.api import config
from .db_class import DB

db = DB(config.DATABASE_URI)