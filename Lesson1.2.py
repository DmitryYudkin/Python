Time = int(input('Insert Your time in seconds'))
Hours = Time // 3600
Minutes = (Time - Hours * 3600) // 60
Seconds = Time % 60
print(f'{Hours:02}.{Minutes:02}.{Seconds:02}')