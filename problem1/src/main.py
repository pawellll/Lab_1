#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

import sys

from SystemMonitorDaemon import SystemMonitorDaemon
from Configuration import Configuration as Conf
import argparse


def setup_parser():
    par = argparse.ArgumentParser(description="System monitor daemon")

    par.add_argument('action', choices=[Conf.ARG_START, Conf.ARG_STOP, Conf.ARG_RESTART])
    par.add_argument(Conf.ARG_CPU, action="store_true", help=Conf.ARG_CPU_HELP)
    par.add_argument(Conf.ARG_MEM, action="store_true", help=Conf.ARG_MEM_HELP)
    par.add_argument(Conf.ARG_NET, action="store_true", help=Conf.ARG_NET_HELP)

    return par


if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()

    daemon = SystemMonitorDaemon(Conf.PID_FILE_PATH)

    if args.action == "start":
        mode = ""
        if getattr(args, Conf.ARG_CPU[1:]):
            mode += "c"
        if getattr(args, Conf.ARG_MEM[1:]):
            mode += "m"
        if getattr(args, Conf.ARG_NET[1:]):
            mode += "n"

        if not mode:
            mode = "cnm"
        daemon.set_mode(mode)
        daemon.start()
    elif args.action == "stop":
        daemon.stop()
    elif args.action == "restart":
        daemon.restart()

