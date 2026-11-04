from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.core.config import DEEPSEEK_API_KEY, DASHSCOPE_API_KEY

def create_rag_chain():
    print("正在初始化知识库...")
    llm = ChatOpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com/v1", model="deepseek-chat", temperature=0)
    embeddings = DashScopeEmbeddings(dashscope_api_key=DASHSCOPE_API_KEY, model="text-embedding-v2")

    loader = TextLoader("./test.txt", encoding="utf-8")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    prompt = ChatPromptTemplate.from_template("""
    你是一个严谨的助手。请仅根据下面提供的资料来回答问题。
    如果资料中没有答案，请直接说“根据现有资料无法回答”，绝对不要自己编造。
    资料：
    {context}
    问题：{question}
    """)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )