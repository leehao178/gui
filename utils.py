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


# import numpy as np


def check_monotonicity(data: np.array) -> bool:
    """
    檢查輸入的numpy array是否為連續上升或下降。
    
    參數：
    data -- 輸入的numpy array
    
    返回值：
    如果輸入的numpy array為連續上升或下降，則返回False；否則返回True。
    """
    
    # 檢查相鄰是否有相同數值
    if np.any(data[:-1] == data[1:]):
        print("資料中有相同數值")
        # 將相同數值的元素替換成nan
        data = data.astype(float)
        data[np.where(data[:-1] == data[1:])[0]+1] = np.nan
    
    # 檢查資料是否為連續上升
    if np.all(np.diff(data) > 0):
        print("資料為連續上升")
        return False
    
    # 檢查資料是否為連續下降
    elif np.all(np.diff(data) < 0):
        print("資料為連續下降")
        return False
    
    # 資料不是連續上升或下降
    else:
        print("資料不是連續上升或下降")
        return True




continuous_rising_integers = np.arange(1, 11)
print(continuous_rising_integers)
continuous_descending_integers = np.arange(10, 0, -1)
print(continuous_descending_integers)

random_integers = np.random.randint(0, 100, 10)
print(random_integers)

real_data = np.array([1, 3, 2, 7, 8, 6, 8, 6, 5, 5])
print(real_data)
ans = check_monotonicity(real_data)




if ans:
    print('True')
else:
    print('False')