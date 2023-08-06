def s_bsort(arr):
                n = len(arr)
                for i in range(0,n-1,1):
                    for j in range(0, n-i-1,1):
                          if arr[j] > arr[j + 1] :
                             arr[j], arr[j + 1] = arr[j + 1], arr[j]                
                          print ("Sorted array : ")
                for i in range(len(arr)):
                    print (arr[i])


#salman bubble sort
