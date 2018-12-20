#app.py
from flask import Flask, render_template, request
app = Flask(__name__)
import random
import requests
import json
from faker import Faker
from bs4 import BeautifulSoup

@app.route("/")
def hello():
    return "Hello World!"
    
    
@app.route('/lotto')
def lotto():
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    # print(type(res))
    # print(type(json.loads(res))) # json 이라는 외부 모듈을 사용하여 list 형식을 dict 형식으로 변경함.
    lotto_dict = json.loads(res)
    #print(lotto_dict["drwNoDate"])
    
    
    # 강사님_1 for문 사용, list에
    # lotto_num = []
    # drwtNo = ["drwtNo1", "drwtNo2", "drwtNo3", "drwtNo4", "drwtNo5", "drwtNo6"]
    # for num in drwtNo:
    #     number = lotto_dict[num] # 우리가 가지고 오고 싶은 변수는 lotto_dict에 있음
    #     lotto_num.append(number)
    # /강사님_1
    
    # 강사님_2 formating 사용해서 drwtNo 에서 숫자만 늘려갈 예정
    week_format_num = []
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)] # 넣고 싶은 공간에 {}를 넣는다. 그 후 format method를 넣으면 int형으로 변한다.
        week_format_num.append(num)
    # /강사님_2
    
    # 강사님_3 formating 사용해서 소름돋게
    # for i in range(1,7):
    #     num = week_format_num.append(lotto_dict["drwtNo{}".format(i)])
    # /강사님_3
    
    
    # lotto_num = []
    # lotto_num = get_value(lotto_dict)
    # getattr
    #   for i in lotto_num:
    #       lotto_num.append()
    
    # pick = 우리가 생성한 번호
    # week_num = 이번주 당첨 번호
    # 위 두 값을 비교해서 로또 당첨 등수 출력
    # 두 개의 값의 inter
    
    num_list = range(1,46)
    # material = random.sample(num_list, 6)
    # material.sort()
    material = [2, 6, 25, 28, 30, 33]
    
    # 갯수만 맞추기_내 방식
    # a = set(week_format_num)
    # b = set(material)
    # c = a.intersection(b)
    # d = []
    # if len(c) == 6:
    #     d = "1등"
    # elif len(c) == 5:
    #     d = "2등"
    # elif len(c) == 4:
    #     d = "3등"
    # elif len(c) == 3:
    #     d = "4등"
    # elif len(c) == 2:
    #     d = "5등"
    # else:
    #     d = "꽝"
    # /갯수만 맞추기
    
# 로또_내 방식
    bnum = [lotto_dict["bnusNo"]] # 보너스 번호, int형은 intersection과 union이 되지 않음. list로 저장해야 됨.
    a = set(week_format_num) # 당첨 번호, 집합 형식으로 변경
    b = set(material) # 추천 번호, 집합 형식으로 변경
    c = a.intersection(b) # 1, 3, 4, 5, 꽝 확인. by 교집합의 갯수 / a & b 이렇게도 할 수 있음.
    e = b.intersection(bnum) # 보너스 번호가 있는지 확인.
    f = c.union(e) # 보너스 번호가 있다면 추가되었을거고, 없다면 추가되지 않겠지. / a | b 이렇게도 할 수 있음.
    
    if len(c) == 6:
        d = "1등"
    elif len(f) == 6:
        d = "2등"
    elif len(c) == 5:
        d = "3등"
    elif len(c) == 4:
        d = "4등"
    elif len(c) == 3:
        d = "5등"
    else:
        d = "꽝"
# /로또_내 방식
    
    return render_template("lotto.html", material = material, week_format_num = week_format_num, d = d)
    
#로또_강사님
@app.route('/lottery')
def lottery():
    #로또 정보를 가져온다.
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    #1등 당첨 번호를 week 리스트에 넣는다.
    week = []
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week.append(num)
        
    #보너스 번호를 bonus변수에 넣는다.
    bonus = lotto_dict["bnusNo"]
    
    #임의의 로또 번호를 생성한다.
    pick = random.sample(range(1,46), 6)
    
    #비교해서 몇 등인지 저장한다.
    match = len(set(pick) & set(week))
    
    if match == 6:
        text = "1등"
    elif match == 5:
        if bonus in pick:
            text = "2등"
        else:
            text = "3등"
    elif match == 4:
        text = "4등"
    elif match == 3:
        text = "5등"
    else:
        text = "꽝"
    
    #사용자에게 데이터를 넘긴다.
    return render_template("lottery.html", week=week, pick=pick, text=text)
#/로또_강사님

@app.route('/ping') #사용자 입력 페이지
def ping():
    return render_template("ping.html")
    
@app.route('/pong') #출력 페이지
def pong():
    input_name = request.args.get('name') #파라미터를 입력해야합니다. , 사이트의 /pong? 뒤에 나오는,, 'args : 인자, 파라미터. 즉, 데이터'
    fake = Faker('ko_KR')
    fake_job = fake.job()
    return render_template("pong.html", html_name = input_name, fake_job = fake_job)
    
    
    
@app.route('/your_name')
def your_name():
    return render_template("your_name.html")
    

@app.route('/death_disease') #무엇을 만들까? 
def death_disease():
    # 질병 리스트
    url = 'https://terms.naver.com/list.nhn?cid=50871&categoryId=50871'
    res = requests.get(url).text
    
    soup = BeautifulSoup(res, 'html.parser')
    
    list_disease = []
    # list_disease = soup.select_one('#content > div.list_wrap > ul > li:nth-of-type(1)').text
    # print(list_disease)
    # input_disease = soup.select_one('#content > div.list_wrap > ul > li:nth-of-type(2) > div.info_area > div.subject > strong > a').text
    # print(input_disease)
    for kinds in list(range(1, 50)):
        input = soup.select_one('#content > div.list_wrap > ul > li:nth-of-type({}) > div.info_area > div.subject > strong > a'.format(kinds)).text
        list_disease.append(input)
    
    input_disease = random.sample(list_disease, 1)
    
    # 이름 받기
    input_name = request.args.get('name')
    
    # 죽을 나이 생성
    numbers = list(range(1, 100))
    input_age = random.sample(numbers, 1)
    
    return render_template("death_disease.html", html_name = input_name, html_age = input_age[0], html_disease = input_disease[0])
    