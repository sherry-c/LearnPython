import akshare as ak

# 获取数据
df = ak.stock_zh_a_hist(
    symbol="600519",        # 股票代码
    period="daily",         # 日线数据
    start_date="20240101",  # 起始日期
    end_date="20250705",    # 结束日期
    adjust="qfq"            # 前复权
)

# 查看前5行
print(df.tail())

# 保存到CSV
df.to_excel("600519.xlsx", index=False)