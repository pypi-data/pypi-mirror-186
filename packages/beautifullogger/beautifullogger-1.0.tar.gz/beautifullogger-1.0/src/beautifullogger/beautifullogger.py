import logging
import termcolor
import sys

class BeautifulFormatter(logging.Formatter):

    mformat = "[{asctime}] {coloredlevel} @ {filename}:{lineno:<4d}: {message}"

    colors = {
        logging.DEBUG : ("grey", ""),
        logging.INFO  : ("green", ""),
        logging.WARNING  : ("green", "on_yellow"),
        logging.ERROR  : ("green", "on_red"),
        logging.CRITICAL  : ("white", "on_red"),
    }

    def get_colored_level(self, level, levelname) :
        if(levelname in self.colors) :
            (fontc, backc) = self.colors[levelname]
            if(fontc!="" and backc!=""):
                return termcolor.colored(" {:8s} ".format(levelname), fontc, backc)
            elif(fontc!=""):
                return termcolor.colored(" {:8s} ".format(levelname), fontc)
            elif(backc!=""):
                return termcolor.colored(" {:8s} ".format(levelname), backc)
            else:
                return " {:8s} ".format(levelname)
        else:
            return " {:8s} ".format(levelname)

    def format(self, record):
        record.coloredlevel=self.get_colored_level(record.levelno, record.levelname) 
        formatter = logging.Formatter(self.mformat, style='{')
        return formatter.format(record)



def make_beautiful(handler : logging.Handler) -> None:
    handler.setFormatter(BeautifulFormatter())


rootLogger = logging.getLogger()
stderr_handler = ()
log_handler =()

def setup_beautiful_logging(logfile:str ="log.txt", logmode:str ="a"):
    global stderr_handler
    global log_handler
    global rootLogger
    rootLogger.setLevel(0)
    stderr_handler = logging.StreamHandler(stream=sys.stderr)
    log_handler = logging.FileHandler(filename = logfile, mode = logmode)
    log_handler.setLevel(0)
    stderr_handler.setLevel(0)
    log_handler.formatter=logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s - %(message)s @ %(filename)s:%(lineno)s')
    make_beautiful(stderr_handler)
    rootLogger.addHandler(stderr_handler)
    rootLogger.addHandler(log_handler)

def addLevel(level, levelname, font_color="", background_color=""):
    logging.addLevelName(level, levelname.upper())
    stderr_handler.formatter.colors[level]=(font_color, background_color)

    def writeLog(self, msg):
        self.log(level, msg)

    logging.Logger.focus=writeLog
    setattr(logging.Logger, levelname.lower(), writeLog)

def setColor(level, font_color="", background_color=""):
    stderr_handler.formatter.colors[level]=(font_color, background_color)


# class BeautifulLogger(logging.logger):

#     __logger_handler_ = logging.StreamHandler()

#     @property
#     def FOCUS(self):
#         return 25


#     def __init__(self, name : str):
#         if logging.getLevelName(self.FOCUS )!="FOCUS" :
#             logging.addLevelName(self.FOCUS, "FOCUS")
#         self = logging.getLogger(str)
#         self .setLevel(logging.DEBUG)
#         self.addHandler(self.logger_handler)
#         make_beautiful(self.logger_handler)
#         self.logger_handler.setLevel(logging.DEBUG)
#         self.logger_handler.formatter.colors[self.FOCUS] = ("green", "on_magenta")
    
#     def set_colors(self, level : int, font_color="", background_color=""):
#         self.__logger_handler_.formatter.colors[level]=(font_color, background_color)



# def make_default_config(module_name : str, logfile : str ="log.txt") -> logging.Logger :
#     if(str=="__main__"):
#         logging.basicConfig(level=0, filename=logfile, filemode="a", format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s @ %(filename)s:%(lineno)s')
#         logging.info("New Run Start")
        
    
#     logger = logging.getLogger(str)
#     logger.setLevel(logging.DEBUG)
#     logger_handler = logging.StreamHandler()
#     logger.addHandler(logger_handler)
#     make_beautiful(logger_handler)
#     logger_handler.setLevel(logging.DEBUG)
#     logger_handler.formatter.colors["FOCUS"] = ("green", "on_magenta")
#     return logger
    

    




# Provided API

def setup_beautiful_logging(logfile:str ="log.txt", logmode:str ="a"):
    rootLogger = logging.getLogger()
    rootLogger.setLevel(0)
    stderr_handler = logging.StreamHandler(stream=sys.stderr)
    log_handler = logging.FileHandler(logfile, logmode)
    log_handler.setLevel(0)
    stderr_handler.setLevel(0)
    make_beautiful(stderr_handler)
    rootLogger.addHandler(stderr_handler)
    rootLogger.addHandler(log_handler)
    def changeColors(level, font_color="", background_color=""):
        stderr_handler.formatter.colors[level]=(font_color, background_color)
    rootLogger.setColors = changeColors


# def setup_logger(name:str, logfile:str ="log.txt", logmode:str ="a"):
#     """ 
#     Helper function to facilitate the adoption of loggers. 
#     If you are an advanced user of the logging library, you may not want to use it.

#     Creates (or modifies) the logger with name with the following default setting:
#         - All levels are log messages are displayed in a custom colored format (beautiful)
#         - The logger has a new level named focus between INFO and WARNING, accessible as logger.FOCUS, usable with logger.focus(msg)
#         - The logger has a method set_colors to change the color settings
#         - You may use all logger options of the logging library. 
#             The current default 
        
#     If the parameter name is "__main__" (i.e. the initial interpreted python file), 
#     then we also call basic_config to modify the root logger (to which all loggers pass messages to)
#     with a configuration that logs all messages file "logfile"
       
#     Args:
#         name (str): The name of the logger. Please use the variable __name__ for good default configuration.
#         logfile (str): The name of the file to log to for the root logger. Is only relevant if the parameter name is "__main__"
#         logmode (str): How the logfile should be opened. Defaults to append, but "w" could be a relevant choice.

#     Returns:
#         logger: the modified/created logger 


#     """
#     if(str=="__main__"):
#         logging.basicConfig(level=0, filename=logfile, filemode=logmode, format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s @ %(filename)s:%(lineno)s')
        
    
#     logger = logging.getLogger(str)
#     logger.setLevel(logging.DEBUG)
#     logger_handler = logging.StreamHandler()
#     logger.addHandler(logger_handler)
#     make_beautiful(logger_handler)
#     logger_handler.setLevel(logging.DEBUG)
#     logger_handler.formatter.colors["FOCUS"] = ("green", "on_magenta")
#     return logger
# make_beautiful(logger) -> logger.set_color(front, back)
# make_beautiful(handler) -> handler.set_color(font, back)
# 
