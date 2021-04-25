# Match.groupdict(default=None)
# 일치의 모든 이름 있는 서브 그룹을 포함하고, 서브 그룹의 이름을 키로 사용하는 딕셔너리를 반환한다.
# defualt 인자는 일치에 참여하지 않는 그룹에 사용된다.

import re

m = re.match(r"(?P<fisrt_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict())
# {'fisrt_name': 'Malcolm', 'last_name': 'Reynolds'}