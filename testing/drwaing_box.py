def draw_msg_box(leangth , width , msg):
    if((leangth < 50) or (width < 20)):
        spaces = leangth - 2
        find_spaces = spaces * " "
        width_middle = (width+1)/2
        box_right = (leangth - len(msg))/2
        box_left = (leangth - len(msg))/2
        print("#" * leangth)
        for x in range(1,width):
            additons = 1
            print("#" + find_spaces + "#")
            if(additons == width_middle):
                print(msg)
            additons = additons+1
        print("#" * leangth)
      # while(additons < width):
       #     if(additons == width_middle):
        #        print(msg)
         #   additons = additons+1
if __name__=="__main__":
    l = int(input("Enter Your Item Leangth :"))
    w = int(input("Enter Your Item Width   :"))
    m = input("Enter Your MSG  :")
    draw_msg_box(l , w ,m)