def findTriplets(arr): #[97, -27 , -34, 61, -39]
    #code here
    n = len(arr)
    arr = sorted(arr)
    found = False
   
    l = 0
    r = n-1
    while (l < r):
            print("l",l)
            for i in range(1,n-1):
                if (l == i) or (r == i)or(l==r):
                    continue
                s = arr[l]+arr[r]+arr[i]
                print(arr[l],arr[r],arr[i])
                if s == 0:
#                     print(arr[l],arr[r],arr[i])
                    found = True
                    return True
            r = r-1
            print("r",r)
            if (l < n-1) and (r == l):
#                     print("ok")
                l += 1
                r = n-1

    if found == False:
        return False
