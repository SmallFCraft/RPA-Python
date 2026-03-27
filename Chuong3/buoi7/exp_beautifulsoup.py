from bs4 import BeautifulSoup
import requests
import pandas as pq

dataList = []
dataStats = []

for i_page in range(1,6):
    # 1. Lấy dữ liệu trong 5 trang đầu
    url = "http://books.toscrape.com/catalogue/page-" + str(i_page) + ".html"
    # 2. Lấy thông tin.
    response = requests.get(url)
    content_res = response.content
    soup = BeautifulSoup(content_res, 'html.parser')
    #print(soup)

    product_books = soup.find_all("article", class_ = "product_pod")
    # print(product_books)
    for i_book in product_books:
        # print(i_book)
        # Tên sách
        name = i_book.h3.a["title"]
        print(name)
        # Giá sách
        price = i_book.find("p", "price_color").text
        print(price)
        # Đánh giá
        rate = i_book.find("p", "star-rating")["class"][1]
        print(rate)
        # Tình trạng
        stock = str(i_book.find("p", "instock availability").text).replace("\n", "").strip()
        print(stock)
        
        dataList.append({
            "Tên sản phẩm" : name,
            "Giá" : price,
            "Đánh giá" : rate,
            "Tình trạng" : stock
        })



# Thống kê
# 1. Tổng số sách
tongSach = len(dataList)
print("Tổng số sách đã thu nhập là: " + str(tongSach))

# 2. Giá trung bình
tongGia = 0
for i_sach in dataList:
    gia = float(i_sach["Giá"].replace("£", ""))
    tongGia += gia

giaTB = tongGia/tongSach
print(f"Giá trung bình: £{giaTB:.2f}")

# 3. Số sách theo từng đánh giá 
demRate = {}
for i_rate in dataList:
    rating = i_rate["Đánh giá"]
    if rating in demRate:
        demRate[rating] += 1
    else:
        demRate[rating] = 1

for rating, soLuong in demRate.items():
    print(f"Đánh giá {rating}: {soLuong} sách")

# 4. Sách đắt nhất và rẻ nhất

dataStats = [
    {"Thông tin": "Tổng số sách", "Số liệu": tongSach},
    {"Thông tin": "Giá trung bình", "Số liệu": f"£{giaTB:.2f}"},
  
]


df_list = pq.DataFrame(dataList)
df_stats = pq.DataFrame(dataStats)
print(df_list)
print(df_stats)

with pq.ExcelWriter("Books.xlsx", engine="openpyxl") as writer:
    df_list.to_excel(writer, sheet_name="Danh Sách Sách", index=False)
    df_stats.to_excel(writer, sheet_name="Thống Kê", index=False)

print("Đã xuất file Books.xlsx thành công!")
