from ib_insync import *
import decimal

ib = IB()
ib.connect("127.0.0.1", 7496, clientId=4001)

butterfly_limit_price = 6.5
call1_limit_price = 5.2
call2_limit_price = 4.1
call3_limit_price = 3.2


def ab_testAT220():
    butterfly_contract = Contract()
    butterfly_contract.symbol = "AAPL"
    butterfly_contract.secType = "BAG"
    butterfly_contract.currency = "USD"
    butterfly_contract.exchange = "SMART"
    option1 = Option('AAPL', '20200327', 230.0, 'C', 'SMART', tradingClass='AAPL')
    option2 = Option('AAPL', '20200327', 235.0, 'C', 'SMART', tradingClass='AAPL')
    option3 = Option('AAPL', '20200327', 240.0, 'C', 'SMART', tradingClass='AAPL')
    contracts = [option1, option2, option3]
    ib.qualifyContracts(*contracts)

    leg1 = ComboLeg()
    leg1.conId = option1.conId  # DBK JUN 21 2019 CS
    leg1.ratio = 1
    leg1.action = "BUY"
    leg1.exchange = "SMART"
    leg2 = ComboLeg()
    leg2.conId = option2.conId  # DBK MAR 15 2019 C
    leg2.ratio = 2
    leg2.action = "SELL"
    leg2.exchange = "SMART"
    leg3 = ComboLeg()
    leg3.conId = option3.conId  # DBK JUN 21 2019 CS
    leg3.ratio = 1
    leg3.action = "BUY"
    leg3.exchange = "SMART"
    butterfly_contract.comboLegs = []
    butterfly_contract.comboLegs.append(leg1)
    butterfly_contract.comboLegs.append(leg2)
    butterfly_contract.comboLegs.append(leg3)

    print(butterfly_contract)
    ib_butter_order = Order()
    ib_butter_order.orderType = 'SNAP PRIM'
    ib_butter_order.action = 'BUY'
    ib_butter_order.totalQuantity = 3
    i = 0

    spread1_contract = Contract()
    spread1_contract.symbol = "AAPL"
    spread1_contract.secType = "BAG"
    spread1_contract.currency = "USD"
    spread1_contract.exchange = "SMART"
    option1 = Option('AAPL', '20200327', 245.0, 'C', 'SMART', tradingClass='AAPL')
    option2 = Option('AAPL', '20200327', 250.0, 'C', 'SMART', tradingClass='AAPL')
    contracts = [option1, option2]
    ib.qualifyContracts(*contracts)
    leg1 = ComboLeg()
    leg1.conId = option1.conId  # DBK JUN 21 2019 C
    leg1.ratio = 1
    leg1.action = "BUY"
    leg1.exchange = "SMART"
    leg2 = ComboLeg()
    leg2.conId = option2.conId  # DBK MAR 15 2019 C
    leg2.ratio = 1
    leg2.action = "SELL"
    leg2.exchange = "SMART"
    spread1_contract.comboLegs = []
    spread1_contract.comboLegs.append(leg1)
    spread1_contract.comboLegs.append(leg2)
    print(spread1_contract)
    ib_call1_order = Order()
    ib_call1_order.orderType = 'SNAP PRIM'
    ib_call1_order.action = 'BUY'
    ib_call1_order.totalQuantity = 3

    spread2_contract = Contract()
    spread2_contract.symbol = "AAPL"
    spread2_contract.secType = "BAG"
    spread2_contract.currency = "USD"
    spread2_contract.exchange = "SMART"
    option1 = Option('AAPL', '20200327', 255.0, 'C', 'SMART', tradingClass='AAPL')
    option2 = Option('AAPL', '20200327', 260.0, 'C', 'SMART', tradingClass='AAPL')
    contracts = [option1, option2]
    ib.qualifyContracts(*contracts)
    leg1 = ComboLeg()
    leg1.conId = option1.conId  # DBK JUN 21 2019 C
    leg1.ratio = 1
    leg1.action = "BUY"
    leg1.exchange = "SMART"
    leg2 = ComboLeg()
    leg2.conId = option2.conId  # DBK MAR 15 2019 C
    leg2.ratio = 1
    leg2.action = "SELL"
    leg2.exchange = "SMART"
    spread2_contract.comboLegs = []
    spread2_contract.comboLegs.append(leg1)
    spread2_contract.comboLegs.append(leg2)
    print(spread2_contract)
    ib_call2_order = Order()
    ib_call2_order.orderType = 'SNAP PRIM'
    ib_call2_order.action = 'BUY'
    ib_call2_order.totalQuantity = 3

    spread3_contract = Contract()
    spread3_contract.symbol = "AAPL"
    spread3_contract.secType = "BAG"
    spread3_contract.currency = "USD"
    spread3_contract.exchange = "SMART"
    option1 = Option('AAPL', '20200327', 265.0, 'C', 'SMART', tradingClass='AAPL')
    option2 = Option('AAPL', '20200327', 270.0, 'C', 'SMART', tradingClass='AAPL')
    contracts = [option1, option2]
    ib.qualifyContracts(*contracts)
    leg1 = ComboLeg()
    leg1.conId = option1.conId  # DBK JUN 21 2019 C
    leg1.ratio = 1
    leg1.action = "BUY"
    leg1.exchange = "SMART"
    leg2 = ComboLeg()
    leg2.conId = option2.conId  # DBK MAR 15 2019 C
    leg2.ratio = 1
    leg2.action = "SELL"
    leg2.exchange = "SMART"
    spread3_contract.comboLegs = []
    spread3_contract.comboLegs.append(leg1)
    spread3_contract.comboLegs.append(leg2)
    print(spread3_contract)
    ib_call3_order = Order()
    ib_call3_order.orderType = 'SNAP PRIM'
    ib_call3_order.action = 'BUY'
    ib_call3_order.totalQuantity = 3

    ib.reqMarketDataType(3)
    data = ib.reqTickers(butterfly_contract)
    butter_offset = (data[0].ask + data[0].bid) / 2
    butter_delta_offset = (data[0].ask - data[0].bid) / 8
    print('Butterfly Spread Ask price: ', data[0].ask)
    print('Butterfly Spread Bid Price: ', data[0].bid)
    print('Butterfly Spread Mid Price: ', (data[0].ask + data[0].bid) / 2)
    print(butter_offset)
    print(butter_delta_offset)

    ib.reqMarketDataType(3)
    data = ib.reqTickers(spread1_contract)
    call1_offset = (data[0].ask + data[0].bid) / 2
    call1_delta_offset = (data[0].ask - data[0].bid) / 8
    print('Call1 Spread Ask price: ', data[0].ask)
    print('Call1 Spread Bid Price: ', data[0].bid)
    print('Call1 Spread Mid Price: ', (data[0].ask + data[0].bid) / 2)
    print(call1_offset)
    print(call1_delta_offset)

    ib.reqMarketDataType(3)
    data = ib.reqTickers(spread2_contract)
    call2_offset = (data[0].ask + data[0].bid) / 2
    call2_delta_offset = (data[0].ask - data[0].bid) / 8
    print('Call2 Spread Ask price: ', data[0].ask)
    print('Call2 Spread Bid Price: ', data[0].bid)
    print('Call2 Spread Mid Price: ', (data[0].ask + data[0].bid) / 2)
    print(call2_offset)
    print(call2_delta_offset)

    ib.reqMarketDataType(3)
    data = ib.reqTickers(spread3_contract)
    call3_offset = (data[0].ask + data[0].bid) / 2
    call3_delta_offset = (data[0].ask - data[0].bid) / 8
    print('Call3 Spread Ask price: ', data[0].ask)
    print('Call3 Spread Bid Price: ', data[0].bid)
    print('Call3 Spread Mid Price: ', (data[0].ask + data[0].bid) / 2)
    print(call3_offset)
    print(call3_delta_offset)

    butter_flag = True
    call1_flag = True
    call2_flag = True
    call3_flag = True

    while i < 8:
        if butter_flag:
            ib.reqMarketDataType(3)
            data = ib.reqTickers(butterfly_contract)
            c = decimal.Decimal(butter_offset)
            limit_price = data[0].bid + butter_offset
            print('Butterfly Spread Offset Price :', limit_price)
            if limit_price < butterfly_limit_price:
                ib_butter_order.auxPrice = float(round(c, 2))
                butter_trade = ib.placeOrder(butterfly_contract, ib_butter_order)
                ib.sleep(2)
                if butter_trade.orderStatus.status == 'Filled':
                    print('', butter_trade)
                    print('Butterfly Spread Flll Price', butter_trade.orderStatus.lastFillPrice)
                    butter_flag = False
                if butter_trade.orderStatus.status == 'Cancelled':
                    butter_flag = False
            butter_offset += butter_delta_offset

        if call1_flag:
            ib.reqMarketDataType(3)
            data = ib.reqTickers(spread1_contract)
            c = decimal.Decimal(call1_offset)
            limit_price = data[0].bid + call1_offset
            print('Call1 Spread Offset Price :', limit_price)
            if limit_price < call1_limit_price:
                ib_call1_order.auxPrice = float(round(c, 2))
                call1_trade = ib.placeOrder(spread1_contract, ib_call1_order)
                ib.sleep(2)
                if call1_trade.orderStatus.status == 'Filled':
                    print('', call1_trade)
                    print('Call1 Spread Flll Price', call1_trade.orderStatus.lastFillPrice)
                    call1_flag = False
                if call1_trade.orderStatus.status == 'Cancelled':
                    call1_flag = False
            call1_offset += call1_delta_offset

        if call2_flag:
            ib.reqMarketDataType(3)
            data = ib.reqTickers(spread2_contract)
            c = decimal.Decimal(call2_offset)
            limit_price = data[0].bid + call2_offset
            print('Call2 Spread Offset Price :', limit_price)
            if limit_price < call2_limit_price:
                ib_call3_order.auxPrice = float(round(c, 2))
                call2_trade = ib.placeOrder(spread2_contract, ib_call2_order)
                ib.sleep(2)
                if call2_trade.orderStatus.status == 'Filled':
                    print('', call2_trade)
                    print('Call2 Spread Flll Price', call2_trade.orderStatus.lastFillPrice)
                    call2_flag = False
                if call2_trade.orderStatus.status == 'Cancelled':
                    call2_flag = False
            call2_offset += call2_delta_offset

        if call3_flag:
            ib.reqMarketDataType(3)
            data = ib.reqTickers(spread3_contract)
            c = decimal.Decimal(call3_offset)
            limit_price = data[0].bid + call3_offset
            print('Call3 Offset Price :', limit_price)
            if limit_price < call3_limit_price:
                ib_call3_order.auxPrice = float(round(c, 2))
                call3_trade = ib.placeOrder(spread3_contract, ib_call3_order)
                ib.sleep(2)
                if call3_trade.orderStatus.status == 'Filled':
                    print('', call3_trade)
                    print('Call3 Spread Flll Price', call3_trade.orderStatus.lastFillPrice)
                    call3_flag = False
                if call3_trade.orderStatus.status == 'Cancelled':
                    call3_flag = False
            call3_offset += call3_delta_offset

        ib.sleep(2)
        i += 1


if __name__ == '__main__':
    ab_testAT220()
