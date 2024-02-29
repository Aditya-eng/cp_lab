
print("\n")
entry="Welcome to the Asia's no. 1 online supermarket---- AAYA Supermarket"
print("\t\t",entry)
print("\n")

                                                    # MODULES 
import os
import math
import random
import smtplib
import time
import mysql.connector as mys

#------------------------------------------------------------------------------------------------------------------------

mycon= mys.connect(host="localhost", user="root",passwd="",database="super")
mycursor= mycon.cursor()
mycursor.execute('Use super')

my_cart=[]


name= input("What's your name ? ")
address=input("Enter your address: ") 
contactno=int(input("Enter your contact number: "))

#------------------------------------------------------------------------------------------------------------------------
def prices(list1):                                                               # Function 1 (EXECUTION OF DICT)
    mycursor.execute('''Create table if not exists Items (
    Item_code integer not null,
    Item_name varchar(50) not null unique,
    Prices decimal not null)''');

    for key in list1:

        query= "insert into Items values ({},'{}',{})".format(key,list1[key][0],list1[key][1])
        mycursor.execute(query)
        mycon.commit()
        print(key,". ",list1[key])
    
    #mycursor.execute("Select * from Items order by item_code")
    #mydata=mycursor.fetchall()
    #for row in mydata:
      #  print(row[0],":",row[1],":",row[2])
    #print("\n")
            
#-------------------------------------------------------------------------------------------------------------------------

def cart(list1):                             # Function 2 (CATEGORY)
    ans="y"
    while ans =="y":
        product= int(input("which product (no.) you want to add to ur cart: "))
        qty=int(input("Quantity of product ? "))
        ans=input("Do you want to add more product from this category ? (y/n) ")

        list1[product][0] +=  " x " + str(qty)
        list1[product][1] *= qty                     # new_price
        my_cart.append(list1[product])
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------
    
def grocery():                                                               # Function 3 (GROCERY)
    print("1. Dairy Product \t\t 2. Pantry \t\t 3. Personal Care \t\t 4. Fruits \n 5. Vegs \t\t 6. Freezer essentials \t\t 7. Baby Care")
    print("\n")
    gro=int(input("Choose an option (1/2/3/4/5/6/7): "))

#------------------------------------------------------------------------------------------------------------------------------------------------------
    if gro==1:  #dairy product
        print("We have a variety of dairy products")
        time.sleep(1)
        print("........................................................\n")
       
        items={1:["Milk (1 L)",50],
                2:["Yogurt (1 kg)",46],
                3:["Bread",12],
                4:["Butter (100 gm)",50],
                5:["Cream (250 mL)",63],
                6:["Cheese (100 gm)",69],
                7:["Ice Cream",40],
                8:["Milk Powder (200 gm)",60],
                9:["Paneer (500 gm)",150],
                10:["Chocolate Cake (1 Kg)",1099]}
        prices(items)
        cart(items)
               
#--------------------------------------------------------------------------    

    elif gro==2:                                                     #pantry
        print("Here's the list1 of pantry items:")
        time.sleep(2)
        print("........................................................\n")
        items={1:["Vegetable Oil (1 L)", 87],
               2:["Vinegar (250 mL)",250],
               3:["Ketchup(900 mL)",165],
               4:["Mayonnaise (250 gm)", 75],
               5:["Baking powder (100 gm)",120],
               6:["Black pepper (100 gm)",140],
               7:["Oregano (150 gm)",180],
               8:["Rice (1 Kg)",60],
               9:["Peanut Butter (350 gm)",159],
               10:["Oats (1 Kg)",180],
               11:["Baking Soda (100 gm)",134],
               12:["Flour (1 Kg)",28],
               13:["Corn flour (1 Kg)",251],
               14:["Almonds (1 Kg)",750],
               15:["Cashew (1 Kg)",800],
               16:["Date (1 Kg)",333]}
        prices(items)
        cart(items)
