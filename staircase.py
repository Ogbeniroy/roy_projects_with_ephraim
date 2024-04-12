def firstbox(height,length:int,steps):
    end_character = (length + 1)
    space_character = (length-2)
    if steps ==1:
        print("*"* length)
        for i in range(1,height - 1):
            print("*"+" "* space_character +"*")
        print("*"* length)
        
    elif steps > 1 and steps <3:
        print("*"* length)
        for i in range(1,height - 1):
            print("*"+" "* space_character +"*")      
        
        print("*"+" "* space_character +"*" * end_character)
        space_character += end_character - 1
        for i in range(1,height - 1):
            print("*"+" "* space_character +"*")
        print("*"* (space_character + 2))
    
    elif   steps > 2:
        print("*"* length)
        for i in range(1,height - 1):
            print("*"+" "* space_character +"*")      
        
        for stepping in range(7): 
            print("*"+" "* space_character +"*" * end_character)
            space_character += end_character - 1
            for i in range(1,height - 1):
                print("*"+" "* space_character +"*")
        
                
        print("*"* (space_character + 2))
            
            
            
            
            
        #print("*"* length)

firstbox(6,7,5)



''' firstbox is good and ready to go
do not touch
'''     
'''        
def lastbox(height,length,steps):
    if steps == 2:
        print("*" + " "*(length-2) + "*" * (length * steps - (length - 1)))
    for i in range(1,height - 1):
        print("*" + " "* (length  * 2 - 2)  + "*")
    print("*" * length * steps)       
 '''       
'''
level 2 done
'''
        
'''       
def lastbox(height,length,steps):
    for stepping in range(2,steps):  
        print("*" + " "*(length-2) + "*" * (length * steps - (length - 1)))
        for i in range(1,height - 1):
            print("*" + " "* (length  * 2 - 2)  + "*")
        length +=length
    print("*" * length) 

'''

''' 
def otherbox(height,length,steps):
    num_length = 1
    if steps ==2:
        while num_length >0 and num_length < height:
            print("*" + " "* (length  * 2 - 3)  + "*")
            num_length +=1 
        print("*"* (length * 2))
'''
'''    for i in range(2,steps):
    print("*" + " "* (length-2)  + "*"* length )
    step = 2
    while step >1 and step < height:
        print("*" + " "* (length  * 2 - 3)  + "*")
        step +=1
'''           

#lastbox(6,7,5)


        


