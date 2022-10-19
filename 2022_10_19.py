class EmptyClass:
    pass

class MyClass:
    def hello(self):
        return "hello world"

class Hello:
    def create_name(self, name):
        self.name = name

    def display_name(self):
        return self.name

    def greet(self):
        print(f"Hello {self.name}!")

class Greetings:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi {0}!".format(self.name))

class Bag:
    def __init__(self):
        self._data = []

    def add(self, value):
        self._data.append(value)

    def __str__(self):
        return "Bag({0})".format(str(self._data))

    def add_twice(self, value):
        #v1 student method
        #self.data.append(value)
        #self.data.append(value)

        #v2
        self.add(value)
        self.add(value)

class Proba:
    counter = 0

    def __init__(self):
        Proba.counter += 1

    def hello(self):
        print("hello")

class Balloon:
    unique_colors = set()

    def __init__(self, color):
        self.color = color
        Balloon.unique_colors.add(color)

    @staticmethod
    def unique_color_count():
        return len(Balloon.unique_colors)

def main():
    #o = EmptyClass()
    mc = MyClass()
    print(mc.hello())

    h = Hello()
    h.create_name("Alice")
    print(h.display_name())
    h.greet()

    g = Greetings("Alice")
    g.say_hi()

    b = Bag()
    b.add(5)
    b.add(3)
    print(b)
    b.add_twice(9)
    print(b)

    p1 = Proba()
    p2 = Proba()
    p3 = Proba()
    print(Proba.counter)

    b1 = Balloon("red")
    b2 = Balloon("green")
    b3 = Balloon("green")
    b4 = Balloon("blue")
    print(Balloon.unique_color_count())

####################################################
if __name__ == "__main__":
   main()