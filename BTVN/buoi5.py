from abc import ABC, abstractmethod

# 1. Class Employee
class Employee(ABC):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            return self.__salary
        else:
            print("Lương phải lớn hơn 0!")
            return self.__salary
    
    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Tên: {self.name}")
        print(f"Lương cơ bản: {self.__salary:,.0f} VNĐ")
    
    @abstractmethod
    def calculate_salary(self):
        pass


# 2. Class Developer
class Developer(Employee):
    def __init__(self, id, name, salary, programming_language, overtime_hours):
        super().__init__(id, name, salary)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours
    
    def calculate_salary(self):
        luong_co_ban = self.get_salary()
        luong_tang_ca = self.overtime_hours * 200000
        tong_luong = luong_co_ban + luong_tang_ca
        return tong_luong
    
    def display_info(self):
        print("\n" + "="*50)
        print("THÔNG TIN LẬP TRÌNH VIÊN")
        print("="*50)
        super().display_info()
        print(f"Ngôn ngữ lập trình: {self.programming_language}")
        print(f"Số giờ tăng ca: {self.overtime_hours} giờ")
        print(f"Lương tăng ca: {self.overtime_hours * 200000:,.0f} VNĐ")
        print(f"TỔNG LƯƠNG: {self.calculate_salary():,.0f} VNĐ")
        print("="*50)


# 3. Class Manager
class Manager(Employee):
    def __init__(self, id, name, salary, bonus):
        super().__init__(id, name, salary)
        self.bonus = bonus
    
    def calculate_salary(self):
        luong_co_ban = self.get_salary()
        tong_luong = luong_co_ban + self.bonus
        return tong_luong
    
    def display_info(self):
        print("\n" + "="*50)
        print("THÔNG TIN QUẢN LÝ")
        print("="*50)
        super().display_info()
        print(f"Thưởng: {self.bonus:,.0f} VNĐ")
        print(f"TỔNG LƯƠNG: {self.calculate_salary():,.0f} VNĐ")
        print("="*50)


if __name__ == "__main__":
    print("="*50)
    print("HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY")
    print("="*50)
    
    dev1 = Developer(
        id="DEV001",
        name="Nguyễn Văn A",
        salary=15000000,
        programming_language="Python",
        overtime_hours=20
    )
    
    dev2 = Developer(
        id="DEV002",
        name="Trần Thị B",
        salary=18000000,
        programming_language="Java",
        overtime_hours=15
    )
    
    manager1 = Manager(
        id="MGR001",
        name="Lê Văn C",
        salary=25000000,
        bonus=10000000
    )
    
    manager2 = Manager(
        id="MGR002",
        name="Phạm Thị D",
        salary=30000000,
        bonus=15000000
    )
    
    dev1.display_info()
    dev2.display_info()
    manager1.display_info()
    manager2.display_info()
    
    print("\n" + "="*50)
    print("TEST GETTER VÀ SETTER")
    print("="*50)
    print(f"\nLương hiện tại của {dev1.name}: {dev1.get_salary():,.0f} VNĐ")
    print(f"Tăng lương lên 20,000,000 VNĐ...")
    dev1.set_salary(20000000)
    print(f"Lương mới của {dev1.name}: {dev1.get_salary():,.0f} VNĐ")
    print(f"Tổng lương mới (bao gồm tăng ca): {dev1.calculate_salary():,.0f} VNĐ")
    
    print("\n" + "="*50)
    print("TỔNG HỢP LƯƠNG TOÀN CÔNG TY")
    print("="*50)
    
    danh_sach_nhan_vien = [dev1, dev2, manager1, manager2]
    tong_luong_cong_ty = 0
    
    for nv in danh_sach_nhan_vien:
        tong_luong_cong_ty += nv.calculate_salary()
    
    print(f"Tổng số nhân viên: {len(danh_sach_nhan_vien)}")
    print(f"Tổng lương toàn công ty: {tong_luong_cong_ty:,.0f} VNĐ")
    print("="*50)
