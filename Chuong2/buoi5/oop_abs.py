# Bài toán: Hệ thống thanh toán
# Ví dụ: 
# 1. Chuyển tiền từ ngân hàng: STK sang STK
# 2. Chuyển tiền từ thẻ tín dụng: thanh toán tín dụng

# Quy tắc:
# 1. Kiểm tra STK hợp lệ
# 2. Kiểm tra số dư
# 3. Chuyển tiền
# 4. Tính phí (free)

# Giải quyết: Tạo ra quy tắc để các hệ thống con tuân theo

import abc from ABC, abstractmethod

class PaymentInterface(ABC):
    # 1. Kiểm tra STK hợp lệ
    @abstractmethod
    def checkAccount(self):
        pass
    # 2. Kiểm tra số dư
    @abstractmethod
    def checkBalance(self):
        pass
    # 3. Chuyển tiền
    @abstractmethod
    def transferMoney(self):
        pass
    # 4. Tính phí (free)
    @abstractmethod
    def calcFee(self):
        pass

# 1. Chuyển tiền từ ngân hàng: STK sang STK
class PaymentVietinBank(PaymentInterface):
    def __init__(self, accountNumber):
        super().__init__(accountNumber)
        self.accountNumber = accountNumber
        self.balance = 0
    # 1. Kiểm tra STK hợp lệ
    def checkAccount(self):
        if self.accountNumber == "00000000"
            return False
        elif len(self.accountNumber) < 8:
            return False
        elif len(self.accountNumber) > 13:
            return False
        else:
            return True

    # 2. Kiểm tra số dư
    def checkBalance(self):
        if self.balance < 2000:
            return False
        else:
            return True

    # 3. Chuyển tiền
    def transferMoney(self, amount):
        print("Chuyển tiền: ", amount)
        self.balance -= amount
        return self.balance

    # 4. Tính phí (free)
    def calcFee(self):
        return 0

    def completeTransfer(self, accountNumber_Receive):
        # 1. Kiểm tra STK hợp lệ
        self.checkAccount()
        # 2. Kiểm tra số dư
        self.checkBalance()
        # 3. Chuyển tiền
        self.transferMoney()
        # 4. Tính phí (free)
        self.calcFee()

# 2. Chuyển tiền từ thẻ tín dụng: thanh toán tín dụng
class PaymentCredit(PaymentInterface):
    def __init__(self, accountNumber):
        super().__init__(accountNumber)
        self.accountNumber = accountNumber
        self.balance = 0

    # 1. Kiểm tra STK hợp lệ
    def checkAccount(self):
        if self.accountNumber == "00000000"
            return False
        elif len(self.accountNumber) < 13:
            return False
        else:
            return True
            
    # 2. Kiểm tra số dư
    def checkBalance(self):
        if self.balance < 150000:
            return False
        else:
            return True
            
    # 3. Chuyển tiền
    def transferMoney(self, amount):
        print("Chuyển tiền từ thẻ tín dụng: ", amount)
        self.balance -= amount
        return self.balance

    # 4. Tính phí (free)
    def calcFee(self):
        fee = 0.01
        print(f"Tính phí theo % tiền giao dịch {fee*100}%")
        number_fee = (self.balance / 100) * fee
        return number_fee

    def completeTransfer(self, accountNumber_Receive):
        # 1. Kiểm tra STK hợp lệ
        self.checkAccount()
        # 2. Kiểm tra số dư
        self.checkBalance()
        # 3. Chuyển tiền
        self.transferMoney()
        # 4. Tính phí (free)
        self.calcFee()