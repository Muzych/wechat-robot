import itchat
from itchat.content import *


def app_run():
    @itchat.msg_register(["Text"], isGroupChat=True)
    def group_reply(msg):
        if msg.startswith("draw"):
            msg.user.send("")

    itchat.auto_login()
    itchat.run()


if __name__ == "__main__":
    app_run()
    # 进入Bot文件夹 再结合Bridge文件夹找答案
    # TODO 支持可灵文生图大模型
