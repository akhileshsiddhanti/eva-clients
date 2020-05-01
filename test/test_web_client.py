import unittest 
from unittest import TestCase
from unittest.mock import patch
import asyncio
from clients.web_client import odbc_insert

class TestWebClient(TestCase):
    def setUp(self):
        return super().setUp()

    def testODBCInsert(self):
        output = odbc_insert()
        self.assertTrue("Row" in str(output))
    
    
if __name__ == "__main__":
    unittest.main()
    