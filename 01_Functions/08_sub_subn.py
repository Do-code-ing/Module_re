# re.sub(pattern, repl, string, count=0, flags=0) (repl : replace(ment))
# string에서 겹치지 않는 pattern의 가장 왼쪽 일치를 repl로 치환하여 얻은 string을 반환한다.
# pattern을 찾지 못하면, string이 변경되지 않고 반환된다.
# repl은 문자열이나 함수가 될 수 있다.

import re

s = re.sub("[a-z]", "0", "abc123")
print(s)
# 000123

# re.subn(pattern, repl, string, count=0, flags=0)
# sub()와 같은 연산을 수행하지만, (새 문자열, 치환한 횟수)의 형식인 tuple을 반환한다.

sn = re.subn("[a-z]", "0", "abc123")
print(sn)
# ('000123', 3)