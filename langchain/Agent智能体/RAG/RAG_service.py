"""
总结服务类：用户提问，搜索参考资料 将提问和参考资料提交给模型，让模型总结回复
"""
from langchain_core.output_parsers import StrOutputParser
from RAG.vector_store import VectorStoreService
from main.prompt_loader import load_rag_prompts
from langchain_core.prompts import PromptTemplate
from model.factory import chat_model
class RagSummaryService:
    def __init__(self):
        self.vector_store=VectorStoreService()
        self.retriever=self.vector_store.get_retriever()
        self.prompt_text=load_rag_prompts()
        self.prompt_template=PromptTemplate.from_template(template=self.prompt_text)
        self.model=chat_model
        self.chain=self._init_chain()
    def _init_chain(self):
        chain=self.prompt_template|self.model|StrOutputParser()
        return chain
    def retriever_docs(self,query:str):
        return self.retriever.invoke(query)
    def rag_summarize(self,query):
        context_docs=self.retriever_docs(query)
        context=""
        cnt=0
        for doc in context_docs:
            cnt+=1
            context+=f"参考消息{cnt}:{doc.page_content}"
        print("context:",context)
        return self.chain.invoke({
            "input":query,
            "context":context,
        }
        )
if __name__ == '__main__':
    rag=RagSummaryService()
    print(rag.rag_summarize("公司几点上班"))
