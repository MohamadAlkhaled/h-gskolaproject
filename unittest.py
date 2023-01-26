import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_add_tuple(self):
        result = add((1, 2), (3, 4))
        self.assertEqual(result, (1, 2, 3, 4))

if __name__ == '__main__':
    unittest.main()