# Pattern.sub(repl, string, count=0)
# sub() 함수와 같은데, 컴파일된 패턴을 사용한다.

import re

p = re.compile("[a-z]")
print(p.sub("0", "abc123"))
# 000123
print(p.subn("0", "abc123"))
# ('000123', 3)