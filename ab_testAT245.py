from ib_insync import *
import decimal
#
# ib = IB()
# ib.connect("127.0.0.1", 7496, clientId=4001)

butterfly_max_limit_price = 6.5
call1_max_limit_price = 9.2
call2_max_limit_price = 5.1
call3_max_limit_price = 3.2

expiration_date = '20200409'

butter_strike1 = 245
butter_strike2 = 250
butter_strike3 = 255
butter_quantity1 = 1
butter_quantity2 = 2
butter_quantity3 = 1
butter_type1 = 'PUT'
butter_type2 = 'PUT'
butter_type3 = 'PUT'
butter_action1 = 'BUY'
butter_action2 = 'SELL'
butter_action3 = 'BUY'
butter_spread_action = 'BUY'
butter_spread_quantity = 3

call1_strike1 = 260
call1_strike2 = 265
call1_quantity1 = 1
call1_quantity2 = 1
call1_type1 = 'PUT'
call1_type2 = 'PUT'
call1_action1 = 'BUY'
call1_action2 = 'SELL'
call1_spread_action = 'BUY'
call1_spread_quantity = 3

call2_strike1 = 270
call2_strike2 = 275
call2_quantity1 = 1
call2_quantity2 = 1
call2_type1 = 'PUT'
call2_type2 = 'PUT'
call2_action1 = 'BUY'
call2_action2 = 'SELL'
call2_spread_action = 'BUY'
call2_spread_quantity = 3

call3_strike1 = 280
call3_strike2 = 285
call3_quantity1 = 1
call3_quantity2 = 1
call3_type1 = 'PUT'
call3_type2 = 'PUT'
call3_action1 = 'BUY'
call3_action2 = 'SELL'
call3_spread_action = 'BUY'
call3_spread_quantity = 3

global_min_offset = 0.05
global_max_offset = 2.0


