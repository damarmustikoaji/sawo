import unittest
import sys
import time
from selenium import webdriver

LOGIN = None

class BelajarTest(unittest.TestCase):

    SERVER = None
    EMAIL = None
    PASSWORD = None
    BROWSER = None

    @classmethod
    def setUpClass(cls):
        if cls.BROWSER == "Chrome":
            cls.driver = webdriver.Chrome(executable_path='driver/chromedriver')
        elif cls.BROWSER == "PhantomJS":
            cls.driver = webdriver.PhantomJS(executable_path='driver/phantomjs')
        elif cls.BROWSER == "Firefox":
            cls.driver = webdriver.Firefox(executable_path='driver/geckodriver')
        elif cls.BROWSER == "Opera":
            cls.driver = webdriver.Opera(executable_path='driver/operadriver')
        elif cls.BROWSER == "Mobile":
            mobile_emulation = {
            "deviceName": "iPhone 5"
            #"deviceName": "Nexus 5"
            }
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            cls.driver = webdriver.Chrome(executable_path='driver/chromedriver', chrome_options=chrome_options)
        else:
            assert False, "Browser driver not found '"+cls.BROWSER+"'"
        cls.driver.set_window_size(1280, 800)

    def test_a_login(self):
        global LOGIN
        self.startTime = time.time()
        self.driver.get(self.SERVER)
        assert "Google" in self.driver.title
        print self.driver.title
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    command = len(sys.argv)
    if command == 5:
        BelajarTest.BROWSER = sys.argv.pop()
        BelajarTest.SERVER = sys.argv.pop()
        BelajarTest.PASSWORD = sys.argv.pop()
        BelajarTest.EMAIL = sys.argv.pop()
    else:
        sys.exit("ERROR : Please check again your argument")
    suite = unittest.TestLoader().loadTestsFromTestCase(BelajarTest)
    unittest.TextTestRunner(verbosity=0).run(suite)
