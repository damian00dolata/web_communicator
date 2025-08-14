import uvicorn
from restapi import RestAPI
from sockio import SockIO
from dbase import Database
from utils.error_handler import add_exception_handlers

class MainApp:
  def __init__(self) -> None:
    self.sio = SockIO()
    self.db = Database()
    self.restApi = RestAPI(self.db, self.sio)
    add_exception_handlers(self.restApi.app, debug=True)
    
if __name__ == '__main__':
  uvicorn.run('main:mainApp.restApi.app')
    
mainApp = MainApp()