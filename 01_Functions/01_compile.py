# 출처 https://wikidocs.net/4308#re

# re.compile(pattern, flags)
# pattern이 기준인 정규식 패턴 object를 만들어 반환한다.

import re

p = re.compile("ab*")
print(p)
# re.compile('ab*')
print(type(p))
# <class 're.Pattern'>

# 간단히 사용해보자
a = "abbb"
print(p.match(a))
# <re.Match object; span=(0, 4), match='abbb'>

# flags는 필요한 경우, 옵션을 제공하면 된다.
# 옵션의 종류는 다음과 같다.
#   DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
#   IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
#   MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
#   VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)
# 옵션을 사용할 때는 re.DOTALL 과 같이 입력하거나 re.S 처럼 약어를 사용하여 입력해도 된다.
# 자세한 옵션 사용 방법은 후에 설명하겠다.