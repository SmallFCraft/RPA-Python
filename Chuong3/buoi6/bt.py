import pandas as pd

dataSV = {
    "MaSV" : ["MS001", "MS002", None, "MS004", "MS005"],
    "HoTen" : ["Huy", "Bao", "Tan", "Trunglele", "Nguyen Van A"],
    "Lop" : ["23CT1", "23CT2", None, "23CT4", "25CT5"],
    "DiemPython" : [8.0, 7.9, 9.3, 7.4, 9.4],
    "DiemWeb" : [9.0, 8.3, 7.3, 6.3, None],
    "DiemDatabase" : [7.0, 6.3, 9.3, 7.4, 8.8]
}

dfInput = pd.DataFrame(data = dataSV)

# 2. Đọc file hoặc đọc từ dữ liệu và kiểm tra dữ liệu null
print("____________________________________")
print(dfInput)

# 3. Điền giá trị null = 0
print("____________________________________")
print(dfInput.fillna(0))

# 4. Tạo cột DiemTB = trung bình 3 môn
print("____________________________________")
DiemTB = (dfInput["DiemPython"] + dfInput["DiemWeb"] + dfInput["DiemDatabase"]) / 3
print(DiemTB)

# 5. Tạo cột


