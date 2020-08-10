import unittest

import requests


class AUatTest(unittest.TestCase):
    def test_we_can_hit_the_service(self):
        response = requests.get("http://local_steam_server:5000/")
        self.assertEqual(response.text, "Hello, World!")


if __name__ == '__main__':
    unittest.main()
