import random
import datetime
import time
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# Use the updated Base from SQLAlchemy 2.0
Base = declarative_base()

class MachineData(Base):
    __tablename__ = 'machine_data'
    id = Column(Integer, primary_key=True)
    machine_id = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    temperature = Column(Float)  # Corrected column name
    cycle_count = Column(Integer)
    status = Column(String)

# Set up database connection
engine = create_engine('sqlite:///C:/Users/parag/predictive_maintenance/maintenance_db.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def generate_data():
    machine_ids = ['M1', 'M2', 'M3', 'M4']
    statuses = ['active', 'idle', 'error']
    
    while True:
        for machine in machine_ids:
            data = MachineData(
                machine_id=machine,
                temperature=random.uniform(60, 100),  # Corrected column name
                cycle_count=random.randint(1000, 5000),
                status=random.choice(statuses)
            )
            session.add(data)
        session.commit()
        time.sleep(10)  # Simulate data coming every 10 seconds

if __name__ == '__main__':
    generate_data()