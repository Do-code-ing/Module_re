# match object는 항상 True 값을 가진다.
# match() 와 search() 는 일치가 없을 때 None을 반환하기 때문에,
# 간단한 if문으로 일치가 있는지 검사할 수 있다.

import re

p = re.compile("[a-z]")
m = p.match("abc123")
if m:
    print(m)
    # <re.Match object; span=(0, 1), match='a'>
print(bool(m))
# True

m = p.match("123abc")
if m:
    print(m)
print(bool(m))
# False