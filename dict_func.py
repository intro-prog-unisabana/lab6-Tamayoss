# Write your code here!
def employee_print(employee_info):
    datos = employee_info.copy()
    
    llaves_base = ["Name", "Salary", "Role"]
    
    for key in llaves_base:
      
        valor = datos.pop(key, "N/A")
        print(f"{key}: {valor}")


    if len(datos) > 0:
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    else:
        print("No other info!")


employee_info = {
    "Name": "Diego",
    "Salary": 5000000,
    "Role": "Janitor",
    "Years at company": 9001,
    "Hours per week": 2
}
employee_print(employee_info)
