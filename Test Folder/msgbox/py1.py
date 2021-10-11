def draw_msg_box(leangth , width , type):
    if ((leangth < 50) and (width < 20)):
        print("#" * leangth)
        find_spaces = leangth - 2
        converter = str(width)
        #colunms = (len(converter)+1)/2
        for x in range(1 , width):
            demo = (len(converter)+1)/2
            if (demo):
                l = width[1]+(len(converter)+1)/2)-1
                print(l)
            print("#" + " " * find_spaces + "#")
        print("#" * leangth)
    else :
        print("Wrong Values !")
        
if __name__ == "__main__":
    a = int(input("Enter Your Item Leangth :"))
    b = int(input("Enter Your Item Width   :"))
    c = str(input("What Did You Type       :"))
    draw_msg_box(a ,b ,c)