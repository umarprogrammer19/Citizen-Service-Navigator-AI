from fastapi import FastAPI
from routers import eligibility_router

app = FastAPI()

app.include_router(eligibility_router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Citizen Service Navigator AI API!"}
