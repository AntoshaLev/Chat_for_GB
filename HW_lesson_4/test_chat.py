import sys

sys.path.append('../HW_lesson_3/')

import unittest
from HW_lesson_3 import chat


class TestChat(unittest.TestCase):
    """ Тестирование чата """

    def setUp(self):
        self.s = chat.get_server_socket('localhost', 7777)
        self.c = chat.get_client_socket('localhost', 7777)
        self.sender = self.s.accept()[0]

        chat.send_data(self.c, {'test': 'test'})

    def tearDown(self):
        self.c.close()
        self.s.close()

    def test_get_data(self):
        self.assertEqual(chat.get_data(self.sender), {'test': 'test'})

    def test_send_data(self):
        with self.assertRaises(TypeError):
            chat.send_data()


if __name__ == '__main__':
    unittest.main()
