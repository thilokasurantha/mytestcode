
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
        print(" #" * length)
if __name__ == "__main__":
    a = int(input("Enter Your Item Length :"))
    b = int(input("Enter Your Item Width  :"))
draw_box(a , b)
