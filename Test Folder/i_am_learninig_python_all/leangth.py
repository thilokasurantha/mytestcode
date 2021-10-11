
def draw_box(length ,width):                                                
    k = "#"
    v = length+2-2
    r = "  "
    l = v * r 

    if (length > 50) or (width > 20):
        print("Wrong Value !")
    else :
        print(" #" * length)                        
        for n in (k * width):                                          
            print(n ,  l , n)                      
        print("#" * length)

def draw_box2(length, width):
    if (length > 50) or (width > 20):
        print("Length should be <=50, Width <=20 !")
        return
    print ("#" * length)
    spaces = length - 2 
    special_rows = width - 2 
    for n in range(1,special_rows):
        print ("#" + spaces * ' ' + "#")
    print("#" * length)


if __name__ == "__main__":
    a = int(input("Enter Your Item Length :"))
    b = int(input("Enter Your Item Width  :"))
    draw_box2(a , b)

