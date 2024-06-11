from fastapi import APIRouter, HTTPException
from typing import List
from app.database import get_sales_data
import utils.data_formatting as formatting


router = APIRouter()

@router.get("/by_employee")
def get_sales_by_employee(key_employee: int, start_date: str, end_date: str):
    
    df = get_sales_data()
    
    # Formats employee_id as appears on database
    key_employee = formatting.add_pipe(key_employee)

    result = df[(df["KeyEmployee"] == key_employee) & 
                (df["KeyDate"] >= start_date) &
                (df["KeyDate"] <= end_date)]
    
    return result.to_dict(orient="records")

@router.get("/by_product")
def get_sales_by_product(key_product: int, start_date: str, end_date: str):

    df = get_sales_data()

    key_product = formatting.add_pipe(key_product)

    result = df[(df["KeyProduct"] == key_product) & 
                (df["KeyDate"] >= start_date) &
                (df["KeyDate"] <= end_date)]
    return result.to_dict(orient="records")

@router.get("/by_store")
def get_sales_by_store(key_store: str, start_date: str, end_date: str):
    df = get_sales_data()

    key_store = formatting.add_pipe(key_store)

    result = df[(df["KeyStore"] == key_store) & 
                (df["KeyDate"] >= start_date) &
                (df["KeyDate"] <= end_date)]
    return result.to_dict(orient="records")



    