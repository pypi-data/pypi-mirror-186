import os
import itertools
import multiprocessing as mp
import zlib

from .equity_curves import *
from .signals import *
from .aggregate import *

def multi_process(function, parameters, number_of_core=8):
    pool = mp.Pool(processes=number_of_core)
    pool.map(function, parameters)
    pool.close()


def filename_only(para_combination):
    para_dict = para_combination['para_dict']
    start_date = para_combination['start_date']
    end_date = para_combination['end_date']
    py_filename = para_combination['py_filename']
    start_date_str = datetime.datetime.strptime(start_date, '%Y-%m-%d').strftime("%Y%m%d")
    end_date_str = datetime.datetime.strptime(end_date, '%Y-%m-%d').strftime("%Y%m%d")
    summary_mode = para_combination['summary_mode']
    freq = para_combination['freq']


    save_name = f'file={py_filename}&date={start_date_str}{end_date_str}&freq={freq}&summary_mode={summary_mode}&'

    for key in list(para_dict.keys()):
        para = para_combination[key]
        if key == 'code':
            if str(para).isdigit():
                para = str(para).zfill(5)

        if isinstance(para, float):
            if para.is_integer():
                para = int(para)

        save_name += f'{key}={str(para)}&'

    return save_name


def path_reference_code(save_name):
    reference_code = str(zlib.crc32(bytes(save_name, 'UTF-8')))[:6]
    return reference_code

def generate_filepath(para_combination,folder=''):
    save_name = filename_only(para_combination)

    reference_code = path_reference_code(save_name)
    save_name = reference_code + '_' + save_name[:-1]     # position -1 to avoid '&' at the end

    output_folder = para_combination['output_folder']
    filepath = os.path.join(folder,output_folder, f'{save_name}.csv')

    return filepath


def mp_cal_performance(tuple_data):
    para_combination = tuple_data[0]
    manager_list = tuple_data[1]

    result = cal_performance(para_combination)
    index = para_combination['reference_index']
    manager_list.append((index,result))


def generate_backtest_result(all_para_combination, number_of_core=8):
    manager_list = mp.Manager().list()# To save the result with index number

    cal_performance_list = []
    for para_combination in all_para_combination:
        cal_performance_list.append((para_combination, manager_list))

    pool = mp.Pool(processes=number_of_core)
    pool.map(mp_cal_performance, cal_performance_list)
    pool.close()

    df_backtest_result = pd.DataFrame()
    df_backtest_result['reference_code'] = np.NaN
    df_backtest_result['reference_index'] = np.NaN
    para_keys = all_para_combination[0]['para_dict'].keys()
    for key in para_keys:
        df_backtest_result[key] = np.NaN
    for key in manager_list[0][1].keys():
        df_backtest_result[key] = np.NaN

    for mp_data in manager_list:
        reference_index = mp_data[0]
        result_dict = mp_data[1]
        para_combination = all_para_combination[reference_index]
        save_name = filename_only(para_combination)
        reference_code = path_reference_code(save_name)
        df_backtest_result.at[reference_index, 'reference_code'] = reference_code
        df_backtest_result.at[reference_index, 'reference_index'] = reference_index
        for key in para_keys:
            df_backtest_result.at[reference_index, key] = para_combination[key]
        for key in result_dict:
            df_backtest_result.at[reference_index, key] = result_dict[key]

    # print(df_backtest_result)
    df_backtest_result['reference_index'] = df_backtest_result['reference_index'].astype(int)
    df_backtest_result.to_csv('backtest_result.csv')



def plot_signal_analysis(py_filename, output_folder, start_date, end_date, para_dict, signal_settings):

    app = signals.Signals(py_filename, output_folder, start_date, end_date, para_dict, generate_filepath, signal_settings)

    return app


def plot(mode, all_para_combination={},  subchart_settings={}):
    if mode == 'equity_curves':
        result_df = pd.read_csv('backtest_result.csv', index_col=0)
        app = equity_curves.Plot(all_para_combination, result_df, subchart_settings)
    if mode == 'aggregate':
        app = aggregate.Aggregate()


    return app




def calculate_mdd(df_csv, col):
    df = df_csv.copy()
    roll_max = df[col].cummax()
    daily_drawdown = df[col] / roll_max - 1.0
    max_daily_drawdown = daily_drawdown.cummin()

    return min(list(max_daily_drawdown)), min(list(df[col] - roll_max))


