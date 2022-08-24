import requests
import pandas as pd

def get_response(api_key, stat_code, period, start_date, end_date, base_url='http://ecos.bok.or.kr/api',
stat_type = 'StatisticSearch', data_type = 'json',
lang = 'kr', group_code = None, start_data = 1, end_data = 100, 
item_code1 = None, item_code2 = None, item_code3 = None, item_code4 = None):
    '''
    Parameters
    - api_key
    - stat_code
    - period: (ex) A, Q, M, SM, D
    - start_date: (ex) 2015, 2015Q1, 201501, 20150101
    - end_date: (ex) 2015, 2015Q1, 201501, 20150101
    - stat_type: (defalut) StatisticSearch
    - data_type: (defalut) json
    - lang: (defalut) kr
    - group_code: (defalut) None
    - start_data: (defalut) 1
    - end_data: (defalut) 100
    - item_code1: (defalut) None
    - item_code2: (defalut) None
    - item_code3: (defalut) None
    - item_code4: (defalut) None
    '''

    args = {
    'stat_type': stat_type,
    'api_key' : api_key,
    'data_type': data_type,
    'lang': lang,
    'group_code': group_code,
    'start_data': str(start_data),
    'end_data': str(end_data),
    'stat_code': stat_code,
    'period': period,
    'start_date': start_date,
    'end_date': end_date,
    'item_code1': item_code1,
    'item_code2': item_code2,
    'item_code3': item_code3,
    'item_code4': item_code4,
    }
    
    # smaple: http://ecos.bok.or.kr/api/StatisticSearch/sample/xml/kr/1/10/200Y001/A/2015/2021/10101/?/?/?
    url = base_url
    for a in args.values():
        if a != None:
            url = url + '/' + a
    print(url)

    response = requests.get(url).json()[stat_type]['row']
    
    return response


if __name__ == '__main__':
    print(get_response('*********',  '902Y015', 'Q', '2000Q1', '2022Q4', item_code1='KOR'))       # 2000년부터 2022년 2분기까지 분기별 경제성장률(전분기대비) 데이터 가져오기