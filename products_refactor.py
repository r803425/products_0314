import os

# 讀取檔案
def read_file(filename, products):
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    print('-------------------------------------------')
    return products

# 讀取檔案，剩下檢查檔案在不在
# def read_file(filename):
#     # products = []
#     if os.path.isfile(filename):
#         print('成功找到檔案')
#         # with open(filename, 'r', encoding = 'utf-8') as f:
#         #     for line in f:
#         #         if '商品,價格' in line:
#         #             continue
#         #         name, price = line.strip().split(',')
#         #         products.append([name, price])
#         # print(products)
#     else:
#         print('找不到檔案哦!!!，請寫入檔案新增')
#     print('-------------------------------------------')
    # return products

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入名稱(按q/Q離開) : ')
        if name == 'q' or name == 'Q':
            break
        price = input('請輸入價格 : ')
        products.append([name, price])
    print(products)
    print('-------------------------------------------')
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        # print(p)
        print(p[0], '的價格是', p[1])
    print('-------------------------------------------')

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename = 'products.csv'
    products = []
    if os.path.isfile(filename):
        print('成功找到檔案')
        products = read_file(filename, products)
    else:
        print('找不到檔案哦!!!，請寫入檔案新增')
    products = user_input(products)
    print_products(products)
    write_file(filename, products)
    
main()