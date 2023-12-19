it's for object oriented programming

a class is a definition of an object. an object is (usually) a representation of a thing. for example, you could have a class called Animal that stores info about an animal, such as it's name:

```py
class Animal:
  name: str

  def __init__(self, name: str) -> None:
    """Initialise the object."""
    self.name = name
```

(will come back to the `__init__` function)

this is useful, because then you can easily have 2 animals without having to copy/paste code:

```py
class Animal:
  name: str

  def __init__(self, name: str) -> None:
    """Initialise the object."""
    self.name = name

dog = Animal("Terrence")
cat = Animal("Dave")
```

you can also make classes have functions attached to them, usually these are called methods:

```py
class Animal:
  name: str

  def __init__(self, name: str) -> None:
    """Initialise the object."""
    self.name = name

  def noise() -> None:
    """Make a noise!"""
    print(f"hi i am {self.name}.")

dog = Animal("Terrence")
cat = Animal("Dave")

dog.noise()
cat.noise()
```

this will print:

```
hi i am Terrence.
hi i am Dave.
```

The `__init__` method is a "magic method", that initialises a new instance of a class into an object. It's what gets called when you do `Animal("Terrence")`.

Also, you'll see the `self` argument in the `__init__` method. This is a reference to the newly created object. We're setting `name` on the `self` variable in the class, so that each new object can keep track of their individual name.

The really cool part of object oriented programming is inheritance. You can make a class inherit from another class, and it will get all the methods and attributes of the parent class. So, instead of having 2 Animals, we can have a Dog, and a Cat:

```py
class Animal:
  name: str

  def __init__(self, name: str) -> None:
    """Initialise the object."""
    self.name = name

  def noise() -> None:
    """Make a noise!"""
    print(f"hi i am {self.name}.")

class Dog(Animal):
    def noise() -> None:
        """Make a noise!"""
        print(f"hi i am {self.name}.")
        print("woof.")

class Cat(Animal):
    def noise() -> None:
        """Make a noise!"""
        print(f"hi i am {self.name}.")
        print("meow.")

dog = Animal("Terrence")
cat = Animal("Dave")

dog.noise()
cat.noise()
```

this will print:

```
hi i am Terrence.
woof.
hi i am Dave.
meow.
```

to clean up the code a bit, we can use `super()` to call the parent class's method:

```py
class Animal:
  name: str

  def __init__(self, name: str) -> None:
    """Initialise the object."""
    self.name = name

  def noise() -> None:
    """Make a noise!"""
    print(f"hi i am {self.name}.")

class Dog(Animal):
    def noise() -> None:
        """Make a noise!"""
        super().noise()
        print("woof.")

class Cat(Animal):
    def noise() -> None:
        """Make a noise!"""
        super().noise()
        print("meow.")

dog = Animal("Terrence")
cat = Animal("Dave")

dog.noise()
cat.noise()
```

this will print:

```
hi i am Terrence.
woof.
hi i am Dave.
meow.
```

you can also change attributes of a class after you've set them in the `__init__` method. Let's say that Cats are allowed to have different names, because they don't really care what they're called as long as they get food.

```py
class Animal:
  name: str

  def __init__(self, name: str) -> None:
    """Initialise the object."""
    self.name = name

  def noise() -> None:
    """Make a noise!"""
    print(f"hi i am {self.name}.")

class Dog(Animal):
    def noise() -> None:
        """Make a noise!"""
        super().noise()
        print("woof.")

class Cat(Animal):
    def noise() -> None:
        """Make a noise!"""
        super().noise()
        print("meow.")
    
    def set_name(self, name: str) -> None:
        """Set the name of the cat."""
        self.name = name

dog = Animal("Terrence")
cat = Animal("Dave")

dog.noise()
cat.noise()
cat.set_name("Jeff")
cat.noise()
```

this will print:

```
hi i am Terrence.
woof.
hi i am Dave.
meow.
hi i am Jeff.
meow.
```

Note that if you did something like making the `noise` method do something other than what it is supposed to do, like this:

```py
class Animal:
  name: str

  def __init__(self, name: str) -> None:
    """Initialise the object."""
    self.name = name

  def noise() -> None:
    """Make a noise!"""
    print(f"hi i am {self.name}.")

class Dog(Animal):
    def noise() -> None:
        """Make a noise!"""
        super().noise()
        print("woof.")

class Cat(Animal):
    def noise() -> None:
        """Make a noise!"""
        self.name = "Jeff"  # uh oh
        super().noise()
        print("meow.")
    
    def set_name(self, name: str) -> None:
        """Set the name of the cat."""
        self.name = name

dog = Animal("Terrence")
cat = Animal("Dave")

dog.noise()
cat.noise()
cat.set_name("Jeff")
cat.noise()
```

which will print:

```
hi i am Terrence.
woof.
hi i am Jeff.
meow.
hi i am Jeff.
meow.
```

Then that would be a violation of the Liskov Substitution Principle, which basically says that a subclass of a class should be able to be swapped out for the parent class without breaking anything.

In this case, the `noise` method of the `Cat` class is not doing what it is supposed to do, which is make a noise. It's setting the name of the cat to "Jeff", therefore breaking Liskov Substitution Principle.

It's a good idea to follow Liskov, because then you can do cool things like iterating over a list of different objects that all inherit from one class, and treat them all the same. That's how my reporting engine works at work. E.g:

```py
class Animal:
  name: str

  def __init__(self, name: str) -> None:
    """Initialise the object."""
    self.name = name

  def noise() -> None:
    """Make a noise!"""
    print(f"hi i am {self.name}.")

class Dog(Animal):
    def noise() -> None:
        """Make a noise!"""
        super().noise()
        print("woof.")

class Cat(Animal):
    def noise() -> None:
        """Make a noise!"""
        super().noise()
        print("meow.")
    
    def set_name(self, name: str) -> None:
        """Set the name of the cat."""
        self.name = name

animals = [Dog("Terrence"), Cat("Dave"), Cat("Phil")]

for animal in animals:
    animal.noise()
```

this will print:

```
hi i am Terrence.
woof.
hi i am Dave.
meow.
hi i am Phil.
meow.
```