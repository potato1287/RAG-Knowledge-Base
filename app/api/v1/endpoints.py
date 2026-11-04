from fastapi import APIRouter
from app.schemas.chat import QueryRequest
from app.services.rag_service import create_rag_chain
from app.services.cache_service import cache_service

router = APIRouter()

# 在模块加载时初始化 RAG 链条
rag_chain = create_rag_chain()

@router.post("/chat")
async def chat_with_ai(request: QueryRequest):
    print(f"收到用户提问: {request.query}")
    
    # 1. 查缓存
    cached_answer = cache_service.get(request.query)
    if cached_answer:
        print("命中缓存！直接秒回。")
        return {"code": 200, "message": "success (from cache)", "answer": cached_answer}
    
    # 2. 查大模型
    try:
        print("未命中缓存，正在呼叫大模型...")
        response = rag_chain.invoke(request.query)
        cache_service.set(request.query, response)
        return {"code": 200, "message": "success", "answer": response}
    except Exception as e:
        return {"code": 500, "message": str(e), "answer": "系统繁忙，请稍后再试"}