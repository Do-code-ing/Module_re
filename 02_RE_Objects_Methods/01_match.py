# Pattern.match(string[, pos[, endpos]])
# 문자열의 처음에서 0개 이상의 문자가 이 정규식과 일치하면, 해당하는 match object를 반환한다.
# 일치하지 않으면 None을 반환한다. (길이가 0인 일치와는 다르다.)
# pos : 검색을 시작할 문자열의 index를 제공한다. 기본값은 0이다.
# endpos : 문자열을 어디까지 검색할지 제한한다.

import re

p = re.compile("B") # 패턴을 만들고
m = p.match("ABC") # 매치해보자
print(m)
# None
m = p.match("ABC", 1)
print(m)
# <re.Match object; span=(1, 2), match='B'>
