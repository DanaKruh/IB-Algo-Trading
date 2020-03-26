from ib_insync import *
from ab_testAT235 import ab_testAT235
from ab_testAT240 import ab_testAT240
from ab_testAT245 import ab_testAT245
from ab_testAT250 import ab_testAT250
from ab_testAT255 import ab_testAT255
from ab_testAT260 import ab_testAT260

from datetime import datetime
import dateutil.parser
import time

def main():
    end_time = '2020-03-26 17:57'
    ib = IB()
    ib.connect("127.0.0.1", 7496, clientId=4001)
    endDateTime = dateutil.parser.parse(end_time, ignoretz=True)  # convert string to datetime.
    while datetime.now() < endDateTime:
        stock_contract = Stock('AAPL', 'SMART', 'USD')  # create contract
        ib.qualifyContracts(stock_contract)  # it makes the contract with unique id
        ib.reqMarketDataType(3)  # wait for reqTickers value
        market_ticker = ib.reqTickers(stock_contract)  # Get ticker data
        stock_price = market_ticker[0].last  # Stock Price

        print('Stcok Price:', stock_price)
        if 240 > stock_price > 235:
            ab_testAT235(ib)
        elif 245 > stock_price > 240:
            ab_testAT240(ib)
        elif 250 > stock_price > 245:
            ab_testAT245(ib)
        elif 255 > stock_price > 250:
            ab_testAT250(ib)
        elif 260 > stock_price > 255:
            ab_testAT255(ib)
        elif stock_price > 260:
            ab_testAT260(ib)

        time.sleep(60)  # every 1min   1min = 60s
    ib.disconnect()


if __name__ == '__main__':
    main()
