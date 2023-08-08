import unittest
import requests
from config import DIVIDE_MICROSERVICE_PORT

class TestDivideMicroservice(unittest.TestCase):
    def test_divide(self):
        data = {
            'num1': 50,
            'num2': 10
        }
        response = requests.post('http://localhost:{DIVIDE_MICROSERVICE_PORT}/divide', json=data)
        result = response.json()['result']
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
