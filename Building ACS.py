company_floors = 4 
offices_per_floor = 6
high_offices = 0
medium_offices = 0 
low_offices = 0 

for floor in range(company_floors):
    print(f"========== Floor {floor + 1} ==========")
    
    for office in range(offices_per_floor):
        if (office + 1) % 3 == 0:
            print(f'Office {office + 1}: HIGH')
            high_offices += 1
        elif (office + 1) % 2 == 0 and (office + 1) % 3 != 0:
            print(f"Office {office + 1}: MEDIUM")
            medium_offices += 1
        else: 
            print(f"Office {office + 1}: LOW")
            low_offices += 1


total_offices = company_floors * offices_per_floor

print()


print(f"Total floors: {company_floors}")
print(f"Total offices: {total_offices}")
print(f"HIGH offices: {high_offices}")
print(f"MEDIUM offices: {medium_offices}")
print(f"LOW offices: {low_offices}")

#oh. fuck you