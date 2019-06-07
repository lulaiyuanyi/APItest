import unittest
import requests

class TestWeather(unittest.TestCase):
    def setUp(self):
        self.r = requests.session()
        self.url = "http://47.104.190.48:8000/weather_json/"
    def tearDown(self):
        self.r.close()

    def test_01(self):
        '''time=2019-04-05,city=上海'''

        par = {
        'time':'2019-04-05',
        'city':'上海'
        }

        self.r = requests.get(self.url,params=par)
        print(self.r.text)

        reason = self.r.json()["reason"]
        print(reason)
        exp = "success"
        # assert reason==exp
        self.assertTrue(reason==exp)






if __name__ == '__main__':
    unittest.main()
