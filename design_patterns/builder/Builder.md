### Builder Pattern

Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to
produce different types and representations of an object using the same construction code.

In languages like Java or C#, where method overloading is allowed, if you see a constructor methods like the ones below
to create different kinds of objects based on the constructor method being called, you need a Builder pattern.

```java
class Pizza {
 Pizza(int size) { ... }
 Pizza(int size, boolean cheese) { ... }
 Pizza(int size, boolean cheese, boolean pepperoni) { ... }
 // ...
} 
```

*Use the Builder pattern to get rid of a “telescopic constructor”.* The telescopic constructor problem occurs when we
are forced to create a new constructor for supporting different ways of creating an object. The problem is that we end
up with many constructors and long parameter lists, which are hard to manage.

This problem does not exist in Python, because it can be solved in at least two ways:

* With named parameters (or keyword arguments)
* With argument list unpacking