from pydantic import BaseModel, Field
from typing import Annotated
from fastapi import FastAPI
app = FastAPI()

class User(BaseModel):
    # username: str = Field(..., min_length=3, max_length=50)
    # password: str = Field(..., min_length=8, max_length=50)
    username: Annotated[str, Field(min_length=3, max_length=10,description="用户名 3-10位")]
    password: Annotated[int, Field(min_length=8, max_length=10,description="密码 8-10位")]
@app.post("/register")
async def create_user(user: User):
    return {"username": user.username, "password": user.password}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
