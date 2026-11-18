
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Employee Management API", version="2.1")

# Data model
class Employee(BaseModel):
    id: int
    name: str
    role: str

# In-memory database
employees_db = [
    {"id": 1, "name": "Alice Smith", "role": "Software Engineer"},
    {"id": 2, "name": "Bob Jones", "role": "Data Scientist"}
]

# Get all employees
@app.get("/employees")
def get_employees():
    return employees_db

# Get employee by ID
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees_db:
        if emp["id"] == emp_id:
            return emp

    raise HTTPException(status_code=404, detail="Employee not found")

# Add employee
@app.post("/employees")
def add_employee(emp: Employee):
    for existing in employees_db:
        if existing["id"] == emp.id:
            raise HTTPException(status_code=400, detail="Employee ID already exists")

    employees_db.append(emp.model_dump())
    return emp

# Update employee
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, updated_emp: Employee):
    for index, emp in enumerate(employees_db):
        if emp["id"] == emp_id:
            if updated_emp.id != emp_id:
                raise HTTPException(status_code=400, detail="Employee ID cannot be changed")

            employees_db[index] = updated_emp.model_dump()
            return updated_emp

    raise HTTPException(status_code=404, detail="Employee not found")

# Delete employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    for emp in employees_db:
        if emp["id"] == emp_id:
            employees_db.remove(emp)
            return {"message": "Employee deleted successfully"}

    raise HTTPException(status_code=404, detail="Employee not found")

# Health check
@app.get("/health")
def health():
    return {"status": "ok", "version": "2.1"}
