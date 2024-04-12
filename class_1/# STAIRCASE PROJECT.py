# STAIRCASE PROJECT

def draw_rectangle(length:int, height:int, remove_top:int=0, remove_btm:int=0, keep_first:bool=False, append:int=0):
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
    for i in range(height):
        if i == 0:
            if remove_top < length and keep_first:
                print("* ", "  "*(remove_top-1-append), "* "*append, "* "* (length-remove_top), sep='')
            elif remove_top < length :
                print("  "*(remove_top), "* "* (length-remove_top), sep='')
        elif i == height-1:
            if remove_btm < length:
                print("  "*(remove_btm), "* "* (length-remove_btm), sep='')
        else:
            print("*", ' '*(length*2-3), "*", sep='')
    

def draw_staircase(height, length, num_staircase):
    init_length = length
    for i in range(num_staircase):
        if i == 0:
            draw_rectangle(length, height, remove_btm=length)
        elif i == num_staircase-1:
            draw_rectangle((length*i)+init_length, height, remove_top=(init_length*i), keep_first=True, append=1)
        else: 
            draw_rectangle((length*i)+init_length, height, remove_btm=(length*i)+init_length, remove_top=(init_length*i), keep_first=True, append=1)


def get_value(prompt:str=''):
    while True:
        value = input(prompt)
        if value.isnumeric() is False:
            print("Please pass a positive integer!")
            continue
        return int(value)


if __name__ == "__main__":
    print("WELCOME TO MY STAIRCASE PROJECT\n\n")

    height = get_value("enter the height of the stairs: ")
    length = get_value("enter the length of the stairs: ")
    number = get_value("enter the number of the stairs: ")

    draw_staircase(height, length, number)