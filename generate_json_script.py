import sys
import pandas as pd
import json

if len(sys.argv) != 2:
    print("Usage: python generate_json_script.py <excel_file_path>")
    sys.exit(1)

# 读取 Excel 表格
excel_file_path = sys.argv[1]
df = pd.read_excel(excel_file_path)

# 初始化 JSON 数据
json_data = {
    "globalConfig": {
        "limitSize": "500",
        "block": True
    },
    "specialConfig": {}
}

# 处理每一行数据
for index, row in df.iterrows():
    zip_name = row['zip包名']
    deadline = pd.Timestamp(row['修复完成时间']) if not pd.isna(row['修复完成时间']) else None
    status = str(row['修复状态'])

    # 如果是修复中状态，添加到 specialConfig
    if status == '修复中' and deadline:
        json_data['specialConfig'][zip_name] = {
            "limitSize": "500",
            "block": False,
            "deadline": deadline.strftime("%Y-%m-%d")
        }

# 输出 JSON 数据
json_file_path = 'output.json'  # 替换为你的实际输出路径
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print(f'生成的 JSON 文件保存在 {json_file_path} 中。')
