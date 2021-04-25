# Match.start([group])
# Match.end([group])
# 그룹과 일치하는 부분 문자열의 시작과 끝 인덱스를 반환한다.
# group의 기본값은 0이다. (전체 일치 문자열을 뜻한다.)
# 그룹이 있지만, 일치에 기여하지 않으면, -1을 반환한다.

import re

email = "zxcvbn658@remove_thisnaver.com"
m = re.search("remove_this", email)
print(m.start())
# 10
print(m.end())
# 21
print(email[:m.start()] + email[m.end():])
# zxcvbn658@naver.com