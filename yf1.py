from datetime import datetime
import pandas as pd
import yfinance as yf
from wallstreet import Stock, Call, Put
import argparse


def main():
    parser = argparse.ArgumentParser(description="Find best trading strategies")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("ticker", type=str,
                        help="stock ticker")
    # group.add_argument("-t", "--ticker", action="store_true")
    group.add_argument("-d", "--date", action="store_true")
    parser.add_argument("-s", "--strategy", help="the strategy")
    # parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()

    ticker = yf.Ticker(args.ticker)

    # get stock info
    print('****** Info **********')
    print(ticker.info)
    # input("Press Enter to continue...")

    # get historical market data
    print('****** History **********')
    hist = ticker.history(period="max")
    print(hist)
    # input("Press Enter to continue...")

    print('****** Actions **********')
    # show actions (dividends, splits)
    print(ticker.actions)
    # input("Press Enter to continue...")

    print('****** dividends **********')
    # show dividends
    print(ticker.dividends)
    # input("Press Enter to continue...")

    # show splits
    ticker.splits

    # show financials
    print('****** financials **********')
    print(ticker.financials)
    print(ticker.quarterly_financials)
    # input("Press Enter to continue...")

    # show major holders
    print(ticker.major_holders)

    # show institutional holders
    print(ticker.institutional_holders)
    # input("Press Enter to continue...")
    # show balance heet
    print(ticker.balance_sheet)
    print(ticker.quarterly_balance_sheet)

    # show cashflow
    ticker.cashflow
    ticker.quarterly_cashflow

    # show earnings
    print(ticker.earnings)
    print(ticker.quarterly_earnings)

    # show sustainability
    print(ticker.sustainability)

    # show analysts recommendations
    print(ticker.recommendations)

    # show next event (earnings, etc)
    print('****** calendars **********')
    print(ticker.calendar)
    # input("Press Enter to continue...")

    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    print(ticker.isin)

    # show options expirations
    print('****** calendars **********')
    print(ticker.options)
    # input("Press Enter to continue...")
    # get option chain for specific expiration
    opt = ticker.option_chain(ticker.options[0])
    # data available via: opt.calls, opt.puts
    print(opt.calls)
    # input("Press Enter to continue...")
    print(opt.puts)
    # input("Press Enter to continue...")
    history = ticker.history()
    last_quote = (history.tail(1)['Close'].iloc[0])
    last_price = int(last_quote)
    # calls
    for opt in ticker.options:
        try:
            data = []
            dt = datetime.fromisoformat(opt)
            option = Call(args.ticker)  # d=dt.day, m=dt.month, y=dt.year, strike=ticker.)
            for strike in option.strikes:
                if strike < last_price - 40 or strike > last_price + 25:
                    continue
                print(f'strike = {strike}')
                option.set_strike(strike)
                item = {}
                item['strike'] = strike
                item['price'] = option.price
                item['iv'] = option.implied_volatility()
                item['delta'] = option.delta()
                item['vega'] = option.vega()
                item['gamma'] = option.gamma()
                # print(f'theta = {option.theta()}')
                # print(f'vega = {option.vega()}')
                data.append(item)
            dataframe = pd.DataFrame(data)
            dataframe.to_csv(f'call-{args.ticker}-{dt}')
            print(dataframe.to_csv())
        except Exception as e:
            print (f'{type(e)}: {str(e)} ')
            continue

        # put
        for opt in ticker.options:
            try:
                data = []
                dt = datetime.fromisoformat(opt)
                option = Put(args.ticker)  # d=dt.day, m=dt.month, y=dt.year, strike=ticker.)
                for strike in option.strikes:
                    if strike < last_price - 40 or strike > last_price + 25:
                        continue
                    print(f'strike = {strike}')
                    option.set_strike(strike)
                    item = {}
                    item['strike'] = strike
                    item['price'] = option.price
                    item['iv'] = option.implied_volatility()
                    item['delta'] = option.delta()
                    item['vega'] = option.vega()
                    item['gamma'] = option.gamma()
                    # print(f'Rho = {option.rho()}')
                    # print(f'type = {option.Option_type}')
                    # print(f'theta = {option.theta()}')
                    # print(f'vega = {option.vega()}')
                    data.append(item)
                dataframe = pd.DataFrame(data)
                dataframe.to_csv(f'put-{args.ticker}-{dt}')
                print(dataframe.to_csv())
            except Exception as e:
                print(f'{type(e)}: {str(e)} ')
                continue




if __name__ == '__main__':
    main()
