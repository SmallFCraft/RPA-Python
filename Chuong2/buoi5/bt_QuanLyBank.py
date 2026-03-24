# Bài Tập: Xây dựng hệ thống quản lý tài khoản ngân hàng với các loại tài khoản khác nhau

import abc from ABC, abstractmethod

class Account(ABC):
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.balance = balance

    @abstractmethod
    def guiTien(self, amount):
        pass
    
    def rutTien(self, amount):
        pass
    
    def chuyenTien(self, amount):
        pass
    
    def kiemTraSoDu(self):
        pass
    
    