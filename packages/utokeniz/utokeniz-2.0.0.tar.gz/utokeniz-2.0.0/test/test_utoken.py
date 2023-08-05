import unittest
import sys

sys.path.insert(0, './')

from utoken import encode, decode
from utoken.exceptions import InvalidKeyError, InvalidTokenError


class TestUtoken(unittest.TestCase):
    def setUp(self) -> None:
        self.content_1 = {'message': 'Test'}
        # content_2 = {'message': 'UnitTest'}

        self.key_1 = 'FirstKey'
        self.key_2 = 'SecondKey'

        self.token_1 = encode(self.content_1, self.key_1)
        self.token_2 = encode(self.content_1, self.key_2)
        self.token_3 = 'fake_token'

    def test_key_decode(self):
        decode_key_1 = decode(self.token_1, self.key_1)
        self.assertEqual(decode_key_1, self.content_1)

        decode_key_2 = decode(self.token_2, self.key_2)
        self.assertEqual(decode_key_2, self.content_1)

        with self.assertRaises(InvalidKeyError):
            decode(self.token_1, self.key_2)

        with self.assertRaises(InvalidTokenError):
            decode(self.token_3, self.key_1)


if __name__ == '__main__':
    unittest.main()
