# Pattern.search(string[, pos[, endpos]])
# 문자열을 스캔하여 정규식과 일치하는 첫 번째 위치를 찾고, 해당하는 match object를 반환한다.
# 문자열의 어느 위치에서도 패턴과 일치하지 않으면 None을 반환한다. (길이가 0인 일치와는 다르다.)
# pos : 검색을 시작할 문자열의 index를 제공한다. 기본값은 0이다.
# endpos : 문자열을 어디까지 검색할지 제한한다.

import re

p = re.compile("d")
print(p.search("dog"))
# <re.Match object; span=(0, 1), match='d'>