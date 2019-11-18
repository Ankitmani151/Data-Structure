for i in range(1,len(arr)):
    curnum=arr[i]
    position=i
    while (position>0 and arr[position-1]>curnum):
        arr[position]=arr[position-1]
        position=position-1
        
    arr[position]=curnum
