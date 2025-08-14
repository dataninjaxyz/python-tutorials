import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")

x = 44
logging.info("This is an info, value of x: %d", x)

y = {"name": "DataNinja", "occupation": "Python nerd", "email": "info@dataninja.xyz"}
logging.info("This is an info, logging complex data: %s", y)
