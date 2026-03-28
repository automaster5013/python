products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall = [ ]    # 리콜 대상 제품 리스트는?

for p in products:
    if p.startswith('SIRO'):    # 제품명이 SIRO 로 시작하는가?
        recall.append(p)

print(recall)

################################################################
