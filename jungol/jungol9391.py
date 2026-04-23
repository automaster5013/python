h, m = map(int, input().split())
# print(h, m)
if h >= 12:
    signal = "PM"
    if h >= 13:
        h -= 12
else:
    signal = "AM"

print(f"{h:02d} : {m:02d} {signal}")

####################################################(방법01)

h, m = map(int, input().split())
# print(h, m)
signal = "PM" if h >= 12 else "AM"
compute_h = h - 12 if h >= 13 else h

print(f"{compute_h:02d} : {m:02d} {signal}")

####################################################(방법02)

h, m = map(int, input().split())
# print(h, m)
signal = "AM"
if h >= 12:
    signal = "PM"
    if h >= 13: h -= 12

tepal = "{:02d} : {:02d} {}"
print(tepal.format(h, m, signal))

####################################################(방법03)

h, m = map(int, input().split())
# print(h, m)
is_pm = h // 12
signal = ["AM", "PM"][is_pm]

h = h - 12 if h >= 13 else h

print("%02d : %02d %s" % (h, m, signal))

####################################################(방법04)

