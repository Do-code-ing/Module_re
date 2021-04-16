# re.findall(pattern, string, flags=0)
# string에서 겹치지 않는 pattern의 모든 일치를 문자열 list로 반환한다.
# string은 왼쪽에서 오른쪽으로 스캔 되고, 일치는 찾은 순서대로 반환한다.
# 하나 이상의 groups가 pattern에 있으면, groups list를 반환한다.
# 두 개 이상의 groups가 pattern에 있으면 tuple list를 반환한다.

import re

f = re.findall("[a-z]+", "abc123def")
print(f)
# ['abc', 'def']
f = re.findall("(ab)", "abc123abc")
print(f)
# ['ab', 'ab']
f = re.findall("(a).*(c)", "abc123abc")
print(f)
# [('a', 'c')]