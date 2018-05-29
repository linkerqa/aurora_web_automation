# -*- coding: utf-8 -*-

import os
import unittest
from common.test_report import CreateReport
from test_cases.tc_create_dataset import CreateDataset
from test_cases.tc_edit_dataset import EditDataset
from test_cases.tc_edit_image import EditImage


if __name__ == '__main__':
    suite = unittest.TestSuite()
    cases = [CreateDataset("test_create_dataset"),
             EditImage("test_edit_image"),
             EditDataset("test_edit_dataset")]
    suite.addTests(cases)
    suite_name = os.path.basename(__file__)[3:-3]

    test_report = CreateReport()
    test_report.create_report(suite, suite_name)