#------------------------------------------------------------------------------

    elif gro==3:                                                 # personal care
        print("Ohh wait a second.......")
        time.sleep(2)
        print("........................................................\n")
        
        items={1:["Hand soaps (pack of 3)", 200],
               2:["Shampoo (1 L)",580],
               3:["Razor",299],
               4:["Blades (pack of 3)",284],
               5:["Shaving cream (418 gm)",200],
               6:["Body lotion",398],
               7:["Perfumes (154 mL)",212],
               8:["Lipstick (3 shades)",299],
               9:["Cotton buds",25],
               10:["Hair band",120],
               11:["Tissue papers (pack of 100 napkins)",54],
               12:["Eye liner",375],
               13:["Cleansing pads (pack of 5)",120],
               14:["Powder (300 gm)",135],
               15:["Detergents (1 Kg)",95],
               16:["Hair dyes (36 mL)",115],
               17:["Toothpaste (150 gm x 2)",134],
               18:["Toothbrush",60],
               19:["Hand mirror",300]}
        prices(items)
        cart(items)
#--------------------------------------------------------------------------------

    elif gro==4:                                                   #Fruits
        print("Here's the list1 of Fruits available (Prices are of 1 Kg):")
        time.sleep(2)
        print("........................................................\n")
        items={1:["Mango",95],
               2:["Apple",110],
               3:["Banana",45],
               4:["Guava",100],
               5:["Orange",114],
               6:["Watermelon",65],
               7:["Pomegranate",135],
               8:["Grapes",60],
               9:["Papaya",40],
               10:["Pineapple",67],
               11:["Coconut",38],
               12:["Pumpkin",51],
               13:["Strawberry",178],
               14:["Litchi",85],
               15:["Kiwi",125]}
        prices(items)
        cart(items)
#-----------------------------------------------------------------------------------

    elif gro==5:    #Vegs
        print("Here's the list1 of Vegetables available (Prices are of 1 Kg):")
        time.sleep(2)
        print("........................................................\n")
        items={1:["Potato",20],
               2:["Onion",18],
               3:["Tomato",30],
               4:["Eggplant",35],
               5:["Peas",56],
               6:["Broccoli",64],
               7:["Cauliflower",32],
               8:["Garlic",240],
               9:["Turnip",50],
               10:["Green chilli",48],
               11:["Mushroom (1 Packet)", 35],
               12:["Raddish",25],
               13:["Capsicum",69],
               14:["Spinach",21],
               15:["Lady finger",72],
               16:["Bottle Gourd",24]}
        prices(items)
        cart(items)
#--------------------------------------------------------------------------------
    elif gro==6:                                                     #Freezer essentials
        print("Ohh wait a second.......")
        time.sleep(2)
        print("........................................................\n")
        
        items={1:["Frozen Peas (1 Kg)",105],
               2:["Frozen green beans (1 Kg)",65],
               3:["Frozen broccoli (1 Kg)", 50],
               4:["Frozen spinach (1 Kg)",75],
               5:["Frozen pizza (medium)",80]}
        prices(items)
        cart(items)

#--------------------------------------------------------------------------------

    elif gro==7:                                                    #dairy product
        print("Huraahhhhhhh babies........")
        time.sleep(1)
        print("........................................................\n")
       
        items={1:["Diaper (44 large pcs)",355],
               2:["Nail clipper",120],
               3:["Shampoo (300 gm)",200],
               4:["Body lotion(400 mL)",180],
               5:["Oil (100 mL)",132],
               6:["Cream (200 mL)",160],
               7:["Toothbrush (pack of 3)",99],
               8:["Baby wipes (400 wipes)",380]}
        prices(items)
        cart(items)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pharmacy():                                                         # Function 4 (PHARMACY)
    print("1, Ayurvedic medicine \t 2. Alopathic medicine \t 3. Homeopathic medicine")
    med={1:"Ayurvedic medicine",2:"Alopathic medicine",3:"Homeopathic medicine"}
    choosemed=int(input("Enter 1,2 or 3:"))
    
    if choosemed==1:                                                        # Ayurvedic
        print("we have following ayurvedic medicine")
        print("------------------------")
        ayu={1:["Balarishta",151],
        2:["Ashvagandha",94],
        3:["Lohasava",90],
        4:["Mustakarishta",176],
        5:["Kanakasava",143],
        6:["Arka pudina",102]}
        prices(ayu)
        cart(ayu)
        
    elif choosemed==2:                                                      # Alopathic
        print("we have following alopathic medicines")
        print("------------------------")
        alo={1:["Paracetamol",46],
             2:["Meftal spas",57],
             3:["Amoxicillin",93],
             4:["Metformin",128],
             5:["B complex",26],
             6:["Cough syrup",71],
             7:["Augmentin",99]}
        prices(alo)
        cart(alo)
        
    elif choosemed==3:                                                      # Homeopathic
        print("we have following homeopathic medicine")
        print("-----------------------------")
        hom={1:["arnica",98],
            2:["cuprum",44],
            3:["cantharis",103],
            4:["aconite",146],
            5:["rhus tox",69],
            6:["causticum",81]}
        prices(hom)
        cart(hom)

