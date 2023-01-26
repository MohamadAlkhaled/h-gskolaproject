import unittest

def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def concat(a,b):
 return a + " " + b


class Test(unittest.TestCase):

    def test_add(self):
        result = add(1, 2)
        self.assertEqual(result, 3)
    
    def test_sub(self):
         result = sub(4,1)
         self.assertGreater(result, 2)
    
    def test_concat(self):
        result =concat("Hello","World")
        self.assertEqual(result, "Hello World")
   

if __name__ == '__main__':
    unittest.main()
