# Write your code here!
def temp_and_color(diccionario):
    
    temperatura = diccionario.get("temp")
    color = diccionario.get("color")
    return temperatura, color

data1 = {"temp": 22.5, "color": "blue", "status": "ok"}
print(temp_and_color(data1))  

data2 = {"status": "ok"}
print(temp_and_color(data2))