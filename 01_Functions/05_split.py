# re.split(pattern, string, maxsplit=0, flags=0)
# string을 pattern으로 나누어 list로 반환한다.
# pattern에서 ()가 사용되면 pattern의 모든 그룹 텍스트도 list의 일부로 반환된다.
# maxsplit이 0이 아니면, 최대 maxsplit 만큼 분할하고, 나머지 문자열은 list의 마지막 element로 반환한다.

import re

s = re.split(r'\W+', 'Words, words, words.')
print(s)
# ['Words', 'words', 'words', '']
s = re.split(r'(\W+)', 'Words, words, words.')
print(s)
# ['Words', ', ', 'words', ', ', 'words', '.', '']
s = re.split(r'\W+', 'Words, words, words.', 1)
print(s)
# ['Words', 'words, words.']
s = re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
print(s)
# ['0', '3', '9']

# string의 시작 부분이 pattern과 일치하면, list의 첫 번째 element는 빈 string이다.
# 마지막 element도 마찬가지로 빈 string이다.

s = re.split(r'(\W+)', '...words, words...')
print(s)
# ['', '...', 'words', ', ', 'words', '...', '']

# pattern에 대한 빈(empty) 일치는 이전의 빈 일치와 인접하지 않을 때만 반환한다.

s = re.split(r'\b', 'Words, words, words.') # \b로 지정한 문자열이 empty하기에, 각 문자타입 별로 split된다.(아마도 ㅜ.ㅜ)
print(s)
# ['', 'Words', ', ', 'words', ', ', 'words', '.']
s = re.split(r'\W*', '...words...')
print(s)
# ['', '', 'w', 'o', 'r', 'd', 's', '', '']
s = re.split(r'(\W*)', '...words...') # 전과 같은 기준이지만, 결과 list에 pattern과 일치한 것들도 반환
print(s)
# ['', '...', '', '', 'w', '', 'o', '', 'r', '', 'd', '', 's', '...', '', '', '']