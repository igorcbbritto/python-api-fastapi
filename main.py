from fastapi import FastAPI
from datetime import datetime
import psutil

app = FastAPI(
    title="Python System Monitor API",
    description="API simples para monitoramento de recursos do sistema usando FastAPI e psutil",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "API de monitoramento funcionando",
        "timestamp": datetime.now()
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "timestamp": datetime.now()
    }

@app.get("/metrics")
def metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "timestamp": datetime.now()
    }
