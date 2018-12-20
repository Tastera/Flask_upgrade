# phonebook = {
#     "치킨나라" : "02 - 000 - 0000",
#     "피자공주" : "02 - 001 - 0001"
# }
# print(phonebook["치킨나라"])

# 가수 그룹 딕셔너리
idol_twice = {
    "나연" : 24,
    "정연" : 25,
    "모모" : 21,
    "사나" : 28,
    "지효" : 33,
    "미나" : 31,
    "다현" : 42,
    "채영" : 25,
    "쯔위" : 70
}

idol_winner = {
    "민호" : 25,
    "진우" : 30,
    "승훈" : 27,
    "승윤" : 40
}

idol = {
    "남돌" : idol_winner,
    "여돌" : idol_twice
}

# print(idol)
# print(idol["남돌"]["민호"])


score = {
    "수학" : 50,
    "국어" : 70,
    "영어" : 100
}

# for score_key, score_value in score.items():
#     print(score_key)
#     print(score_value)
    
# for score_key in score.keys():
#     print(score_key)
    
# for score_value in score.values():
#     print(score_value)
    
# sum = 0

# for score_value in score.values():
#     sum += score_value
    
# average = sum/len(score)
# print(average)



ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}

#1. ssafy를 진행하는 지역
location_number = len(ssafy["location"])
print(location_number)

#2. 파이썬스탠다드 라이브러리에 requests가 있는가?
if "requests" in ssafy["language"]["python"]["python standard library"]:
    print("True")
else:
    print("False")

#3. 광주 1반 반장의 이름 출력.
print(ssafy["classes"]["gj1"]["class president"])

#4. ssafy에서 배우는 언어들 출력
for ssafy_language in ssafy["language"]:
    print(ssafy_language)

#5. ssafy
for gj2 in ssafy["classes"]["gj2"].values():
    print(gj2)
    
#6. framework들의 이름과 설명을 다음과 같이 출력하세요
f_key = []
f_value = []
for framework_key in ssafy["language"]["python"]["frameworks"]:
    f_key.append(framework_key)
for framework_value in ssafy["language"]["python"]["frameworks"].values():
    f_value.append(framework_value)

print(f_key[0]+"는 "+f_value[0]+"이다.")
print(f_key[1]+"는 "+f_value[1]+"이다.")


#7. 오늘 당번을 뽑기 위해 '살핌' 조원 중 1 명을 랜덤으로
import random
slave_list = ssafy["classes"]["gj1"]["groups"]["살핌"]
slave = random.sample(slave_list, 1)
print("오늘 당번은 "+slave[0]+"입니다")

#오늘 당번은 문동식 입니다.