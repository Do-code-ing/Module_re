# Match.expand(template)
# sub() 가 수행하는 것과 똑같이 template에서 역참조 대체를 수행한 결과 문자열을 반환한다.

import re

m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
print(m)
# <re.Match object; span=(0, 11), match='foo,bar,baz'>
print(m.group())
# foo,bar,baz
print(m.expand(r'\2'))
# bar
print(m.expand(r'[\3] -> [\1]'))
# [baz] -> [foo]

m = re.search(r'(?P<num>\d+)', 'foo123qux')
print(m)
# <re.Match object; span=(3, 6), match='123'>
print(m.group(1))
# 123
print(m.expand(r'--- \g<num> ---'))
# --- 123 ---