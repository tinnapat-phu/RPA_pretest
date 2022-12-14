#
#----- TIME COMPLEXITY = O(MN^3) ------
#

def value_recur(sum,depth_count,start_index):

    for i in range(start_index,len(a)):
        #For tracking the element we've collected
        checkarray[depth_count] = a[i]

        if(depth_count > 0 and sum-a[i] >= 0) :
     
            value_recur(sum-a[i],depth_count-1,start_index=i)
                
            

        elif(depth_count == 0 and sum-a[i] == 0):
            print("Selected elements C[",current_index,"]: ",checkarray[::-1])
            c[current_index] = 1
        
        #no need to continue check current_index if we already had list of valid answer
        if(c[current_index] == 1):
            break
  
    
    return


a = [5, 2, 3, 4, 10, 11]
b = [5, 7 , 26]
c = [0] * len(b)
checkarray = [0] * len(b)
current_index = 0

for index in range(len(b)):
    current_index = index
    value_recur(b[current_index],depth_count = 2,start_index = 0)

print("c[i] = ",c)