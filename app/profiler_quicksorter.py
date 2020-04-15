import cProfile
from quicksorter import Quicksorter
from random import randint
import sys
from memory_profiler import profile
from datetime import datetime

arr= []


sys.stdout = open('./logs/profiler_quicksorter_log.txt', 'a+')


@profile
def profile_quicksorter():
    Quicksorter.quick_sort(arr,0,len(arr)-1)

for i in range(700):
    arr.append({"rating": randint(0,5)})

try:
    print(f'-------------------------------------Quicksorter profile:{datetime.now()}')
    print(f'{len(arr)} elements')
    print("Performance profiling:")
    cProfile.run('Quicksorter.quick_sort(arr,0,len(arr)-1)')
    print("Memory Profiling:")
    profile_quicksorter()

except Exception as e:
    print(f"Error Ocurred: {e}")

