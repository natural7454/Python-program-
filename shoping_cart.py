products={
    "karela":80,
    "bhindi":100,
    "tomato":60,
    "patato":20,
    "Onion":60,
    "adarak":150
}

print("Show Products Deteils:-\n 1.All products\n 2.Add to cart\n 3.Remove your product \n 4.view your products\n 5.total bill your products \n 6.exit")

cart={}
while True:
    choice=input("Enter Your Choice:-")
    if(choice=="1"):
        for item,value in products.items():
            print(f'{item} -- {value}')
    elif(choice=="2"):
        item=input("Enter your Item Add to cart:-")
        if item in products:
            qty=int(input("Enter your Qty-:"))
            cart[item]=cart.get(item,0)+qty
            print(f'{item} Add to item!!!')
        else:
            print("product does not exiets in Cart!!!!!!!!!")  
    elif(choice=="3"):  
        item=input("Enter your product remove Now:-")
        if item in products:
            del cart[item]
            print(f"{item} remove item!!!")
        else:
            print("This Is products doest Not Exits")   
    elif(choice=="4"):
        if not  cart:
            print("cart Empty")
        else:
          for item,value in cart.items():
             print(f'{item} -- {value}')
    elif(choice=="5"):
        total=0
        print("\n Total bill:-")
        for item,qty in cart.items():
            price=products[item]*qty
            total=total+price
            print(f'{item} * {qty}=RS.{price}')
            print(f'Total bill is:-{total}')
    elif(choice=="6"):
        print("thanks for shoping!!!!")
        break









        
