import numpy as np



def check_spec(sorted_data):
    # 取得最新的兩筆資料
    latest_data = sorted_data[-2:]
    
    # 判斷是否在範圍內
    within_spec = np.logical_and(
        latest_data['point'] >= latest_data['lowspec'],
        latest_data['point'] <= latest_data['highspec']
    )
    
    # 檢查是否全部為 True
    return np.all(within_spec)


def check_spec2(sorted_data):
    # 取得最新的兩筆資料
    latest_data = sorted_data[-2:]
    
    # 判斷是否在範圍內
    for data in latest_data:
        point = data['point']
        lowspec = data['lowspec']
        highspec = data['highspec']
        if point < lowspec or point > highspec:
            return False
    
    return True


def check_order(data):
    # 檢查資料筆數是否小於 6
    if len(data) < 6:
        return False
    
    # 設置計數器和上一次的旗標
    count = 1
    prev_flag = 0
    
    # 逐個檢查每一點是否連升降
    for i in range(1, len(data)):
        # 判斷上升或下降
        curr_flag = 1 if data[i] > data[i-1] else -1
        
        # 如果與上一次判斷結果不同，則返回 True
        if curr_flag != prev_flag:
            return True
        
        # 如果連續上升，計數器加一
        if curr_flag == 1:
            count += 1
        
        # 如果計數器達到 6，返回 False
        if count == 6:
            return False
        
        # 更新上一次的旗標
        prev_flag = curr_flag
    
    # 迴圈結束都沒有返回 False，表示沒有連續上升的情況
    return True
