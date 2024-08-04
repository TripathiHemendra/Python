class Leaf():
    color="green"
    def __init__(self,color):
        self.color=color
leaf1=Leaf("Blue")
color1=leaf1.color
leaf1.color="orange"
color2=leaf1.color
color3=Leaf.color
print(color1+color3+color2)