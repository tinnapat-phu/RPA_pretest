def unsta_to_sta(input , key=lambda x: x):

    #add extra space for keep index for comparison
    a_order = [(key(x), i, x) for i, x in enumerate(input)] 

    #run unstable sorting
    a_order.sort()

    #keep only result , remove the index 
    Array = [x for key,i,x in a_order]

    return Array

Array = [7,4 ,9 ,0 , -1, 1, 10,1]
print(unsta_to_sta(Array))