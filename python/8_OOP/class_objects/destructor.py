class person:
    
    def __init__(self):
        print("Created")
        
    def __del__(self):
        print("Destroyed")


p1 = person()
p2 = person()

del p1
del p2