def calculate_win_rate_info(df_csv):
    df = df_csv.copy()
    num_of_trade = list(df['action'] == 'open').count(True)
    num_of_loss = list(df['pnl'] < 0).count(True)
    num_of_win = num_of_trade - num_of_loss

    if num_of_trade > 0:
        win_rate = round(100 * num_of_win / num_of_trade, 2)
        loss_rate = round(100 * num_of_loss / num_of_trade, 2)
    else:
        win_rate = '--'
        loss_rate = '--'

    # win_rate = str(int(round(100 * num_of_win / num_of_trade, 0))) if num_of_trade > 0 else '--'

    return num_of_trade, num_of_loss, num_of_win, win_rate, loss_rate


def calculate_win_rate(df_csv):
    df = df_csv.copy()
    df = df[df['action'].notnull()].reset_index(drop=True)
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['pnl'] = df['realized_pnl'].shift(-1)
    df['year'] = pd.DatetimeIndex(df['date']).year
    year_list = list(set(df['year']))
    year_list.sort()

    win_rate_dict = {}
    win_rate_dict['Overall'] = calculate_win_rate_info(df)

    for year in year_list:
        win_rate_dict[year] = calculate_win_rate_info(df.loc[df['year'] == year])

    return win_rate_dict


def calculate_sharp_ratio(df_csv, col):
    df = df_csv.copy()
    holding_period_day = (df.loc[df.index[-1], 'date'] - df.loc[df.index[0], 'date']).days
    net_profit = df.at[df.index[-1], col] - df.at[df.index[0], col]

    initial_capital = df.loc[df.index[0], col]
    equity_value_pct_series = df[col].pct_change()
    equity_value_pct_series = equity_value_pct_series.dropna()

    return_on_capital = net_profit / initial_capital
    annualized_return = (1 + return_on_capital) ** (365 / holding_period_day) - 1
    annualized_std = equity_value_pct_series.std() * math.sqrt(365)

    if annualized_std > 0:
        annualized_sr = annualized_return / annualized_std
    else:
        annualized_sr = 0

    return_on_capital = round(100 * return_on_capital, 2)
    annualized_return = round(100 * annualized_return, 2)
    annualized_std = round(100 * annualized_std, 2)
    annualized_sr = round(annualized_sr, 2)

    return net_profit, holding_period_day, return_on_capital, annualized_return, annualized_std, annualized_sr


