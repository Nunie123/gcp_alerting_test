# test_python_scripts.py
import unittest

class TestScripts(unittest.TestCase):

    def test_script(self):
        self.assertTrue(1==1)
        self.assertTrue(1==0)

if __name__ == '__main__':
    unittest.main()