            
def file(laptop_dict,laptop_id):
      file = open("laptops.txt","r")

      for each_line in file:
          each_line = each_line.replace("\n"," ")
   
          laptop_dict.update ({laptop_id: each_line.split(",")})
          laptop_id += 1


#To read the text file 
def read_file():
    
      file = open("laptops.txt","r")
      num = 1
      for each_line in file:
        print(num,"\t"+each_line.replace(",","\t|\t  "))
        num = num+1
      file.close()
