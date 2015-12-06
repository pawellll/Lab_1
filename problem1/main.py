#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

import sys
from SystemMonitorDaemon import SystemMonitorDaemon
from Configuration import Configuration as Conf


def bad_usage_handler():
    print(Conf.USAGE)
    print(Conf.OPTIONS_DESC)
    sys.exit(2)


if __name__ == "__main__":
    daemon = SystemMonitorDaemon(Conf.PID_FILE_PATH)

    argLen = len(sys.argv)
    if argLen == 2:
        if 'start' == sys.argv[1]:
            print('Starting daemon in default mode (Network+Memory+Cpu)')
            daemon.set_mode('cnm')
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
    elif argLen == 3:
        if 'start' == sys.argv[1]:
            daemon.set_mode(sys.argv[2])
            print('Starting daemon in mode:%s' % sys.argv[2])
            daemon.start()
        else:
            bad_usage_handler()
    else:
        bad_usage_handler()
