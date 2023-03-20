import unittest

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover("testcase", "test*.py")
    runer = unittest.TextTestRunner()
    runer.run(suite)