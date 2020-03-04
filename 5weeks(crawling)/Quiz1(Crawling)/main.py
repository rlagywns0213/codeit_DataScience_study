import requests

# 코드를 작성하세요
years = list(range(2010, 2019))
months = list(range(1, 13))
weeks = list(range(0, 5))

rating_pages=[]

for year in years:
    for month in months:
        for week in weeks:
            response = requests.get("https://workey.codeit.kr/ratings/index?year="+str(year)+ "&month=" +str(month) + "&weekIndex=" + str(week))
            rating_pages.append(response.text)
# 테스트 코드
print(len(rating_pages)) # 가져온 총 페이지 수 
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드