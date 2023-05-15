import numpy as np
from utils import check_spec


# 讀取CSV檔案
data = np.genfromtxt('data.csv', delimiter=',', dtype=None, names=True)

# 將color欄位相同的資料分類
colors = np.unique(data['color'])
for color in colors:
    color_data = data[data['color'] == color]
    
    # 對color_data進行排序
    sorted_data = np.sort(color_data, order='date')
    
    # 檢查最新的兩筆資料是否在範圍內
    is_within_spec = check_spec(sorted_data)
    
    print(f'{color} is within spec: {is_within_spec}')
