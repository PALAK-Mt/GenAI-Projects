

from fastapi import APIRouter, Query
from app.agents.stock_agent import analyze_stock

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to the Financial AI Agent API. Use /analyze?ticker=XYZ"}

@router.get("/analyze")
def analyze(ticker: str = Query(...)):
    return analyze_stock(ticker)
