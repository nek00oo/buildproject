import unittest
from build import mypow


class mypowtest(unittest.TestCase):
    def test(self):
        self.assertEquals(mypow(1, 2), 1)
        self.assertEquals(mypow(2, 2), 4)
        self.assertEquals(mypow(3, 2), 9)
        
