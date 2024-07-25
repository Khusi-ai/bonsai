import datetime
import read
import write
import display_messages

laptop_dict = {}		
laptop_id = 1
read.file(laptop_dict,laptop_id)  #Calling the function file from read file.

#Defining function purchase for operating the purchasing laptops
def purchase():
    display_messages.fill_information()
    name = input("Enter the name of manufacturer: ")
    phone_number = input("Enter phone number: ")
    address = input("Enter the address: ")
    print("--------------------------------------------")

    purchased_laptop = [] #Creating an empty list
    loop = True
    while loop ==  True:
        display_messages.table()
        read.read_file()  #Calling the function read_file from read module
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        
    #to check the validility of id
     
        try:  #using event handling
            valid_id = int(input("Enter the ID of laptop: "))
        except ValueError:
            display_messages.exception()
            continue
        while valid_id <= 0 or valid_id > len(laptop_dict):
            display_messages.invalid_error()
            valid_id = int(input("Enter the ID of laptop: "))
       

    # Updating the text file
        try:
            user_quantity = int(input("Please provide the number of quantity you want to purchase: " ))
        except ValueError:
            display_messages.exception()
            continue
        print("\n")
        quantity = laptop_dict[valid_id][3]
         
        laptop_dict[valid_id][3] = int(laptop_dict[valid_id][3]) + int(user_quantity)
        write.value(laptop_dict)   #Calling the function value with paramter laptop_dict from write module
       
    #User purchased items

        laptop_name = str(laptop_dict[valid_id][0])
        selected_quantity = user_quantity
        unit_laptop_price = str(laptop_dict[valid_id][2])
        price = str(laptop_dict[valid_id][2].replace("$",""))
        total_amount = int(price)* int(selected_quantity)
        total_with_VAT = int(total_amount)+int((0.13)*int(total_amount)) #adding VAT 13%
        
        purchased_laptop.append([laptop_name, selected_quantity, unit_laptop_price, total_with_VAT])
   

        print("----------------------------------------")
        ask_user = input("Do you want to continue?(y/n)").lower()
        print("----------------------------------------")
        if ask_user == 'y':
            loop = True 
        else:
            total = 0
            cost_shipping = 200
            for i in purchased_laptop:
                total = total + int(i[3])
                grand_total_amount = str( float(total + cost_shipping ))  #200 is the shipping cost
    
           
            current_date_and_time = datetime.datetime.now()
            #Generating the bill for purchased items
            print("\n")
            print("----------------------------------------------------------------")
            print("|\t\t\t   Bill\t\t\t\t       |")
            print("|\n\t\t\t\t\t\t\t       |")
            print("|"+  str(name) +" \t| "+str(address)+"\t | "+str(phone_number) )
            print("----------------------------------------------------------------")
            print("|  NAME: E-zone Electronics \t\t PHONE: 9876543675     |")
            print("|  ADDRESS: Dillibazar, Kathmandu, Nepal")
            print("|  Date and Time: "+str(current_date_and_time),"\t\t       |")
            print("----------------------------------------------------------------")
            print("|\n\t\t\t\t\t\t\t       |")
            print("|  Details: \t\t\t\t\t\t       |")
            print("----------------------------------------------------------------")
            print("|Laptop Name \t\t Quantity \t  Price \t Total |")
            print("----------------------------------------------------------------")
            for i in purchased_laptop:
                print("|",str(i[0])," \t ",str(i[1])," \t\t ",str(i[2])," \t ",str(i[3]),"|")
            print("----------------------------------------------------------------")
            print("|  Shipping cost : 200\t\t\t\t\t       |")
            print("|  Total amount: $"+ str( grand_total_amount),"\t\t\t\t       |")
            print("----------------------------------------------------------------")
            print("\n")
            # Calling function print_bill_of_purchase with parameters name, address, phone_number, purchased_laptop and grand_total_amount from write module 
            write.print_bill_of_purchase(name,address,phone_number,purchased_laptop,grand_total_amount) 
            loop = False

            
