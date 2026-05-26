def solution(id_pw, db):
    user_id, user_pw = id_pw[0], id_pw[1]
    db_dict = {row[0]: row[1] for row in db}
    
    if user_id in db_dict:
        if db_dict[user_id] == user_pw:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"


id_pw1 = ["meosseugi", "1234"]
db1 = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

id_pw2 = ["programmer01", "15789"]
db2 = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

id_pw3 = ["rabbit04", "98761"]
db3 = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]

print(solution(id_pw1, db1))
print(solution(id_pw2, db2))
print(solution(id_pw3, db3))

#############################################################################

def solution(id_pw, db):
    user_id, user_pw = id_pw
    id_found = False  
    
    for db_id, db_pw in db:
        if db_id == user_id:
            id_found = True
            if db_pw == user_pw:
                return "login"
                
    return "wrong pw" if id_found else "fail"


id_pw1 = ["meosseugi", "1234"]
db1 = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

id_pw2 = ["programmer01", "15789"]
db2 = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

id_pw3 = ["rabbit04", "98761"]
db3 = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]

print(solution(id_pw1, db1))
print(solution(id_pw2, db2))
print(solution(id_pw3, db3))

#############################################################################

def solution(id_pw, db):
    if id_pw in db:
        return "login"
        
    db_ids = [row[0] for row in db]
    if id_pw[0] in db_ids:
        return "wrong pw"
        
    return "fail"


id_pw1 = ["meosseugi", "1234"]
db1 = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

id_pw2 = ["programmer01", "15789"]
db2 = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

id_pw3 = ["rabbit04", "98761"]
db3 = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]

print(solution(id_pw1, db1))
print(solution(id_pw2, db2))
print(solution(id_pw3, db3))

#############################################################################

def solution(id_pw, db):
    user_id, user_pw = id_pw
    db_dict = dict(db) 
    
    saved_pw = db_dict.get(user_id)
    
    if saved_pw is None:
        return "fail"
    
    return "login" if saved_pw == user_pw else "wrong pw"


id_pw1 = ["meosseugi", "1234"]
db1 = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

id_pw2 = ["programmer01", "15789"]
db2 = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

id_pw3 = ["rabbit04", "98761"]
db3 = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]

print(solution(id_pw1, db1))
print(solution(id_pw2, db2))
print(solution(id_pw3, db3))

#############################################################################

def solution(id_pw, db):
    user_id, user_pw = id_pw
    i = 0
    n = len(db)
    while i < n:
        if db[i][0] == user_id:
            
            return "login" if db[i][1] == user_pw else "wrong pw"
        i += 1
        
    return "fail"


id_pw1 = ["meosseugi", "1234"]
db1 = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

id_pw2 = ["programmer01", "15789"]
db2 = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

id_pw3 = ["rabbit04", "98761"]
db3 = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]

print(solution(id_pw1, db1))
print(solution(id_pw2, db2))
print(solution(id_pw3, db3))

#############################################################################

