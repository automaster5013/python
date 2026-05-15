def solution(my_strings, parts):
    answer = []
    for idx, string in enumerate(my_strings):
        s, e = parts[idx]
        answer.append(string[s : e + 1])
        
    return "".join(answer)







print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))
# print(solution("progressive", [0,4]))
# print(solution("hamburger", [1,2]))
# print(solution("hammer", [3,5]))
# print(solution("ahocorasick", [7,7]))






























