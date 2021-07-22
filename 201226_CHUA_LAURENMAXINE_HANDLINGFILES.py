products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    order = products[code]
    return order

get_product("brewedcoffee")

def get_property(code,property_):
    answer = products[code][property_]
    return answer 

get_property("frappuccino","price")

def main():
    orderlist=[]
    while True:
        order = input("Please enter product code and quantity {product_code},{quantity}): ")
        if order == "/":
            break
        orderlist.append(order.split(','))
        
        norepeats=[x[0] for x in orderlist]
        norepeats=list(set(norepeats))
        norepeats.sort()
        
        final=[]
        for product in norepeats:
            productquantity=[product,0]
            for i in orderlist:
                if i[0]==product:
                    productquantity[1]+=int(i[1])
                    
            final.append(productquantity)
            
        with open("receipt.txt","w") as receipt:
            receipt.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL

        ''')
        total=0
        for product in final:
            name=get_property(product[0],'name')
            subtotal=int(product[1])*get_property(product[0],"price")
            total+=subtotal
            
            with open("receipt.txt", "a") as receipt:
                receipt.write('\n'+f'{product[0]}\t\t{name}\t\t{product[1]}\t\t\t\t{subtotal}')
                
        with open('receipt.txt','a+') as receipt:
            receipt.write(f'''
            
Total:\t\t\t\t\t\t\t\t\t\t{total})
==
        ''')
            receipt.seek(0)
            print(receipt.read())
    
main()
