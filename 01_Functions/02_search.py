# re.search(pattern, string, flags=0)
# string을 스캔하여 정규식 pattern이 일치하는 첫 번째 위치를 찾고, 대응하는 match object를 반환한다.
# 일치하는게 없다면 None을 반환한다.

import re

m = re.search("[a-z]+", "abc123def")
print(m)
# <re.Match object; span=(0, 3), match='abc'>
m = re.search("[a-z]+", "123abc456")
print(m)
# <re.Match object; span=(3, 6), match='abc'>