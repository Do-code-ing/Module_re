# re.escape(pattern)
# pattern에서 특수 문자를 escape 처리한다.
# 정규식 메타 문자가 포함되어 있을 수 있는 임의의 리터럴 문자열을 일치시킬 때 유용하다.

import re

p = re.escape("www.naver.com")
print(p)
# www\.naver\.com

p = re.escape("\w")
print(p)
# \\w

# 참고
# 버전 3.7에서 변경:
# 정규식에서 특별한 의미를 가질 수 있는 문자만 이스케이프 됩니다.
# 결과적으로, '!', '"', '%', "'", ',', '/', ':', ';', '<', '=', '>', '@' 및 〈》〉는 더는 이스케이프 되지 않습니다.