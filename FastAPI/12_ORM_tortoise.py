from typing import Dict
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
app = FastAPI()



TORTOISE_ORM: Dict = {
    "connections": {
        # 开发环境使用 SQLite（基于文件，无需服务器）
        # "default": "sqlite://db.sqlite3",
        # 生产环境示例: PostgreSQL
        # "default": "postgres://user:password@localhost:5432/dbname",
        # 生产环境示例: MySQL
        "default": "mysql://root:331721@127.0.0.1:3306/fastapi_db",
    },
    "apps": {
        "models": {
            "models": ["aerich.models"],  # 模型模块和 Aerich 迁移模型
            "default_connection": "default",#默认链接
        }
    },
    # 连接池配置（推荐）
    "use_tz": False,  # 是否使用时区
    "timezone": "UTC",  # 默认时区
    "db_pool": {
        "max_size": 10,  # 最大连接数
        "min_size": 1,   # 最小连接数
        "idle_timeout": 30  # 空闲连接超时（秒）
    }
}

register_tortoise(app,
                  config=TORTOISE_ORM,
                  generate_schemas=True,        #生成表结构
                  add_exception_handlers=True   #异常处理打开
                  )
if __name__=="__main__":
    import uvicorn
    uvicorn.run("12_ORM_tortoise:app", host="127.0.0.1", port=8080, reload=True)
