#################################
#   uvicorn main:app --reload   #
#               or              # 
#        python ./main.py       #
#################################

import uvicorn
from restapi import RestAPI
from sockio import SockIO
from dbase import Database

class MainApp:
  def __init__(self) -> None:
    self.sio = SockIO()
    self.db = Database()
    self.restApi = RestAPI(self.db, self.sio)
    
if __name__ == '__main__':
  uvicorn.run('main:mainApp.restApi.app')
    
mainApp = MainApp()