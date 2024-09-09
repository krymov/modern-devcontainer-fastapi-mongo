from fastapi import FastAPI


app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()