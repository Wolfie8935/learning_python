capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

final_list = list(zip(countries, capitals))

for country, capital in final_list:
    print(f"The capital of {country} is {capital}")