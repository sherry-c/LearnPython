import akshare as ak
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta
import matplotlib

# 设置中文字体（根据系统选择）
matplotlib.rcParams["font.family"] = "SimHei"  # Windows
# matplotlib.rcParams["font.family"] = "Heiti SC"  # macOS
# matplotlib.rcParams["font.family"] = "WenQuanYi Zen Hei"  # Linux

# 解决负号显示为方块的问题
matplotlib.rcParams["axes.unicode_minus"] = False

# 1. 获取贵州茅台前复权数据（2020-2025年）
def get_stock_data():
    df = ak.stock_zh_a_hist(
        symbol="600519",
        period="daily",
        start_date="20200101",
        end_date="20250701",  # 使用当前日期
        adjust="qfq"  # 前复权处理除权除息
    )
    # 数据清洗与格式化
    df['日期'] = pd.to_datetime(df['日期'])
    df.set_index('日期', inplace=True)
    df.rename(columns={'收盘': 'close', '成交量': 'volume'}, inplace=True)
    return df[['close', 'volume']]


# 2. 计算技术指标和交易信号
def calculate_signals(df):
    # 计算60日均线
    df['ma60'] = df['close'].rolling(window=60).mean()

    # 计算5日成交量均值
    df['vol_ma5'] = df['volume'].rolling(window=5).mean()

    # 识别突破信号（收盘价>60日均线且前一日≤均线）
    df['breakout'] = (df['close'] > df['ma60']) & (df['close'].shift(1) <= df['ma60'].shift(1))

    # 识别成交量放大（当日成交量>5日均量1.5倍）
    df['volume_spike'] = df['volume'] > 1.5 * df['vol_ma5']

    # 综合买入信号
    df['buy_signal'] = df['breakout'] & df['volume_spike']

    # 计算20日后涨跌幅
    df['future_close'] = df['close'].shift(-20)
    df['20d_return'] = (df['future_close'] - df['close']) / df['close']

    return df.dropna()


# 3. 策略回测与统计
def backtest_strategy(df):
    # 提取所有买入信号点
    buy_points = df[df['buy_signal']].copy()

    # 统计基本结果
    win_rate = len(buy_points[buy_points['20d_return'] > 0]) / len(buy_points)
    avg_return = buy_points['20d_return'].mean()
    max_gain = buy_points['20d_return'].max()
    max_loss = buy_points['20d_return'].min()

    print(f"信号出现次数: {len(buy_points)}次")
    print(f"胜率: {win_rate:.2%}")
    print(f"平均收益率: {avg_return:.2%}")
    print(f"最大盈利: {max_gain:.2%} | 最大亏损: {max_loss:.2%}")

    return buy_points


# 4. 可视化结果
def visualize_results(df, buy_points):
    plt.figure(figsize=(14, 8))

    # 绘制价格和均线
    plt.plot(df.index, df['close'], label='贵州茅台收盘价', alpha=0.8)
    plt.plot(df.index, df['ma60'], label='60日均线', color='orange', linestyle='--')

    # 标记买入点
    plt.scatter(buy_points.index,
                buy_points['close'],
                color='red', s=80, marker='^',
                label='买入信号')

    # 添加20日后的价格标记
    for date, row in buy_points.iterrows():
        future_date = date + timedelta(days=20)
        future_price = row['future_close']
        color = 'green' if future_price > row['close'] else 'maroon'

        plt.plot([date, future_date],
                 [row['close'], future_price],
                 color=color, alpha=0.4)
        plt.scatter(future_date, future_price, color=color, s=60)

    # 设置图表格式
    plt.title('贵州茅台突破60日均线+成交量放大策略回测 (2020-2025)', fontsize=14)
    plt.xlabel('日期')
    plt.ylabel('价格（前复权）')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.tight_layout()
    plt.show()


# 主流程
if __name__ == "__main__":
    # 获取并处理数据
    stock_data = get_stock_data()
    processed_data = calculate_signals(stock_data)

    # 回测并显示统计结果
    signal_points = backtest_strategy(processed_data)

    # 可视化结果
    visualize_results(processed_data, signal_points)