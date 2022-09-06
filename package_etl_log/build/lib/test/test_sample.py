import unittest
from src.package_etl_log import etl_log

class TestETLLog(unittest.TestCase):

    def test_createLogs(self):
        with self.assertRaises(Exception):
            etl_log.create_logs()


    def test_set_status(self):
        etl_log.set_statusFalse()
        self.assertFalse(etl_log.get_status())
        etl_log.set_statusTrue()
        self.assertTrue(etl_log.get_status())


if __name__ == '__main__':
    unittest.main()