"""API contract scaffold. No uploads, storage or inference implemented."""
from fastapi import FastAPI, HTTPException

app = FastAPI(title="KrishiDhwani — scaffold", version="0.0.1")

@app.get("/health")
def health():
    return {"status": "scaffold", "inference_ready": False}

def pending():
    raise HTTPException(status_code=501, detail="Scaffold only: feature not implemented")

@app.post("/audio")
def upload_audio():
    return pending()

@app.get("/results")
def results():
    return pending()

@app.get("/nodes")
def nodes():
    return pending()

@app.post("/feedback")
def feedback():
    return pending()
