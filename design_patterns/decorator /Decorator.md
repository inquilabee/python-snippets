### Decorator

Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside
special wrapper objects that contain the behaviors.

As Python developers, we can write decorators in a Pythonic way (meaning using the language's features), thanks to the
built-in decorator feature. What exactly is this feature? A Python decorator is a `callable` (function, method, or
class) that gets a function object func_in as input, and returns another function object func_out. It is a commonly used
technique for extending the behavior of a function, method, or class.

### Use cases

The decorator pattern shines when used for implementing cross-cutting concerns.

Examples of cross-cutting concerns are as follows:

* Data validation
* Caching
* Logging
* Monitoring
* Debugging
* Business rules
* Encryption

In general, all parts of an application that are generic and can be applied to many other parts of it are considered to
be cross-cutting concerns.

### References

- https://levelup.gitconnected.com/mastering-decorators-in-python-3-588cb34fff5e
- https://realpython.com/primer-on-python-decorators