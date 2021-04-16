# 특수 시퀀스
# 자주 사용하는 문자 클래스
# \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
# \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

import re

p = re.findall("\d", "abc 123")
print(p)
# ['1', '2', '3']

p = re.findall("\D", "abc 123")
print(p)
# ['a', 'b', 'c', ' ']

p = re.findall("\s", "abc 123")
print(p)
# [' ']

p = re.findall("\S", "abc 123")
print(p)
# ['a', 'b', 'c', '1', '2', '3']

p = re.findall("\w", "abc 123")
print(p)
# ['a', 'b', 'c', '1', '2', '3']

p = re.findall("\W", "abc 123")
print(p)
# [' ']

# 자주 사용하지 않는 문자 클래스
# \A - Caret(^)과 동일한 표현식이다.
# \Z - Dollar($)와 동일한 표현식이다.
# \b - 지정된 문자가 단어의 시작 또는 끝에 있는 일치 항목을 반환한다.
# \B - 지정된 문자가 단어의 시작 또는 끝이 아닌 일치 항목을 반환한다. (\b와 반대)

p = re.findall("The", "The World The Dog")
print(p)
# ['The', 'The']
p = re.findall("\AThe", "The World The Dog")
print(p)
# ['The']
p = re.findall("^The", "The World The Dog")
print(p)
# ['The']

p = re.findall(".*d\Z", "abcd")
print(p)
# ['abcd']

p = re.findall(r"\bain","The rain in Spain") # ain으로 시작하는 모든 ain
print(p)
# []
p = re.findall(r"ain\b","The rain in Spain") # ain으로 끝나는 모든 ain
print(p)
# ['ain', 'ain']

p = re.findall(r"\Bain","The rain in Spain") # ain으로 시작하지 않는 모든 ain
print(p)
# ['ain', 'ain']
p = re.findall(r"ain\B","The rain in Spain") # ain으로 끝나지 않는 모든 ain
print(p)
# []

# 그 외에 기능이 몇 개 더 있지만, 쓰임새가 흔하지 않다 생각하여 설명하지 않도록 하겠다.
# 생략한 기능들에 대해 알고 싶다면, 아래의 주소에 들어가 보도록 하자.
# https://docs.python.org/ko/3/library/re.html#regular-expression-syntax