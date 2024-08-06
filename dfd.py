import pandas as pd
data = {
    '학번': range(2000,2010),
    '성적' : [85, 95, 75, 70, 100, 95, 85, 50, 85]
}
print(data)
print(pd.DataFrame(data))
print('----------')
print('프레임 컬럼 순서 변경')
print(pd.DataFrame(data, columns = ['성적','학번']))


# import numpy as np
# data = [1,2,3]
# arr1 = np.array(data)
#
# print(arr1, type(arr1))