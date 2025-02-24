def is_leap_year(year):  
    """Kiểm tra xem năm có phải là năm nhuận hay không."""  
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  
        return True  
    else:  
        return False  

nhap_nam = int(input("Nhập năm cần kiểm tra: "))  
if is_leap_year(nhap_nam):  
    print(f"Năm {nhap_nam} là năm nhuận.")  
else:  
    print(f"Năm {nhap_nam} không phải là năm nhuận.")
