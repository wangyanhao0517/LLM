matrix = [[1,2,3],[4,5,6]]
# matrix = [[2,3]]
m, n = len(matrix), len(matrix[0])
# 遍历上半部分
res = [matrix[0][0]]
tag = 1
for i in range(1, m + n -1):
    if i % 2 == 0:
        
print(res)