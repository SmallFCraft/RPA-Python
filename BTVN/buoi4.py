import math

# Bài 1: Giải phương trình bậc 2: ax^2 + bx + c = 0
def giai_phuong_trinh_bac_2(a, b, c):
    print(f"\n=== Bài 1: Giải phương trình {a}x² + {b}x + {c} = 0 ===")
    
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm")
            else:
                print("Phương trình vô nghiệm")
        else:
            x = -c / b
            print(f"Phương trình có nghiệm duy nhất: x = {x}")
    else:
        delta = b**2 - 4*a*c
        print(f"Delta = {delta}")
        
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta == 0:
            x = -b / (2*a)
            print(f"Phương trình có nghiệm kép: x = {x}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"Phương trình có 2 nghiệm phân biệt:")
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")

# Bài 2: In ra bảng cửu chương từ 2 đến 9
def bang_cuu_chuong():
    print("\n=== Bài 2: Bảng cửu chương từ 2 đến 9 ===")
    for i in range(2, 10):
        print(f"\n--- Bảng cửu chương {i} ---")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")

# Bài 3: Tính tổng các số chẵn từ 1 đến 100
def tong_so_chan():
    print("\n=== Bài 3: Tổng các số chẵn từ 1 đến 100 ===")
    tong = sum(i for i in range(1, 101) if i % 2 == 0)
    print(f"Tổng các số chẵn từ 1 đến 100: {tong}")

# Bài 4: Kiểm tra số nguyên tố
def kiem_tra_nguyen_to(n):
    print(f"\n=== Bài 4: Kiểm tra {n} có phải số nguyên tố không ===")
    
    if n < 2:
        print(f"{n} không phải là số nguyên tố")
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(f"{n} không phải là số nguyên tố")
            return False
    
    print(f"{n} là số nguyên tố")
    return True

# Bài 5: In ra hình tam giác với chiều cao n
def in_tam_giac(n):
    print(f"\n=== Bài 5: Hình tam giác với chiều cao {n} ===")
    for i in range(1, n + 1):
        print("* " * i)

# Bài 6: Tìm ƯCLN và BCNN của hai số
def ucln_bcnn(a, b):
    print(f"\n=== Bài 6: ƯCLN và BCNN của {a} và {b} ===")
    
    # Tính ƯCLN bằng thuật toán Euclid
    ucln = math.gcd(a, b)
    
    # Tính BCNN theo công thức: BCNN = (a * b) / ƯCLN
    bcnn = abs(a * b) // ucln
    
    print(f"ƯCLN({a}, {b}) = {ucln}")
    print(f"BCNN({a}, {b}) = {bcnn}")

# Bài 7: Đếm số lượng chữ số của một số nguyên
def dem_chu_so(n):
    print(f"\n=== Bài 7: Đếm số lượng chữ số của {n} ===")
    so_luong = len(str(abs(n)))
    print(f"Số {n} có {so_luong} chữ số")

# Chương trình chính
if __name__ == "__main__":
    print("=" * 50)
    print("CHƯƠNG TRÌNH BÀI TẬP BUỔI 4")
    print("=" * 50)
    
    # Bài 1: Giải phương trình bậc 2
    giai_phuong_trinh_bac_2(1, -5, 6)  # x^2 - 5x + 6 = 0
    
    # Bài 2: Bảng cửu chương
    bang_cuu_chuong()
    
    # Bài 3: Tổng số chẵn
    tong_so_chan()
    
    # Bài 4: Kiểm tra số nguyên tố
    kiem_tra_nguyen_to(17)
    kiem_tra_nguyen_to(20)
    
    # Bài 5: In tam giác
    in_tam_giac(5)
    
    # Bài 6: ƯCLN và BCNN
    ucln_bcnn(48, 18)
    
    # Bài 7: Đếm chữ số
    dem_chu_so(12345)
    dem_chu_so(-9876)
    
