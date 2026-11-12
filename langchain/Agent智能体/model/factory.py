from abc import ABC, abstractmethod
from typing import Optional
import os
# 1. 导入 Embeddings 基类 (用于类型注解)
from langchain_core.embeddings import Embeddings
# 2. 导入智谱的 Embedding 集成类
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_core.language_models import BaseChatModel
from langchain_deepseek import ChatDeepSeek
from main.config_handler import rag_config
#构建聊天模型工厂和嵌入模型工厂
class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        pass
class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return ChatDeepSeek(model=rag_config["model"], temperature=rag_config["temperature"])
class EmbeddingModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return ZhipuAIEmbeddings(model=rag_config["embeddings_name"], api_key=os.getenv("ZHIPU_API_KEY"))
embedding_model=EmbeddingModelFactory().generator()
chat_model=ChatModelFactory().generator()

