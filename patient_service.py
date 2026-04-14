from app.db.database import database

GET_PATIENTS = "SELECT * FROM patients LIMIT 50"
INSERT_PATIENT = """
INSERT INTO patients(name, age, condition)
VALUES (:name, :age, :condition)
RETURNING id
"""

async def get_patients():
    return await database.fetch_all(GET_PATIENTS)

async def create_patient(payload: dict):
    return await database.execute(INSERT_PATIENT, payload)