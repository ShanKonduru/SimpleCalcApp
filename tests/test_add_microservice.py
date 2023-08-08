import unittest
import requests
from config import ADD_MICROSERVICE_PORT

class TestAddMicroservice(unittest.TestCase):
    def test_add(self):
        data = {
            'num1': 5,
            'num2': 10
        }
        response = requests.post('http://localhost:{ADD_MICROSERVICE_PORT}/add', json=data)
        result = response.json()['result']
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
