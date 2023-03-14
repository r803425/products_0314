# 記帳程式
# １.輸入商品名稱(輸入q離開)／價格， 並存入列表
products = []
while True:
    name = input('請輸入名稱(按q/Q離開) : ')
    if name == 'q' or name == 'Q':
        break
    price = input('請輸入價格 : ')
    # # p = []
    # # p.append(name)
    # # p.append(price)
    # p = [name, price]
    products.append([name, price])
print(products)
# print(products[0][0])
# print(products[0][1])
print('---------------------------------')

# 2.印出products的每個物品跟價格
for p in products:
    # print(p)
    print(p[0], '的價格是', p[1])