import pandas as pd
import os

# 1. 定义Excel文件路径
excel_path = "data/600519.xlsx"  # 假设文件与脚本同目录，否则需写绝对路径（如"C:/data/600519.xlsx"）

# 2. 检查文件是否存在
if not os.path.exists(excel_path):
    raise FileNotFoundError(f"文件 {excel_path} 不存在，请检查路径")

df = None
# 3. 读取Excel文件并处理可能的异常
try:
    # 使用pandas读取Excel，指定引擎为openpyxl（兼容.xlsx格式）
    df = pd.read_excel(excel_path, engine='openpyxl')

    # 4. 数据预处理（可选）
    # - 将日期列转为datetime类型（如果列名是"日期"）
    if '日期' in df.columns:
        df['日期'] = pd.to_datetime(df['日期'])

    # - 检查关键列是否存在
    required_columns = ['开盘', '收盘', '成交量']
    for col in required_columns:
        if col not in df.columns:
            print(f"警告：缺失关键列 {col}，数据可能不完整")

    # 5. 打印数据信息
    print(f"成功读取数据，共 {len(df)} 行")
    print(df.tail())  # 显示最后5行

except Exception as e:
    print(f"读取文件时出错: {e}")
    # 可根据具体错误类型细化处理（如ValueError、PermissionError等）

# 6. 使用数据示例（计算5日均线）
if not df.empty and '收盘' in df.columns:
    df['5日均线'] = df['收盘'].rolling(window=5).mean()
    print("\n添加5日均线后的数据：")
    # print(df[['日期', '收盘', '5日均线']].tail())
    print(df.tail())
