# 記帳程式
# 6.檢查檔案，如果沒有檔案會出錯
import os # 作業系統，operating system

products = []
if os.path.isfile('products.csv'): # 相對路徑，檢查檔案在不在
    print('成功找到檔案')
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 強制跳下一迴圈，並不是逃出迴圈
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    print('---------------------------------')
else:
    print('找不到檔案哦!!!，請寫入檔案新增')
    print('---------------------------------')

# 5.讀取檔案
# 變換到第6步驟裡面
# products = []
# with open('products.csv', 'r', encoding = 'utf-8') as f:
#     for line in f:
#         if '商品,價格' in line:
#             continue # 強制跳下一迴圈，並不是逃出迴圈
#         name, price = line.strip().split(',')
#         products.append([name, price])
# print(products)
# print('---------------------------------')

# １.輸入商品名稱(輸入q離開)／價格， 並存入列表
# products = []
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
print('---------------------------------')

# 3.儲存檔案到電腦
# 4.增加商品,價格開頭
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')