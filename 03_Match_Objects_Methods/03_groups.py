# Match.groups(default=None)
# 1에서 패턴에 있는 그룹의 수까지, 일치의 모든 서브 그룹을 포함하는 튜플을 반환한다.
# defualt 인자는 일치에 참여하지 않은 그룹에 사용된다.

import re

m = re.match(r'(\d+)\.(\d+)', "24.1632")
print(m.groups())

# 방금 예시에서 소수점 그 이후의 모든 것을 선택적으로 만들면,
# 모든 그룹이 일치에 참여하지 않을 수 있다.
# 이 그룹은 default 인자가 주어지지 않는 한 기본값 None이 된다.

m = re.match(r'(\d+)\.?(\d+)?', "24")
print(m.groups())
# ('24', None)
print(m.groups('0'))
# ('24', '0')