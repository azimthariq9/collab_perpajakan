from sqlalchemy.orm import Session
from models import Employee


def create_employee(db: Session, name: str, salary: float):
    employee = Employee(name=name, salary=salary)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee
def get_employees(db: Session):
    return db.query(Employee).all()