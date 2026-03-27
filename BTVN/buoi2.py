von_ban_dau = 100000000  
lai_suat_nam = 0.05
thoi_gian_gui = 5

# 1. Tính tiền lãi sau 3 năm
lai_3_nam = von_ban_dau * lai_suat_nam * 3

# 2. Tính tổng tiền nhận được (sau 5 năm)
lai_5_nam = von_ban_dau * lai_suat_nam * thoi_gian_gui
tong_tien = von_ban_dau + lai_5_nam

# 3. Tính tiền lãi trung bình mỗi tháng trong kỳ hạn 5 năm
so_thang = thoi_gian_gui * 12
lai_moi_thang = lai_5_nam / so_thang

# In kết quả ra màn hình với định dạng dễ đọc
print("KẾT QUẢ TÍNH TOÁN LÃI ĐƠN:")
print("-" * 30)
print(f"1. Tiền lãi sau 3 năm: {lai_3_nam:,.0f} VNĐ")
print(f"2. Tổng tiền nhận được (sau 5 năm): {tong_tien:,.0f} VNĐ")
print(f"3. Tiền lãi trung bình mỗi tháng: {lai_moi_thang:,.0f} VNĐ")