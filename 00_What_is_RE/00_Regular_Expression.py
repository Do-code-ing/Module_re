# 정규 표현식(이하 정규식)은
# 복잡한 문자열을 처리할 때 사용하는 기법으로,
# 파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용한다.

# 필요성
# 출처 https://wikidocs.net/1642
# 주민등록번호에 대해 처리하는 경우

# 일반 함수를 만들어 사용
data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))

print("\n".join(result))
# park 800905-*******
# kim  700905-*******

# 정규식 사용
import re 

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
# park 800905-*******
# kim  700905-*******

# 정규식을 사용하면 다음과 같이 간단하게 코드를 작성할 수 있다.
# 만약 바꿔야 할 문자열의 규칙이 더 복잡해진다면 정규식은 그만큼 더 빛을 발한다.