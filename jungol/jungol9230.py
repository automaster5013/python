hour = int(input())
# print(hour)

if hour < 12:
    print("AM")
else:
    print("PM")

##########################################(방법01)

hour = int(input())
# print(hour)
print("AM" if hour < 12 else "PM")

##########################################(방법02)

hour = int(input())
# print(hour)
results = ["AM", "PM"]
print(results[hour >= 12])

##########################################(방법03)

hour = int(input())
# print(hour)
is_pm = bool(hour // 12)
print("PM" if is_pm else "AM")

##########################################(방법04)

time = int(input())
# print(time)

res = ""
if time < 12:
    res = "AM"
else:
    res = "PM"
print(res)

##########################################(방법05)


