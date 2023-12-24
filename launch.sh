#!/bin/bash

# 检查是否已安装 pip3
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 not found. Please install pip3 before running this script."
    exit 1
fi

# 定义依赖库
dependencies=("pandas" "openpyxl")  # 添加 openpyxl

# 检查并安装缺失的依赖库
for dependency in "${dependencies[@]}"; do
    if ! pip3 show $dependency &> /dev/null; then
        echo "Installing $dependency..."
        pip3 install $dependency
    else
        echo "$dependency is already installed."
    fi
done

# 获取 Excel 文件路径
excel_file_path="your_excel_file.xlsx"  # 替换为你的实际 Excel 文件路径

# 执行 Python3 脚本，并传递 Excel 文件路径作为参数
python3 generate_json_script.py "$excel_file_path"
