import requests
from datetime import datetime
import time
import os
import asyncio
import aiohttp
import FinanceDataReader as fdr

import pandas as pd

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

from dateutil.relativedelta import relativedelta

load_dotenv(verbose=True)


class asyncDeepSearchAPI(object):
    _COMPUTE_API = "{}/v1/compute".format('https://api.deepsearch.com')
    _AUTH_ID = os.getenv('_AUTH_ID')
    _AUTH_PW = os.getenv('_AUTH_PW')
    _AUTH = HTTPBasicAuth(_AUTH_ID, _AUTH_PW)
    
    @classmethod
    async def compute(cls, query, locale='ko_KR'):
        params = {
            'input': query,
            'locale': locale
        } 

        async with aiohttp.ClientSession() as sess:
            async with sess.post( url=cls._COMPUTE_API, auth=aiohttp.BasicAuth(cls._AUTH_ID, cls._AUTH_PW), data=params, timeout=120 ) as co_resp:
                response_json = await co_resp.json()
                if (co_resp.status != 200) or (not response_json['success']):
                    try:
                        print("Response code, Success status:", co_resp.status, response_json['success'])
                    except:
                        print(response_json)
                    print("Exception query log:", query)
                    print(response_json)
                    return None

                pods = response_json['data']['pods']  # pods[0]: input

                if pods[1]['class'] == 'Result:DataFrame':
                    data    =    pods[1]['content']['data']
                    index   =   pods[1]['content']['index']
                    dtypes  =  pods[1]['content']['dtypes']
                    columns = pods[1]['content']['columns']

                    results = []

                    no_obs = len(data[columns[0]])
                    for i in range(no_obs):
                        item = dict()
                        for col in columns:
                            item[col] = data[col][i]
                        results.append(item)

                    df_results = pd.DataFrame(results)

                    if df_results.empty:
                        return None

                    for col in dtypes.keys():  # pyarrow converting
                        df_results[col] = df_results[col].astype(dtypes[col])

                    df_results = df_results.set_index(index)  # 'symbol'
                    df_results = df_results.sort_index()

                    return df_results

                elif pods[1]['class'] == 'Result:DocumentTrendsResult':
                    data    =    pods[1]['content']['data']
                    trends  =   pods[1]['content']['data']['trends']
                    total_matches = trends[0]['total_matches']
                    buckets = trends[0]['buckets']

                    df_results = pd.DataFrame(buckets)
                    
                    return df_results

                else:
                    return pods[1]['content']


class DeepSearchAPI(object):
    _COMPUTE_API = "{}/v1/compute".format('https://api.deepsearch.com')
    _AUTH_ID = os.getenv('_AUTH_ID')
    _AUTH_PW = os.getenv('_AUTH_PW')
    _AUTH = HTTPBasicAuth(_AUTH_ID, _AUTH_PW)

    @classmethod
    def compute(cls, query, locale='ko_KR'):
        params = {
            'input': query,
            'locale': locale
        } 

        response = requests.post( url=cls._COMPUTE_API, auth=cls._AUTH, data=params, timeout=120 )

        if (response.status_code != 200) or (not response.json()['success']):
            print("Response code:", response.status_code)
            print("AUTH info:", cls._AUTH_ID, cls._AUTH_PW)
            print("Exception query log:", query)
            return None

        pods = response.json()['data']['pods']  # pods[0]: input

        if pods[1]['class'] == 'Result:DataFrame':
            data    =    pods[1]['content']['data']
            index   =   pods[1]['content']['index']
            dtypes  =  pods[1]['content']['dtypes']
            columns = pods[1]['content']['columns']

            results = []

            no_obs = len(data[columns[0]])
            for i in range(no_obs):
                item = dict()
                for col in columns:
                    item[col] = data[col][i]
                results.append(item)

            df_results = pd.DataFrame(results)

            if df_results.empty:
                return None

            for col in dtypes.keys():  # pyarrow converting
                df_results[col] = df_results[col].astype(dtypes[col])

            df_results = df_results.set_index(index)  # 'symbol'
            df_results = df_results.sort_index()

            return df_results

        elif pods[1]['class'] == 'Result:DocumentTrendsResult':
            data    =    pods[1]['content']['data']
            trends  =   pods[1]['content']['data']['trends']
            total_matches = trends[0]['total_matches']
            buckets = trends[0]['buckets']

            df_results = pd.DataFrame(buckets)
            
            return df_results

        else:
            return pods[1]['content']


class WaveletAPI(object):
    _COMPUTE_API_INDEX = 'https://api.ddi.deepsearch.com/wavelet/v1/indices' 
    _COMPUTE_API = 'https://api.ddi.deepsearch.com/wavelet/v1/prices'
    _AUTH_ID = os.getenv('_AUTH_ID')
    _AUTH_PW = os.getenv('_AUTH_PW')
    _AUTH = HTTPBasicAuth(_AUTH_ID, _AUTH_PW)

    @classmethod
    def compute(cls, symbol, date_from, date_to, interval=None):
        assert type(symbol) == list
        num_of_pdf = len(symbol)
        symbol_str = ','.join(symbol)
        return_dict = dict()
        
        if symbol in [['KOSPI'], ['KOSDAQ']]:
            query = f'{cls._COMPUTE_API_INDEX}/{symbol_str}?from={date_from}&to={date_to}'
        else:
            query = f'{cls._COMPUTE_API}/{symbol_str}?from={date_from}&to={date_to}'

        response = requests.get(query, auth=cls._AUTH)
        
        if (response.status_code != 200):
            print("Response code:", response.status_code)
            print("AUTH info:", cls._AUTH_ID, cls._AUTH_PW)
            print("Exception query log:", query)
            return None
            
        # print(query)

        if symbol in [['KOSPI'], ['KOSDAQ']]:
            data = response.json()['data'][0]
            points = data['points']

            df = pd.DataFrame.from_dict(points)
            df = df.set_index(['timestamp'])
            df.index = pd.to_datetime(df.index)

            return_dict[symbol[0]] = df  #! 인덱스 리턴은 하나밖에 못한다가 됨
            return return_dict

        else:
            for i in range(num_of_pdf):
                try:
                    data = response.json()['data'][i]
                    points = data['points']

                    df = pd.DataFrame.from_dict(points)
                    df = df.set_index(['timestamp'])
                    df.index = pd.to_datetime(df.index)

                    if num_of_pdf == 1:
                        return_dict[data['exchange'] + ':' + data['symbol']] = df
                        return return_dict
                
                    return_dict[data['exchange'] + ':' + data['symbol']] = df
                except:  
                    print("Response code:", response.status_code)
                    print("Exception query log:", query)
                    break

            return return_dict


