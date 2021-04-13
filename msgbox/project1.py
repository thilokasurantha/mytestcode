def dwing_tablet_box(width ,leangth):
    if ((leangth > 50) or (width > 20)):
        print("Whats Wrong !")
    else :
        print("#" * leangth)
        spaces = leangth - 2
        for x in range(0 , width - 2):
            print("#" + " " * spaces + "#")
        print("#" * leangth)
            
if __name__ == "__main__":
    a = int(input("Enter Your Width :"))
    b = int(input("Enter Your Leangth :"))

    dwing_tablet_box(a, b)