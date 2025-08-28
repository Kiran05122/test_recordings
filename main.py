from fastapi import FastAPI
from recordings import router as recordings_router

app = FastAPI(title="Recordings API")

# Подключаем роутер
app.include_router(recordings_router)

if name == "main":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
