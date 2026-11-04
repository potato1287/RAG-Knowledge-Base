# 🧠 企业级 RAG 私有知识库问答 API

本项目是一个基于大语言模型（LLM）与检索增强生成（RAG）技术的智能问答后端系统。旨在解决通用大模型在特定业务（如企业内部规章、私有文档）中容易产生“幻觉”的问题，提供标准化、高可用的 API 服务。

## ✨ 核心特性
- **RAG 检索增强**：精准解析本地文档，基于语义检索相关段落，结合 Prompt 约束生成准确回答，拒绝瞎编。
- **企业级架构**：采用标准 FastAPI 分层架构（Router/Service/Schema/Core），高内聚低耦合，易于扩展。
- **性能优化**：接口层引入 TTL 缓存机制，针对高频重复问题实现毫秒级响应，大幅降低 API 调用成本。
- **环境隔离**：使用 `python-dotenv` 管理敏感密钥，确保代码仓库安全。

## 🛠️ 技术栈
- **语言与框架**：Python 3.10+, FastAPI, Pydantic
- **大模型编排**：LangChain
- **模型服务**：DeepSeek API (对话生成), 阿里云 DashScope (文本向量化)
- **向量数据库**：ChromaDB
- **缓存**：Cachetools (TTL Cache)

## 📂 目录结构
```text
├── app/
│   ├── api/v1/         # API 路由层
│   ├── core/           # 核心配置与密钥管理
│   ├── schemas/        # Pydantic 数据校验模型
│   ├── services/       # 业务逻辑层（RAG链路、缓存服务）
│   └── main.py         # FastAPI 实例入口
├── tests/              # 单元测试（预留）
├── .env                # 敏感环境变量（已被 gitignore 忽略）
├── test.txt            # 测试用知识库文档
└── requirements.txt    # 依赖清单