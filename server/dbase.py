import sqlite3
from sqlite3 import Error
from pathlib import Path
from utils.debug_logger import log_info, log_error

class Database:
  def __init__(self) -> None:
    BASE = Path(__file__).resolve().parent
    DB_PATH = (BASE.parent / "database" / "communicator.db")
    SCHEMA_PATH = (BASE / "schema.sql")
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    log_info("[DB-INFO] Database path initialized.", path=str(DB_PATH))
    
    self.conn = self.create_connection(DB_PATH)
    if self.conn is not None:
      self.apply_schema(self.conn, SCHEMA_PATH)
      self.logoutUsers(self.conn)
    else:
      log_error("[DB-ERROR] Cannot create the database connection", path=str(DB_PATH))

  def create_connection(self, db_file: Path) -> sqlite3.Connection:
    try:
      conn = sqlite3.connect(db_file, detect_types=sqlite3.PARSE_DECLTYPES)
      conn.execute("PRAGMA foreign_keys = ON")
      log_info("[DB-INFO] Database connection established", db_file=str(db_file))
      return conn
    except Error as e:
      log_error("[DB-ERROR] Error while connecting to database", error=str(e), db_file=str(db_file))
      raise

  def apply_schema(self, conn: sqlite3.Connection, schema_path: Path):
    try:
      sql = schema_path.read_text(encoding="utf-8")
      conn.executescript(sql)
      conn.commit()
      log_info("[DB-INFO] Schema applied.", schema_path=schema_path)
    except Error as e:
      log_error("[DB-ERROR] Error while applying schema", error=str(e), schema_path=schema_path)

      conn.rollback()
   
  def logoutUsers(self, conn):
    cur = conn.cursor()
    sql = ''' UPDATE users
              SET isLogged=0 '''
    cur.execute(sql)
    conn.commit()