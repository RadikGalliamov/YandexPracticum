times = '1h 45m,360s,25m,30m 120s,2h 60s'
times = times.split(',')

time = []
for r in times:
    times2 = r.split(' ')
    time += times2

all_times = 0

for t in time:
    if 'h' in t:
        all_times += int(t[:-1])*60
    elif 'm' in t:
        all_times += int(t[:-1])
    else:
        all_times += int(t[:-1])//60

print(all_times)





