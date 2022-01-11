N = 5
# N시 00분 00초 
# 0 <= SS <= 59
ans = 0
for hour in range(0, N+1):
    for minutes in range(0, 60):
        for second in range(0, 60):
            make_time = str(hour) + str(minutes) + str(second)
            if str(N) in make_time:
                # print("있음!!", make_time)
                ans += 1
print("ans: ", ans)

