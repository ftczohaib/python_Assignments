class Circle:
    pi = 3.14;
    def __init__(self):
        self.radius = 0.0;
        self.area = 0.0;
        self.circumference = 0.0;

    def Accept(self):
        self.radius = int(input("Enter the Radius of Circle: "));

    def CalculateArea(self):
        self.area = self.pi*(self.radius**2);

    def CalculateCircumference(self):
        self.circumference = self.pi*(self.radius*2);

    def Display(self):
        print("Radius of a Circle is :",self.radius);
        print("Area of a Circle is :", self.area);
        print("Circumference of a Circle is :", self.circumference);


def main():
    obj1 = Circle();
    obj1.Accept();
    obj1.CalculateArea();
    obj1.CalculateCircumference();
    obj1.Display();

if __name__ == "__main__":
    main();


