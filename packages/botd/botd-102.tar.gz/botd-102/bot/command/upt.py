# This file is placed in the Public Domain.


"uptime"


import time


from bot.utility import elapsed


def __dir__():
    return (
            'upt'
           )


starttime = time.time()


def upt(event):
    "show uptime"
    event.reply(elapsed(time.time()-starttime))
