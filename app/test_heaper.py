import unittest
import time
from heaper import Heaper
from random import randint
from datetime import datetime


class TestHeap(unittest.TestCase):

    def fill_array(self,arr):
        for i in range(1000):
            arr.append({"rating": randint(0,5)})

    def test_sort_descending(self):
        arr= []
        self.fill_array(arr)
        expected  = sorted(arr, key=lambda k: k['rating'], reverse = True) 
        Heaper.heapSort(arr,"rating",True)
        self.assertEqual(arr,expected)

    def test_sort_ascending(self):
        arr= []
        self.fill_array(arr)
        expected  = sorted(arr, key=lambda k: k['rating'])
        Heaper.heapSort(arr, "rating")
        self.assertEqual(arr,expected)



if __name__ == '__main__':
    log_file = './logs/heaper_test_log.txt'
    with open(log_file, "a+") as f:
        f.write('Heaper_test:'+str(datetime.now()))
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
