from fastapi import APIRouter, UploadFile, File, Form
from app.services.image_caption import generate_caption
from app.services.fashion_ai import generate_fashion_advice
from app.services.trend_analysis import analyze_trends
from app.schemas.response import RecommendationResponse

router = APIRouter(tags=["Fashion Recommendation"])

@router.post("/recommend", response_model=RecommendationResponse)
async def recommend_outfit(
    gender: str = Form(...),
    occasion: str = Form(...),
    style: str = Form(...),
    image: UploadFile = File(...)
):
    # Image → Text
    image_description = generate_caption(image)

    # AI Outfit Recommendation
    outfit_advice = generate_fashion_advice(
        gender, occasion, style, image_description
    )

    # Trend Analysis
    trends = analyze_trends(outfit_advice)

    return {
        "image_description": image_description,
        "outfit_recommendation": outfit_advice,
        "trend_insights": trends
    }