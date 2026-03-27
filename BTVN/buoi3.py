def main():
    while True:
        # Hiển thị Menu
        print("\n" + "="*40)
        print("    MENU BÀI TẬP PYTHON CƠ BẢN")
        print("="*40)
        print("1. Nhập và in thông tin cá nhân")
        print("2. Tính diện tích và chu vi hình chữ nhật")
        print("3. Chuyển đổi nhiệt độ từ C sang F")
        print("4. Kiểm tra số nguyên chẵn hay lẻ")
        print("5. Tính tổng, hiệu, thương của hai số thực")
        print("0. Thoát chương trình")
        print("="*40)
        
        # Lấy lựa chọn của người dùng
        lua_choi = input("Vui lòng chọn bài tập (0-5): ")
        
        if lua_choi == '1':
            print("\n--- Bài 1: Thông tin cá nhân ---")
            ho_ten = input("Nhập họ tên của bạn: ")
            tuoi = int(input("Nhập tuổi của bạn: "))
            diem_tb = float(input("Nhập điểm trung bình: "))
            
            print("\nKết quả:")
            print(f"Họ tên: {ho_ten} | Tuổi: {tuoi} | Điểm TB: {diem_tb}")

        elif lua_choi == '2':
            print("\n--- Bài 2: Hình chữ nhật ---")
            chieu_dai = float(input("Nhập chiều dài: "))
            chieu_rong = float(input("Nhập chiều rộng: "))
            
            chu_vi = (chieu_dai + chieu_rong) * 2
            dien_tich = chieu_dai * chieu_rong
            
            print(f"\nKết quả: Chu vi = {chu_vi}, Diện tích = {dien_tich}")

        elif lua_choi == '3':
            print("\n--- Bài 3: Chuyển đổi nhiệt độ ---")
            do_c = float(input("Nhập nhiệt độ (độ C): "))
            do_f = (do_c * 9/5) + 32
            print(f"\nKết quả: {do_c}°C = {do_f}°F")

        elif lua_choi == '4':
            print("\n--- Bài 4: Kiểm tra chẵn lẻ ---")
            so_nguyen = int(input("Nhập vào một số nguyên: "))
            if so_nguyen % 2 == 0:
                print(f"\nKết quả: {so_nguyen} là số chẵn.")
            else:
                print(f"\nKết quả: {so_nguyen} là số lẻ.")

        elif lua_choi == '5':
            print("\n--- Bài 5: Tổng, Hiệu, Thương ---")
            so_a = float(input("Nhập số thực thứ nhất: "))
            so_b = float(input("Nhập số thực thứ hai: "))
            
            print(f"\nKết quả:")
            print(f"Tổng: {so_a + so_b}")
            print(f"Hiệu: {so_a - so_b}")
            
            if so_b != 0:
                print(f"Thương: {so_a / so_b}")
            else:
                print("Thương: Lỗi chia cho 0!")

        elif lua_choi == '0':
            print("\nCảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break # Thoát khỏi vòng lặp while

        else:
            print("\nLựa chọn không hợp lệ. Vui lòng thử lại!")
        
        # Dừng lại một chút để người dùng đọc kết quả trước khi hiện lại menu
        input("\nNhấn Enter để tiếp tục...")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()