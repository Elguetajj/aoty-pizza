import cProfile
from heaper import Heaper
from random import randint
import sys
from memory_profiler import profile
from datetime import datetime


arr= []

sys.stdout = open('./logs/profiler_heaper_log.txt', 'a+')

@profile
def profile_heaper():
    Heaper.heapSort(arr)



for i in range(10000):
    arr.append({"rating": randint(0,5)})

try:
    print(f'-------------------------------------Heapsorter profile:{datetime.now()}')
    print(f'{len(arr)} elements')
    print("Performance profiling:")
    cProfile.run('Heaper.heapSort(arr)')
    print("Memory profiling:")
    profile_heaper()

except Exception as e:
    print(f"Error Ocurred: {e}")



    



