from databases import Database

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/clinical_db"

database = Database(DATABASE_URL)