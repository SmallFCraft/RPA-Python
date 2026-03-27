from abc import ABC, abstractmethod

# 1. Class Account
class Account(ABC):
    def __init__(self, so_tai_khoan, ten_chu_tai_khoan, so_du):
        self.so_tai_khoan = so_tai_khoan
        self.ten_chu_tai_khoan = ten_chu_tai_khoan
        self.__so_du = so_du  
    
    def get_so_du(self):
        return self.__so_du
    
    def set_so_du(self, so_du):
        if so_du >= 0:
            self.__so_du = so_du
            return self.__so_du
        else:
            print("Số dư không thể âm!")
            return self.__so_du
    
    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien
            print(f"✓ Nạp tiền thành công: {so_tien:,.0f} VNĐ")
            print(f"Số dư hiện tại: {self.__so_du:,.0f} VNĐ")
            return True
        else:
            print("✗ Số tiền nạp phải lớn hơn 0!")
            return False
    
    def rut_tien(self, so_tien):
        if so_tien <= 0:
            print("✗ Số tiền rút phải lớn hơn 0!")
            return False
        elif so_tien > self.__so_du:
            print(f"✗ Số dư không đủ! Số dư hiện tại: {self.__so_du:,.0f} VNĐ")
            return False
        else:
            self.__so_du -= so_tien
            print(f"✓ Rút tiền thành công: {so_tien:,.0f} VNĐ")
            print(f"Số dư còn lại: {self.__so_du:,.0f} VNĐ")
            return True
    
    def hien_thi_thong_tin(self):
        print(f"Số tài khoản: {self.so_tai_khoan}")
        print(f"Tên chủ tài khoản: {self.ten_chu_tai_khoan}")
        print(f"Số dư: {self.__so_du:,.0f} VNĐ")
    
    @abstractmethod
    def tinh_lai_suat(self):
        pass


# 2. Class SavingsAccount
class SavingsAccount(Account):
    def __init__(self, so_tai_khoan, ten_chu_tai_khoan, so_du, lai_suat_thang=0.005):
        super().__init__(so_tai_khoan, ten_chu_tai_khoan, so_du)
        self.lai_suat_thang = lai_suat_thang  # Mặc định 0.5% / tháng
    
    def tinh_lai_suat(self):
        so_du_hien_tai = self.get_so_du()
        tien_lai = so_du_hien_tai * self.lai_suat_thang
        so_du_moi = so_du_hien_tai + tien_lai
        self.set_so_du(so_du_moi)
        print(f"✓ Tính lãi thành công!")
        print(f"Tiền lãi: {tien_lai:,.0f} VNĐ ({self.lai_suat_thang*100}%)")
        print(f"Số dư mới: {so_du_moi:,.0f} VNĐ")
        return tien_lai
    
    def hien_thi_thong_tin(self):
        print("\n" + "="*50)
        print("TÀI KHOẢN TIẾT KIỆM")
        print("="*50)
        super().hien_thi_thong_tin()
        print(f"Lãi suất tháng: {self.lai_suat_thang*100}%")
        print("="*50)


# 3. Class CurrentAccount
class CurrentAccount(Account):
    def __init__(self, so_tai_khoan, ten_chu_tai_khoan, so_du, phi_duy_tri=50000):
        super().__init__(so_tai_khoan, ten_chu_tai_khoan, so_du)
        self.phi_duy_tri = phi_duy_tri  # Mặc định 50,000 VNĐ / tháng
    
    def tinh_lai_suat(self):
        so_du_hien_tai = self.get_so_du()
        if so_du_hien_tai >= self.phi_duy_tri:
            so_du_moi = so_du_hien_tai - self.phi_duy_tri
            self.set_so_du(so_du_moi)
            print(f"✓ Đã trừ phí duy trì: {self.phi_duy_tri:,.0f} VNĐ")
            print(f"Số dư còn lại: {so_du_moi:,.0f} VNĐ")
            return -self.phi_duy_tri
        else:
            print(f"✗ Số dư không đủ để trừ phí duy trì!")
            return 0
    
    def hien_thi_thong_tin(self):
        print("\n" + "="*50)
        print("TÀI KHOẢN THANH TOÁN")
        print("="*50)
        super().hien_thi_thong_tin()
        print(f"Phí duy trì tháng: {self.phi_duy_tri:,.0f} VNĐ")
        print("="*50)