#--------------------------------------------------------------------------------------------------------------------------------------
def snacks():                                                           # Function 5 (SNACKS)
    print("1. Doughnuts\t 2. Soup \t 3. Nachos \t 4. Cookies \t 5.Chips \t 6. Fritters  " )
    snacks = int(input("1 or 2 or 3 or 4 or 5 or 6 " ) )

    #------------------------------------------------------------------------------------------------------------------
    if snacks == 1:                                      # Doughnuts
        print(" We have chosen the best three varieties of doughnuts")
        items = {1:["Chocolate frosted doughnuts",50],
                 2:["Cruller" , 40],
                 3:["Jelly doughnuts",55]}
        prices(items)
        cart(items)

   #--------------------------------------------------------------------------------------------------------------------

    elif snacks == 2 :                                   # soup
        print(" Here's for soup :")
        items = {1:["Tomato soup", 20],
                 2:["Veg soup" , 25],
                 3:["Non - veg soup" , 35]}
        prices(items)
        cart(items)

    #------------------------------------------------------------------------------------------------------------------------

    elif snacks == 3 :                                   # nachos
        print(" For Nachos :")
        items = {1:["Cheeseburst nachos",20],
                2:["Salt nachos",15],
                3:["Tangy and spicy nachos",25]}
        prices(items)
        cart(items)

  #-----------------------------------------------------------------------------------------------------------------------
    if snacks == 4 :                                     #  cookies
        print(" For Cookies :")
        items = {1:["Chocolate chip cookies",25],
                 2:["Oatmeal raisin cookies",30],
                 3:["Berne wafer",45]}
        prices(items)
        cart(items)

  #-----------------------------------------------------------------------------------------------------------------------
    elif snacks == 5 :                                  # chips
        print(" For Chips :")
        items = {1:["Banana chips",50],
                 2:["Potatochips",35],
                 3:["Chilli & Lemon",40]}
        prices(items)
        cart(items)
#----------------------------------------------------------------------------------------------------------------------------
    elif snacks == 6:                                    # fritters
        print("For Fritters :")
        items = {1:["Corn fritters",60],
                 2:["Spaghetti",75],
                 3:["Banana fritters",50]}
        prices(items)
        cart(items)
#---------------------------------------------------------------------------------------------------------------------------
        
def drinks():                                                                       # Function 6 (DRINKS)
    print("1. Tea\t 2. Coffee \t 3. Soft drinks \t 4. Mocktails\t 5.Shakes \t 6. Smoothie\t 7. Energy drinks  " )
    drinks= int(input("1 or 2 or 3 or 4or 5 or 6 " ) )
#-----------------------------------------------------------------------------------------------------------------------------
    if drinks == 1 :                              # Tea
        print("we have some best  refresing and healthy varieties  , TEA" )
        items = {1:["Bubble tea",15],
                 2:["Green tea" , 25],
                 3:["White tea ",20]}
        prices(items)
        cart(items)
#------------------------------------------------------------------------------------------------------------------------------------
    elif  drinks == 2:                           # Coffee
         print ("coffee :")
         items = {1:["Espresso",75],
                  2:["Cappuccino",80],
                  3:["Cold coffee",50],
                  4:["Dalgona ", 45]}
         prices(items)
         cart(items)