#Defining function sell for selling laptops
def sell():
    display_messages.fill_information()
    name = input("Enter the name of customer: ")
    phone_number = input("Enter phone number: ")
    address = input("Enter address: ")
    print("--------------------------------------------")

    sell_laptop = [] #Creating empty list
    loop = True
    while loop ==  True:
        display_messages.table()
        read.read_file() #Calling the function read_file from read module
        print("-------------------------------------------------------------------------------------------------------------------------------------")
    

        #checking the validility of id
        try:  #Use of event handling
            
            valid_id = int(input("Enter the ID of laptop: "))
        except:
            display_messages.exception()
            continue
        while valid_id <= 0 or valid_id > len(laptop_dict):
            display_messages.invalid_error()
            valid_id = int (input("Enter the ID of laptop:"))
            
        quantity = laptop_dict[valid_id][3]
        if( int(quantity) < 1):
            display_messages.quantity_unavailable()
            valid_id = int (input("Enter the ID of laptop:"))
        
    # Updating the text file
        try:
            user_quantity = int(input("Please provide the number of quantity you want to sell: " ))
        except ValueError:
            display_messages.exception()
            continue
        print("\n")
        quantity = laptop_dict[valid_id][3]
        while user_quantity<= 0 or user_quantity > int(quantity):
            print("Quantity trying to be entered is not valid! ")
            user_quantity = int(input("Please provide the number of quantity you want to sell: "))

         
        laptop_dict[valid_id][3] = int(laptop_dict[valid_id][3]) - int(user_quantity)
        write.value(laptop_dict) #Calling function value with parameter laptop_dict from write module


        laptop_name = str(laptop_dict[valid_id][0])
        selected_quantity = user_quantity
        unit_laptop_price = str(laptop_dict[valid_id][2])
        price = str(laptop_dict[valid_id][2].replace("$",""))
        total_amount = int(price)* int(selected_quantity)
      
        
        sell_laptop.append([laptop_name, selected_quantity, unit_laptop_price, total_amount]) #adding sold laptops to the empty list



        print("------------------------------------")
        ask_user = input("Do you want to continue?(y/n)").lower()
        print("------------------------------------")
        if ask_user == 'y':
            loop = True 
        else:
            total = 0
            cost_shipping = 200
            for i in sell_laptop:
                total = total + int(i[3])
            grand_total_amount = str( float(total + cost_shipping ))  #200 is the shipping cost
    
            
            current_date_and_time = datetime.datetime.now()
            #Generating bill for sold laptops
            print("\n")
            print("----------------------------------------------------------------")
            print("|\t\t\t   Bill\t\t\t\t       |")
            print("|\n\t\t\t\t\t\t\t       |")
            print("|  E-zone ELectronics  \t| Kathmadu  \t | 9876543675 \t       |")
            print("----------------------------------------------------------------")
            print("|  NAME: "+str(name),"\t\t\t PHONE: "+str(phone_number))
            print("|  ADDRESS: "+str(address))
            print("|  Date and Time: "+str(current_date_and_time),"\t\t       |")
            print("----------------------------------------------------------------")
            print("|\n\t\t\t\t\t\t\t       |")
            print("|  Details: \t\t\t\t\t\t       |")
            print("----------------------------------------------------------------")
            print("|Laptop Name \t\t Quantity \t  Price \t Total |")
            print("----------------------------------------------------------------")
            for i in sell_laptop:
                print("|",str(i[0])," \t ",str(i[1])," \t\t ",str(i[2])," \t ",str(i[3]),"|")
            print("----------------------------------------------------------------")
            print("|  Shipping cost : 200\t\t\t\t\t       |")
            print("|  Total amount: $"+ str( grand_total_amount),"\t\t\t\t       |")
            print("----------------------------------------------------------------")
            print("\n")
            
            #Calling function print_bill_of_sell with parameters name, address, phone_number, sell_laptop and grand_total_amount from write module 
            write.print_bill_of_sell(name,address,phone_number,sell_laptop,grand_total_amount)
            loop = False

   



    
            

      
   

    
    
    
     
    

























    
