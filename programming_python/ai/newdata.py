import pandas as pd

houses_data = {
    'Masa7a': [200, 350, 150, 450, 280, 180, 500],             # المساحة م²
    'Ghoraf': [4, 6, 3, 7, 5, 4, 8],                           # عدد الغرف
    'Doraat_Miah': [3, 5, 2, 6, 4, 3, 6],                      # عدد دورات المياه
    '3omr_Albeet': [5, 0, 12, 2, 7, 15, 1],                    # عمر البيت بالسنوات
    'Al_Mantaqa': [3, 5, 2, 5, 4, 2, 5],                       # تقييم الحي (1 إلى 5)
    
   
    'Target_Price': [950000, 2400000, 650000, 3100000, 1600000, 780000, 3800000],  # السعر الكلي بالريال
    'Target_Installment': [4750, 12000, 3250, 15500, 8000, 3900, 19000],            # القسط الشهري
    'Target_Deposit': [95000, 240000, 65000, 310000, 160000, 78000, 380000]         # الدفعة الأولى
}


df = pd.DataFrame(houses_data)
df.to_excel("real_estate.xlsx", index=False)

print("real_estate.xlsx")
