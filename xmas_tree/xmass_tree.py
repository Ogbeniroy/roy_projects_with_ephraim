def xmasstree():
    pass


def drawtriangle(height = 3, num_reduce = 2):
    spacecal = height - 1
    for idx, i in enumerate(numgen(height)):
        if not (idx < num_reduce):
            print(" " * spacecal + "*" * i)
        spacecal -=1

    

  
        
def numlist(nums):
    startnum = 1
    result = []
    for num in range(nums):
        result.append(startnum)
        startnum +=2
    return result
     

#gen version 
def numgen(nums):
    startnum = 1
    
    for num in range(nums):
        yield startnum
        startnum +=2
    
        
        
    
        
    




if __name__ == "__main__":
    xmasstree()
    drawtriangle(5)
    
   # drawtriangle(5)
   # print(numlist(4))
    #print(list(numgen(4)))