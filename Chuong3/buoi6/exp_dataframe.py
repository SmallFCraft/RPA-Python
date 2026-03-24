import pandas as pd

dataDict = {
    "Ten" : ["Bảo", "Huy", "Trunglele", "Tân", "Nguyen Van"],
    "Lop" : ["23CT1", "23CT2", "23CT3", "23CT4", "25CT5"],
    "DiemTB" : [8.0, 7.9, 9.3, 7.4, 9.4],
    "Tuoi" : [20, 20, "", 20 ,21],
    "Dia Chi" : ["DN", "HCM", "HN", "ĐN", "BN"]
}

dfInput = pd.DataFrame(data = dataDict) 

print(dfInput)

print("____________________________________")
# Truy xuất cột Tên
print(dfInput["Ten"])

print("____________________________________")
# Truy xuất cột Điểm
print(dfInput["DiemTB"])

# Truy xuất dòng row
print("____________________________________")
print(dfInput.loc[0])

# Lấy ra giá trị trong 0 = index, tên cột
print("____________________________________")
print(dfInput.loc[0, "Ten"])

# Lấy ra giá trị tại cột DiemTB >= 8.0 và Lớp 23CT1
print("____________________________________")
df_filler = dfInput[(dfInput["DiemTB"] >= 8.0) & (dfInput["Lop"] == "23CT1")] 
print(df_filler)

myVar = None
myStr = ""
myName = "Huy"
print("____________________________________")

#Xóa dũ liệu dòng trống: NaN
print(dfInput.dropna())

# Điền dữ liệu vào dòng trống: NaN
print(dfInput.fillna(0))

# GroupBy: Cột Lớp - lấy ra bảng điểm theo lớp
df_group_by = dfInput.groupby("Lop")
print(df_group_by)

for i_group in df_group_by:
    print(i_group)
    print("____________________________________")
