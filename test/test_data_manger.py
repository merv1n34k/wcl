#!/usr/bin/env python3
import os
import sys
import unittest
from pathlib import Path

ROOT_PATH = str(Path(os.path.dirname(os.path.realpath(__file__))).parent)
sys.path.append(ROOT_PATH)

class DataManagerTest(unittest.TestCase):
    def setUp(self):
        print('up')

    def tearDown(self):
        print('down')

    def test_foo(self):
        print('foo')

    def test_bar(self):
        print('bar')

if __name__ == '__main__':
    unittest.main()
