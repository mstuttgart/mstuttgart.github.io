---
title: "Understanding SOLID Principles: A Beginner's Guide"
datePublished: Fri Oct 11 2024 21:01:59 GMT+0000 (Coordinated Universal Time)
cuid: cm257qxl800010ajzfbjp1k1b
slug: understanding-solid-principles-a-beginners-guide
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1728911471646/e03bdeaf-117c-47cd-8e94-d8b271bf08af.png
tags: beginners, object-oriented-programming, solid-principles, oop-design-principles

---

Every day, new requirements for our application arise, and we need to make improvements to meet them while keeping our code easy to read and maintain. If our application is built using Object-Oriented design, we can follow the SOLID principles to achieve this.

SOLID is an acronym for five principles of software design using **Object-Oriented Programming (OOP).** These principles are not linked to any specific programming language, so they work regardless of the language you use.

These principles were introduced by [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin) in a paper titled [Design Principles and Design Patterns](https://web.archive.org/web/20150906155800/http://www.objectmentor.com/resources/articles/Principles_and_Patterns.pdf).

The acronym **SOLID** was later proposed by Michael Feathers and stands for:

* \[S\]ingle Responsibility Principle
    
* \[O\]pen-Closed Principle
    
* \[L\]iskov Substitution Principle
    
* \[I\]nterface Segregation Principle
    
* \[D\]ependency Inversion Principle
    

These principles help software developers design and write Object-Oriented programs with low coupling and high cohesion. They also make it easier to maintain and refactor the code when needed.

# Single Responsibility Principle

This principle states:

> There should never be more than one reason for a class to change

We say that a class must be cohesive, meaning it should have only one responsibility.

Why is it a problem if a class has more than one responsibility?

When a class has multiple responsibilities, each one can change independently. This makes the class more coupled, meaning changes can have a bigger impact on other classes that inherit from it.

For example, let's look at the following code:

```python
class Server: 

	def create_connection(self):
	    pass

	def check_connection(self):
	    pass

	def close_connection(self):
	    pass

	def send_package(self):
	    pass

	def receive_package(self):
	    pass
```

In the `Server` class, we see it has two responsibilities: managing connections (create, close, and check) and managing data packages (send and receive). As a result, all classes that inherit from it also take on these two behaviors.

### Applying the principle

Using the **Single Responsibility Principle**, we can split a class into two separate classes, each with its own responsibility: Connection managers and Package managers.

```python
class ConnectionManager:
	"""Manager connection only"""

	def create_connection(self):
	    pass

	def check_connection(self):
	    pass

	def close_connection(self):
	    pass
```

```python
class PackageManager:
	"""Manager send and receive data packages only"""

	def send_package(self):
	    pass

	def receive_package(self):
	    pass
```

The **Single Responsibility Principle** is one of the hardest principles to apply because the idea of a class's responsibility can differ among software developers. They decide if a behavior fits within the class's scope. To apply this principle effectively, we should always focus on the problem we want to solve and the software architecture we use in our design.

# Open-Close Principle

We must always be careful when inheriting and changing class source code to avoid breaking code that already works. The **Open-Close Principle** helps us prevent this.

This principle states:

> Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

Let's break down each part of this quote:

* **Open to extension** means that a class's behavior can be expanded. We should be able to create a child class and extend a method to adjust its behavior based on the needs of our application.
    
* **Closed to modification** means that a class's source code cannot be changed. No one is allowed to alter the original class's source code to meet new application requirements. Changing the class's source code can affect other functionalities that rely on this class's behavior.
    

For example, let's examine the following classes that represent the geometric shapes: *square* and *circle*

```python
class Square:
	
    def __init__(self, lenght):
	    super().__init__()
	    self.lenght = lenght
```

```python
class Circle:
	
	def __init__(self, radius):
	    super().__init__()
	    self.radius = radius
```

We also have a class that calculates the area of these shapes and returns the result.

```python
import math

class ShapeAreaCalculator:

	def calc_area(self, shape):
	    """Calculate area of shape"""

		area = 0

	    if isinstance(shape, Square):
		    area = shape.lenght ** 2
			
        elif isinstance(shape, Circle):
		    area = math.pi * shape.radius ** 2

        return area
```

The problem with the `ShapeAreaCalculator` class is that whenever a new geometric shape is added, we need to add another `if` statement to check the `shape`. This increases the size and complexity of the `calc_area` method. In other words, the `ShapeAreaCalculator` class is not closed to modification.

### Applying the principle

To start fixing the issue, let's enhance the geometric shape classes by creating a base class called `Shape`. This class will have a method named `area`, which will be extended by all geometric shapes that inherit from it.

```python
class Shape:

	def area(self):
	    pass
```

Let’s update the `Square` and `Circle` classes, make them inherit from `Shape` class.

```python
class Square(Shape):
	
	def __init__(self, lenght):
	    super().__init__()
	    self.lenght = lenght

	def area(self):
	    return self.lenght ** 2
```

```python
import math

class Circle(Shape):
	
	def __init__(self, radius):
	    super().__init__()
	    self.radius = radius

	def area(self):
	    return math.pi * self.radius ** 2
```

Now, every new geometric shape must inherit from the `Shape` class and implement its own `area` method.

All shape classes are now open to extension but closed to modification. This means they won't need changes when a new shape is added.

Finally, let's update the `calc_area` method so that it doesn't need changes when a new shape is added.

```python
class ShapeAreaCalculator:

	def calc_area(self, shape):
	    """Calcule area of shape"""
	    area = shape.area()
	    return area
```

This way, the `calc_area` method doesn't need changes, no matter how many new geometric shapes are added to our application.

# Liskov Substitution Principle

This principle states:

> Functions that use pointers or references to a base class must be able to use objects from derived classes without needing to know it.

It means that all children of our base class must have the same methods. If a class `S` is a child of class `T`, then all objects of class `T` can be replaced by objects of class `S` without needing to change our application.

### Applying the principle

For example, consider a class named `Shape`. All classes that inherit from `Shape` must have an `area` method.

```python
class Shape:

    def area(self):
        raise NotImplementedError("Subclasse should implement this")
```

When a class inherits from the `Shape` class, it must implement its own `area` method; otherwise, the application will raise a `NotImplementedError`.

Now, let's consider a class named `ShapeAreaCalculator`.

```python
class ShapeAreaCalculator:

    def calc_area(self, shape):
        """Calcule area of shape"""
        return shape.area()
```

The `calc_area` method takes a `shape` object as a parameter without needing to know its specific class. We can substitute the `shape` object with any object from a child class of `Shape`, and the application will still function properly.

The **Liskov Substitution Principle** is a fundamental concept for implementing **Polymorphism** in object-oriented software.

# Interface Segregation Principle

This principle states:

> A class should never be forced to implement an interface or method that it will not use.

This situation usually occurs when we create classes or interfaces that are too generic, aiming to cover all possible uses of our application.

### Applying the principle

For example, let's look at our `Shape` class:

```python
class Shape:

    def area(self):
        raise NotImplementedError("Subclasse should implement this")
```

This class is usually used as the base class for `Square` and `Circle` classes, which are geometric shapes that implement the `area` method:

```python
class Square(Shape):
	
    def __init__(self, lenght):
        super().__init__()
        self.lenght = lenght
        
    def area(self):
        return self.lenght ** 2
```

```python
class Circle(Shape):
	
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
```

Now, let's say we want to enhance our `Shape` class to include 3D geometric shapes like cubes and spheres. To do this, we add a new method called `volume` to the `Shape` class.

```python
class Shape:

    def area(self):
        raise NotImplementedError("Subclasse should implement this")
    
    def volume(self):
        raise NotImplementedError("Subclasse should implement this")
```

Consider the new method `volume`. All our child classes will need to implement it. However, it doesn't make sense for `Square` and `Circle` to have a `volume` method because they are 2D geometric shapes. They won't use it.

The **Interface Segregation Principle** advises us to add only methods that our classes will actually use. To solve this issue, let's create a new base class called `Solid`. This class will represent 3D geometric shapes, making it logical to include a `volume` method.

```python
class Solid:
    
    def volume(self):
        raise NotImplementedError("Subclasse should implement this")
```

# Dependency Inversion Principle

This principle states:

> Only depend on abstractions, not on implementations.

In practical terms, no class should inherit from a concrete class, and no method should override an already implemented method. Our classes should always extend from interfaces or abstract classes.

### Applying the principle

Take a look at the following classes:

```python
class Shape:
    "Base class"

    def area(self):
        raise NotImplementedError("Subclasse should implement this")
        

class Square(Shape):
    "Square shape"
	
    def __init__(self, lenght):
        super().__init__()
        self.lenght = lenght
        
    def area(self):
        return self.lenght ** 2
        

class Circle(Shape):
    "Circle shape"
	
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
```

The `Square` and `Circle` classes override the `area` method of the `Shape` base class, which is an abstraction. We could make the `Square` class inherit from the `Circle` class.

```python
class Square(Circle):
	
    def __init__(self, radius, lenght):
        super().__init__(radius)
        self.lenght = lenght
        
    def area(self):
        return self.lenght ** 2
```

This type of inheritance breaks the **Dependency Inversion Principle** because `Circle` is a concrete class. This approach leads to some problems:

1. Our **Square** class will have a *radius* attribute, which doesn't make any sense for the **Square** class since the attribute represents the radius of a *circle*. When creating a **Square** object, we will need to provide not only the length of the square's sides but also a value for *radius*, even though it will never be used.
    
2. We have to override the implementation of the *area* method from the **Circle** class, because if we don't, the Square class will use the *area* implementation from the parent **Circle** class, returning the wrong area calculation. This is because both the area formula and the value of the *radius* attribute (as seen in item 1) will be incorrect.
    

Based on the example above, we can conclude that we should always use abstract classes and interfaces whenever possible. This way, we avoid inheriting behaviors and attributes that are already implemented.

# Conclusion

In conclusion, the SOLID principles offer a strong framework for designing and maintaining object-oriented software, with each principle focusing on a specific part of software design. By using these principles, developers can make their code less complex, improve readability, and make maintenance and scaling easier. Following SOLID principles leads to more reliable and efficient software development practices.

# **References**

* <cite>Martin, Robert C. (2014). "The Single Responsibility Principle". The Clean Code Blog</cite>
    
* *Martin, Robert C. (1996).* *"The Open-Closed Principle", <cite>C++ Report</cite>*
    
* <cite>Martin, Robert C. (March 1996). "The Liskov Substitution Principle"</cite> <cite>(PDF). </cite> *<cite>C++ Report</cite>*<cite>. Archived from the original</cite> <cite>(PDF) on 2015-11-28</cite>
    
* *Martin, Robert C. (June 1996). “The Interface Segregation Principle”. C++ Report*
    
* *Martin, Robert C. (May 1996). “The Dependency Inversion Principle”. C++ Report*