#9
vrk = int(input())

day_seconds = 24 * 3600
days = vrk // day_seconds
vrk2 = vrk % day_seconds
hours = vrk2 // 3600  
minutes = (vrk2 % 3600) // 60  
seconds = vrk2 % 60  

print(days, hours, minutes, seconds)