#--------------------------------------------------------------------------------------------------------------------------------------------------
    elif drinks == 3 :                           # Soft Drinks
          print ("Soft drinks :")

          items = {1:["Mountain Dew (1 L)",80],
                   2:["Sprite(1 L)",60],
                   3:["Coca-cola (1L)",70],
                   4:["Maaza (1L) ", 65]}
          prices(items)
          cart(items)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
    elif drinks == 4:                           # Mocktails
          print ("Mocktails:")

          items = {1:["Cucumber-lemonade",65],
                   2:["Blue shoe",50],
                   3:["Lemon- Basil mojito",70],
                   4:["Floral Ginger Rose Fizz ", 45]}
          prices(items)
          cart(items)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    elif drinks == 5:                           # Shakes
          print ("Shakes :")

          items = {1:["Mangoshake",35],
                   2:["Strawberry shake",40],
                   3:["Chocolate milkshake",50],
                   4:["Cookies-cream milkshake ", 65]}
          prices(items)
          cart(items)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
    elif drinks == 6:                           # Drinks
          print ("Smoothie :")

          items = {1:["Tropical mango ",75],
                   2:["Watermelon",80],
                   3:["Virgin Miami Vice",50],
                   4:["Chocolate banana ", 45]}
          prices(items)
          cart(items)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif drinks  == 7:
          print ("Energy drinks :")

          items = {1:["Red bull",70],
                   2:["Celsius sugar free",60],
                   3:["NOS",50]}
          prices(items)
          cart(items)


#--------------------------------------------------------------------------------------------------------------------------------------
print("\n")

ans="y"
while ans=="y":
    print("1. Grocery \t 2. Pharmacy \t 3. Snacks \t 4. Drinks ")
    choose1= int(input("1 or 2 or 3 or 4: "))
    print("\n")
    if choose1==1:
        grocery()
    elif choose1==2:
        pharmacy()
    elif choose1==3:
        snacks()
    elif choose1==4:
        drinks()
    print("\n")
    #if ans=="y":
        #mycursor.execute('''Create table Items2 (
        #Item_code integer primary key not null,
        #Item_name varchar(50) not null unique,
        #Prices decimal not null)''');
    ans=input("Want to purchase more items from different departments ? (y/n) ")
    
print("\n")
#print("Your cart has the following items: ")
#for i in my_cart:
#    print(i)
#print("\n")

#------------------------------------------------------------------------------------------------------------------------------------

                                                        # BILLING
a="DISCOUNT"
print(a.center(100))
                                  # bas SQL me add krne ke liye hai ye 


mycursor.execute('''Create table if not exists mycart (
Item varchar(50),
Price integer)''');

for key in my_cart:
    query="insert into mycart values ('{}',{})".format(my_cart[key][0],my_cart[key][1])
    mycursor.execute(query)
    mycon.commit()

mycursor.execute("select * from mycart order by Price")    
mydata2= mycursor.fetchall()
for row in mydata2:
    print(row[0],":",row[1],":",row[2])
print("\n")




amount=0
for i in my_cart:
    amount+=i[1]
print("Total Amount: ",amount)

#------------------------------------------------------------------------------------------------------------

disc=0                                              # DISCOUNT
if amount in range(1000,3000):
    disc+=5
        
elif amount in range(3000,5000):
    disc+=10
        
elif amount in range(5000,7000):
    disc+=20
        
elif amount>=7000:
    disc+=30
        
disam=(amount*disc)//100
amt=amount-disam
print("Congrats!! you get discount of",disc,"%")
print("Total amount is",amt)

print("\n")

for i in my_cart:
    print(i[0],"\t\t",str(i[1]))

