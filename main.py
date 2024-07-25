import operations
import display_messages

    
display_messages.welcome_message()
loop = True
while loop == True:
    
    display_messages.select_option()
    try:
        user_input = int(input("Enter the option according to your need : "  ))
    except ValueError:
        display_messages.main()
        continue
   
    if user_input == 1:
        display_messages.purchase()
        operations.purchase()
    if user_input == 2:
        display_messages.sell()
        operations.sell()

    if user_input != 3:
        display_messages.display()
       
            
    else:
        display_messages.exit()
        loop = False
      
    


    
    
