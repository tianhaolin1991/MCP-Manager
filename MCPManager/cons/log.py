import logging
import os
from datetime import datetime

from cons.constants import WORK_DIR

# 屏蔽三方库LOG
logging.getLogger("mcp.client.sse").setLevel(logging.CRITICAL)
logging.getLogger("mcp.client.sse").propagate = False
logging.getLogger("mcp.client.stdio").setLevel(logging.CRITICAL)
logging.getLogger("mcp.client.stdio").propagate = False

def setup_loggers(logger):
    os.makedirs(f'{WORK_DIR}//logs', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    run_log_file = f'{WORK_DIR}//logs//run_{timestamp}.log'
    # 设置运行日志
    file_handler = logging.FileHandler(run_log_file, encoding='utf-8')
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    console_handler = logging.StreamHandler()  # 默认输出到sys.stdout（控制台）
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')  # 控制台日志格式可简化
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False

LOGGER = logging.getLogger('MCP_MANAGER')
setup_loggers(LOGGER)