class asyncWaveletAPI(object):
    _COMPUTE_API_INDEX = 'https://api.ddi.deepsearch.com/wavelet/v1/indices' 
    _COMPUTE_API = 'https://api.ddi.deepsearch.com/wavelet/v1/prices'
    _AUTH_ID = os.getenv('_AUTH_ID')
    _AUTH_PW = os.getenv('_AUTH_PW')
    _AUTH = HTTPBasicAuth(_AUTH_ID, _AUTH_PW)

    @classmethod
    def compute():
        return


class HaystackAPI(object):
    """
    api.ddi.deepsearch.com/haystack/v1/news/_search?query=삼성전자&count=1
        - https://help.deepsearch.com/ddi/haystack/search

    @category - section: 
        - news
            politics, economy, society, culture, world, tech, entertainment, opinion
        - research
            market, strategy, company, industry, economy, bond   
        - company
            ir, disclosure
        - patent
            patent
    """
    _COMPUTE_API = "{}/v1".format('https://api.ddi.deepsearch.com/haystack')
    _AUTH_ID = os.getenv('_AUTH_ID')
    _AUTH_PW = os.getenv('_AUTH_PW')
    _AUTH = HTTPBasicAuth(_AUTH_ID, _AUTH_PW)

    @classmethod
    def compute(cls, category, section, params, module='_search?', group_by='securities.symbol', locale='ko_KR'):
        assert type(params) is dict
        url = os.path.join(cls._COMPUTE_API, category, section, module)
        if module == '_aggregation?':
            params['groupby'] = group_by
        response = requests.get( url=url, auth=cls._AUTH, params=params, timeout=30 )

        if (response.status_code != 200) or (not response.json()['found']):
            print("Response code, Found status:", response.status_code, response.json()['found'])
            print("Exception query log:", response.url)
            return None

        return response.json()['data']


class asyncHaystackAPI(object):
    """
    api.ddi.deepsearch.com/haystack/v1/news/_search?query=삼성전자&count=1
        - https://help.deepsearch.com/ddi/haystack/search

    @category - section: 
        - news
            politics, economy, society, culture, world, tech, entertainment, opinion
        - research
            market, strategy, company, industry, economy, bond   
        - company
            ir, disclosure
        - patent
            patent
    """
    _COMPUTE_API = "{}/v1".format('https://api.ddi.deepsearch.com/haystack')
    _AUTH_ID = os.getenv('_AUTH_ID')
    _AUTH_PW = os.getenv('_AUTH_PW')
    _AUTH = HTTPBasicAuth(_AUTH_ID, _AUTH_PW)

    @classmethod
    async def compute(cls, category, section, params, locale='ko_KR'):
        assert type(params) is dict
        url = os.path.join(cls._COMPUTE_API, category, section, '_search?')
        async with aiohttp.ClientSession() as sess:
            async with sess.get( url=url, auth=aiohttp.BasicAuth(cls._AUTH_ID, cls._AUTH_PW), params=params, timeout=120 ) as co_resp:
                response_json = await co_resp.json()
                if (co_resp.status != 200):# or (not response_json['found']):
                    print("Response code, Success status:", co_resp.status)#, response_json['found'])
                    print("Exception query log:", co_resp.url)
                    print(response_json)
                    return None
        return response_json['data']



