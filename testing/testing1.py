def draw_box(width , leangth):
    if (leangth > 50) or (width > 20):
        print("wrong value !")
    else :
        print("#" * leangth)
        find_spaces = leangth - 2
        y = find_spaces
        for x in "#" * width:
            print(x," " * find_spaces,x)
        print("#" * leangth)

if __name__ == "__main__":
    a = int(input("Enter Your Item Width :"))
    b = int(input("Enter Your Item Leangth :"))
draw_box(a , b)