def ab_testAT245(ib):
    butterfly_contract = Contract()
    butterfly_contract.symbol = "AAPL"
    butterfly_contract.secType = "BAG"
    butterfly_contract.currency = "USD"
    butterfly_contract.exchange = "SMART"
    option1 = Option('AAPL', expiration_date, butter_strike1, butter_type1, 'SMART', tradingClass='AAPL')
    option2 = Option('AAPL', expiration_date, butter_strike2, butter_type2, 'SMART', tradingClass='AAPL')
    option3 = Option('AAPL', expiration_date, butter_strike3, butter_type3, 'SMART', tradingClass='AAPL')
    contracts = [option1, option2, option3]
    ib.qualifyContracts(*contracts)

    leg1 = ComboLeg()
    leg1.conId = option1.conId  # DBK JUN 21 2019 CS
    leg1.ratio = butter_quantity1
    leg1.action = butter_action1
    leg1.exchange = "SMART"
    leg2 = ComboLeg()
    leg2.conId = option2.conId  # DBK MAR 15 2019 C
    leg2.ratio = butter_quantity2
    leg2.action = butter_action2
    leg2.exchange = "SMART"
    leg3 = ComboLeg()
    leg3.conId = option3.conId  # DBK JUN 21 2019 CS
    leg3.ratio = butter_quantity3
    leg3.action = butter_action3
    leg3.exchange = "SMART"
    butterfly_contract.comboLegs = []
    butterfly_contract.comboLegs.append(leg1)
    butterfly_contract.comboLegs.append(leg2)
    butterfly_contract.comboLegs.append(leg3)

    print(butterfly_contract)
    ib_butter_order = Order()
    ib_butter_order.orderType = 'SNAP PRIM'
    ib_butter_order.action = butter_spread_action
    ib_butter_order.totalQuantity = butter_spread_quantity
    i = 0

    spread1_contract = Contract()
    spread1_contract.symbol = "AAPL"
    spread1_contract.secType = "BAG"
    spread1_contract.currency = "USD"
    spread1_contract.exchange = "SMART"
    option1 = Option('AAPL', expiration_date, call1_strike1, call1_type1, 'SMART', tradingClass='AAPL')
    option2 = Option('AAPL', expiration_date, call1_strike2, call1_type2, 'SMART', tradingClass='AAPL')
    contracts = [option1, option2]
    ib.qualifyContracts(*contracts)
    leg1 = ComboLeg()
    leg1.conId = option1.conId  # DBK JUN 21 2019 C
    leg1.ratio = call1_quantity1
    leg1.action = call1_action1
    leg1.exchange = "SMART"
    leg2 = ComboLeg()
    leg2.conId = option2.conId  # DBK MAR 15 2019 C
    leg2.ratio = call1_quantity2
    leg2.action = call1_action2
    leg2.exchange = "SMART"
    spread1_contract.comboLegs = []
    spread1_contract.comboLegs.append(leg1)
    spread1_contract.comboLegs.append(leg2)
    print(spread1_contract)
    ib_call1_order = Order()
    ib_call1_order.orderType = 'SNAP PRIM'
    ib_call1_order.action = call1_spread_action
    ib_call1_order.totalQuantity = call1_spread_quantity

    spread2_contract = Contract()
    spread2_contract.symbol = "AAPL"
    spread2_contract.secType = "BAG"
    spread2_contract.currency = "USD"
    spread2_contract.exchange = "SMART"
    option1 = Option('AAPL', expiration_date, call2_strike1, call2_type1, 'SMART', tradingClass='AAPL')
    option2 = Option('AAPL', expiration_date, call2_strike2, call2_type2, 'SMART', tradingClass='AAPL')
    contracts = [option1, option2]
    ib.qualifyContracts(*contracts)
    leg1 = ComboLeg()
    leg1.conId = option1.conId  # DBK JUN 21 2019 C
    leg1.ratio = call2_quantity1
    leg1.action = call2_action1
    leg1.exchange = "SMART"
    leg2 = ComboLeg()
    leg2.conId = option2.conId  # DBK MAR 15 2019 C
    leg2.ratio = call2_quantity2
    leg2.action = call2_action2
    leg2.exchange = "SMART"
    spread2_contract.comboLegs = []
    spread2_contract.comboLegs.append(leg1)
    spread2_contract.comboLegs.append(leg2)
    print(spread2_contract)
    ib_call2_order = Order()
    ib_call2_order.orderType = 'SNAP PRIM'
    ib_call2_order.action = call2_spread_action
    ib_call2_order.totalQuantity = call2_spread_quantity

    spread3_contract = Contract()
    spread3_contract.symbol = "AAPL"
    spread3_contract.secType = "BAG"
    spread3_contract.currency = "USD"
    spread3_contract.exchange = "SMART"
    option1 = Option('AAPL', expiration_date, call3_strike1, call3_type1, 'SMART', tradingClass='AAPL')
    option2 = Option('AAPL', expiration_date, call3_strike2, call3_type2, 'SMART', tradingClass='AAPL')
    contracts = [option1, option2]
    ib.qualifyContracts(*contracts)
    leg1 = ComboLeg()
    leg1.conId = option1.conId  # DBK JUN 21 2019 C
    leg1.ratio = call3_quantity1
    leg1.action = call3_action1
    leg1.exchange = "SMART"
    leg2 = ComboLeg()
    leg2.conId = option2.conId  # DBK MAR 15 2019 C
    leg2.ratio = call2_quantity2
    leg2.action = call2_action2
    leg2.exchange = "SMART"
    spread3_contract.comboLegs = []
    spread3_contract.comboLegs.append(leg1)
    spread3_contract.comboLegs.append(leg2)
    print(spread3_contract)
    ib_call3_order = Order()
    ib_call3_order.orderType = 'SNAP PRIM'
    ib_call3_order.action = call3_spread_action
    ib_call3_order.totalQuantity = call3_spread_quantity


    ib.reqMarketDataType(4)
    butter_data = ib.reqTickers(butterfly_contract)
    butter_offset = (butter_data[0].ask + butter_data[0].bid) / 2
    if butter_offset < global_min_offset:
        butter_offset = global_min_offset
    if butter_offset > global_max_offset:
        butter_offset = global_max_offset
    butter_delta_offset = (butter_data[0].ask - butter_data[0].bid) / 8
    print("Butterfly (+{} {}{}, -{} {}{}, +{} {}{})".format(butter_quantity1, butter_strike1, butter_type1,
                                                            butter_quantity2, butter_strike2, butter_type2,
                                                            butter_quantity3, butter_strike3, butter_type3))
    print('Butterfly max limit price:', butterfly_max_limit_price)
    print('Butterfly Spread Ask price: ', butter_data[0].ask)
    print('Butterfly Spread Bid Price: ', butter_data[0].bid)
    print('Butterfly Spread Mid Price: ', (butter_data[0].ask + butter_data[0].bid) / 2)
    print('Butterfly offset:', butter_offset)
    print('Butterfly delta offset: ', butter_delta_offset)

    ib.reqMarketDataType(4)
    call1_data = ib.reqTickers(spread1_contract)
    call1_offset = (call1_data[0].ask + call1_data[0].bid) / 2
    if call1_offset < global_min_offset:
        call1_offset = global_min_offset
    if call1_offset > global_max_offset:
        call1_offset = global_max_offset
    call1_delta_offset = (call1_data[0].ask - call1_data[0].bid) / 8
    print(
        "Call1 (+{} {}{}, -{} {}{})".format(call1_quantity1, call1_strike1, call1_type1, call1_quantity2, call1_strike2,
                                            call1_type2))
    print('Call1 max limit price:', call1_max_limit_price)
    print('Call1 Spread Ask price: ', call1_data[0].ask)
    print('Call1 Spread Bid Price: ', call1_data[0].bid)
    print('Call1 Spread Mid Price: ', (call1_data[0].ask + call1_data[0].bid) / 2)
    print('Call1 offset:', call1_offset)
    print('Call1 delta offset: ', call1_delta_offset)

    ib.reqMarketDataType(4)
    call2_data = ib.reqTickers(spread2_contract)
    call2_offset = (call2_data[0].ask + call2_data[0].bid) / 2
    if call2_offset < global_min_offset:
        call2_offset = global_min_offset
    if call2_offset > global_max_offset:
        call2_offset = global_max_offset
    call2_delta_offset = (call2_data[0].ask - call2_data[0].bid) / 8
    print(
        "Call2 (+{} {}{}, -{} {}{})".format(call2_quantity1, call2_strike1, call2_type1, call2_quantity2, call2_strike2,
                                            call2_type2))
    print('Call2 max limit price:', call2_max_limit_price)
    print('Call2 Spread Ask price: ', call2_data[0].ask)
    print('Call2 Spread Bid Price: ', call2_data[0].bid)
    print('Call2 Spread Mid Price: ', (call2_data[0].ask + call2_data[0].bid) / 2)
    print('Call2 offset:', call2_offset)
    print('Call2 delta offset: ', call2_delta_offset)

    ib.reqMarketDataType(4)
    call3_data = ib.reqTickers(spread3_contract)
    call3_offset = (call3_data[0].ask + call3_data[0].bid) / 2
    if call3_offset < global_min_offset:
        call3_offset = global_min_offset
    if call3_offset > global_max_offset:
        call3_offset = global_max_offset
    call3_delta_offset = (call3_data[0].ask - call3_data[0].bid) / 8
    print(
        "Call3 (+{} {}{}, -{} {}{})".format(call3_quantity1, call3_strike1, call3_type1, call3_quantity2, call3_strike2,
                                            call3_type2))
    print('Call3 max limit price:', call3_max_limit_price)
    print('Call3 Spread Ask price: ', call3_data[0].ask)
    print('Call3 Spread Bid Price: ', call3_data[0].bid)
    print('Call3 Spread Mid Price: ', (call3_data[0].ask + call3_data[0].bid) / 2)
    print('Call3 offset:', call3_offset)
    print('Call3 delta offset: ', call3_delta_offset)

    butter_flag = True
    call1_flag = True
    call2_flag = True
    call3_flag = True
    butter_trade = ''
    call1_trade = ''
    call2_trade = ''
    call3_trade = ''
    while i < 10:
        if butter_flag:
            c = decimal.Decimal(butter_offset)
            limit_price = butter_data[0].bid + butter_offset
            print('Butterfly Spread Limit Price :', limit_price)
            if limit_price < butterfly_max_limit_price:
                ib_butter_order.auxPrice = float(round(c, 2))
                if butter_trade == '':
                    butter_trade = ib.placeOrder(butterfly_contract, ib_butter_order)
                    ib.sleep(2)
                    if butter_trade.orderStatus.status == 'Filled':
                        print('', butter_trade)
                        print('************BUTTERFLY SPREAD Flll PRICE: ', butter_trade.orderStatus.lastFillPrice)
                        butter_flag = False
                    if butter_trade.orderStatus.status == 'Cancelled':
                        butter_flag = False
                else:
                    if butter_trade.orderStatus.status == 'Filled':
                        print('************BUTTERFLY SPREAD Flll PRICE: ', butter_trade.orderStatus.lastFillPrice)
                        butter_flag = False
                    elif butter_trade.orderStatus.status == 'Cancelled':
                        butter_flag = False
                    else:
                        butter_trade = ib.placeOrder(butterfly_contract, ib_butter_order)
                        ib.sleep(2)
                        if butter_trade.orderStatus.status == 'Filled':
                            print('************BUTTERFLY SPREAD Flll PRICE: ', butter_trade.orderStatus.lastFillPrice)
                            butter_flag = False
                        if butter_trade.orderStatus.status == 'Cancelled':
                            butter_flag = False
            butter_offset += butter_delta_offset

        if call1_flag:
            c = decimal.Decimal(call1_offset)
            limit_price = call1_data[0].bid + call1_offset
            print('Call1 Spread Limit Price :', limit_price)
            if limit_price < call1_max_limit_price:
                ib_call1_order.auxPrice = float(round(c, 2))
                if call1_trade == '':
                    call1_trade = ib.placeOrder(spread1_contract, ib_call1_order)
                    ib.sleep(2)
                    if call1_trade.orderStatus.status == 'Filled':
                        print('************CALL1 SPREAD Flll PRICE', call1_trade.orderStatus.lastFillPrice)
                        call1_flag = False
                    if call1_trade.orderStatus.status == 'Cancelled':
                        call1_flag = False
                else:
                    if call1_trade.orderStatus.status == 'Filled':
                        print('************CALL1 SPREAD Flll PRICE', call1_trade.orderStatus.lastFillPrice)
                        call1_flag = False
                    elif call1_trade.orderStatus.status == 'Cancelled':
                        call1_flag = False
                    else:
                        call1_trade = ib.placeOrder(spread1_contract, ib_call1_order)
                        ib.sleep(2)
                        if call1_trade.orderStatus.status == 'Filled':
                            print('************CALL1 SPREAD Flll PRICE', call1_trade.orderStatus.lastFillPrice)
                            call1_flag = False
                        if call1_trade.orderStatus.status == 'Cancelled':
                            call1_flag = False
            call1_offset += call1_delta_offset

        if call2_flag:
            c = decimal.Decimal(call2_offset)
            limit_price = call2_data[0].bid + call2_offset
            print('Call2 Spread Limit Price :', limit_price)
            if limit_price < call2_max_limit_price:
                ib_call2_order.auxPrice = float(round(c, 2))
                if call2_trade == '':
                    call2_trade = ib.placeOrder(spread2_contract, ib_call2_order)
                    ib.sleep(2)
                    if call2_trade.orderStatus.status == 'Filled':
                        print('************CALL2 SPREAD Flll PRICE', call2_trade.orderStatus.lastFillPrice)
                        call2_flag = False
                    if call2_trade.orderStatus.status == 'Cancelled':
                        call2_flag = False
                else:
                    if call2_trade.orderStatus.status == 'Filled':
                        print('************CALL2 SPREAD Flll PRICE', call2_trade.orderStatus.lastFillPrice)
                        call2_flag = False
                    elif call2_trade.orderStatus.status == 'Cancelled':
                        call2_flag = False
                    else:
                        call2_trade = ib.placeOrder(spread2_contract, ib_call2_order)
                        ib.sleep(2)
                        if call2_trade.orderStatus.status == 'Filled':
                            print('************CALL2 SPREAD Flll PRICE', call2_trade.orderStatus.lastFillPrice)
                            call2_flag = False
                        if call2_trade.orderStatus.status == 'Cancelled':
                            call2_flag = False
            call2_offset += call2_delta_offset

        if call3_flag:
            c = decimal.Decimal(call3_offset)
            limit_price = call3_data[0].bid + call3_offset
            print('Call3 Spread Limit Price :', limit_price)
            if limit_price < call3_max_limit_price:
                ib_call3_order.auxPrice = float(round(c, 2))
                if call3_trade == '':
                    call3_trade = ib.placeOrder(spread3_contract, ib_call3_order)
                    ib.sleep(2)
                    if call3_trade.orderStatus.status == 'Filled':
                        print('************CALL3 SPREAD Flll PRICE', call3_trade.orderStatus.lastFillPrice)
                        call3_flag = False
                    if call3_trade.orderStatus.status == 'Cancelled':
                        call3_flag = False
                else:
                    if call3_trade.orderStatus.status == 'Filled':
                        print('************CALL3 SPREAD Flll PRICE', call3_trade.orderStatus.lastFillPrice)
                        call3_flag = False
                    elif call3_trade.orderStatus.status == 'Cancelled':
                        call3_flag = False
                    else:
                        call3_trade = ib.placeOrder(spread3_contract, ib_call3_order)
                        ib.sleep(2)
                        if call3_trade.orderStatus.status == 'Filled':
                            print('************CALL3 SPREAD Flll PRICE', call3_trade.orderStatus.lastFillPrice)
                            call3_flag = False
                        if call3_trade.orderStatus.status == 'Cancelled':
                            call3_flag = False
            call3_offset += call3_delta_offset
        ib.sleep(2)
        i += 1


# if __name__ == '__main__':
#     ab_test()
