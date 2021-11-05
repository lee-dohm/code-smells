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
| Deciding on how things will look from the surface/outside (i.e. When we design a class' **public interface**) |                                | **Private or protected modifiers**: keep implementation details hidden         |
|                                                                                                           |                                | Use of **local variables** and scopes                                          |
|                                                                                                           |                                | **Defensive copy**                                                             |

## Separation of Concerns (Reducing coupling)

> the only available technique for effective ordering of one's thoughts, that i know of. <br />
> It is being one- and multiple-track minded simultaneously. <br />
> -- E.W. Dijkstra, ”On the Role of Scientific Thought”

Each module has a **well-defined responsibility they are concerned with.**

Responsibilities should overlap as little as possible.

DRY: **shared responsibilities often leads to repeated code.**

Unclear responsibilities are hard to use.

## DIP and abstraction

DIP requires abstraction and facilitates separation of concern

## Common mistakes

### Simplicity **does not mean** less classes.

We are trying to simplify the program overall

❑ fewer classes means bigger classes
❑ remember we are trying to minimise the number of things the programmer has to think about simultaneously

❑ usually have to think about everything in the class you’re modifying (cognitive capacity still overloaded)

❑ so no net gain from making classes bigger


#### Classes are systems too

If you try to fix the problem by combining classes into larger classes, leaving many methods and attributes private, you will indeed simplify interactions between classes – but we're trying to reduce the overall complexity of the system!

* although you've made things simpler at class level, those larger classes themselves will be harder to maintain
* quadratic rise in interactions within the class boundary: methods, attributes, etc.

Only way to reduce net complexity is to **define relatively small classes**
* **minimise dependencies** between them
* **hide any information** that isn’t relevant to other classes
* this decreases that N

### Overdoing dependency inversion

Using **too many abstract classes is also a bad thing**

* Adding an interface adds complexity to your design

* Worth it if complexity is being taken away elsewhere

* Worth it if you want to be able to develop components in isolation (such as GMailer and MoodleMessager, earlier)

#### Confusing abstraction with abstract

Using abstraction can help you build classes that are easier to use and maintain
• This is not the same as sprinkling the abstract keyword into your code – the key to making your code better is thinking carefully about
– what each code module is for
– how it should look from other parts of the code
– which aspects of the code might need to be reused or specialised 

**Declaring a class to be abstract only means you can’t instantiate it**.

**Declaring a method to be abstract only means you need to override it with a concrete implementation in order to be able to instantiate the class** it is in. 

Neither of these approaches guarantee that your abstraction is useful or clean – that’s a design issue, not an implementation issue.

