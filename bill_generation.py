
from datetime import datetime

name=input("enter your name:")

# lists
list='''

tshirt              Rs 399/1
jeans_pant          Rs 999/1
shirt               Rs 799/1
formal_shoe         Rs 1099/1
sneeker_shoe        Rs 1499/1
slippers            Rs 349/1
bath_towel          Rs 450/1
bath_soap           Rs 220/1
tooth_brush         Rs 112/1
tooth_paste         Rs 220
perfume             Rs 280/1
watch               Rs 2499/1
chocolate           Rs 295/1

'''

#decleration
price=0
pricelist=[]
total_price=0
final_price=0
i_list=[]
q_list=[]
p_list=[]


#rates for items
items={'tshirt':399,
       'jeans_pant':999,
       'shirt':799,
       'formal_shoe':1099,
       'sneeker_shoe':1499,
       'slippers':349,
       'bath_towel':450,
       'bath_soap':220,
       'tooth_brush':112,
       'tooth_paste':220,
       'perfume':280,
       'watch':2499,
       'chocolate':295}

# option=int(input("for list of items press 1:"))
# if option==1:
#     print(list)

for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or press 0 for exit:"))
    if inp1==0:
        break
    if inp1==1:
        item=input("Enter the items:")
        quantity=int(input("Enter the quantity:"))

        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            total_price+=price
            i_list.append(item)
            q_list.append(quantity)
            p_list.append(price)
            gst=(total_price*2)/100
            final_price=gst+total_price
        else:
            print("sorry your item is out of stock:")
        
    else:
        print("you have entered incorrect option:")

    inp=input("need to bill the items yes or no:")
    if inp=='yes':
        pass
        if final_price!=0:
            print(35*"~","Dmart",38*"~")
            print(28*" ","whitefield_bangalore")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(80*"-")
            print("sno",8*" ",'items',12*" ",'quantity',15*" ",'price')

            for i in range(len(pricelist)):
                print(i,7*' ',1*" ",i_list[i],10*' ',q_list[i],23*" ",p_list[i])

            print(80*"-")
            print(45*" ",'total_price:','Rs',total_price)
            print(47*" ",'gst amount:','Rs',gst)
            print(80*"-")
            print(45*" ",'final_price:','Rs',final_price)
            print(80*"-")
            print(25*" ",'thanks for ypur shopping')
            print(35*"~","Dmart",38*"~")


