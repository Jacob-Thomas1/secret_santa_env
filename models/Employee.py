class Employee:
    def __init__(self, employee_name: str, employee_email: str, previous_santa: "Employee" = None):
        self.previous_santa = previous_santa
        self.employee_name = employee_name
        self.employee_email = employee_email
        self.secret_santa = None
        
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_name == other.employee_name and self.employee_email == other.employee_email
        return False

    def __hash__(self):
        return hash((self.employee_name, self.employee_email))