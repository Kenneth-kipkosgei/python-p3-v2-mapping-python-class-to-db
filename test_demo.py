#!/usr/bin/env python3

import sys
sys.path.append('lib')

from __init__ import CONN, CURSOR
from department import Department

# Clean slate
Department.drop_table()
Department.create_table()

# Create departments
payroll = Department.create("Payroll", "Building A, 5th Floor")
hr = Department.create("Human Resources", "Building C, East Wing")

print("Created departments:")
print(payroll)
print(hr)

# Update HR department
hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(f"\nUpdated HR: {hr}")

# Query database
departments = CURSOR.execute('SELECT * FROM departments').fetchall()
print(f"\nDatabase contents: {departments}")

# Delete payroll
payroll.delete()
print(f"\nDeleted payroll department")

# Final database state
departments = CURSOR.execute('SELECT * FROM departments').fetchall()
print(f"Final database contents: {departments}")