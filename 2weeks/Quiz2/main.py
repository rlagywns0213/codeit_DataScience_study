'''80명 이상의 학생이 수강하는 과목은 “Auditorium”에서 진행됩니다.
40명 이상, 80명 미만의 학생이 수강하는 과목은 “Large room”에서 진행됩니다.
15명 이상, 40명 미만의 학생이 수강하는 과목은 “Medium room”에서 진행됩니다.
5명 이상, 15명 미만의 학생이 수강하는 과목은 “Small room”에서 진행됩니다.
폐강 등의 이유로 status가 “not allowed”인 수강생은 room assignment 또한 “not assigned”가 되어야 합니다.
''' 
import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

# 코드를 작성하세요.
df["room assignment"] = "not assigned"

allowed = df["status"] == "allowed"
course_list = df.loc[allowed,'course name'].value_counts()
#각 강의실 규모에 해당되는 과목리스트 만들기
auditorium_list = list(course_list[course_list>=80].index)
largeroom_list = course_list[(course_list>=40)&(course_list<80)].index
mediumroom_list =course_list[(course_list>=15)&(course_list<40)].index
smallroom_list =course_list[(course_list>=5)&(course_list<15)].index
for course in auditorium_list:
    df.loc[(df["course name"]== course) & allowed,"room assignment"] = "Auditorim"
for course in largeroom_list:
    df.loc[(df["course name"]== course)  & allowed,"room assignment"] = "Large room"
for course in mediumroom_list:
    df.loc[(df["course name"]== course)  & allowed,"room assignment"] = "Medium room"
for course in smallroom_list:
    df.loc[(df["course name"]== course)  & allowed,"room assignment"] = "Small room" 
# 정답 출력

df