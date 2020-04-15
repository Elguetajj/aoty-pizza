import sys
import unittest
from quicksorter import Quicksorter
from random import randint
from datetime import datetime

class TestQuicksort(unittest.TestCase):

  
  def fill_array(self,arr):
    for i in range(1000):
        arr.append({"rating": randint(0,5)})

  def test_sort(self):
    arr= []
    self.fill_array(arr)
    expected  = sorted(arr, key=lambda k: k['rating'], reverse=True) 
    Quicksorter.quick_sort(arr,0,len(arr)-1)
    self.assertEqual(arr,expected)



if __name__ == '__main__':
   log_file = './logs/quicksorter_test_log.txt'
   with open(log_file, "a+") as f:
      f.write('Quicksorter_test:'+str(datetime.now()))
      runner = unittest.TextTestRunner(f)
      unittest.main(testRunner=runner)