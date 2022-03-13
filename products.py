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
#簡潔的寫法:
#products.append([name, price])
	
#基礎寫法	
#   p=[]
#	p.append(name)
#	p.append(price)

print(products)

#存取二維清單
#product[0][0] 先走進去第0格 

for p in products:
	print('The price of', p[0], 'is', p[1])

with open('products.csv', 'w') as f: 
#現在是write所以原本沒有這個檔案沒有關係
#但如果本來有
#用f稱呼打開的檔案
#csv是非常常用的檔案
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
		#針對f的檔案，做write的動作，這個才是真正的寫入
		#open只是打開檔案，要有寫f.write才真正寫
		#csv檔案是透過","去做格子區隔的

