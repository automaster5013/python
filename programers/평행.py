def solution(dots):
    [a, b, c, d] = dots
    
    def get_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    if get_slope(a, b) == get_slope(c, d): return 1
    if get_slope(a, c) == get_slope(b, d): return 1
    if get_slope(a, d) == get_slope(b, c): return 1
    
    return 0

#######################################################(방법01)




























































def solution(dots):
    def get_vector(idx1, idx2):
        return (dots[idx1][0] - dots[idx2][0], dots[idx1][1] - dots[idx2][1])

    # (AB vs CD)
    v1 = get_vector(0, 1)
    v2 = get_vector(2, 3)
    if v1[1]/v1[0] == v2[1]/v2[0]: return 1
    
    # (AC vs BD)
    v1 = get_vector(0, 2)
    v2 = get_vector(1, 3)
    if v1[1]/v1[0] == v2[1]/v2[0]: return 1
    
    # (AD vs BC)
    v1 = get_vector(0, 3)
    v2 = get_vector(1, 2)
    if v1[1]/v1[0] == v2[1]/v2[0]: return 1
    
    return 0

#######################################################(방법02)
























































def solution(dots):
    cases = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]
    
    for p1, p2, p3, p4 in cases:
        dy1 = dots[p1][1] - dots[p2][1]
        dx1 = dots[p1][0] - dots[p2][0]
        dy2 = dots[p3][1] - dots[p4][1]
        dx2 = dots[p3][0] - dots[p4][0]
        
        if dy1 * dx2 == dy2 * dx1:
            return 1
            
    return 0

#######################################################(방법02)



