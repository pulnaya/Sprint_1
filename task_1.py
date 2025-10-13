s = '1h 45m,360s,25m,30m 120s,2h 60s'
result = 0

for el in s.replace(',', ' ').split():
    if 'h' in el:
        result += int(el[:-1])*60
    elif 'm' in el:
        result += int(el[:-1])
    else:
        result += int(el[:-1])//60

print(result)