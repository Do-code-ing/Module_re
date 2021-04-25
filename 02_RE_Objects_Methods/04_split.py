# Pattern.split(string, maxsplit=0)
# split() 함수와 같은데, 컴파일된 패턴을 사용한다.

import re

p = re.compile(" ")
print(p.split("Hello World"))
# ['Hello', 'World']