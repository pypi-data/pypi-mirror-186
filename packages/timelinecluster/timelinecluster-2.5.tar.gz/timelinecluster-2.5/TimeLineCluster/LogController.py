import logging
from datetime import datetime
class LogController:

    def __init__(self, text="", app="", path_log_app=""):
        self.app_name = app
        self.text_long = text
        self.logger = logging.getLogger(app)
        self.logger.setLevel(logging.DEBUG)
        self.path_log_app = path_log_app
    def genLog(self, message, level):
        file_name = self.path_log_app + datetime.now().strftime("%Y_%m_%d") + ".log"
        fh = logging.FileHandler(file_name, encoding = "UTF-8")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        if(level == "info"):
            self.logger.info(message)  
        else:
            self.logger.error(message)
        self.logger.handlers.clear()
        return True
            
    def convertDf2StringForLog(self, data , key):
        val_str = ""
        i = 0
        for item in data.iloc:
            if(i > 0):
                val_str += ", " + str(item[key])
            else:
                val_str += str(item[key])
            i += 1
        return str(key) + " : " + "[" + str(val_str) + "]" 