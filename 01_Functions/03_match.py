# re.match(pattern, string, flags=0)
# string 시작 부분에서 0개 이상의 문자가 정규식 pattern과 일치하면, 해당 match object를 반환한다.
# 일치하지 않으면 None을 반환한다.

import re

m = re.match("[a-z]+", "abc123def")
print(m)
# <re.Match object; span=(0, 3), match='abc'>
m = re.match("[a-z]+", "123abc456")
print(m)
# None