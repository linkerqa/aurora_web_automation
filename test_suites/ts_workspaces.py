# -*- coding: utf-8 -*-

import os
import unittest
from common.test_report import CreateReport
from test_cases.tc_create_workspace import CreateWorkspace

if __name__ == "__main__":
    suite = unittest.TestSuite()
    cases = [CreateWorkspace("test_create_workspace")]
    suite.addTests(cases)
    suite_name = os.path.basename(__file__)[3:-3]

    test_report = CreateReport()
    test_report.create_report(suite, suite_name)
