#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

import unittest
from SystemMonitorDaemon import SystemMonitorDaemon
from Configuration import Configuration as Conf


class SystemMonitorDaemonTest(unittest.TestCase):
    def test_set_mode(self):
        daemon = SystemMonitorDaemon(Conf.PID_FILE_PATH)
        mode = "mnc"
        daemon.set_mode(mode)
        self.assertTrue(daemon._memory)
        self.assertTrue(daemon._network)
        self.assertTrue(daemon._cpu)

    def test_init(self):
        daemon = SystemMonitorDaemon(Conf.PID_FILE_PATH)
        self.assertEqual(Conf.PID_FILE_PATH, daemon.pidfile)
        self.assertFalse(daemon._memory)
        self.assertFalse(daemon._network)
        self.assertFalse(daemon._cpu)


if __name__ == '__main__':
    unittest.main()
