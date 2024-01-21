# employee of the month check with tuples
work_hours = [
    ("amit", 200),
    ("sanjay", 140),
    ("Ankit", 170),
    ("Pramod", 165),
    ("Lavkush", 210),
]


def check_employee(work_hours):
    max_hours = 0
    employee_name = ""

    for employee, hours in work_hours:
        if max_hours < hours:
            employee_name = employee
            max_hours = hours

    return (employee_name, max_hours)


result = check_employee(work_hours)
print(f"Employee of the month is {result[0]} with {result[1]} hours")
