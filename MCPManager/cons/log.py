import logging
import os
from datetime import datetime

from cons.constants import WORK_DIR


def setup_loggers(run_logger):
    os.makedirs(f'{WORK_DIR}//logs', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    # 设置运行日志
    run_log_file = f'{WORK_DIR}//logs//run_{timestamp}.log'
    run_handler = logging.FileHandler(run_log_file, encoding='utf-8')
    run_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    run_handler.setFormatter(run_formatter)
    run_logger.addHandler(run_handler)
    run_logger.setLevel(logging.INFO)


LOGGER = logging.getLogger('MCP_MANAGER')
setup_loggers(LOGGER)
