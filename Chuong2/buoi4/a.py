# a = int(input('Nhap so a: '))
# b = int(input('Nhap so b: '))

# def tinhTong(a , b):
#     tong = a + b
#     return tong, "abc", "a"

# print(tinhTong(a,b))

# rs1, mystr = tinhTong(a, b)
# print("rs type: ", type(rs1))
# print("my str: ", type(mystr))


def soChan():
    return sum(i for i in range(1, 11) if i % 2 == 0)
print(soChan()) 
