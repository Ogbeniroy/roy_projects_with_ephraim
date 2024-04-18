
import staircaseproject

def xmasstree(height,stackno):
    stacktriangle(height,stackno)
    trainglestem(height)

def drawtriangle(height = 3, num_reduce = 0):
    spacecal = height - 1
    for idx, i in enumerate(numgen(height)):
        if not (idx < round(num_reduce)):
            print(" " * spacecal + "*" * i)
        spacecal -=1

def stacktriangle(height,stackno):
    '''
    stack of triangles below the top of the xmas tree
    ''' 
    stackcount = 0
    while  stackcount < stackno:
        if stackcount == 0:
            drawtriangle(height,num_reduce=0)
        else :
            drawtriangle(height,num_reduce = height /2 )
        stackcount +=1
        
def trainglestem(height):
    width = 3
    longness = height 
    heightcheck = 0
    baselength = numlist(height)[-1]
    no_of_space = baselength - 3
    while  heightcheck < longness:
        print(" "* (no_of_space//2)  + "***" + " " * (no_of_space//2))
        heightcheck +=1
        
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
    height = staircaseproject.get_value("please enter a number for height : ")
    stackno = staircaseproject.get_value("please enter a number for stackno : ")
    xmasstree(height,stackno)  