# Match.group([group1, ...])
# 일치의 하나 이상의 서브 그룹을 반환한다.
# 단일 인자가 있으면, 결과는 단일 문자열이다.
# 인자가 여러개면, 결과는 인자당 하나의 항목이 있는 튜플이다.
# 인자가 없으면, group1의 기본값은 0이다. (전체 일치가 반환된다.)

import re

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group()) # = group(0)
# Isaac Newton
print(m.group(1))
# Isaac
print(m.group(2))
# Newton
print(m.group(1, 2))
# ('Isaac', 'Newton')

# 정규식 (?P<name>...) 문법을 사용하면,
# groupN 인자는 그룹 이름으로 그룹을 식별하는 문자열일 수도 있다.

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.group("first_name"))
# Malcolm
print(m.group("last_name"))
# Reynolds

# 이 경우도 마찬가지로 인덱스로 참조할 수 있다.
print(m.group())
# Malcolm Reynolds
print(m.group(1))
# Malcolm
print(m.group(2))
# Reynolds

# 그룹이 여러번 일치하면, 마지막 일치만 사용할 수 있다.
m = re.match(r'(..)+', "a1b2c3")
print(m.group())
# a1b2c3
print(m.group(1))
# c3

# 다음과 같이 사용할 수도 있다.
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m[0])
# Isaac Newton
print(m[1])
# Isaac
print(m[2])
# Newton