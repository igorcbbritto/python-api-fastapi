from fastapi import FastAPI
import psutil
import datetime

app = FastAPI(title="Server Monitoring API")


@app.get("/")
def home():
    return {
        "message": "API de monitoramento funcionando",
        "timestamp": str(datetime.datetime.now())
    }


@app.get("/status")
def server_status():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('C:\\').percent
    }


@app.get("/health")
def health_check():
    return {
        "status": "online"
    }
