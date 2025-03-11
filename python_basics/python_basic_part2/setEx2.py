sdata1 = {1,2,3,4}
sdata2 = {3,4,5,6}

# 합집합
print(set.union(sdata1,sdata2))
print(sdata1.union(sdata2))
print(sdata1 | sdata2)
# 출력 : {1,2,3,4,5,6}
print()

#교집합
print(set.intersection(sdata1,sdata2))
print(sdata1.intersection(sdata2))
print(sdata1 & sdata2)
# 출력 : {3,4}
print()

#차집합
print(set.difference(sdata1,sdata2))
print(sdata1.difference(sdata2))
print(sdata1 - sdata2) 
# 출력 : {1,2}
print()

#대칭차집합
print(set.symmetric_difference(sdata1,sdata2))
print(sdata1.symmetric_difference(sdata2))
print(sdata1 ^ sdata2)
# 출력 : {1,2,5,6}
print()
