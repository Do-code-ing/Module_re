# Pattern.findall(string[, pos[, endpos]])
# findall() 함수와 유사한데, 컴파일된 패턴을 사용한다.
# 하지만 search() 처럼 검색 영역을 제한하는 선택적 pos와 endpos 매개 변수도 받아들인다.

import re

p = re.compile("a")
print(p.findall("abcabc"))
# ['a', 'a']