print("n")
#------------------------------------------------------------------------------------------------------------------------------------
#def delivery():                                     # Function 7 (DELIVERY)
 #   print("Shipping to ",address)
 #   print("Estimated delivery: ",)          # Date and time feature from SQL
  #  print("\n")

 #   print("\tItems \t ₹",amt)
  #  print("\tDelivery \t ₹",30)
  #  print("\tOrder total \t₹",amt+30)

  #  mycursor.execute('''Create table if not exists Delivery (
  #  Delivery_details varchar(50),
  #  Delivery_details integer)''');

    #mycursor.execute("insert into Delivery values ('Shipping to,'{}')".format(address))
    #mycursor.execute("insert into Delivery values ('Estimated delivery,'{}')")

  #  mycursor.execute("insert into Delivery values ('Items',{})".format(amt))
 #   mycursor.execute("insert into Delivery values ('Delivery charge',30)")
  #  mycursor.execute("insert into Delivery values ('Order total',{})".format(amt+30))
    
#------------------------------------------------------------------------------------------------------------------------------------
 
def OTP():                                                                  # Function 8 (OTP)
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
        
    msg = "\t\t AAYA Supermarket \n"+ OTP + " is your OTP"


    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("ashuanand8804@gmail.com", "ukpdglfnidppwdxd")

    emailid = input("Enter your email: ")
    print("An OTP has been sent to your e-mail")
    s.sendmail('ashuanand8804@gmail.com',emailid,msg)


    while True:
        x = input("Enter Your OTP >>> ")
        if x == OTP:
            print("\t\t\tLogged in successfully")
        else:
            print("Incorrect OTP....Try again")
            continue
        break
#------------------------------------------------------------------------------------------------
                                                               # PAYMENT
print("\n")
print("\t\t\t*****Mode of payment*****")
print("1. Credit Card")
print("2. Net Banking") 
print("3. Pay on Delivery")

ask=int(input("Choose an option (1,2,3): "))
print("\n")

#-------------------------------------------------------------------------------------------------

if ask==1:                                           # 1. CREDIT CARD
    z1=input("Enter the name of card owner: ")
    z2=input("Enter the card number: ")
    z3=int(input("Enter the expiry month of the card: "))
    z4=int(input("Enter the expiry year of the card: "))
    z5=input("Save your details ? (y/n) ")                                      # add in SQL
    print("\n")
    print("Net payable amount: ",amount)

    while True:
        z6=input("Are you sure you want to pay ? (y/n)")
        if z6=="y":
            OTP()
                
        else:
            break
        break
    
        
#-----------------------------------------------------------------------------------------------
    
elif ask==2:                                        # 2. NET BANKING
    x={
        1: "State Bank of India",
        2: "Axis Bank",
        3: "Standard Chartered Bank",
        4: "HDFC Bank",
        5: "ICICI Bank",
        6: "Kotak Bank",
        7: "Bank of baroda - Corporate Banking",
        8: "Indian Bank"
        }

    for i in x:
        print(i,". ",x[i])
    print("\n")
    bank1=int(input("Choose your bank (1/2/3/4/5/6/7/8): "))

    print("Selected bank: ",x[bank1])
    print("\n")

    #delivery()

    d=input("Proceed and pay ? (y/n) ")
    if d=="y":
        print("Proceeding........")
        time.sleep(3)
    print("\n")    

    print("\t\t\tLog in and pay")
    OTP()
    
#--------------------------------------------------------------------------------------------------
                                                        
elif ask==3:                    # PAY ON DELIVERY
    print("Okay")

#--------------------------------------------------------------------------------------------------
print("\n")
while True:
    e=input("Place your order and pay ? (y/n) >>> ")

    if e=="y":
        print("Wait....don't shut down your device")
        time.sleep(5)

    else:
        break
    break

#---------------------------------------------------------------------------------------------------

#mycursor.execute('''Create table Confirmation (
#Details varchar(50) not null,
#Description varchar(50))''');


#mycursor.execute("insert into Confirmation values ('Name', '{}')".format(name))
#mycursor.execute("insert into Confirmation values ('Shiping_address', '{}')".format(address))
#mycursor.execute("insert into Confirmation values ('Contact_number', '{}')".format(contactno))
#mycursor.execute("insert into Confirmation values ('Net_payable_amount', '{}')".format(amt))
#mycursor.execute("insert into Confirmation values ('Estimated_delivery', '{}')".format(name))
#mycon.commit()



