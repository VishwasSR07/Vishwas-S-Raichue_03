# 19. Using **kwargs in Functions  
def show_info(**kwargs):
    print("Vishwas's info:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Vishwas", age=25, city="Pune")
