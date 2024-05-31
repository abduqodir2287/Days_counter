from src.presentation.rest.days.router import days_counter_router

from fastapi import FastAPI

app = FastAPI()
app.include_router(days_counter_router)

@app.get("/")
async def hello():
	return {"Message": "Hello world"}

