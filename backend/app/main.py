from fastapi import FastAPI

app = FastAPI(
    title="Event Management API",
    description="API pour la gestion d'événements et d'inscriptions",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Event Management API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
