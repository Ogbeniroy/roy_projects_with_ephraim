def four_sides_staircase(height,length:int,steps):
    '''
    A function that draws a hallow rectangle.
        params:
            -length: The length of the rectangle.
            -height: The height of the rectangle.
            -steps: The number of steps for the staircase.
            -end_character: number of asterics needed at the end of the line.
            -space_character: number of empty spaces needed.
            
            
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

four_sides_staircase(4,5,7)
four_sides_staircase(8,9,6)
four_sides_staircase(4,6,10)


        


