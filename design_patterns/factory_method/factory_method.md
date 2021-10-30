### Factory Method 

- Also known as Virtual Constructor.

- Factory Method is a creational design pattern that provides an interface for creating
  objects in a superclass, but allows subclasses to alter the type of objects that
  will be created. (RDP)

- The factory method is based on a single function written to handle our object creation task.
  We execute it, passing a parameter that provides information about what we want, and, as
  a result, the wanted object is created. Interestingly, when using the factory method, we are not 
  required to know any details about how the resulting object is implemented and where it is coming from. (MPDP)
  
- Real World Example: An example of the factory method pattern used in reality is in the 
  context of a **plastic toy construction kit**. The molding material used to construct plastic toys is the same, but
  different toys (different figures or shapes) can be produced using the right plastic molds.
  This is like having a factory method in which the input is the name of the toy that we want
  (for example, duck or car) and the output (after the molding) is the plastic toy that was
  requested. (MPDP)
  
- Django Framework: The Django web framework uses the factory method pattern for
  creating the fields of a web form. The `forms` module, included in Django, supports the
  creation of different kinds of fields (for example, CharField, EmailField, and so on). And
  parts of their behavior can be customized using attributes such as max_length or
  required.
  
  ```python
   from django import forms
    
    class PersonForm(forms.Form):
        name = forms.CharField(max_length=100)
        birth_date = forms.DateField(required=False)
  ```
  
  (MPDP)

- The factory method centralizes object creation and tracking your objects becomes much easier. 
  
  It is absolutely fine to create more than one factory method, and this is how it is typically 
  done in practice. Each factory method logically groups the creation of objects that have similarities. 
  For example,
    * one factory method might be responsible for connecting you to different databases 
      (MySQL, SQLite), 
    * another factory method might be responsible for creating the geometrical 
      object that you request (circle, triangle), and so on.
      
  (MPDP)





  
