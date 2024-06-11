from fastapi import FastAPI
import app.database as database
import app.routers.sales as sales


app = FastAPI()

@app.on_event("startup")
def startup_event():
    database.load_data() # Load data on startup

app.include_router(sales.router, prefix="/sales", tags=["sales"])