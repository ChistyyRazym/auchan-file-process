from auchan_file_process.process_files import process_files
from auchan_file_process.settings import Settings
from auchan_file_process.json_logging import logger


setting = Settings()

directory_paths = setting.input_dir

logger.debug("start file process")
try:
    process_files(directory_paths)
except Exception as error:
    logger.debug(error)
else:
    logger.debug("end file process")
