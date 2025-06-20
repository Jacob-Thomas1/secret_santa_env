import pandas as pd
import random

from models.Employee import Employee
from models.SecretSanta import SecretSanta

def return_employee_list(file_path, previous_santa_file_path):

    try:
        df = pd.read_excel(file_path)
        df_previous = pd.read_excel(previous_santa_file_path)

        #checks for any missing columns and empty file
        if 'Employee_Name' not in df.columns:
            raise ValueError("The Excel file must contain a 'Name' column.")
        if 'Employee_EmailID' not in df.columns:
            raise ValueError("The Excel file must contain an 'Email' column.")
        if df.empty:
            raise FileNotFoundError("The Excel file is empty.")


        # Create Employee objects from the DataFrame
        employees = []
        for index, row in df.iterrows():
            
                
            name = row['Employee_Name'].strip()
            email = row['Employee_EmailID'].strip()
            
            # Break if the name or email is empty
            if not name or not email:
                break
            
            prev_santa = Employee("None", "None")  # Default previous Santa if not found
            # Check if the previous year's data is available
            
            #if the previous year's data is available, fetch the previous Secret Santa
            if not(df_previous.loc[df_previous['Employee_EmailID'] == email, 'Secret_Child_Name'].empty):
                prev_name = df_previous.loc[df_previous['Employee_EmailID'] == email, 'Secret_Child_Name'].values[0]
                prev_email = df_previous.loc[df_previous['Employee_EmailID'] == email, 'Secret_Child_EmailID'].values[0]
                prev_santa = Employee(prev_name, prev_email) 
            
            employees.append(Employee(name, email, prev_santa))
            
        print("\n           ******       Previous (2023) Secret Santa assignments:        ****** \n")
        for employee in employees:
            print(f"{employee.employee_name} ({employee.employee_email}) had -> {employee.previous_santa.employee_name} ({employee.previous_santa.employee_email})")
        print("\n\n")
        
        return employees

    except Exception as e:
        print(f"Error reading the file: {e}")
        return []
