# 출처
# https://docs.python.org/ko/3/library/re.html
# https://docs.python.org/ko/3/howto/regex.html#regex-howto
# https://wikidocs.net/4308#_1
# https://www.w3schools.com/python/gloss_python_regex_sequences.asp

# 메타 문자:
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

p = re.findall("[abc]", "a")
print(p)
# ['a']
p = re.findall("[abc]", "before")
print(p)
# ['b']
p = re.findall("[abc]", "dude")
print(p)
# []

# 참고
# [] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(from-to)를 의미한다.
# 예를 들어, [a-c]는 [abc]와 동일하다. [0-5]는 [012345]와 동일하다.
#   - [a-zA-Z] : 알파벳 모두
#   - [0-9] : 숫자

p = re.findall("[a-zA-z]", "abc123")
print(p)
# ['a', 'b', 'c']

# 2. Caret(^)
# 문자열의 시작과 일치한다.
# 예를 들어, 정규식 ^a의 경우, 문자열 "abc"에서 "a"와 일치한다.

p = re.findall("^a", "abc")
print(p)
# ['a']

p = re.findall("^a.*", "abcdef") # a로 시작하는 문자열을 일치시킬 때
print(p)
# ['abcdef']

# 주의
# [] 안에 메타 문자 ^ 를 사용할 경우 반대라는 의미를 갖는다.
# 예를 들어, [^0-9]는 숫자가 아닌 문자만 매치한다.

p = re.findall("[^a-zA-Z]", "abc123")
print(p)
# ['1', '2', '3']

# 3. Dollar($)
# 문자열의 끝이나 문자열 끝의 개행 문자 바로 직전과 일치한다.
# 문자열 "foobar"에서, 정규식 foo의 경우, "foo"와 "foobar" 모두 일치하지만,
# 정규식 foo$의 경우, "foo"만 일치한다.

p = re.findall("foo", "foobar")
print(p)
# ['foo']
p = re.findall("foo$", "foobar")
print(p)
# []
p = re.findall("foo$", "foo")
print(p)
# ['foo']

# 4. Dot(.)
# 메타 문자 Dot(.)은 줄바꿈 문자인 \n 을 제외한 모든 문자와 매치됨을 의미한다.
# (참고: re.DOTALL 옵션을 주면 \n 문자와도 매치된다.)
# 정규식 a.b는 "a + 모든 문자 + b"와 같다.
# 예를 들어, "aab","a0b","abc"가 정규식 a.b와 매치될 때,
#   - "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
#   - "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
#   - "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않는다.

p = re.findall("a.b", "aab")
print(p)
# ['aab']
p = re.findall("a.b", "a0b")
print(p)
# ['a0b']
p = re.findall("a.b", "abc")
print(p)
# []

# 정규식 a[.]b는 "a + Dot(.)문자 + b"와 같다.
# 따라서 a[.]b는 "a.b" 문자열과 매치되고, "a0b" 문자열과는 매치되지 않는다.

p = re.findall("a[.]b", "a.b")
print(p)
# ['a.b']
p = re.findall("a[.]b", "a0b")
print(p)
# []

# 5. 반복(*)
# 정규식 ca*t에서 메타 문자 * 은 * 바로 앞에 있는 문자 a가 0회 이상 반복될 수 있음을 의미한다.
# 즉, 다음과 같은 경우에 모두 매치된다.

p = re.findall("ca*t", "ct")
print(p)
# ['ct']
p = re.findall("ca*t", "cat")
print(p)
# ['cat']
p = re.findall("ca*t", "caaat")
print(p)
# ['caaat']

# 6. 반복(+)
# 메타 문자 * 이 0회 이상 반복이라면, 메타 문자 + 는 1회 이상 반복될 수 있음을 의미한다.
# 예를 들어, 정규식 ca+t는 "c + a(1회 이상 반복) + t "와 같다.

p = re.findall("ca+t", "ct")
print(p)
# []
p = re.findall("ca+t", "cat")
print(p)
# ['cat']
p = re.findall("ca+t", "caaat")
print(p)
# ['caaat']

