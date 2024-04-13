def firstbox(height,length:int,steps):
    '''
    A function that draws a hallow rectangle.
        params:
            -length: The length of the rectangle.
            -height: The height of the rectangle.
            -remove_top: The length to remove from the top part of the rectangle starting from the left.
            -remove_btm: The length to remove from the bottom part of the rectangle starting from the left.
            -keep_first: Whether to keep the first asterik or not.
            
            -append: append an asterik to the begining of a removed line.
'''
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

print("Welcome to my staircase builder  ")

firstbox(4,5,7)
firstbox(8,9,6)
firstbox(4,6,10)


        


