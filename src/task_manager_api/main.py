from fastapi import FastAPI
import uvicorn

from task_manager_api.users.routes import router as user_router

app = FastAPI()
app.include_router(user_router)

def main():
    uvicorn.run("main:app", host="0.0.0.0", port=3232, reload=True)

if __name__ == "__main__":
    main()
