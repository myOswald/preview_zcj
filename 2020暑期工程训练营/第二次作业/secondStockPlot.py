def plotContrast(df):
    "对比两只股票close的变化"

    from matplotlib import pyplot as plt
    import pandas as pd

    df['trade_date'] = pd.to_datetime(df.pop('trade_date'), format='%Y%m%d')
    sz1 = df[::2].set_index('trade_date')  # 第一支股票
    sz2 = df[1::2].set_index('trade_date')  # 第二支股票
    fig,ax = plt.subplots()
    sz1.plot(ax=ax,y='close',label='000001.SZ')
    sz2.plot(ax=ax,y='close',label='000002.SZ')
    plt.ylabel('Share Price')
    plt.title('The contrast of tow stocks')
    plt.legend(loc='upper right')

def plotKline(sz):
    "绘制k线图，红色表示下跌，绿色表示上涨"

    from matplotlib import pyplot as plt
    sz = sz[::2]  # 绘制第一支股票的k线图
    fig,ax = plt.subplots()
    thick_width = 0.7
    thin_width = 0.1
    price_up = sz[sz['close'] >= sz['open']]  # 股票价格上涨
    price_down = sz[sz['close'] < sz['open']]  # 股票价格下跌

    plt.bar(price_up['trade_date'],price_up['close'] - price_up['open'],thick_width,bottom=price_up['open'],color='g')
    plt.bar(price_up['trade_date'],price_up['high'] - price_up['close'],thin_width,bottom=price_up['close'],color='g')
    plt.bar(price_up['trade_date'],price_up['low'] - price_up['open'],thin_width,bottom=price_up['open'],color='g')

    plt.bar(price_down['trade_date'],price_down['open'] - price_down['close'],thick_width,bottom=price_down['close'],color='r')
    plt.bar(price_down['trade_date'],price_down['high'] - price_down['open'],thin_width,bottom=price_down['open'],color='r')
    plt.bar(price_down['trade_date'],price_down['low'] - price_down['close'],thin_width,bottom=price_down['close'],color='r')

    plt.ylabel('Price')
    plt.title('k plot of one stock')
    fig.autofmt_xdate()
    fig.tight_layout()

    plt.show()
