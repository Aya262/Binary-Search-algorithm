def binary_search_while(list,target):
    min = 0
    max = len(list) - 1
    index = -1
    while (max >= min and index == -1):
        # print("Iteration {} have min {} and max {}".format(i, min, max))
        mid = (min + max) // 2
        # print("Mid index equal {}".format(mid))
        # print("mid value equal {}".format(primes[mid]))
        if primes[mid] > target:
            max = mid - 1
        elif primes[mid] < target:
            min = mid + 1
        else:
            index = mid

    if index == -1:
        print("The number not found!")
    else:
        print("The Number exist at index {}".format(index))


def binary_search_recursive(list,target):
    index=-1
    s=''
    min=0
    max=len(list)-1
    mid=(min+max)//2
    if len(list)==0:
        s="The number doesn't exist"
    elif list[mid]<target:
        index += mid + 1
        s,index=binary_search_recursive(list[mid+1:],target)
    elif list[mid]>target:
        s,index=binary_search_recursive(list[:mid],target)
    else :
        index += mid
        s="The number {} exist ".format(target)
    return s,index



if __name__=='__main__':
     print("Welcome to search for a number using binary search , Enter a number")
     target=int(input())
     primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        #   [0,1,2,3,4 ,5 ,6 ,7 ,8 ,9 ,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
     #binary_search_while(primes,target)
     s,index=binary_search_recursive(primes,target)
     print("{} at index {}".format(s,index+1))