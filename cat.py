class cat:
    def __init__(self,name):
        self.name = name
    def greet(self , anothercat):
        self.anothercat = anothercat
        print(f"Hello I am {self.name} ! I see you are also a cool fluffy kitty {anothercat.get_name()} , let's together purr at the human, so that they shall give us food")

    def get_name(self):
        return self.name

# cat1 = cat("Kittosaurus Rex")
# cat2 = cat("Snowball IX")
# cat1.saying_hi(cat2)