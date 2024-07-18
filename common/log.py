import sys

from loguru import logger


def _reset_logger():
    # 移除所有默认的处理器
    logger.remove()

    # 添加控制台处理器
    logger.add(
        sys.stdout,
        colorize=True,
        format="[<level>{level}</level>][<green>{time:YYYY-MM-DD HH:mm:ss}</green>][{file}:{line}] - {message}",
        level="INFO",
    )

    # 添加文件处理器
    logger.add(
        "run.log",
        backtrace=True,
        diagnose=True,
        format="[<level>{level}</level>][{time:YYYY-MM-DD HH:mm:ss}][{file}:{line}] - {message}",
        level="INFO",
        encoding="utf-8",
        rotation="20 MB",
    )


def _get_logger():
    _reset_logger()
    return logger


# 日志句柄
logge = _get_logger()
