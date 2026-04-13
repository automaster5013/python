def GetCategory(gender, age):
    mapping = {
        ('M', True): 'MAN',
        ('M', False): 'BOY',
        ('F', True): 'WOMAN',
        ('F', False): 'GIRL'
    }
    return mapping[(gender.upper(), age >= 20)]

gen, age = input().split()
# print(gen, age)
print(GetCategory(gen, int(age)))

#########################################################(방법01)

def GetCategory(gender, age):
    g = gender.upper()
    is_adult = age >= 20
    
    if g == 'M':
        return 'MAN' if is_adult else 'BOY'
    else:
        return 'WOMAN' if is_adult else 'GIRL'

data = input().split()
gen, age = data[0], int(data[1])
# print(gen, age)
print(GetCategory(gen, age))

#########################################################(방법02)

def GetCategory(gender, age):
    table = [
        ['MAN', 'BOY'],  
        ['WOMAN', 'GIRL'] 
    ]
    
    g_idx = 0 if gender.upper() == 'M' else 1
    a_idx = 0 if age >= 20 else 1
    
    return table[g_idx][a_idx]

gen, age = input().split()
# print(gen, age)
print(GetCategory(gen, int(age)))

#########################################################(방법03)

def GetCategory(gender, age):
    is_adult = age >= 20
    is_male = gender.upper() == 'M'
    
    if is_male:
        return 'MAN' if is_adult else 'BOY'
    else:
        return 'WOMAN' if is_adult else 'GIRL'
    
gen, age = input().split()
# print(gen, age)
print(GetCategory(gen, int(age)))

#########################################################(방법04)

def check_info(g, a):
    if g == 'M' or g == 'm':
        if a >= 20:
            ret = 'MAN'
        else:
            ret = "BOY"
    else:
        if a >= 20:
            ret = "WOMAN"
        else:
            ret = "GIRL"
    return ret

gender, age = input().split()
# print(gender, int(age))
print (check_info(gender, int(age)))

#########################################################(방법05)

