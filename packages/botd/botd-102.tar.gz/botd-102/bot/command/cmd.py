# This file is placed in the Public Domain.


"commands"


from bot.handler import Command


def __dir__():
    return (
            'cmd',
           )


def cmd(event):
    "list commands"
    event.reply(",".join(sorted(Command.cmd)))
