# Pattern.fullmatch(string[, pos[, endpos]])
# 문자열 전체가 정규식과 일치하면, 해당하는 match object를 반환한다.
# 일치하지 않으면 None을 반환한다. (길이가 0인 일치와는 다르다.)
# pos와 endpos는 search에서와 같은 의미다.

import re

p = re.compile("o[gh]")
print(p.fullmatch("dog"))
# None
print(p.fullmatch("ogre"))
# None
print(p.fullmatch("doggie", 1, 3))
# <re.Match object; span=(1, 3), match='og'>