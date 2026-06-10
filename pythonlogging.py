# import logging
#filename lekhena vani by default consolema print hunxa
#level chai by default warning samma hunxa i.e 30
#by default append modema hunxa
# logging.basicConfig(filename='log.txt',level=logging.WARNING)
# logging.basicConfig(filename='log.txt',level=10,filemode="w")
#logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',filename='log.txt',level=10,filemode="w")
# logging.basicConfig(format='%(process)s:%(asctime)s:%(levelname)s:%(name)s:%(message)s',filename='log.txt',level=10,filemode="w",datefmt='%A %B %d/%m/%Y %I:%M:%S %p')
# print("This is demo of logging")
# logging.debug("This is code is corrected")
# logging.info("This is only information")
# logging.warning("This is warning information")
# logging.error("This is error information")
# logging.critical("This is critical information")

# import logging
# logging.basicConfig(filename='abc.txt',level=logging.WARNING)
# logging.info("Process Started")
# try:
#   x=int(input("Enter first number : "))
#   y=int(input("Enter second number : "))
#   print("The result is : ",x/y)
# except ZeroDivisionError as z:
#   print("Probably there is zero divison error.You need to check your log file for more info.")
#   logging.exception(z)
# except ValueError as v:
#   print("Probably there is value error.You need to check your log file for more info.")
#   logging.exception(v)
# logging.info("Proces Completed")

#Making own logger

import logging
logger=logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)
filehandler=logging.FileHandler("sujan.log",mode='w')
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")

