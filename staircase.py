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
            
            
            
            
            
       

firstbox(6,7,5)




        