def resample_summary_to_daily(para_combination, folder=''):
    # Need to deal with the start date and date

    start_date = para_combination['start_date']
    end_date = para_combination['end_date']
    sectype = para_combination['sectype']
    lot_size = para_combination['lot_size']
    intraday = para_combination['intraday']
    freq = para_combination['freq']
    sec_profile = para_combination['sec_profile']
    margin_req = sec_profile['margin_req']
    multiplier = sec_profile['multiplier']

    # Read backtest data
    save_path = generate_filepath(para_combination=para_combination,folder=folder)
    df_backtest = pd.read_csv(save_path, index_col=0)  # Daraframe that may not be daily
    df_backtest['date'] = pd.to_datetime(df_backtest['date'], format='%Y-%m-%d')
    df_backtest = df_backtest.loc[(df_backtest['date'] >= start_date) & (df_backtest['date'] <= end_date)]
    df_backtest = df_backtest.reset_index(drop=True)  # Reset Index

    trade_pair = zip(*(iter(list(df_backtest.index)),) * 2)  # Group df_backtest by 2
    initial_capital = df_backtest.iloc[-1].equity_value - df_backtest['realized_pnl'].sum()
    last_realized_capital = initial_capital

    # Read source data
    data_folder = para_combination['data_folder']
    code = para_combination['code']
    data_path = os.path.join(folder,data_folder, f'{code}_{freq}.csv')
    df_csv = pd.read_csv(data_path)
    df_daily = pd.DataFrame()  # Dataframe for Daily
    df_daily['open'] = df_csv['open']
    df_daily['high'] = df_csv['high']
    df_daily['low'] = df_csv['low']
    df_daily['close'] = df_csv['close']
    df_daily['volume'] = df_csv['volume']
    df_daily.index = pd.to_datetime(df_csv['datetime'], format='%Y-%m-%d %H:%M:%S')

    if intraday:
        df_daily = df_daily.resample('1D').agg({'open': 'first', 'high': 'max', 'low': 'min',
                                                'close': 'last', 'volume': 'sum',
                                                }).copy()

    df_daily['date'] = df_daily.index
    df_daily = df_daily.loc[(df_daily['date'] >= start_date) & (df_daily['date'] <= end_date)]
    df_daily = df_daily.loc[df_daily['close'].isnull() == False].copy()  # Filter out non trading day
    df_daily['bah'] = df_daily['close'] * (initial_capital / df_daily.iloc[0].close)  # Calculate all bah value
    df_daily.at[df_daily.index[0], 'equity_value'] = initial_capital  # Set the equity value at the beginning
    df_daily['action'] = None
    df_daily['realized_pnl'] = None
    df_daily['unrealized_pnl'] = None
    df_daily['signal_value'] = None

    for i, j in trade_pair:
        open_date = df_backtest.at[i, 'date']
        close_date = df_backtest.at[j, 'date']
        dates = pd.date_range(start=open_date, end=close_date)  # Determine days between open_date and close_date
        now_close = df_daily.at[open_date, 'close']
        # print(i, j)
        # print(dates)
        # print(df_backtest.at[i, 'date'], df_backtest.at[i, 'action'])
        # print(df_backtest.at[j, 'date'], df_backtest.at[j, 'action'])


        if sectype == 'STK':
            num_of_share = lot_size * (last_realized_capital // (now_close * lot_size))
        elif sectype == 'FUT':
            num_of_share = last_realized_capital // margin_req

        open_price = df_backtest.at[i, 'open_price']
        commission = df_backtest.at[j, 'commission']

        df_daily.at[open_date, 'signal_value'] = df_daily.at[open_date, 'bah']  # Mark the open for each trade_pair

        # print(open_price, df_daily.at[open_date, 'bah'])

        # If only one date in the dates (i.e. open and close at the same day), add one more to avoid error
        if open_date == close_date:
            dates = list(dates) + list(dates)
            dates = pd.to_datetime(dates, format='%Y-%m-%d')

        # For the situation that open and close is not the same day. If same, close pnl will replace this one
        df_daily.at[open_date, 'action'] = 'open'
        unrealized_pnl = num_of_share * multiplier * (now_close - open_price) - commission
        unrealized_pnl = round(unrealized_pnl, 3)
        df_daily.at[open_date, 'unrealized_pnl'] = unrealized_pnl
        # print(open_date, 'Open!', open_price, now_close, unrealized_pnl)

        ### record unrealised pnl and realized pnl and the same time
        ### unrealised pnl for the equity value in between
        for date in dates[1:]:
            if date == close_date:  # close position on this date

                # clear the open pnl as open and close same day should not aggregate
                if open_date == close_date:
                    df_daily.at[date, 'unrealized_pnl'] = None

                # unrealized_pnl
                if df_daily.at[date, 'unrealized_pnl']:  # if there is already unrealized_pnl, aggregate
                    df_daily.at[date, 'unrealized_pnl'] = df_daily.at[date, 'unrealized_pnl'] + df_backtest.at[
                        j, 'realized_pnl']
                else:
                    df_daily.at[date, 'unrealized_pnl'] = df_backtest.at[j, 'realized_pnl']

                # realized pnl
                if df_daily.at[date, 'realized_pnl']:  # if there is already realized_pnl, aggregate
                    df_daily.at[date, 'realized_pnl'] = df_daily.at[date, 'realized_pnl'] + df_backtest.at[
                        j, 'realized_pnl']
                else:
                    df_daily.at[date, 'realized_pnl'] = df_backtest.at[j, 'realized_pnl']

                df_daily.at[date, 'action'] = df_backtest.at[j, 'action']
                df_daily.at[date, 'commission'] = df_backtest.at[j, 'commission']
                last_realized_capital = last_realized_capital + df_backtest.at[j, 'realized_pnl']

                # print(date, 'Close!', open_price, df_backtest.at[j, 'close_price'], df_backtest.at[j, 'realized_pnl'])

            else:
                try:
                    now_close = df_daily.at[date, 'close']
                    unrealized_pnl = num_of_share * multiplier * (now_close - open_price) - commission
                    unrealized_pnl = round(unrealized_pnl, 3)
                    if df_daily.at[date, 'unrealized_pnl']:
                        df_daily.at[date, 'unrealized_pnl'] = df_daily.at[date, 'unrealized_pnl'] + unrealized_pnl
                    else:
                        df_daily.at[date, 'unrealized_pnl'] = unrealized_pnl

                    # print(date, 'Not yet close', open_price, now_close, unrealized_pnl)

                except:
                    pass
                    # print(date, 'Not yet close', 'Holiday!')

        # print()

    last_equity_value = initial_capital
    for i in df_daily.index[1:]:
        if df_daily.at[i, 'realized_pnl']:
            df_daily.at[i, 'equity_value'] = last_equity_value + df_daily.at[i, 'realized_pnl']
            last_equity_value = df_daily.at[i, 'equity_value']

        elif df_daily.at[i, 'unrealized_pnl']:
            df_daily.at[i, 'equity_value'] = last_equity_value + df_daily.at[i, 'unrealized_pnl']

    df_daily['equity_value'] = df_daily['equity_value'].fillna(method='ffill')  # Fill na for equity value only

    # df_daily.to_csv('df_daily.csv')

    return df_daily




def cal_performance(para_combination):

    start_date = para_combination['start_date']
    end_date = para_combination['end_date']

    intraday = para_combination['intraday']
    summary_mode = para_combination['summary_mode']

    if (intraday or summary_mode):
        df_daily = resample_summary_to_daily(para_combination=para_combination)
    else:
        save_path = generate_filepath(para_combination=para_combination)
        df_backtest = pd.read_csv(save_path, index_col=0)  # Daraframe that may not be daily
        df_backtest['date'] = pd.to_datetime(df_backtest['date'], format='%Y-%m-%d')
        df_backtest = df_backtest.loc[(df_backtest['date'] >= start_date) & (df_backtest['date'] <= end_date)]
        df_backtest = df_backtest.reset_index(drop=True)  # Reset Index
        df_daily = df_backtest.copy()

    result_dict = {}

    # Determine years at the beginning
    start_date_year = datetime.datetime.strptime(start_date, '%Y-%m-%d').year
    end_date_year = datetime.datetime.strptime(end_date, '%Y-%m-%d').year
    year_list = list(range(start_date_year, end_date_year + 1))
    for y in year_list: result_dict[str(y)] = []

    # df = pd.read_csv(save_path)
    df = df_daily.copy()
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

    # Strategy Performance
    net_profit, holding_period_day, return_on_capital, annualized_return, annualized_std, annualized_sr = calculate_sharp_ratio(df, 'equity_value')
    mdd_pct, mdd_dollar = calculate_mdd(df, 'equity_value')
    mdd_pct = mdd_pct * -100
    mdd_dollar = mdd_dollar * -1

    # Win Rate (need to use df_backtest directly)
    save_path = generate_filepath(para_combination=para_combination)
    df_backtest = pd.read_csv(save_path, index_col=0)
    win_rate_dict = calculate_win_rate(df_backtest)
    num_of_trade, num_of_loss, num_of_win, win_rate, loss_rate = win_rate_dict['Overall']
    # print('net_profit',net_profit)

    # BaH Performance
    bah_net_return, holding_period_day, bah_return, \
    bah_annualized_return, bah_annualized_std, bah_annualized_sr = calculate_sharp_ratio(df, 'close')
    initial_capital = df.loc[df.index[0], 'equity_value']
    df['bah_equity_curve'] = df['close'] * initial_capital // df.loc[df.index[0], 'close']
    bah_mdd_pct, bah_mdd_dollar = calculate_mdd(df, 'bah_equity_curve')
    bah_mdd_pct = bah_mdd_pct * -100
    bah_mdd_dollar = bah_mdd_dollar * -1

    total_commission = df['commission'].sum()

    result_dict['holding_period_day'] = holding_period_day
    result_dict['total_commission'] = total_commission

    result_dict['net_profit'] = net_profit
    result_dict['return_on_capital'] = return_on_capital
    result_dict['annualized_return'] = annualized_return
    result_dict['annualized_std'] = annualized_std
    result_dict['annualized_sr'] = annualized_sr
    result_dict['mdd_dollar'] = mdd_dollar
    result_dict['mdd_pct'] = mdd_pct
    result_dict['num_of_trade'] = num_of_trade
    result_dict['win_rate'] = win_rate
    result_dict['loss_rate'] = loss_rate
    if mdd_dollar == 0:
        result_dict['net_profit_to_mdd'] = np.inf
    else:
        result_dict['net_profit_to_mdd'] = net_profit / mdd_dollar

    result_dict['bah_return'] = bah_return
    result_dict['bah_annualized_return'] = bah_annualized_return
    result_dict['bah_annualized_std'] = bah_annualized_std
    result_dict['bah_annualized_sr'] = bah_annualized_sr
    result_dict['bah_mdd_dollar'] = bah_mdd_dollar
    result_dict['bah_mdd_pct'] = bah_mdd_pct

    # Cov
    df3 = df[df['action'] == 'open']
    df3 = df3.set_index('date')
    signal_year_count = df3.groupby(lambda x: x.year).size()

    signal_year_std = np.std(signal_year_count)
    signal_year_mean = np.mean(signal_year_count)
    cov = round(signal_year_std / signal_year_mean, 3)

    result_dict['cov'] = cov

    # Win rate by year
    for year in year_list:
        try:
            result_dict[str(year)] = win_rate_dict[year][0]
            result_dict[f'{year}_win_rate'] = win_rate_dict[year][3]

        except Exception as e:
            # print(e)
            result_dict[str(year)] = 0
            result_dict[f'{year}_win_rate'] = '--'

    result_dict['return_to_bah'] = return_on_capital - bah_return

    return result_dict

