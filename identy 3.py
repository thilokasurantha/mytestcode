
def  analyze_id(id_str):
    first_2 = id[0:2]
    second_3 = id[2:5]
    mo_dt = int(second_3)
    
    print("Your Birth IS : 19"+ first_2 )
    
    if mo_dt > 500 :
        print("Your Are Female")
    else :
        print("You Are Male")
        
    month , date = get_date_and_month(int(first_2) , mo_dt )
    print("Your Month IS :" , month)
    print("Your Date Is  :" ,date)
    
def get_date_and_month(first_2 , mo_dt):
        
    months = []
        
    cur_month = 0
    date = 1
        
    while (mo_dt >(date + months [cur_month])):
        date = date + months[cur_month]
        cur_month = cur_month+1
            
    return cur_month+1 , mo_dt - date
        
if __name__=="__main__":
    id = input("Enter Your ID :")
    
    while len(id) < 10 :
        print("You Are Invalid !!")
        id = input("Enter Your ID :")
print("Your Identy Card IS : " , id)
analyze_id(id)
