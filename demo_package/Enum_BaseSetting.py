from enum import Enum

from pydantic_settings import BaseSettings


class Interview(str,Enum):
    WARMUP = "warmup"
    TECH_BASE = "tech_base"
    PROJECT = "project"
    CLOSING = "closing"
    FINISHED = "finished"

class BaseSettingDemo(BaseSettings):
    milvus_host : str = 'localhost'
    milvus_port : int = 19530

if __name__ == '__main__':
    bs = BaseSettingDemo()
    print(bs)
    print(Interview.WARMUP.value)