# 4. Class VIPAccount
class VIPAccount(Account):
    def __init__(self, so_tai_khoan, ten_chu_tai_khoan, so_du, lai_suat_thang=0.01):
        super().__init__(so_tai_khoan, ten_chu_tai_khoan, so_du)
        self.lai_suat_thang = lai_suat_thang  # Mặc định 1% / tháng
        self.han_muc_rut = 100000000  # Hạn mức rút 100 triệu / lần
    
    def tinh_lai_suat(self):
        """
        Tính lãi suất cao hơn cho tài khoản VIP
        """
        so_du_hien_tai = self.get_so_du()
        tien_lai = so_du_hien_tai * self.lai_suat_thang
        so_du_moi = so_du_hien_tai + tien_lai
        self.set_so_du(so_du_moi)
        print(f"✓ Tính lãi VIP thành công!")
        print(f"Tiền lãi: {tien_lai:,.0f} VNĐ ({self.lai_suat_thang*100}%)")
        print(f"Số dư mới: {so_du_moi:,.0f} VNĐ")
        return tien_lai
    
    def rut_tien(self, so_tien):
        if so_tien > self.han_muc_rut:
            print(f"✗ Vượt quá hạn mức rút! Hạn mức: {self.han_muc_rut:,.0f} VNĐ")
            return False
        else:
            return super().rut_tien(so_tien)
    
    def hien_thi_thong_tin(self):
        print("\n" + "="*50)
        print("TÀI KHOẢN VIP")
        print("="*50)
        super().hien_thi_thong_tin()
        print(f"Lãi suất tháng: {self.lai_suat_thang*100}%")
        print(f"Hạn mức rút: {self.han_muc_rut:,.0f} VNĐ")
        print("="*50)


if __name__ == "__main__":
    print("="*50)
    print("HỆ THỐNG QUẢN LÝ TÀI KHOẢN NGÂN HÀNG")
    print("="*50)
    
    danh_sach_tai_khoan = []
    
    tk1 = SavingsAccount(
        so_tai_khoan="TK001",
        ten_chu_tai_khoan="Nguyễn Văn A",
        so_du=10000000,
        lai_suat_thang=0.005
    )
    
    tk2 = CurrentAccount(
        so_tai_khoan="TK002",
        ten_chu_tai_khoan="Trần Thị B",
        so_du=5000000,
        phi_duy_tri=50000
    )
    
    tk3 = VIPAccount(
        so_tai_khoan="TK003",
        ten_chu_tai_khoan="Lê Văn C",
        so_du=50000000,
        lai_suat_thang=0.01
    )
    
    danh_sach_tai_khoan = [tk1, tk2, tk3]
    
    print("\n>>> DANH SÁCH TÀI KHOẢN BAN ĐẦU <<<")
    for tk in danh_sach_tai_khoan:
        tk.hien_thi_thong_tin()
    
    print("\n" + "="*50)
    print("TEST CHỨC NĂNG NẠP TIỀN")
    print("="*50)
    print(f"\n>>> Nạp 2,000,000 VNĐ vào tài khoản {tk1.so_tai_khoan} <<<")
    tk1.nap_tien(2000000)
    
    print("\n" + "="*50)
    print("TEST CHỨC NĂNG RÚT TIỀN")
    print("="*50)
    print(f"\n>>> Rút 1,000,000 VNĐ từ tài khoản {tk2.so_tai_khoan} <<<")
    tk2.rut_tien(1000000)
    
    print("\n" + "="*50)
    print("TEST TÍNH LÃI SUẤT / PHÍ DUY TRÌ")
    print("="*50)
    
    print(f"\n>>> Tính lãi cho tài khoản tiết kiệm {tk1.so_tai_khoan} <<<")
    tk1.tinh_lai_suat()
    
    print(f"\n>>> Trừ phí duy trì cho tài khoản thanh toán {tk2.so_tai_khoan} <<<")
    tk2.tinh_lai_suat()
    
    print(f"\n>>> Tính lãi VIP cho tài khoản {tk3.so_tai_khoan} <<<")
    tk3.tinh_lai_suat()
    
    print("\n" + "="*50)
    print("DANH SÁCH TÀI KHOẢN SAU KHI GIAO DỊCH")
    print("="*50)
    for tk in danh_sach_tai_khoan:
        tk.hien_thi_thong_tin()
    
    print("\n" + "="*50)
    print("TỔNG HỢP HỆ THỐNG")
    print("="*50)
    tong_so_du = sum(tk.get_so_du() for tk in danh_sach_tai_khoan)
    print(f"Tổng số tài khoản: {len(danh_sach_tai_khoan)}")
    print(f"Tổng số dư toàn hệ thống: {tong_so_du:,.0f} VNĐ")
    print("="*50)
