# Abstraction

## What is abstraction?

The action of deciding **what information to encapsulate into a module** and **what information to expose** to the rest of the code (make public).

We perform abstraction when **we bundle related items together, name the module and then use it**

Abstraction depends heavily on the **context** and the mental model of the developer responsible for the abstraction.


Abstraction could involve:

* Collecting lines of code together into a **method or function**.
* Collecting related data into a **class**.
* grouping classes into **packages**

If abstraction is done well you won't have to worry about their internals (**separation of concern** and **cognitive load**).

## Abstraction, encapsulation and information hiding

| Abstraction                                                                                               | Encapsulation                  | Information hiding                                                             |
| :-:                                                                                                       | :-:                            | :-:                                                                            |
| When we decide how things should look from outside                                                        | When we bundle things together | When we use **encapsulation mechanism** that doesn't allow access from outside |
| Deciding on how things will look from the surface/outside (i.e. When we design a class' public interface) |                                | **Private or protected modifiers**: keep implementation details hidden         |
|                                                                                                           |                                | Use of **local variables** and scopes                                          |
|                                                                                                           |                                | **Defensive copy**                                                             |
