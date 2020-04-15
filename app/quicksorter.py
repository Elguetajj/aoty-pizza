class Quicksorter:

    @classmethod
    def partition(cls,arr, start, n):
        pivot = arr[start]["rating"]
        low = start + 1
        high = n

        while True:
            while low <= high and arr[high]["rating"] <= pivot:
                high = high - 1

            while low <= high and arr[low]["rating"] >= pivot:
                low = low + 1

       
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
            else:
                break

        arr[start], arr[high] = arr[high], arr[start]

        return high

    @classmethod
    def quick_sort(cls,arr, start, n):
        if start >= n:
            return

        p = cls.partition(arr, start, n)
        cls.quick_sort(arr, start, p-1)
        cls.quick_sort(arr, p+1, n)


