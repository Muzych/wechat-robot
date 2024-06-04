import time

from common.log import logge


def run():
    try:
        while True:
            logge.info("This is an info message.")
            time.sleep(1)
    except Exception as e:
        logge.error("App startup failed!")
        logge.exception(e)


if __name__ == "__main__":
    run()
