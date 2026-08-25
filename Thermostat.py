temp_query = 10
heating_events = 0
comfy_readings = 0
cooling_events = 0

for tempurature in range(temp_query):
    tempurature = 0
    highest = tempurature
    lowest = tempurature
    thermo_reading = int(input(" Enter Room Temperature: "))

    if thermo_reading > tempurature:
        highest = 

    if thermo_reading < tempurature:
        lowest = tempurature

    if thermo_reading <=60:
        print("HEATING REQUIRED")
        heating_events += 1

    elif thermo_reading >= 60 and thermo_reading <= 75:
    #I need to understand the logic behind when i HAVE to put the 
    #variable before the operator and when i dont
        print("COMFORTABLE")
        comfy_readings += 1 
    
    else:
        print("COOLING REQUIRED")
        cooling_events += 1

    


        
    
print()
print(f"# of Heating Events: {heating_events}")
print(f"# of Comfortable Events: {comfy_readings}")
print(f"# of Cooling Events: {cooling_events}")
print()
print(f"Highest temp: {highest}")
print(tempurature)

#im over 40 lines... and im beat.