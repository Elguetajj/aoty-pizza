from random import randint

class Heaper:
    @classmethod        
    def maxheap(cls, arr, n, i): 
        largest = i  
        left_child = 2 * i + 1    
        right_child = 2 * i + 2     
        
        if left_child < n and arr[i]["rating"] < arr[left_child]["rating"]: 
            largest = left_child
     
        if right_child < n and arr[largest]["rating"] < arr[right_child]["rating"]: 
            largest = right_child
     
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] 
            cls.maxheap(arr, n, largest) 

    @classmethod
    def minheap(cls,arr, n, i):
        largest = i  
        left_child = 2 * i + 1    
        right_child = 2 * i + 2     
        
        if left_child < n and arr[i]["rating"] > arr[left_child]["rating"]: 
            largest = left_child
     
        if right_child < n and arr[largest]["rating"] > arr[right_child]["rating"]: 
            largest = right_child
     
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] 
            cls.minheap(arr, n, largest) 


    
    @classmethod
    def heapSort(cls, arr:list, descending:bool=False): 
        n = len(arr) 
        if (descending == True):
              # Build a minheap. 
            for i in range(n//2 - 1, -1, -1): 
                cls.minheap(arr, n, i) 
        
            # One by one extract elements 
            for i in range(n-1, 0, -1): 
                arr[i], arr[0] = arr[0], arr[i]
                cls.minheap(arr, i, 0) 
        
        else:
            # Build a maxheap. 
            for i in range(n//2 - 1, -1, -1): 
                cls.maxheap(arr, n, i) 
        
            # One by one extract elements 
            for i in range(n-1, 0, -1): 
                arr[i], arr[0] = arr[0], arr[i]
                cls.maxheap(arr, i, 0) 

