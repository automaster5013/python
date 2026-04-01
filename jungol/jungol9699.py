class SoccerTeam:
    def __init__(self, n, p):
        self.name = n
        self.points = int(p)

n, m = map(int, input().split())

teams = [SoccerTeam(*input().split()) for _ in range(n)]

for t in reversed(teams):
    if t.points >= m:
        print(t.name)

########################################################(방법01)

class SoccerTeam:
    def __init__(self, name, points):
        self.name = name
        self.points = int(points)

n, m = map(int, input().split())

all_teams = []
for _ in range(n):
    name, pts = input().split()
    all_teams.append(SoccerTeam(name, pts))

filtered_names = []
for team in all_teams:
    if team.points >= m:
        filtered_names.append(team.name)

for name in filtered_names[::-1]:
    print(name)

########################################################(방법02)

class SoccerData:
    def __init__(self, name, score):
        self.name = name
        self.score = int(score)

n, m = map(int, input().split())

db = []
for _ in range(n):
    name, s = input().split()
    db.append(SoccerData(name, s))

for i in range(len(db) - 1, -1, -1):
    if db[i].score >= m:
        print(db[i].name)

########################################################(방법03)

class SoccerTeam:
    def __init__(self, name, wp):
        self.name = name
        self.wp = int(wp)

all_teams = []
N, M = map(int, input().split())

for i in range(N):
    team_name, wp = input().split()
    all_teams.append(SoccerTeam(team_name, wp))

filtered_names = []
for team in all_teams:
    if team.wp >= M:
        filtered_names.append(team.name)

for name in filtered_names[::-1]:
    print(name)

# print(team_name, wp)

########################################################(방법04)

class SoccerTeam:
    def __init__(self, name, wp):
        self.name = name
        self.wp = wp

    def print_info(self):
        print(self.name, self.wp)

lst = []
res = []
N, M = map(int, input().split())

for i in range(N):
    team_name, wp = input().split()
    # print(team_name, wp)
    lst.append(SoccerTeam(team_name, wp))

# for j in range (len(lst)):
#     lst[j].print_info()

for k in range(len(lst)):
    if int(lst[k].wp) >= M:
        res.append(lst[k].name)

# print(res)
for x in range(len(res) -1, -1, -1):
    print(res[x])

########################################################(방법05)

N, M = map(int,input().split())
L = []
class Xx:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def __str__(self):
        return f'{self.n}'

for i in range(N):
    n, s =input().split()
    if int(s) >= M:
        L.append(Xx(n, s))
    else:
        continue

for t in L[::-1]:
    print(t.n)

########################################################(방법05)

class Soccer:
    def __init__(self, T, W):
        self.T = T
        self.W = W

    def WIN_TEAM(self, i):
        if i.win >= self.W:
            return i.team
        return None

T, W = map(int, input().split())

info = Soccer(T, W)

teams = []
for _ in range(info.T):
    t_name, t_win = input().split()
    teams.append(Soccer(t_name, int(t_win)))

for i in range(info.T -1, -1, -1):
    result = info.WIN_TEAM(teams[i])
    if result:
        print(result)

########################################################(방법06)

