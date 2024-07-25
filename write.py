import datetime

#defining function value with parameter laptop_dict
def value(laptop_dict):
     file = open("laptops.txt","w")
     for values in laptop_dict.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
            file.write("\n")
     file.close()

#defining function print_bill_of_purchase with parameters name,address,phone_number,purchased_laptop and grand_total_amount
def print_bill_of_purchase(name,address,phone_number,purchased_laptop,grand_total_amount):
            current_date_and_time = datetime.datetime.now()
            hour = (datetime.datetime.now().hour)
            minute = (datetime.datetime.now().minute)
            second = (datetime.datetime.now().second)

            
            file =  open(str(name)+"_"+str(hour)+"-"+str(minute)+"-"+str(second)+".txt",'w')
            file.write("\n")
            file.write("---------------------------------------------------------")
            file.write("\n\t\tBill")
            file.write("\n")
            file.write("|"+  str(name) +" \t| "+str(address)+"\t | "+str(phone_number) )
            file.write("\n---------------------------------------------------------")
            file.write("\nNAME: E-zone Eleactronics ")
            file.write("\nPHONE: 9876543675")
            file.write("\nAddress: Dillibazar, Kathmandu, Nepal")
            file.write("\nDate and Time: "+str(current_date_and_time))
            file.write("\n--------------------------------------------------------")
            file.write("\n")
            
            file.write("Details: ")
            file.write("\n--------------------------------------------------------")
            file.write("\nLaptop Name \t Quantity \t  Price \t Total")
            file.write("\n--------------------------------------------------------")
            file.write("\n")
            for i in purchased_laptop:
                file.write("\n"+str(i[0])+" \t "+str(i[1])+" \t\t "+str(i[2])+" \t "+str(i[3])+"\n")
            file.write("\n--------------------------------------------------------")
            file.write("\nShipping cost : 200")
            file.write("\n---------------------------------")
            file.write("\nTotal amount: $"+ str( grand_total_amount))
            file.write("\n--------------------------------------------------------")
            file.write("\n")
            file.close()

#defining function print_bill_of_sell with parameters name,address,phone_number,sell_laptop and grand_total_amount
def print_bill_of_sell(name,address,phone_number,sell_laptop,grand_total_amount):

            current_date_and_time = datetime.datetime.now()
            hour = (datetime.datetime.now().hour)
            minute = (datetime.datetime.now().minute)
            second = (datetime.datetime.now().second)

            
            file =  open(str(name)+"_"+str(hour)+"-"+str(minute)+"-"+str(second)+".txt",'w') 
            file.write("\n")
            file.write("---------------------------------------------------------")
            file.write("\n\t\tBill")
            file.write("\n")
            file.write("E-zone Electronics  |Dillibazar,Kathmadu   | 9876543675\n")
            file.write("---------------------------------------------------------")
            file.write("\nNAME: "+str(name))
            file.write("\nPHONE: "+str(phone_number))
            file.write("\nAddress: "+str(address))
            file.write("\nDate and Time: "+str(current_date_and_time))
            file.write("\n--------------------------------------------------------")
            file.write("\n")
            
            file.write("Details: ")
            file.write("\n--------------------------------------------------------")
            file.write("\nLaptop Name \t Quantity \t  Price \t Total")
            file.write("\n--------------------------------------------------------")
            file.write("\n")
            for i in sell_laptop:
                file.write("\n"+str(i[0])+" \t "+str(i[1])+" \t\t "+str(i[2])+" \t "+str(i[3])+"\n")
            file.write("\n--------------------------------------------------------")
            file.write("\nShipping cost : 200")
            file.write("\n---------------------------------")
            file.write("\nTotal amount: $"+ str( grand_total_amount))
            file.write("\n--------------------------------------------------------")
            file.write("\n")
            file.close()

           
