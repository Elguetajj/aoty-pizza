class Heaper:
    @classmethod        
    def heapify(cls, arr, n, i): 
        largest = i  
        left_child = 2 * i + 1    
        right_child = 2 * i + 2     
        
        if left_child < n and arr[i]["rating"] < arr[left_child]["rating"]: 
            largest = left_child
     
        if right_child < n and arr[largest]["rating"] < arr[right_child]["rating"]: 
            largest = right_child
     
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] 
            cls.heapify(arr, n, largest) 
    
    @classmethod
    def heapSort(cls, arr): 
        n = len(arr) 
    
        # Build a maxheap. 
        for i in range(n//2 - 1, -1, -1): 
            cls.heapify(arr, n, i) 
    
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i]
            cls.heapify(arr, i, 0) 
    