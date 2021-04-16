# re.compile(pattern, flags=0)
# 정규식 패턴을 정규식 object를 만들어 반환한다.
# 정규식 object는 match(), search() 및 기타 method를 일치시키는 데 사용한다.

import re

p = re.compile("ab*")
print(p) 
# re.compile('ab*')
print(type(p))
# <class 're.Pattern'>

# flags는 필요한 경우, 옵션을 제공하면 된다.
# 옵션의 종류는 다음과 같다.
#   re.DOTALL(S) - 특수 문자 '.' 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
#   re.IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
#   re.MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
#   re.VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)
#   re.LOCALE(L) - 바이트열 패턴에서, \w,\W,\b,\B 및 대소문자를 구분하지 않는 일치를 현재 로케일에 의존하도록 한다.
#   re.ASCII(A) - 유니코드 패턴에서, \w와 같은 특수 시퀀스가 전체 유니코드 일치 대신 ASCII 전용 일치를 수행하도록 한다.
# 옵션을 사용할 때는 re.DOTALL 과 같이 입력하거나 re.S 처럼 약어를 사용하여 입력해도 된다.