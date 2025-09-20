from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

# Initialize FastAPI app
app = FastAPI(title="Legal Compliance MVP")

# --- CORS setup ---
app.add_middleware(
    CORSMiddleware,
    # Change this to your real Deepsite frontend domain
    allow_origins=[
        "https://your-deepsite-subdomain.deepsite.io",
        "http://localhost:5173",   # dev
        "http://localhost:8000"    # dev
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Root route now accepts GET and HEAD
@app.get("/", methods=["GET", "HEAD"])
def read_root():
    return {"message": "Welcome to Legal Compliance MVP"}

@app.post("/analyze/")
async def analyze_file(file: UploadFile = File(...)):
    """
    Accept a document upload and return a dummy compliance check result.
    """
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Dummy compliance logic (replace with real AI/LLM logic later)
    result = {
        "filename": file.filename,
        "status": "Processed",
        "compliance_risks": [
            {"issue": "Missing GDPR clause", "severity": "High"},
            {"issue": "No data retention policy", "severity": "Medium"}
        ]
    }

    return {"analysis": result}
