list = [1,2,4,6,8]
target = 9
for i,j in enumerate(list):
    if target - j in list:
        print(i)
for i in range(len(list)):
    for j in range(len(list)):
        if list[i] + list[j] == target:
            print(i,j)