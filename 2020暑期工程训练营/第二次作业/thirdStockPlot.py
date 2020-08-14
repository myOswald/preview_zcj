def plotScatter(df):
    "绘制散点图，横轴为volume，纵轴为close"

    from matplotlib import pyplot as plt
    
    plt.scatter(df['volume'][::3],df['close'][::3])
    plt.xlabel('Volume')
    plt.ylabel('Share Price')
    plt.title('Volume & Share Price')
    plt.show()

def plotBox(df):
    "绘制箱型图"

    import pandas as pd
    from matplotlib import pyplot as plt

    closedf = pd.DataFrame()
    closedf = pd.concat([closedf,df['close']])
    closedf.columns = ['000001']
    closedf.plot(kind='box')
    plt.ylabel('Share Price')
    plt.title('Boxplot of one stock')
