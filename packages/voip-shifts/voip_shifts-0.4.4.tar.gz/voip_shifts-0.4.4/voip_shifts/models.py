from sqlalchemy import Integer, Column, String, ForeignKey, Boolean, DateTime, Date
from sqlalchemy.orm import relationship

from voip_shifts.config import Base

class CompanyModel(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    timezone = Column(Integer, nullable=False)
    source_phone = Column(String(25), nullable=False)
    destination_phone = Column(String(25))
    info = Column(String(100), nullable=True)
    subscription_active = Column(Boolean, nullable=False, default=False)
    clients = relationship("ClientModel", backref="company")
    employees = relationship("EmployeeModel", backref="company")
    daily_reports = relationship("DailyReportModel", backref="company")
    timetables = relationship("TimetableModel", backref="company")

    def __str__(self):
        return f"Comapny: {self.name}"

    def __repr__(self):
        return f"Company: {self.name}"

class ClientModel(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(35), nullable=True)
    last_name = Column(String(35), nullable=True)
    internal_id = Column(String(25), nullable=False)
    info = Column(String(100), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"))
    timetables = relationship("TimetableModel", backref="client")


class EmployeeModel(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(35), nullable=True)
    last_name = Column(String(35), nullable=True)
    internal_id = Column(String(25), nullable=False)
    info = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE", onupdate="CASCADE"))
    timetables = relationship("TimetableModel", backref="employee")

    def __str__(self):
        return f"Employee internal_id: {self.internal_id}"

    def __repr__(self):
        return f"Employee internal_id: {self.internal_id}"


class TimetableModel(Base):
    __tablename__ = "timetables"
    id = Column(Integer, primary_key=True)
    regularly = Column(Boolean, nullable=False)
    active = Column(Boolean, nullable=False)
    skip = Column(Boolean, nullable=False)
    date = Column(Date)
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=False)
    service_id = Column(String(15), nullable=False)
    job_id = Column(String(37), nullable=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"))
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"))
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"))

    def __str__(self):
        return f"{self.start_date} [{self.id}]"

    def __repr__(self):
        return f"Timetable with employee: {self.employee_id} \
         client: {self.client_id} start at: {self.start_date} end at {self.end_date}"


class DailyReportModel(Base):
    __tablename__ = "daily_reports"
    id = Column(Integer, primary_key=True)
    call_count = Column(Integer)
    date = Column(Date)
    company_id = Column(Integer, ForeignKey("companies.id"))

