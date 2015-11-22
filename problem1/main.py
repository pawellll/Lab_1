#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

import sys
import time
import logging
import os
import subprocess
from Configuration import Configuration as Conf
from Daemon import Daemon


class SystemMonitorDaemon(Daemon):
    """Daemon class providing system monitoring for cpu, memory and network"""
    def __init__(self, pidfile):
        Daemon.__init__(self,pidfile)
        self._cpu = False
        self._network = False
        self._memory = False

    def run(self):
        while True:
            if self._cpu:
                self._log_state(Conf.CPU_COMMAND)

            if self._memory:
                self._log_state(Conf.MEM_COMMAND)

            if self._network:
                self._log_state(Conf.NET_COMMAND)

            time.sleep(1)

    def _log_state(self,command):
        logging.info(self._run_bash(command))

    """set mode for system monitor c=CPU,n=NETWORK,m=MEMORY"""
    def set_mode(self, mode):
        self._setup_logging(Conf.LOGGING_PATH, Conf.LOGGING_LEVEL, Conf.LOGGING_FORMAT)
        self._cpu = True if 'c' in mode else False
        self._network = True if 'n' in mode else False
        self._memory = True if 'm' in mode else False

    """Run bash command"""
    @staticmethod
    def _run_bash(command):
        call_bash = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
        return call_bash.communicate()[0]

    """Setup logging for class"""
    @staticmethod
    def _setup_logging(log_path, logging_level, logging_format):
        # remove log file if exists
        try:
            os.remove(log_path)
        except OSError:
            pass

        logging.basicConfig(filename=log_path, level=logging_level, format=logging_format)
        logging.info("Logging has been initialised")


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
