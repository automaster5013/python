name = input()
age = int(input())

current_year = 2019
target_year = current_year - age + 100

print(f"{name}(은)는 {target_year}년에 100세가 될 것입니다.")

################################################################(방법01)

info = []
info.append(input())  
info.append(int(input()))  

year100 = 2019 - info[1] + 100
print(info[0] + "(은)는 " + str(year100) + "년에 100세가 될 것입니다.")

################################################################(방법02)

name, age = input(), int(input())
base_year = 2019

result_year = base_year + (100 - age)

output = "{}(은)는 {}년에 100세가 될 것입니다.".format(name, result_year)
print(output)

################################################################(방법03)

name = input()
year = 2019 - int(input()) + 100

message = name + "(은)는 " + str(year) + "년에 100세가 될 것입니다."
print(message)

################################################################(방법04)

name = input()
while True:
    try:
        age_str = input()
        age = int(age_str)
        break
    except ValueError:
        pass 

target = 2019 - age + 100
print("%s(은)는 %d년에 100세가 될 것입니다." % (name, target))

################################################################(방법05)

now = datetime.now()
