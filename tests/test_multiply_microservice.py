import unittest
import requests
from config import MULTIPLY_MICROSERVICE_PORT


class TestMultiplyMicroservice(unittest.TestCase):
    def test_multiply(self):
        data = {
            'num1': 5,
            'num2': 10
        }
        response = requests.post('http://localhost:{MULTIPLY_MICROSERVICE_PORT}/multiply', json=data)
        result = response.json()['result']
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()
