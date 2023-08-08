import unittest
import requests
from config import SUBTRACT_MICROSERVICE_PORT

class TestSubtractMicroservice(unittest.TestCase):
    def test_subtract(self):
        data = {
            'num1': 15,
            'num2': 5
        }
        response = requests.post('http://localhost:{SUBTRACT_MICROSERVICE_PORT}/subtract', json=data)
        result = response.json()['result']
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
