import unittest
import lisbre_uni3

class MyTestCase(unittest.TestCase):
    def test_accion(self):
        a=[[0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,1,0,0,0,1],
           [0,0,0,1,0,0],
           [0,0,1,0,0,0],
           [1,0,0,0,1,0]]
        b=[[6],
           [2],
           [1],
           [5],
           [3],
           [10]]
        d=1
        c=[[0], [0], [9], [5], [12], [1]]
        self.assertEqual(lisbre_uni3.canic(a,b,d), c)
    def test_canic(self):
        a=[[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [1/6,1/3,0,1,0,0,0,0],
           [1/6,1/3,0,0,1,0,0,0],
           [1/3,1/3,1/3,0,0,1,0,0],
           [1/6,0,1/3,0,0,0,1,0],
           [1/6,0,1/3,0,0,0,0,1]]
        b=[[1],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0],
           [0]]
        d=2
        c=[[0], [0], [0], [1/6], [1/6], [1/3], [1/6], [1/6],]
        self.assertEqual(lisbre_uni3.canic(a,b,d), c)

if __name__ == '__main__':
    unittest.main()