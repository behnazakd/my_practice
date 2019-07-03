lst = [50.29999924, 142.8000031,242.6000061, 338.3999939, 435.7999878, 533.2999878, 626.5, 730.900024, 838.799987, 959.4000244, 1070.1999, 1317.900024, 1447.699951, 1581.699951]
t_one = 50
t_tow = 100
for i in range(len(lst) - 1):
    diff=lst[i + 1] - lst[i]
print(diff)
if diff <= t_one :
    print("diff is short")
elif diff >= t_tow:
    print("diff is long")
else :
    print("diff is normal")