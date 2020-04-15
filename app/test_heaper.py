import unittest
import time
from heaper import Heaper
from random import randint
from datetime import datetime


class TestHeap(unittest.TestCase):

    def fill_array(self,arr):
        for i in range(1000):
            arr.append({"rating": randint(0,5)})

    def test_sort(self):
        arr= []
        self.fill_array(arr)
        expected  = sorted(arr, key=lambda k: k['rating']) 
        Heaper.heapSort(arr)
        self.assertEqual(arr,expected)


if __name__ == '__main__':
   log_file = './logs/heaper_test_log.txt'
   with open(log_file, "a+") as f:
        f.write('Heaper_test:'+str(datetime.now()))
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)