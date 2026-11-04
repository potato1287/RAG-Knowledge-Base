from fastapi import FastAPI
from app.api.v1.endpoints import router as v1_router

app = FastAPI(title="企业知识库 AI 助手 API", version="1.0.0")

# 挂载 v1 版本的路由
app.include_router(v1_router, prefix="/api/v1", tags=["Chat"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)