import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")

# 如果环境变量没读到，直接报错，防止带病运行
if not DEEPSEEK_API_KEY or not DASHSCOPE_API_KEY:
    raise ValueError("未找到 API Key，请检查 .env 文件是否配置正确！")