from fastapi import APIRouter, HTTPException
from typing import List
from app.database import get_sales_data
import utils.data_formatting as formatting
from app.services import sales_service


router = APIRouter()

@router.get("/by_employee")
def get_sales_by_employee(key_employee: str, start_date: str, end_date: str):
    return sales_service.get_sales_by_employee(key_employee, start_date, end_date)

@router.get("/by_product")
def get_sales_by_product(key_product: str, start_date: str, end_date: str):
    return sales_service.get_sales_by_product(key_product, start_date, end_date)

@router.get("/by_store")
def get_sales_by_store(key_store: str, start_date: str, end_date: str):
    return sales_service.get_sales_by_store(key_store, start_date, end_date)

@router.get("/total_average_by_store")
def get_total_average_by_store(key_store: str):
    return sales_service.get_total_average_by_store(key_store)

@router.get("/total_average_by_product")
def get_total_average_by_product(key_product: str):
    return sales_service.get_total_average_by_product(key_product)



    