#!/usr/bin/env python3
import i3ipc
import psutil


def exit_lemonbar():
    PROCNAME = ["lemonbar", "i3_lemonbar.sh"]
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() in PROCNAME:
            proc.kill()


def on_shutdown(conn):
    print('Exiting lemonbar...')
    exit_lemonbar()
    print('Closing i3 session')


conn = i3ipc.Connection()

conn.on('ipc_shutdown', on_shutdown)

conn.main()
