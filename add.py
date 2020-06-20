def add(a, b):
    return a + b

def faster_add(a, b):
    return a + b

import unittest
import random
class TestAddition(unittest.TestCase):
    def test_add(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = add(a, b)
        self.assertEqual(c, a + b)

    def test_fasteradd(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = faster_add(a, b)
        self.assertEqual(c, a + b)

if __name__ == '__main__':
    unittest.main()