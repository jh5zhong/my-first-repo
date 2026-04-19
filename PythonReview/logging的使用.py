#只有warning,error,critical有信息打印
import logging
s = "有错误"
logging.debug(s)
logging.info(s)
logging.warning(s)
logging.error(s)
logging.critical("This is critical log")
