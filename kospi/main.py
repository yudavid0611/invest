import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ecos.ecos import get_response
import matplotlib.pyplot as plt
from datetime import date
from pprint import pprint


response = get_response('M', 'insert_api_key!' '200001', '202207', '901Y014', item_code1='1070000', end_data=1000)       # 2000년 1월부터 2022년 07월까지 코스피 월별 종가 데이터 가져오기
# pprint(response)


columns = ['time', 'kospi']                                                         # 칼럼명 지정
df = pd.DataFrame(columns = columns)                                                # 데이터를 담을 데이터프레임 생성

for idx, v in enumerate(response):                                                  # 데이터 담기
    df.loc[idx, 'time'] = v['TIME']
    df.loc[idx, 'kospi'] = v['DATA_VALUE']

for i in range(len(df)):
    if df.loc[i, 'time'][-2:] not in ['03', '06', '09', '12']:                      # 각 분기별 마지막 월에 해당하는 경우만 남겨두기
        df.drop(i, inplace=True)

df.reset_index(drop=True, inplace=True)                                             # 인덱스 초기화

year= str(date.today().year).zfill(2)
month = str(date.today().month).zfill(2)
day = str(date.today().day).zfill(2)
df.to_excel('kospi/kospi_{}.xlsx'.format(year[2:]+month+day))