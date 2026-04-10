lst = []
# print(lst)
for i in range(5):
    word = input()
    lst.append(word)

print(lst)

###################################################(방법01)

lst = [input() for i in range(5)]
print(lst)

###################################################(방법02)

def collect_words(limit):
    word_list = []
    i = 0
    while i < limit:
        word = input()
        word_list.append(word)
        i += 1
    return word_list

result = collect_words(5)
print(result)

###################################################(방법03)

class ListCollector:
    def __init__(self, target):
        self.target = target
        self.storage = []

    def collect(self):
        while len(self.storage) < self.target:
            item = input()
            self.storage.append(item)
        return self.storage

collector = ListCollector(5)
print(collector.collect())

###################################################(방법04)

inp = []

for i in range(5):
    s = input()
    inp.append(s)

print(inp)

###################################################(방법05)

