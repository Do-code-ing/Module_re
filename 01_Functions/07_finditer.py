# re.finditer(pattern, string, flags=0)
# string에서 겹치지 않는 RE pattern의 모든 일치를 match object를 산출하는 iterator를 반환한다.
# string은 왼쪽에서 오른쪽으로 스캔 되고, 일치는 찾은 순서대로 반환한다.
# 빈 일치가 포함될 수 있다.

import re

fi = re.finditer("[a-z]*", "abc1def4ghi7")
print(fi)
# <callable_iterator object at 0x0000019658258820>
print(list(fi))
# [<re.Match object; span=(0, 3), match='abc'>,
#  <re.Match object; span=(3, 3), match=''>,
#  <re.Match object; span=(4, 7), match='def'>,
#  <re.Match object; span=(7, 7), match=''>,
#  <re.Match object; span=(8, 11), match='ghi'>,
#  <re.Match object; span=(11, 11), match=''>,
#  <re.Match object; span=(12, 12), match=''>]