# re.fullmatch(pattern, string, flags=0)
# string의 전체가 정규식 pattern과 일치하면, 해당하는 match object를 반환한다.
# 일치하지 않으면 None을 반환한다.

import re

m = re.fullmatch("[a-z]+", "abc123def")
print(m)
# None
m = re.fullmatch("[a-z]+", "abc")
print(m)
# <re.Match object; span=(0, 3), match='abc'>