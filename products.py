#記帳程式
#while loop適合用在不知道次數的情況
products = []

while True:
	name = input('Product name: ')
	if name == 'q':
		break
	price = input('The price of products: ')
	p =[name, price]  #比較簡潔的寫法
	products.append(p)
	
#基礎寫法	
#   p=[]
#	p.append(name)
#	p.append(price)
   
	
#更加簡潔的寫法:
#products.append([name, price])


print(products)

#存取二維清單
#product[0][0] 先走進去第0格 
