#!/usr/bin/env python
# (c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017

import unittest
import os, os.path
from parser import do_request

class TestParsingMethods(unittest.TestCase):

    def test_number_of_results(self):
    	url = "file://"+ os.path.abspath("./test/data.sample")
        self.assertEqual(len(do_request(url)), 50)

if __name__ == '__main__':
    unittest.main()