#記帳程式
import os

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品, 價格' in line:
				continue  #繼續、略過
		    name, price =line,strip().split(',')
		    products.append([name, price])
	return products
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products
def print_products(products):
	for p in prducts:
		print(p[0], '的價格是', p[1])
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ','+str(p[1]) + "\n")
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('具有此檔案')
		products = read_file(filename)
	else:
		print('無此檔案')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()




#後續新增的功能
#products = []
#with open('products.csv', 'r', encoding= 'utf-8') as f:
#	for line in f:
#		name, price = line.strip().split(',')
#切割完直接存成name
#		products.append([name, price])
#print(products)
		   
        #strip先把/n去掉
		#字串切割，把要當切割標準的東西打在括號內


#while loop適合用在不知道次數的情況
#while True:
#	name = input('Product name: ')
#	if name == 'q':
#		break
#	price = input('The price of products: ')
#	price = int(price)
#	p =[name, price]  #比較簡潔的寫法
#	products.append(p)
#簡潔的寫法:
#products.append([name, price])
#基礎寫法	
#   p=[]
#	p.append(name)
#	p.append(price)
#print(products)
#存取二維清單
#product[0][0] 先走進去第0格 
#for p in products:
#	print('The price of', p[0], 'is', p[1])

#with open('products.csv', 'w', encoding='utf-8') as f: 
#現在是write所以原本沒有這個檔案沒有關係
#但如果本來有
#用f稱呼打開的檔案
#csv是非常常用的檔案
#utf-8是可以打開各種語言的廣泛使用編碼
#	f.write('商品,價格\n')
#	for p in products:
#		f.write(p[0] + ',' + str(p[1]) + '\n')
		#針對f的檔案，做write的動作，這個才是真正的寫入
		#open只是打開檔案，要有寫f.write才真正寫
		#csv檔案是透過","去做格子區隔的
		#記得要做casting，把p[1]變成字串

