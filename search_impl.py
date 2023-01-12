li = [3,4,56,73,2,29]
target = 22
flag =0
for i in range(len(li)):
    if li[i]==target:
        flag =1
        break
if flag ==1:
    print("found")
else:
    print("not found")