# 7. 제한된 반복({m,n})
# 메타 문자 {}를 사용하면 반복 횟수를 정할 수 있다.
# {m,n}은 m부터 n회까지 반복하는 것을 의미한다. m과 n을 생략하여 사용할 수도 있다.
# 예를 들어, {3,}의 경우 3회 이상 반복, {,3}의 경우 3회 이하 반복하는 것을 의미한다.
# m이 생략되는 경우 0과 같고, n이 생략되는 경우 무한대와 같다.
# 자세한 사용법은 다음과 같다.

# {m}
# 정규식 ca{2}t는 "c + a(반드시 2회 반복) + t"와 같다.

p = re.findall("ca{2}t", "cat")
print(p)
# []
p = re.findall("ca{2}t", "caat")
print(p)
# ['caat']

# {m,n}
# 정규식 ca{2,5}t는 "c + a(2~5회 반복) + t"와 같다.

p = re.findall("ca{2,5}t", "cat")
print(p)
# []
p = re.findall("ca{2,5}t", "caat")
print(p)
# ['caat']
p = re.findall("ca{2,5}t", "caaaaat")
print(p)
# ['caaaaat']

# {m,n}?로 사용할 수도 있는데, 범위 m~n에서 가능한 적은 반복과 일치하도록 한다.
# 예를 들어, 문자열 a가 6개인 문자열 "aaaaaa"에서
# 정규식 a{3,5}는 5개의 "a"와 일치하고,
# 정규식 a{3,5}?는 3개의 "a"와 일치한다.

p = re.findall("a{3,5}", "aaaaaa")
print(p)
# ['aaaaa']
p = re.findall("a{3,5}?", "aaaaaa")
print(p)
# ['aaa', 'aaa']

# 8. 제한된 반복(?)
# 메타 문자 ? 는 메타 문자 {0,1}과 같다.
# 즉, 0개이거나 1개이거나를 의미한다.
# 정규식 ab?c는 "a + b(있어도 되고 없어도 됨) + c"와 같다.

p = re.findall("ab?c", "abc")
print(p)
# ['abc']
p = re.findall("ab?c", "ac")
print(p)
# ['ac']

# 메타 문자 *, +, ?은 모두 {m,n}형태로 고쳐 쓰는 것이 가능하지만
# 가급적 이해하기 쉽고 표현도 간결한 *, +, ? 의 형태로 사용하는 것이 좋다.

# 9. Non-Greedy 반복(*?, +?, ??)
# 앞서 메타 문자 *, +, ?는 가능한 많은 텍스트와의 일치를 나타내는 탐욕적인 방법이다.
# 정규식 <.*>의 경우 "<a> b <c>"와 일치시킬 때 "<a>"가 아닌 전체 문자열과 일치한다.
# 그런데 뒤에 메타 문자 ? 를 추가하면 비 탐욕적 또는 최소 방식으로 일치를 수행한다.
# 즉, 가능하면 적은 문자와 일치한다.
# 예를 들어, 정규식 <.*?>의 경우 "<a>"나 "<c>"가 일치한다.

p = re.findall("<.*>", "<a> b <c>")
print(p)
# ['<a> b <c>']
p = re.findall("<.*?>", "<a> b <c>")
print(p)
# ['<a>', '<c>']

# 10. Pipe(|)
# 정규식 a|b는 a나 b와 일치함을 의미한다.
# 임의의 정규식 A와 B의 경우 A|B는, 먼저 정규식 A에 대해 일치를 찾고,
# 찾지 못하면 정규식 B에서 찾는다.
# 일단 A가 일치하면, B느 더 긴 일치를 보이더라도 검사하지 않는다.
# 즉 Non-Greedy하다.

p = re.findall("a|b", "a")
print(p)
# ['a']
p = re.findall("ab|bc", "bcd")
print(p)
# ['bc']
p = re.findall("ab|abc", "abcd")
print(p)
# ['ab']

# 11. 탈출 문자(\)
# 특수 문자를 탈출하거나('*', '?'와 같은 문자), 특수 시퀀스(12)를 알려준다.

p = re.findall("\?", "안녕하세요?")
print(p)
# ['?']

# 12. 특수 시퀀스
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