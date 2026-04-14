from fastapi import APIRouter
from app.services.patient_service import get_patients, create_patient

router = APIRouter()

@router.get("/patients")
async def fetch_patients():
    return await get_patients()

@router.post("/patients")
async def add_patient(payload: dict):
    return await create_patient(payload)