data = list(map(int, input().split(' ')))
day = data[0]
hour = data[1]
minute = data[2]
timestamp = data[3]
today = timestamp-((timestamp//(day*hour*minute))*day*hour*minute)
hour_t = today//(hour*minute)
minute_t = (today-(hour_t*hour*minute))//minute
second_t = (today-((hour_t*hour*minute)+(minute_t*minute)))
print(str(hour_t)+' '+str(minute_t)+' '+str(second_t))