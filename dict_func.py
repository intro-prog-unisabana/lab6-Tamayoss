# Write your code here!
def employee_print(employee_info):
    info = employee_info.copy()

    nombre   = info.pop("Name",   "N/A")
    salary = info.pop("Salary", "N/A")
    rol   = info.pop("Role",   "N/A")

    print(f"Name: {nombre}")
    print(f"Salary: {salary}")
    print(f"Role: {rol}")

    if info:
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")