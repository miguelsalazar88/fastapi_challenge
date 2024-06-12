from app.database import get_sales_data
import utils.data_formatting as formatting
from fastapi import HTTPException


ERROR_MESSAGE = "An error occurred while processing the request"

def get_sales_by_employee(key_employee: str, start_date: str, end_date: str):
    
    try:
        df = get_sales_data()
        
        # Formats employee_id as appears on database
        key_employee = formatting.add_pipe(key_employee)

        result = df[(df["KeyEmployee"] == key_employee) & 
                    (df["KeyDate"] >= start_date) &
                    (df["KeyDate"] <= end_date)]
        
        return result.to_dict(orient="records")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_MESSAGE)


def get_sales_by_product(key_product: str, start_date: str, end_date: str):

    try:
        df = get_sales_data()

        key_product = formatting.add_pipe(key_product)

        result = df[(df["KeyProduct"] == key_product) & 
                    (df["KeyDate"] >= start_date) &
                    (df["KeyDate"] <= end_date)]
        return result.to_dict(orient="records")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_MESSAGE)

def get_sales_by_store(key_store: str, start_date: str, end_date: str):

    try:
        df = get_sales_data()

        key_store = formatting.add_pipe(key_store)

        result = df[(df["KeyStore"] == key_store) & 
                    (df["KeyDate"] >= start_date) &
                    (df["KeyDate"] <= end_date)]
        return result.to_dict(orient="records")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_MESSAGE)
    
def get_total_average_by_store(key_store: str):

    try:
        df = get_sales_data()
        key_store = formatting.add_pipe(key_store)
        total_sales = df[df["KeyStore"]== key_store]["CostAmount"].sum()
        average_sales = df[df["KeyStore"]== key_store]["CostAmount"].mean()
        

        return {"total_sales": total_sales,
                "average_sales": average_sales}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_MESSAGE)

def get_total_average_by_product(key_product: str):

    try:
        df = get_sales_data()
        key_product = formatting.add_pipe(key_product)
        total_sales = df[df["KeyProduct"]== key_product]["CostAmount"].sum()
        average_sales = df[df["KeyProduct"]== key_product]["CostAmount"].mean()

        return {"total_sales": total_sales,
                "average_sales": average_sales}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_MESSAGE)

def get_total_average_by_employee(key_employee: str):

    try:
        df = get_sales_data()
        key_employee = formatting.add_pipe(key_employee)
        total_sales = df[df["KeyEmployee"]== key_employee]["CostAmount"].sum()
        average_sales = df[df["KeyEmployee"]== key_employee]["CostAmount"].mean()

        return {"total_sales": total_sales,
                "average_sales": average_sales}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_MESSAGE)