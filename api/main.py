from fastapi import FastAPI ,File , UploadFile
import uvicorn
import nest_asyncio
nest_asyncio.apply()

app = FastAPI()



@app.get("/ping")
async def ping():
    return "Hello : my server  is alive"

@app.post("/ping")
async def predict(
    
    file: UploadFile = File(...)
    
 ):
    pass


if __name__ == "__main__":
    uvcorn.run(app,host = 'localhost', port=8000  )