import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요
response = requests.get("https://workey.codeit.kr/music/index")

soup = BeautifulSoup(response.text, 'html.parser')

li_tags = soup.select(".rank__order li")

# 빈 리스트 생성
search_ranks = []

# 텍스트 추출해서 리스트에 담기
for li in li_tags:
    search_ranks.append(li.text.strip().split(' ')[2])

# 결과 출력
print(search_ranks)

# 결과 출력