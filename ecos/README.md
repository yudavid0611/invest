# 한국은행 경제통계 OpenAPI 사용하기

## 1. 인증키 발급받기
- 아래 사이트에서 회원가입한 후 인증키를 발급 받는다. 어렵지 않다.
- https://ecos.bok.or.kr/api/#/

## 2. API 설명
- 위 홈페이지의 메뉴들을 하나씩 확인해보는 것을 권장한다. 양이 많지 않다.
- '개발 명세서' 메뉴를 보면 크게 6가지 서비스가 제공되는 것을 확인할 수 있다. 이중 우리가 다루는 것은 '**통계 조회 조건 설정**'이며, 이것을 통해 원하는 데이터를 수집할 수 있다.

## 3. ecos.py
- 모듈의 역할: url 생성을 쉽게 해주고 데이터를 받아오는 get_response 함수를 정의한다.
- 코드 상세
    1. parameters
        ``` python
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
        ```
        - 최대한 많은 parameter들의 default 값을 지정했다.
        - 각 parameter의 값들은 일정 형식을 갖추어야 하기 때문에, docstring에 적힌 예시들을 참고하여 알맞게 기입한다.
    2. args: url을 형성하는 순서에 맞게 key-value 쌍을 넣어주었다.
        ``` python
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
        ```
    3. url 만들기: args를 순회하며 url을 만들고, 해당 url을 requests의 get 메서드에 넣어 데이터를 가져온다.
        ``` python
        # smaple: http://ecos.bok.or.kr/api/StatisticSearch/sample/xml/kr/1/10/200Y001/A/2015/2021/10101/?/?/?
        url = base_url
        for a in args.values():
            if a != None:
                url = url + '/' + a

        response = requests.get(url).json()[stat_type]['row']
        
        return response
        ```
    4. 결과 예시
        ``` python
        if __name__ == '__main__':
        print(get_response('***********',  '902Y015', 'Q', '2000Q1', '2022Q4', item_code1='KOR'))       # 2000년부터 2022년 2분기까지 분기별 경제성장률(전분기대비) 데이터 가져오기

        '''
        [{'STAT_CODE': '902Y015', 'STAT_NAME': '9.1.4.1. 국제 주요국 경제성장률', 'ITEM_CODE1': 'KOR', 'ITEM_NAME1': '한국', 'ITEM_CODE2': None, 'ITEM_NAME2': None, 'ITEM_CODE3': None, 'ITEM_NAME3': None, 'ITEM_CODE4': None, 'ITEM_NAME4': None, 'UNIT_NAME': '% ', 'TIME': '2000Q1', 'DATA_VALUE': '1.9'}, {'STAT_CODE': '902Y015', 'STAT_NAME': '9.1.4.1. 국제 주요국 경제성장률', 'ITEM_CODE1': 'KOR', 'ITEM_NAME1': '한국', 'ITEM_CODE2': None, 'ITEM_NAME2': None, 'ITEM_CODE3': None, 'ITEM_NAME3': None, 'ITEM_CODE4': None, 'ITEM_NAME4': None, 'UNIT_NAME': '% ', 'TIME': '2000Q2', 'DATA_VALUE': '1.3'}, {'STAT_CODE': '902Y015', 'STAT_NAME': '9.1.4.1. 국 
        제 주요국 경제성장률', 'ITEM_CODE1': 'KOR', 'ITEM_NAME1': '한국', 'ITEM_CODE2': None, 'ITEM_NAME2': None, 'ITEM_CODE3': None, 'ITEM_NAME3': None, 'ITEM_CODE4': None, 'ITEM_NAME4': None, 'UNIT_NAME': '% ', 'TIME': '2000Q3', 'DATA_VALUE': '2.8'}, {'STAT_CODE': '902Y015', 'STAT_NAME': '9.1.4.1. 국제 주요국 경제성장률', 'ITEM_CODE1': 'KOR', 'ITEM_NAME1': '한국', 'ITEM_CODE2': None, 'ITEM_NAME2': None, 'ITEM_CODE3': None, 'ITEM_NAME3': None, 'ITEM_CODE4': None, 'ITEM_NAME4': None, 'UNIT_NAME': '% ', 'TIME': '2000Q4', 'DATA_VALUE': '-0.3'}, 
        ********이하 생략*********
        '''
        ```