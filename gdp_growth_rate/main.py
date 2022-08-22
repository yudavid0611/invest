import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ecos.ecos import get_response
import matplotlib.pyplot as plt
from datetime import date


response = get_response('Q', 'insert_api_key!', '2000Q1', '`2022Q4', '902Y015', item_code1='KOR')       # 2000년부터 2022년 2분기까지 분기별 경제성장률(전분기대비) 데이터 가져오기

columns = ['time', 'kor']                                                           # 칼럼명 지정
df = pd.DataFrame(columns = columns)                                                # 데이터를 담을 데이터프레임 생성

for idx, v in enumerate(response):                                                  # 데이터 담기
    df.loc[idx, 'time'] = v['TIME']
    df.loc[idx, 'kor'] = v['DATA_VALUE']

year= str(date.today().year).zfill(2)
month = str(date.today().month).zfill(2)
day = str(date.today().day).zfill(2)
df.to_excel('gdp_growth_rate/gdp_growth_rate_{}.xlsx'.format(year[2:]+month+day))