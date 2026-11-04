from fastapi import FastAPI
from cachetools import TTLCache
from schemas import QueryRequest
from rag_core import create_rag_chain

# 初始化 FastAPI
app = FastAPI(title="企业知识库 AI 助手 API")

# 在服务启动时，初始化 RAG 链条（全局调用一次）
print("正在启动服务，加载模型...")
rag_chain = create_rag_chain()

# 初始化缓存
cache = TTLCache(maxsize=100, ttl=3600)

@app.post("/chat")
async def chat_with_ai(request: QueryRequest):
    print(f"收到用户提问: {request.query}")
    
    # 1. 查缓存
    if request.query in cache:
        print("命中缓存！直接秒回。")
        return {"code": 200, "message": "success (from cache)", "answer": cache[request.query]}
    
    # 2. 查大模型
    try:
        print("未命中缓存，正在呼叫大模型...")
        response = rag_chain.invoke(request.query)
        cache[request.query] = response
        return {"code": 200, "message": "success", "answer": response}
    except Exception as e:
        return {"code": 500, "message": str(e), "answer": "系统繁忙，请稍后再试"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)