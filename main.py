from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.recommend import router as recommend_router

app = FastAPI(
    title="StyleSense AI Backend",
    description="Generative AI Fashion Recommendation Platform",
    version="1.0.0"
)

# CORS for React + Vite
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommend_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "StyleSense backend running"}