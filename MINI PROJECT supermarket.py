from datetime import datetime
name=input("enter your name: ")
# LIST OF ITEMS
lists='''
rice        20/kg
sugar       10/kg
salt         5/kg
dal         40/kg
chips       50/kg
kumkum      30/kg
turmeric    10/kg
'''
# DICLARATION
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#  RATES OF ITEMS
items={'rice':20,
       'sugar':10,
       'salt':5,
       'dal':40,
       'chips':50,
       'kumkum':30,
       'turmeric':10}
option=int(input("for list of items press 1: "))
if option==1:
    print(lists)     
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not avaliable")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no :")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","rahul super market",25*"=")
            print(28*" ","bhongir")
            print("name:",name,30* " ","Date:",datetime.now())
            print(75*"-")
            print("sno",5*" ",'items',10*" ","quantity",7*" ","price",)
            
            for i in range(len(pricelist)):
                print(i,8*' ',ilist[i],9*' ',qlist[i],14*" ",plist[i])
            print(75*"-")
            print(50*" ",'totalamount:','Rs',totalprice)
            print("gst amount",40*" ","Rs",gst)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(20*"-","Thanks for visiting")
            print(75*"-")
            
                
                
            
            