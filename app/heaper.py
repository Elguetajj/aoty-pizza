from random import randint

class Heaper:
    @classmethod        
    def maxheap(cls, arr, n, i, key:str): 
        largest = i  
        left_child = 2 * i + 1    
        right_child = 2 * i + 2     
        
        if left_child < n and arr[i][key] < arr[left_child][key]: 
            largest = left_child
     
        if right_child < n and arr[largest][key] < arr[right_child][key]: 
            largest = right_child
     
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] 
            cls.maxheap(arr, n, largest,key) 

    @classmethod
    def minheap(cls,arr, n, i, key:str):
        largest = i  
        left_child = 2 * i + 1    
        right_child = 2 * i + 2     
        
        if left_child < n and arr[i][key] > arr[left_child][key]: 
            largest = left_child
     
        if right_child < n and arr[largest][key] > arr[right_child][key]: 
            largest = right_child
     
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] 
            cls.minheap(arr, n, largest,key) 
    
    @classmethod
    def heapSort(cls, arr:list, key:str, descending:bool=False): 
        n = len(arr) 
        if (descending == True):
              # Build a minheap. 
            for i in range(n//2 - 1, -1, -1): 
                cls.minheap(arr, n, i, key) 
        
            # One by one extract elements 
            for i in range(n-1, 0, -1): 
                arr[i], arr[0] = arr[0], arr[i]
                cls.minheap(arr, i, 0,key) 
        
        else:
            # Build a maxheap. 
            for i in range(n//2 - 1, -1, -1): 
                cls.maxheap(arr, n, i,key) 
        
            # One by one extract elements 
            for i in range(n-1, 0, -1): 
                arr[i], arr[0] = arr[0], arr[i]
                cls.maxheap(arr, i, 0,key) 

