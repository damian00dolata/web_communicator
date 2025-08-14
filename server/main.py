#################################
#   uvicorn main:app --reload   #
#               or              # 
#        python ./main.py       #
#################################

import uvicorn
from server.restapi import RestAPI
from server.sockio import SockIO
from server.dbase import Database
from server.utils.error_handler import add_exception_handlers

class MainApp:
  def __init__(self) -> None:
    self.sio = SockIO()
    self.db = Database()
    self.restApi = RestAPI(self.db, self.sio)
    add_exception_handlers(self.restApi.app, debug=True)
    
if __name__ == '__main__':
  uvicorn.run('server.main:mainApp.restApi.app')
    
mainApp = MainApp()