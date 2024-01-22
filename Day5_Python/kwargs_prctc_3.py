def describe_person(name, **kwargs):
    print(f"Characteristics of {name}:")
    for argument_name , argument_value in kwargs.items():
        print(f"{argument_name}: {argument_value}")
        