class backtest(object):
    _aum = 100_000_000_000.0
    deepsearch = DeepSearchAPI()
    async_deepsearch = asyncDeepSearchAPI()
    wavelet = WaveletAPI()
    
    loop = asyncio.get_event_loop()
    fdr_krx = fdr.StockListing('KRX')
    fdr_krx_delisted = fdr.StockListing('KRX-DELISTING')

    def _split_phases(cls, deepsearch_df):
        return_dict = dict()
        phases = deepsearch_df.index.unique()
        for p in phases:
            pdf = deepsearch_df.loc[p]
            return_dict[p] = pdf
        return return_dict

    def _is_business_day(date):
        return bool(len(pd.bdate_range(date, date)))

    def _datetime_reformer(date):
        formats = [
            "%Y-%m-%d", 
            "%m/%d/%Y",
        ]
        for i in formats:
            try: _datetime = datetime.strptime(date, i)
            except: continue
        return _datetime  #! formats 에 없는 형식일 경우 에러

    @classmethod
    async def _async_main(cls, symbol_list, date_from, date_to, krx=True):
        start = "'"
        separator = "', '"
        query = f"GetStockPrices(([{start + separator.join(symbol_list) + start}]), columns=['change_rate'], date_from={date_from}, date_to={date_to})"
        task = [cls.async_deepsearch.compute(query)]
        result = await asyncio.gather(*task)
        return result
        """
        if krx:
            if "NICE" in [i.split(":")[0] for i in symbol_list]:
                query = ' '.join(symbol_list) + f' {date_from}-{date_to} 주가'  #! 주가수익률은 해당말일을 기준으로 한 점만 보여준다
            else:
            # print(query)
                start = "'"
                separator = "', '"
                query = f"GetStockPrices(([{start + separator.join(symbol_list) + start}]), columns=['close'], date_from={date_from}, date_to={date_to})"
            # query = ' '.join(symbol_list) + f' {date_from}-{date_to} 주가'  #! 주가수익률 계산 오류 있음. 상폐종목 나이스 티커 필요. 
            # start = "'"
            # separator = "', '"
            # query = f'GetStockPrices(([{start + separator.join(symbol_list) + start}]), columns=["close"], date_from={date_from}, date_to={date_to})'
        else:
            start = "'"
            separator = "', '"
            query = f'Global.GetStockPrices(([{start + separator.join(symbol_list) + start}]), columns=["close"], date_from={date_from}, date_to={date_to})'
        task = [cls.async_deepsearch.compute(query)]
        result = await asyncio.gather(*task)
        return result
        """

    def _async_main_wrapper(cls, chunk_krx, chunk_krx_not, _date_from, _date_to, krx=True):
        async_data_krx = cls.loop.run_until_complete( cls._async_main( [i for i in chunk_krx], _date_from, _date_to ) )
        if len(chunk_krx_not) > 0:
            async_data_krx_not = cls.loop.run_until_complete( cls._async_main( [i for i in chunk_krx_not], _date_from, _date_to, krx=False) )
            async_data_krx_not = [ cls._nonkrx_handler(async_data_krx_not[0], _date_from, _date_to) ]
            async_data = [ pd.concat([async_data_krx[0], async_data_krx_not[0]]) ]
        else:
            async_data = async_data_krx
        return async_data


    @classmethod
    def _nonkrx_handler(cls, async_data_krx_not_df, _date_from, _date_to):
        won_dollar = cls.deepsearch.compute('QueryBankOfKoreaSeriesData("BOK:731Y001.0000001")')
        async_data_krx_not = async_data_krx_not_df.rename({'close':f'주가 {_date_from}-{_date_to}'}, axis=1)
        wd_stockprice = pd.merge(async_data_krx_not.reset_index(), won_dollar.reset_index()).set_index(['date', 'symbol'])
        wd_stockprice[f'주가 {_date_from}-{_date_to}'] = wd_stockprice.loc[:, f'주가 {_date_from}-{_date_to}'] * wd_stockprice.loc[:, 'QueryBankOfKoreaSeriesData(BOK:731Y001.0000001)']
        async_data_krx_not[f'주가 {_date_from}-{_date_to}'] = wd_stockprice[f'주가 {_date_from}-{_date_to}']
        return async_data_krx_not


    @classmethod
    def _fdr_handler(cls, symbol, _date_from, _date_to):
        if "KRX:" in symbol: symbol = symbol.split(":")[-1]
        if "NICE:" in symbol: symbol = symbol.split(":")[-1]
        _resp = fdr.DataReader(symbol,_date_from,_date_to)
        if symbol in list(cls.fdr_krx["Symbol"]): 
            _entity_name = cls.fdr_krx[cls.fdr_krx["Symbol"] == symbol]["Name"].values[0]
        else: 
            _entity_name = cls.fdr_krx_delisted[cls.fdr_krx_delisted["Symbol"] == symbol]["Name"].values[0]
        _resp["symbol"] = "KRX:"+symbol
        _resp["entity_name"] = _entity_name
        _resp = _resp.reset_index()[["Date", "symbol", "entity_name", "Close"]].sort_values(by=["Date"])
        _resp.columns = ["date", "symbol", "entity_name", f"주가 {_date_from}-{_date_to}"]
        _resp = _resp.set_index(["date", "symbol"])
        return _resp
        """
        _date_from, _date_to = str(_date_from), str(_date_to)
        if "KRX:" in symbol: symbol = symbol.split(":")[-1]
        if "NICE:" in symbol: symbol = symbol.split(":")[-1]
        _resp = fdr.DataReader(symbol,_date_from,_date_to)
        if symbol in list(cls.fdr_krx["Symbol"]): 
            _entity_name = cls.fdr_krx[cls.fdr_krx["Symbol"] == symbol]["Name"].values[0]
        else: 
            _entity_name = cls.fdr_krx_delisted[cls.fdr_krx_delisted["Symbol"] == symbol]["Name"].values[0]
        _resp["symbol"] = "KRX:"+symbol
        _resp["entity_name"] = _entity_name
        _resp = _resp.reset_index()[["Date", "symbol", "entity_name", "Close"]].sort_values(by=["Date"])
        _resp.columns = ["date", "symbol", "entity_name", f"주가 {_date_from}-{_date_to}"]
        _resp = _resp.set_index(["date", "symbol"])
        return _resp
        """


    @classmethod
    def compute(cls, deepsearch_df, df_to_upload_bool=False, debug=False, fdr=False):
        df = cls._split_phases(cls, deepsearch_df)
        rebalancing_dates = list(df.keys())
        for idx, date in enumerate(rebalancing_dates):
            if datetime.today() < cls._datetime_reformer(date):
                print(rebalancing_dates, rebalancing_dates[:idx])
                rebalancing_dates = rebalancing_dates[:idx]
                break


        _async_batch_size = 10


        total_return = pd.DataFrame()
        for idx, date in enumerate(rebalancing_dates):  # idx starts from 0
            async_result = pd.DataFrame()
            if isinstance(df[date], pd.Series): _df = pd.DataFrame(df[date]).T
            else: _df = df[date]
            ratio = _df.reset_index().set_index(['symbol'])['weight'].astype(float)  # 단축코드, 비중(비중의합은1)
            ratio.index = ratio.index.str.replace(" ", "")
            pdf = list(_df['symbol'])  # 0 은 iter item (timestamp)

            delisted_firm_dict = dict()
            delisted_firm = _df[_df['symbol'] != _df['symbol_listed']]
            for _, row in delisted_firm.iterrows(): delisted_firm_dict[row['symbol_listed']] = row['symbol']

            date = cls._datetime_reformer(date)

            b_days = 0
            while True:
                if not cls._is_business_day(date): date, b_days = date +relativedelta(days=1), b_days +1
                else: break


            if idx+1 != len(rebalancing_dates):  #* if not the last phase
                # _date_from = datetime.strftime(date -relativedelta(days=1), "%Y-%m-%d")
                _date_from_for_close_column = datetime.strftime(date -relativedelta(days=1), "%Y-%m-%d")  # close 기반 하루전날 데이터
                _date_from = datetime.strftime(date, "%Y-%m-%d")  # change_rate 기반 당일 데이터
                _date_to_for_close_column = datetime.strftime(cls._datetime_reformer(rebalancing_dates[idx+1]) -relativedelta(days=1), "%Y-%m-%d")  # 리밸런싱 전날
                _date_to = datetime.strftime(cls._datetime_reformer(rebalancing_dates[idx+1]), "%Y-%m-%d")  # 리밸런싱 당일 종가가 수익률에 포함됨
                
                _async_data_fdr = pd.DataFrame()

                for i in range(len(pdf)//_async_batch_size +1):
                    chunk_start, chunk_end = i*_async_batch_size, (i+1)*_async_batch_size
            
                    chunk = pdf[chunk_start:chunk_end]
                    chunk_krx = [i for i in chunk if (i.startswith('KRX:') | i.startswith('NICE:'))]  # ['KRX:007070', 'KRX:023530', 'KRX:139480', 'KRX:097950']
                    chunk_krx_not = list(set(chunk) - set(chunk_krx))

                    if len(chunk) != len(chunk_krx):
                        print(chunk)
                        print(chunk_krx)
                        import pdb
                        pdb.set_trace()

                    if len(chunk) == 0: break
                    try: 
                        async_data = cls._async_main_wrapper( chunk_krx, chunk_krx_not, _date_from, _date_to)
                    except:
                        async_data = cls._async_main_wrapper(cls, chunk_krx, chunk_krx_not, _date_from, _date_to)


                    for data in async_data: 
                        # data.columns = ['entity_name', 'close']  #! 데이터가 안받아져 왔을 시 죽는다
                        data.columns = ['entity_name', 'change_rate']  #! 데이터가 안받아져 왔을 시 죽는다
                        async_result = pd.concat([async_result, data], axis=0)

                '''
                for i in range(len(pdf)//_async_batch_size +1):
                    chunk_start, chunk_end = i*_async_batch_size, (i+1)*_async_batch_size
            
                    chunk = pdf[chunk_start:chunk_end]
                    chunk_krx = [i for i in chunk if (i.startswith('KRX:') | i.startswith('NICE:'))]
                    chunk_krx_not = list(set(chunk) - set(chunk_krx))

                    # chunk_krx = chunk_krx[chunk_start:chunk_end]
                    # chunk_krx_not = chunk_krx_not[chunk_start:chunk_end]


                    if len(chunk) == 0: break
                    #! 왜 다른가?
                    """try: 
                        async_data_krx = loop.run_until_complete( cls._async_main( cls, [i for i in chunk_krx], _date_from, _date_to ) )
                        if len(chunk_krx_not) > 0:
                            async_data_krx_not = loop.run_until_complete( cls._async_main( cls, [i for i in chunk_krx_not], _date_from, _date_to, krx=False) )
                            async_data_krx_not = [ cls._nonkrx_handler(async_data_krx_not[0], _date_from, _date_to) ]
                            async_data = [ pd.concat([async_data_krx[0], async_data_krx_not[0]]) ]
                        else:
                            async_data = async_data_krx
                    except: 
                        async_data_krx = loop.run_until_complete( cls._async_main( [i for i in chunk_krx], _date_from, _date_to ) )
                        if len(chunk_krx_not) > 0:
                            async_data_krx_not = loop.run_until_complete( cls._async_main( [i for i in chunk_krx_not], _date_from, _date_to, krx=False) )
                            async_data_krx_not = [ cls._nonkrx_handler(async_data_krx_not[0], _date_from, _date_to) ]
                            async_data = [ pd.concat([async_data_krx[0], async_data_krx_not[0]]) ]
                        else:
                            async_data = async_data_krx"""
                    # if (datetime.strptime(_date_from, "%Y-%m-%d") < datetime(2022, 9, 28)) & (datetime(2022, 9, 28) < datetime.strptime(_date_to, "%Y-%m-%d")):
                    #     for symbol in chunk_krx:
                    #         try:
                    #             _async_resp = cls._fdr_handler( symbol, _date_from, _date_to)
                    #         except:
                    #             _async_resp = cls._fdr_handler(cls, symbol, _date_from, _date_to)
                    #         _async_data_fdr = pd.concat([_async_data_fdr, _async_resp]).sort_index()
                    #     async_data = [_async_data_fdr]
                    # else:  # 문제의 기간이 없다면
                    try: 
                        async_data = cls._async_main_wrapper( chunk_krx, chunk_krx_not, _date_from, _date_to)
                    except:
                        async_data = cls._async_main_wrapper(cls, chunk_krx, chunk_krx_not, _date_from, _date_to)


                    for data in async_data: 
                        data.columns = ['entity_name', 'close']  #! 데이터가 안받아져 왔을 시 죽는다
                        async_result = pd.concat([async_result, data], axis=0)
                '''
            else:  #* if the last phase
                _date_from_for_close_column = datetime.strftime(date -relativedelta(days=1), "%Y-%m-%d")  # close 기반 하루전날 데이터 
                _date_from = datetime.strftime(date, "%Y-%m-%d")  # change_rate 기반 당일 데이터
                _date_to = datetime.strftime(datetime.today().date(), "%Y-%m-%d")



                for i in range(len(pdf)//_async_batch_size +1):
                    chunk_start, chunk_end = i*_async_batch_size, (i+1)*_async_batch_size
                    
                    chunk = pdf[chunk_start:chunk_end]
                    chunk_krx = [i for i in chunk if (i.startswith('KRX:') | i.startswith('NICE:'))]
                    chunk_krx_not = set(chunk) - set(chunk_krx)

                    if len(chunk) == 0: break
                    try: 
                        async_data = cls._async_main_wrapper(cls, chunk_krx, chunk_krx_not, _date_from, _date_to)
                    except:
                        async_data = cls._async_main_wrapper( chunk_krx, chunk_krx_not, _date_from, _date_to)


                    for data in async_data:
                        # data.columns = ['entity_name', 'close']
                        data.columns = ['entity_name', 'change_rate']  #! 데이터가 안받아져 왔을 시 죽는다
                        async_result = pd.concat([async_result, data], axis=0)
                '''
                _date_from = datetime.strftime(date -relativedelta(days=1), "%Y-%m-%d")
                _date_to = datetime.strftime(datetime.today().date(), "%Y-%m-%d")

                for i in range(len(pdf)//_async_batch_size +1):
                    chunk_start, chunk_end = i*_async_batch_size, (i+1)*_async_batch_size
                    
                    chunk = pdf[chunk_start:chunk_end]
                    chunk_krx = [i for i in chunk if (i.startswith('KRX:') | i.startswith('NICE:'))]
                    chunk_krx_not = list(set(chunk) - set(chunk_krx))

                    # chunk_krx = chunk_krx[chunk_start:chunk_end]
                    # chunk_krx_not = chunk_krx_not[chunk_start:chunk_end]


                    if len(chunk) == 0: break
                    #! 왜 다른가?
                    """try: 
                        async_data_krx = loop.run_until_complete( cls._async_main( cls, [i for i in chunk_krx], _date_from, _date_to) )  # datetime.strftime(datetime.today(), "%Y-%m-%d")
                        if len(chunk_krx_not) > 0:
                            async_data_krx_not = loop.run_until_complete( cls._async_main( cls, [i for i in chunk_krx_not], _date_from, _date_to, krx=False) )
                            async_data_krx_not = [ cls._nonkrx_handler(async_data_krx_not[0], _date_from, _date_to) ]
                            async_data = [ pd.concat([async_data_krx[0], async_data_krx_not[0]]) ]
                        else:
                            async_data = async_data_krx
                    except: 
                        async_data_krx = loop.run_until_complete( cls._async_main( [i for i in chunk_krx], _date_from, _date_to) )  # datetime.strftime(datetime.today(), "%Y-%m-%d")
                        if len(chunk_krx_not) > 0:
                            async_data_krx_not = loop.run_until_complete( cls._async_main( [i for i in chunk_krx_not], _date_from, _date_to, krx=False) )
                            async_data_krx_not = [ cls._nonkrx_handler(async_data_krx_not[0], _date_from, _date_to) ]
                            async_data = [ pd.concat([async_data_krx[0], async_data_krx_not[0]]) ]
                        else:
                            async_data = async_data_krx"""
                    # if (datetime.strptime(_date_from, "%Y-%m-%d") < datetime(2022, 9, 28)) & (datetime(2022, 9, 28) < datetime.strptime(_date_to, "%Y-%m-%d")):
                    #     _async_data_fdr = pd.DataFrame()
                    #     for symbol in chunk_krx:
                    #         if "NICE:" in symbol:
                    #             symbol = _df[_df["symbol"]==symbol].iloc[0]["symbol_listed"]
                    #         try:  # TypeError: _fdr_handler() takes 4 positional arguments but 5 were given
                    #             _async_resp = cls._fdr_handler( symbol, _date_from, _date_to)
                    #         except:
                    #             _async_resp = cls._fdr_handler(cls, symbol, _date_from, _date_to)
                    #         _async_data_fdr = pd.concat([_async_data_fdr, _async_resp]).sort_index()
                    #     async_data = [_async_data_fdr]
                    # else:
                    try: 
                        async_data = cls._async_main_wrapper( chunk_krx, chunk_krx_not, _date_from, _date_to)
                    except:
                        async_data = cls._async_main_wrapper(cls, chunk_krx, chunk_krx_not, _date_from, _date_to)


                    for data in async_data:
                        data.columns = ['entity_name', 'close']
                        async_result = pd.concat([async_result, data], axis=0)'''
            
            async_result_reset = async_result.reset_index()

            
            #####################################################################################################################
            #* close
            # pdf_returns_ds = async_result_reset.drop_duplicates(subset=['date', 'symbol'], keep='first').pivot(index='date', columns='symbol', values='close').ffill()
            # pdf_returns_async = (pdf_returns_ds.pct_change().fillna(0) +1).cumprod()  #! NICE가 없다

            #* change_rate
            pdf_returns_ds = async_result_reset.drop_duplicates(subset=['date', 'symbol'], keep='first').pivot(index='date', columns='symbol', values='change_rate').ffill()
            pdf_returns_async = (pdf_returns_ds +1).cumprod()
            #####################################################################################################################
            
            # pdf_returns_ds.iloc[0, :] = 0  #* 주가수익률로 계산했을 시기의 코드 
            # pdf_returns_async = (pdf_returns_ds +1).cumprod()  #* 주가수익률로 계산했을 시기의 코드 
            '''
            async_result_reset = async_result.reset_index()
            pdf_returns_ds = async_result_reset.drop_duplicates(subset=['date', 'symbol'], keep='first').pivot(index='date', columns='symbol', values='close').ffill()
            pdf_returns_async = (pdf_returns_ds.pct_change().fillna(0) +1).cumprod()  #! NICE가 없다
            # pdf_returns_ds.iloc[0, :] = 0  #* 주가수익률로 계산했을 시기의 코드 
            # pdf_returns_async = (pdf_returns_ds +1).cumprod()  #* 주가수익률로 계산했을 시기의 코드 
            '''
            pdf_returns_async.columns = [ delisted_firm_dict[i] if i in delisted_firm_dict.keys() else i for i in pdf_returns_async.columns ]

            inherited_budget = ratio * cls._aum  # 시작분배금  #! NICE가 있다 / ratio는 가장 최근의 리밸비중 / 여기서의 cls._aum 은 다음 값으로 업데이트 되기 전임
            #* 시작일은 base_point를 남기고 그 이후부터는 첫날의 리밸런싱 무수익을 떨군다

            """
            ? 이전 코드
            try: _prev_aum_change_async = _aum_change_async
            except: pass
            """
            inherited_budget.index = inherited_budget.index.astype(str)
            pdf_returns_async.columns = pdf_returns_async.columns.astype(str)
            if idx > 0: 
                _aum_change_async = pdf_returns_async[datetime.strptime(_date_from, "%Y-%m-%d").date() +relativedelta(days=1):] *inherited_budget
            else: 
                _aum_change_async = pdf_returns_async *inherited_budget

            cls._aum = _aum_change_async.sum(axis=1)[-1]
            total_return = pd.concat([total_return, _aum_change_async])
            print(cls._aum)

            '''
            try: _prev_aum_change_async = _aum_change_async
            except: pass
            inherited_budget.index = inherited_budget.index.astype(str)
            pdf_returns_async.columns = pdf_returns_async.columns.astype(str)
            if idx > 0: 
                _aum_change_async = pdf_returns_async[datetime.strptime(_date_from, "%Y-%m-%d").date() +relativedelta(days=1):] *inherited_budget
            else: _aum_change_async = pdf_returns_async *inherited_budget

            cls._aum = _aum_change_async.sum(axis=1)[-1]
            total_return = pd.concat([total_return, _aum_change_async])
            print(cls._aum)
            '''

            # total_return = pd.concat([total_return, _aum_change_wavelet])

        if debug == True:
            import pdb
            pdb.set_trace()

        total_return = total_return.groupby(total_return.index).first()

        cls._aum = 100_000_000_000.0  #! 변수 초기화

        '''
        if df_to_upload_bool:
            total_return = total_return.groupby(total_return.index).first()
            base_point = 1000
            daily_aum = total_return.sum(axis=1)
            daily_aum.index = pd.to_datetime(daily_aum.index)
            try:
                daily_idx = daily_aum / daily_aum[datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), "%Y-%m-%d")] *base_point
            except:
                print(f'error check [{rebalancing_dates[0]}] - date index not exists, call the most recent previous date')
                daily_idx = daily_aum / daily_aum[:datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), "%Y-%m-%d")].iloc[-1] *base_point
            daily_idx = daily_idx[datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), "%Y-%m-%d"):]


            kospi = cls.deepsearch.compute(f"코스피 지수 {datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), '%Y-%m-%d')}-{datetime.strftime(datetime.today().date(), '%Y-%m-%d')}").reset_index().set_index('date')
            # from pandas_datareader import data 
            # df_krx = fdr.StockListing('KRX')
            # resp = fdr.DataReader("069500", start=datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), '%Y-%m-%d'), end=datetime.strftime(datetime.today().date(), '%Y-%m-%d'))
            # resp = data.DataReader("KOSPI", "naver", start=datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), '%Y-%m-%d'), end=datetime.strftime(datetime.today().date(), '%Y-%m-%d'))[["Open", "High", "Low", "Close", "Volume"]]
            # resp = resp.astype(float)

            # resp["symbol"] = "KRX:KOSPI"
            # resp["entity_name"] = "코스피"
            # resp = resp.reset_index()[["Date", "symbol", "entity_name", "Close"]].sort_values(by=["Date"])
            # resp.columns = ["date", "symbol", "entity_name", f"주가 {datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), '%Y-%m-%d')}-{datetime.strftime(datetime.today().date(), '%Y-%m-%d')}"]
            # resp = resp.set_index(["date", "symbol"])
            # kospi = resp.reset_index().set_index('date')

            kospi.columns = ['symbol', 'entity_name', 'close']
            kospi.index = pd.to_datetime(kospi.index).date


            # if fdr == False:
            #     kospi = cls.deepsearch.compute(f"코스피 지수 {datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), '%Y-%m-%d')}-{datetime.strftime(datetime.today().date(), '%Y-%m-%d')}").reset_index().set_index('date')
            # kospi.columns = ['symbol', 'entity_name', 'close']
            # kospi.index = pd.to_datetime(kospi.index).date

            #! 한국주식과 미국주식을 섞으면 공휴일이 다르다 
            daily_idx_date_reviewed = daily_idx.loc[kospi.index]
            # kospi_ret = kospi['close'].loc[daily_idx.index].pct_change()  # 당일의 종가수익률이 아니라 판다스에서 추가적으로 계산된 값이므로 첫날의 수익률은 누락 #! 그런데 첫날이 월요일이면 -1day때문에 길이가 안맞는다
            kospi_ret = kospi['close'].pct_change()

            daily_kospi = (kospi_ret+1).cumprod().fillna(1) *base_point
            # daily_kospi.index = daily_kospi.index.date
            #업로드용 파일 가공
            _excel_date_format = "%Y-%m-%d"
            # df_to_upload = pd.concat([daily_idx, daily_kospi], axis=1)
            df_to_upload = pd.concat([daily_idx_date_reviewed, daily_kospi], axis=1)
            df_to_upload.columns = ['index', 'KOSPI']
            df_to_upload.index = pd.to_datetime(df_to_upload.index, format="%Y-%m-%d")
            df_to_upload.index = df_to_upload.index.strftime(_excel_date_format)
            df_to_upload = df_to_upload.reset_index()
            df_to_upload.columns = ['date', 'index', 'KOSPI']

            
            df_to_upload['date'] = df_to_upload['date'].astype(str)

            return df_to_upload
        return total_return
        '''


        if df_to_upload_bool:
            total_return = total_return.groupby(total_return.index).first()
            base_point = 1000
            daily_aum = total_return.sum(axis=1)
            daily_aum.index = pd.to_datetime(daily_aum.index)
            index_calc_start_date = cls._datetime_reformer(rebalancing_dates[0])

            """
            //2023-01-19//
            close 기반 기존의 계산 -> 시가매수
            change_rate 기반 계산 -> 종가매수 
            """
            import copy
            daily_aum_for_change_rate = copy.deepcopy(daily_aum)
            daily_aum_for_change_rate = dict(daily_aum_for_change_rate)
            daily_aum_for_change_rate[index_calc_start_date] = 100_000_000_000
            daily_aum_for_change_rate = pd.Series(daily_aum_for_change_rate).sort_index()

            daily_aum = daily_aum_for_change_rate

            try:
                daily_idx = daily_aum / daily_aum[datetime.strftime(index_calc_start_date, "%Y-%m-%d")] *base_point
            except:
                print(f'error check [{rebalancing_dates[0]}] - date index not exists, call the most recent previous date')
                daily_idx = daily_aum / daily_aum[:datetime.strftime(index_calc_start_date, "%Y-%m-%d")].iloc[-1] *base_point
            daily_idx = daily_idx[datetime.strftime(index_calc_start_date, "%Y-%m-%d"):]


            import FinanceDataReader as fdr
            from pandas_datareader import data 
            resp = data.DataReader("KOSPI", "naver", start=datetime.strftime(index_calc_start_date, '%Y-%m-%d'), end=datetime.strftime(datetime.today().date(), '%Y-%m-%d'))[["Open", "High", "Low", "Close", "Volume"]]
            resp = resp.astype(float)
            resp["symbol"] = "KRX:KOSPI"
            resp["entity_name"] = "코스피"
            resp = resp.reset_index()[["Date", "symbol", "entity_name", "Close"]].sort_values(by=["Date"])
            resp.columns = ["date", "symbol", "entity_name", f"주가 {datetime.strftime(index_calc_start_date, '%Y-%m-%d')}-{datetime.strftime(datetime.today().date(), '%Y-%m-%d')}"]
            resp = resp.set_index(["date", "symbol"])
            kospi = resp.reset_index().set_index('date')
            kospi.columns = ['symbol', 'entity_name', 'close']
            kospi.index = pd.to_datetime(kospi.index).date

            #! 한국주식과 미국주식을 섞으면 공휴일이 다르다 
            _excel_date_format = "%Y-%m-%d"
            try:
                daily_idx_date_reviewed = daily_idx.loc[kospi.index]
            except:
                daily_idx.index = pd.to_datetime(daily_idx.index).date
                daily_idx_date_reviewed = daily_idx
            
            df_to_upload = pd.concat([daily_idx_date_reviewed, kospi["close"]], axis=1).sort_index(ascending=True).bfill()
            df_to_upload.columns = ['index', 'KOSPI']
            df_to_upload.index = pd.to_datetime(df_to_upload.index, format="%Y-%m-%d")
            df_to_upload.index = df_to_upload.index.strftime(_excel_date_format)
            df_to_upload = df_to_upload.reset_index()
            df_to_upload.columns = ['date', 'index', 'KOSPI']

            df_to_upload["index"] = df_to_upload["index"] / df_to_upload["index"].iloc[0] * base_point
            df_to_upload["KOSPI"] = df_to_upload["KOSPI"] / df_to_upload["KOSPI"].iloc[0] * base_point


            df_to_upload['date'] = df_to_upload['date'].astype(str)

            return df_to_upload
        return total_return




class _backtest(object):
    _aum = 100_000_000_000.0
    deepsearch = DeepSearchAPI()
    async_deepsearch = asyncDeepSearchAPI()
    wavelet = WaveletAPI()

    def _split_phases(cls, deepsearch_df):
        return_dict = dict()
        phases = deepsearch_df.index.unique()
        for p in phases:
            pdf = deepsearch_df.loc[p]
            return_dict[p] = pdf
        return return_dict

    def _is_business_day(date):
        return bool(len(pd.bdate_range(date, date)))

    @classmethod
    async def _async_main(cls, symbol_list, date_from, date_to):
        query = ' '.join(symbol_list) + f' {date_from}-{date_to} 주가'  #! 주가수익률은 해당말일을 기준으로 한 점만 보여준다
        task = [cls.async_deepsearch.compute(query)]
        result = await asyncio.gather(*task)
        return result

    @classmethod
    def compute(cls, deepsearch_df, df_to_upload_bool=False, debug=False):
        df = cls._split_phases(cls, deepsearch_df)
        rebalancing_dates = list(df.keys())
        for idx, date in enumerate(rebalancing_dates):
            if datetime.today() < (datetime.strptime(date, "%m/%d/%Y")):
                print(rebalancing_dates, rebalancing_dates[:idx])
                rebalancing_dates = rebalancing_dates[:idx]
                break



        loop = asyncio.get_event_loop()
        _async_batch_size = 10


        total_return = pd.DataFrame()
        for idx, date in enumerate(rebalancing_dates):  # idx starts from 0
            async_result = pd.DataFrame()
            if isinstance(df[date], pd.Series): _df = pd.DataFrame(df[date]).T
            else: _df = df[date]
            ratio = _df.reset_index().set_index(['symbol'])['weight'].astype(float)  # 단축코드, 비중(비중의합은1)
            ratio.index = ratio.index.str.replace(" ", "")
            pdf = list(_df['symbol'])  # 0 은 iter item (timestamp)

            delisted_firm_dict = dict()
            delisted_firm = _df[_df['symbol'] != _df['symbol_listed']]
            for _, row in delisted_firm.iterrows(): delisted_firm_dict[row['symbol_listed']] = row['symbol']

            date = datetime.strptime(date, "%m/%d/%Y")

            b_days = 0
            while True:
                if not cls._is_business_day(date): date, b_days = date +relativedelta(days=1), b_days +1
                else: break


            if idx+1 != len(rebalancing_dates):  #* if not the last phase
                _date_from = datetime.strftime(date -relativedelta(days=1), "%Y-%m-%d")
                _date_to = datetime.strftime(datetime.strptime(rebalancing_dates[idx+1], "%m/%d/%Y") -relativedelta(days=1), "%Y-%m-%d")

                for i in range(len(pdf)//_async_batch_size +1):
                    chunk_start, chunk_end = i*_async_batch_size, (i+1)*_async_batch_size
                    chunk = pdf[chunk_start:chunk_end]
                    if len(chunk) == 0: break
                    #! 왜 다른가?
                    try: async_data = loop.run_until_complete( cls._async_main( cls, [i for i in chunk], _date_from, _date_to ) )
                    except: async_data = loop.run_until_complete( cls._async_main( [i for i in chunk], _date_from, _date_to ) )
                    for data in async_data: 
                        data.columns = ['entity_name', 'close']  #! 데이터가 안받아져 왔을 시 죽는다
                        async_result = pd.concat([async_result, data], axis=0)
            else:  #* if the last phase
                _date_from = datetime.strftime(date -relativedelta(days=1), "%Y-%m-%d")
                _date_to = datetime.strftime(datetime.today().date(), "%Y-%m-%d")

                for i in range(len(pdf)//_async_batch_size +1):
                    chunk_start, chunk_end = i*_async_batch_size, (i+1)*_async_batch_size
                    chunk = pdf[chunk_start:chunk_end]
                    if len(chunk) == 0: break
                    #! 왜 다른가?
                    try: async_data = loop.run_until_complete( cls._async_main( cls, [i for i in chunk], _date_from, _date_to) )  # datetime.strftime(datetime.today(), "%Y-%m-%d")
                    except: async_data = loop.run_until_complete( cls._async_main( [i for i in chunk], _date_from, _date_to) )  # datetime.strftime(datetime.today(), "%Y-%m-%d")
                    for data in async_data:
                        data.columns = ['entity_name', 'close']
                        async_result = pd.concat([async_result, data], axis=0)

            async_result_reset = async_result.reset_index()
            pdf_returns_ds = async_result_reset.drop_duplicates(subset=['date', 'symbol'], keep='first').pivot(index='date', columns='symbol', values='close')
            pdf_returns_async = (pdf_returns_ds.pct_change().fillna(0) +1).cumprod()  #! NICE가 없다
            # pdf_returns_ds.iloc[0, :] = 0  #* 주가수익률로 계산했을 시기의 코드 
            # pdf_returns_async = (pdf_returns_ds +1).cumprod()  #* 주가수익률로 계산했을 시기의 코드 
            pdf_returns_async.columns = [ delisted_firm_dict[i] if i in delisted_firm_dict.keys() else i for i in pdf_returns_async.columns ]

            inherited_budget = ratio * cls._aum  # 시작분배금  #! NICE가 있다 / ratio는 가장 최근의 리밸비중 / 여기서의 cls._aum 은 다음 값으로 업데이트 되기 전임
            #* 시작일은 base_point를 남기고 그 이후부터는 첫날의 리밸런싱 무수익을 떨군다

            try: _prev_aum_change_async = _aum_change_async
            except: pass
            inherited_budget.index = inherited_budget.index.astype(str)
            pdf_returns_async.columns = pdf_returns_async.columns.astype(str)
            if idx > 0: 
                _aum_change_async = pdf_returns_async[datetime.strptime(_date_from, "%Y-%m-%d").date() +relativedelta(days=1):] *inherited_budget
            else: _aum_change_async = pdf_returns_async *inherited_budget

            cls._aum = _aum_change_async.sum(axis=1)[-1]
            total_return = pd.concat([total_return, _aum_change_async])
            print(cls._aum)

            # total_return = pd.concat([total_return, _aum_change_wavelet])

        if debug == True:
            import pdb
            pdb.set_trace()

        total_return = total_return.groupby(total_return.index).first()

        cls._aum = 100_000_000_000.0  #! 변수 초기화

        if df_to_upload_bool:
            total_return = total_return.groupby(total_return.index).first()
            base_point = 1000
            daily_aum = total_return.sum(axis=1)
            try:
                daily_idx = daily_aum / daily_aum[datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), "%Y-%m-%d")] *base_point
            except:
                print(f'error check [{rebalancing_dates[0]}] - date index not exists, call the most recent previous date')
                daily_idx = daily_aum / daily_aum[:datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), "%Y-%m-%d")].iloc[-1] *base_point
            daily_idx = daily_idx[datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), "%Y-%m-%d"):]
            
            """
            daily_aum.index = pd.to_datetime(daily_aum.index)
            daily_idx = daily_aum / daily_aum[datetime.strftime(datetime.strptime(rebalancing_dates[0], "%m/%d/%Y"), "%Y-%m-%d")] *base_point
            daily_idx = daily_idx[datetime.strftime(datetime.strptime(rebalancing_dates[0], "%m/%d/%Y"), "%Y-%m-%d"):]
            # daily_idx.index = daily_idx.index.date
            """

            #* rebalancing_dates[0] 은 해당일 종가매수를 의미한다.
            #* 즉, 월요일부터의 수익률을 보고싶은 경우, 리밸런싱 날짜는 월요일이 아닌 직전 거래일(금요일)을 넣어야 한다.
            _query_kospi = f"코스피 지수 {datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), '%Y-%m-%d')}-{datetime.strftime(datetime.today().date(), '%Y-%m-%d')}"
            resp = cls.deepsearch.compute(_query_kospi).reset_index().set_index('date')
            resp.columns = ['close' if '지수' in i else i for i in resp.columns]
            kospi = resp

            # import FinanceDataReader as fdr
            # from pandas_datareader import data 
            # resp = data.DataReader("KOSPI", "naver", start=datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), '%Y-%m-%d'), end=datetime.strftime(datetime.today().date(), '%Y-%m-%d'))[["Open", "High", "Low", "Close", "Volume"]]
            # resp = resp.astype(float)
            # resp["symbol"] = "KRX:KOSPI"
            # resp["entity_name"] = "코스피"
            # resp = resp.reset_index()[["Date", "symbol", "entity_name", "Close"]].sort_values(by=["Date"])
            # resp.columns = ["date", "symbol", "entity_name", f"주가 {datetime.strftime(cls._datetime_reformer(rebalancing_dates[0]), '%Y-%m-%d')}-{datetime.strftime(datetime.today().date(), '%Y-%m-%d')}"]
            # resp = resp.set_index(["date", "symbol"])
            # kospi = resp.reset_index().set_index('date')
            # kospi.columns = ['symbol', 'entity_name', 'close']
            # kospi.index = pd.to_datetime(kospi.index).date

            #! 한국주식과 미국주식을 섞으면 공휴일이 다르다 
            try:
                daily_idx_date_reviewed = daily_idx.loc[kospi.index]
            except:
                import pdb
                pdb.set_trace()
            # kospi_ret = kospi['close'].loc[daily_idx.index].pct_change()  # 당일의 종가수익률이 아니라 판다스에서 추가적으로 계산된 값이므로 첫날의 수익률은 누락 #! 그런데 첫날이 월요일이면 -1day때문에 길이가 안맞는다
            kospi_ret = kospi['close'].pct_change()

            daily_kospi = (kospi_ret+1).cumprod().fillna(1) *base_point  #* 엑셀 holdings 파일의 date 는 종가매수의 기준일이므로, 날짜를 월요일로 잡아도 월요일 종가매수를 의미한다. 
            # daily_kospi.index = daily_kospi.index.date
            #업로드용 파일 가공
            _excel_date_format = "%Y-%m-%d"
            # df_to_upload = pd.concat([daily_idx, daily_kospi], axis=1)
            df_to_upload = pd.concat([daily_idx_date_reviewed, daily_kospi], axis=1)
            df_to_upload.columns = ['index', 'KOSPI']
            df_to_upload.index = pd.to_datetime(df_to_upload.index, format="%Y-%m-%d")
            df_to_upload.index = df_to_upload.index.strftime(_excel_date_format)
            df_to_upload = df_to_upload.reset_index()
            df_to_upload.columns = ['date', 'index', 'KOSPI']
            df_to_upload['date'] = df_to_upload['date'].astype(str)

            """
            _excel_date_format = "%d/%m/%Y"
            df_to_upload = pd.concat([daily_idx, daily_kospi], axis=1)
            df_to_upload.columns = ['index', 'KOSPI']
            df_to_upload.index = pd.to_datetime(df_to_upload.index, format="%Y-%m-%d")
            df_to_upload.index = df_to_upload.index.strftime(_excel_date_format)
            df_to_upload = df_to_upload.reset_index()
            """

            return df_to_upload
        return total_return
