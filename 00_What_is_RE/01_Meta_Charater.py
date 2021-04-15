# 출처 https://wikidocs.net/4308#_1

# 메타 문자
# 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자
# . ^ $ * + ? { } [ ] \ | ( )

# 1. 문자 클래스 [ ]
# [ ] 사이의 문자들과 매치하겠다는 걸 의미한다.
# 이 사이에는 어떤 문자도 들어갈 수 있다.
# 정규식 [abc]의 의미는 "a,b,c 중 한개의 문자와 매치"를 뜻한다.
# 예를 들어, 문자열 "a", "before", "dude"가 정규식 [abc]와 매치될 때,
#   - "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
#   - "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
#   - "dude"는 정규식과 일치하는 문자인 "a,b,c" 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음
import re

p = re.match("[abc]", "a")
print(p)
# <re.Match object; span=(0, 1), match='a'>
p = re.match("[abc]", "before")
print(p)
# <re.Match object; span=(0, 1), match='b'>
p = re.match("[abc]", "dude")
print(p)
# None

# [] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(from-to)를 의미한다.
# 예를 들어, [a-c]는 [abc]와 동일하다. [0-5]는 [012345]와 동일하다.
#   - [a-zA-Z] : 알파벳 모두
#   - [0-9] : 숫자

p = re.findall("[a-zA-z]", "abc123")
print(p)
# ['a', 'b', 'c']

# 주의
# [] 안에 메타 문자 ^ 를 사용할 경우 반대라는 의미를 갖는다.
# 예를 들어, [^0-9]는 숫자가 아닌 문자만 매치한다.

p = re.findall("[^a-zA-Z]", "abc123")
print(p)
# ['1', '2', '3']

# 자주 사용하는 문자 클래스
# \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
# \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

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

# 2. Dot(.)
# 메타 문자 Dot(.)은 줄바꿈 문자인 \n 을 제외한 모든 문자와 매치됨을 의미한다.
# (참고: re.DOTALL 옵션을 주면 \n 문자와도 매치된다.)
# 정규식 a.b는 "a + 모든 문자 + b"와 같다.
# 예를 들어, "aab","a0b","abc"가 정규식 a.b와 매치될 때,
#   - "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
#   - "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
#   - "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않는다.

p = re.match("a.b", "aab")
print(p)
# <re.Match object; span=(0, 3), match='aab'>
p = re.match("a.b", "a0b")
print(p)
# <re.Match object; span=(0, 3), match='a0b'>
p = re.match("a.b", "abc")
print(p)
# None

# 정규식 a[.]b는 "a + Dot(.)문자 + b"와 같다.
# 따라서 a[.]b는 "a.b" 문자열과 매치되고, "a0b" 문자열과는 매치되지 않는다.

p = re.match("a[.]b", "a.b")
print(p)
# <re.Match object; span=(0, 3), match='a.b'>
p = re.match("a[.]b", "a0b")
print(p)
# None

# 3. 반복(*)
# 정규식 ca*t에서 메타 문자 * 은 * 바로 앞에 있는 문자 a가 0회 이상 반복될 수 있음을 의미한다.
# 즉, 다음과 같은 경우에 모두 매치된다.

p = re.match("ca*t", "ct")
print(p)
# <re.Match object; span=(0, 2), match='ct'>
p = re.match("ca*t", "cat")
print(p)
# <re.Match object; span=(0, 3), match='cat'>
p = re.match("ca*t", "caaat")
print(p)
# <re.Match object; span=(0, 5), match='caaat'>

# 4. 반복(+)
# 메타 문자 * 이 0회 이상 반복이라면, 메타 문자 + 는 1회 이상 반복될 수 있음을 의미한다.
# 예를 들어, 정규식 ca+t는 "c + a(1회 이상 반복) + t "와 같다.

p = re.match("ca+t", "ct")
print(p)
# None
p = re.match("ca+t", "cat")
print(p)
# <re.Match object; span=(0, 3), match='cat'>
p = re.match("ca+t", "caaat")
print(p)
# <re.Match object; span=(0, 5), match='caaat'>

# 5. 반복({m,n}, ?)
# 메타 문자 {}를 사용하면 반복 횟수를 정할 수 있다.
# {m,n}은 m부터 n회까지 반복하는 것을 의미한다. m과 n을 생략하여 사용할 수도 있다.
# 예를 들어, {3,}의 경우 3회 이상 반복, {,3}의 경우 3회 이하 반복하는 것을 의미한다.
# m이 생략되는 경우 0과 같고, n이 생략되는 경우 무한대와 같다.
# 자세한 사용법은 다음과 같다.

# {m}
# 정규식 ca{2}t는 "c + a(반드시 2회 반복) + t"와 같다.

p = re.match("ca{2}t", "cat")
print(p)
# None
p = re.match("ca{2}t", "caat")
print(p)
# <re.Match object; span=(0, 4), match='caat'>

# {m,n}
# 정규식 ca{2,5}t는 "c + a(2~5회 반복) + t"와 같다.

p = re.match("ca{2,5}t", "cat")
print(p)
# None
p = re.match("ca{2,5}t", "caat")
print(p)
# <re.Match object; span=(0, 4), match='caat'>
p = re.match("ca{2,5}t", "caaaaat")
print(p)
# <re.Match object; span=(0, 7), match='caaaaat'>

# ?
# 메타 문자 ? 는 메타 문자 {0,1}과 같다.
# 즉, 0개이거나 1개이거나를 의미한다.
# 정규식 ab?c는 "a + b(있어도 되고 없어도 됨) + c"와 같다.

p = re.match("ab?c", "abc")
print(p)
# <re.Match object; span=(0, 3), match='abc'>
p = re.match("ab?c", "ac")
print(p)
# <re.Match object; span=(0, 2), match='ac'>

# 메타 문자 *, +, ?은 모두 {m,n}형태로 고쳐 쓰는 것이 가능하지만
# 가급적 이해하기 쉽고 표현도 간결한 *, +, ? 의 형태로 사용하는 것이 좋다.