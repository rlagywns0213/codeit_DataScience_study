import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 코드를 작성하세요.
df["status"] = "allowed"
# "information technology” 과목은 심화과목이라 1학년은 수강할 수 없습니다.
condition = (df["course name"] == 'information technology') & (df["year"]==1)
df.loc[condition, "status"] = "not allowed"
#“commerce” 과목은 기초과목이고 많은 학생들이 듣는 수업이라 4학년은 수강할 수 없습니다.
condition2 = (df["course name"]=="commerce") & (df["year"]==4)
df.loc[condition2, "status"] = "not allowed"
#수강생이 5명이 되지 않으면 강의는 폐강되어 수강할 수 없습니다.
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed , "course name"].value_counts()
closed_courses = list(course_counts[course_counts< 5].index)
for course in closed_courses:
    df.loc[df["course name"]== course, "status"] = "not allowed"
# 정답 출력
print(df)