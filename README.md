# Code Smells

"Code Smell" is a term coined by Kent Beck and Martin Fowler and introduced in Martin Fowler's book, [Refactoring][refactoring]. Code Smells are patterns of code that suggest there might be a problem, that there might be a better way of writing the code or that more design perhaps should go into it. They are intended to be used as a guide for when to refactor code. Additionally, I have found them to be very useful in code reviews as a succinct language for when and how to clean up certain chunks of code. I wanted to document and standardize this language so as to make code reviews more valuable.

## List of Code Smells

All page numbers are from [Refactoring][refactoring] unless otherwise noted.

### Refactoring

#### Alternative Classes with Different Interfaces

* p85

Methods or classes that do the same thing but have different signatures.

#### Comments

* p87

It's surprising how often you look at thickly commented code and notice that the comments are there because the code is bad.

#### Data Class

* p86

These are classes that have fields, getting and setting methods for the fields, and nothing else. Such classes are dumb data holders and are almost certainly being manipulated in far too much detail by other classes.

#### Data Clumps

* p81

Data items tend to be like children; they enjoy hanging around in groups together. Often you'll see the same three or four data items together in lots of places: fields in a couple of classes, parameters in many method signatures. Bunches of data that hang around together really ought to be made into their own object.

#### Divergent Change

* p79

Divergent change occurs when one class is commonly changed in different ways for different reasons. If you look at a class and say, "Well, I will have to change these three methods every time I get a new database; I have to change these four methods every time there is a new financial instrument," you likely have a situation in which two objects are better than one. That way each object is changed only as a result of one kind of change.

*See [Single Responsibility Principle][srp]*

#### Duplicate Code

* p76

If you see the same code structure in more than one place, you can be sure that your program will be better if you find a way to unify them.

#### Feature Envy

* p80

A method that seems more interested in a class other than the one it actually is in. The most common focus of the envy is the data. We've lost count of the times we've seen a method that invokes half-a-dozen getting methods on another object to calculate some value.

#### Inappropriate Intimacy

* p85

Sometimes classes become far too intimate and spend too much time delving in each others' private parts. We may not be prudes when it comes to people, but we think our classes should follow strict, puritan rules.

#### Incomplete Library Class

* p86

#### Large Class

* p78

Typically a catch-all class that all the functionality that doesn't go anywhere else is placed in.

*See [Single Responsibility Principle][srp]*

#### Lazy Class

* p83

Each class you create costs money to maintain and understand. A class that isn't doing enough to pay for itself should be eliminated.

#### Long Method

* p76

The longer a procedure is, the more difficult it is to understand.

#### Long Parameter List

* p78

More than three arguments to a function is generally an issue.

#### Message Chains

* p84

You see message chains when a client asks one object for another object, which the client then asks for yet another object, which the client then asks for yet another another object, and so on. This is distinct from [fluent interfaces][fluent] in that with fluent interfaces all of the functions in the chain are essentially called on the first object.

```java
// Message Chain
double salary = database.getCompany(companyName).getManager(managerName).getTeamMember(employeeName).getSalary();

// Fluent Interface
canvas.drawLine(from, to)
      .drawCircle(center, radius)
      .drawText(upperLeft, someText);
```

In the above example, the function calling the message chain has to understand that it needs to go to the database, get the company object, get the manager object from that, get the individual employee's object from there and finally get the salary. If the structure of how employees are stored changes, this code will break. It would be better to simply ask the database for the employee by name and then ask that for its salary, then the structure of how employees are stored can change and the code will continue to work.

#### Middle Man

* p85

You look at a class' interface and find half the methods are delegating to this other class.

#### Parallel Inheritance Hierarchies

* p83

Parallel inheritance hierarchies is really a special case of shotgun surgery. In this case, every time you make a subclass of one class, you also have to make a subclass of another.

#### Primitive Obsession

* p81

People new to objects usually are reluctant to use small objects for small tasks, such as money classes that combine number and currency, ranges with an upper and a lower, and special strings such as telephone numbers and ZIP codes.

#### Refused Bequest

* p87

A class that inherits from another, but hides or removes a lot of the functionality of the parent class.

#### Shotgun Surgery

* p80

Shotgun surgery is similar to divergent change but is the opposite. You whiff this when every time you make a kind of change, you have to make a lot of little changes to a lot of different classes. When the changes are all over the place, they are hard to find, and it's easy to miss an important change.

#### Speculative Generality

* p83

You get it when people say, "Oh, I think we need the ability to do this kind of thing someday" and thus want all sorts of hooks and special cases to handle things that aren't required. The result often is harder to understand and maintain. If all this machinery were being used, it would be worth it. But if it isn't, it isn't. The machinery just gets in the way, so get rid of it.

#### Switch Statements

* p82

Often you find the same switch statement scattered about a program in different places. If you add a new clause to the switch, you have to find all these switch statements and change them.

#### Temporary Field

* p84

Sometimes you see an object in which an instance variable is set only in certain circumstances. Such code is difficult to understand, because you expect an object to need all of its variables.

### Clean Code

The Code Smells from Clean Code seem to devolve into "do things this way" rather than "this is an indicator of bad code that should be changed".

#### Artificial Coupling

* Clean Code p293

#### Base Classes Depending on Their Derivatives

* Clean Code p291

#### Build Requires More Than One Step

* Clean Code p287

Building a project should be a single trivial operation. You should not have to check many little pieces out from source code control. You should not need a sequence of arcane commands or context dependent scripts in order to build the individual elements. You should not have to search near and far for all the various little extra JARs, XML files, and other artifacts that the system requires. You *should* be able to check out the system with one simple command and then issue one other simple command to build it.

```bash
git clone mySystem
cd mySystem
ant all
```

#### Clutter

* Clean Code p293

#### Code at Wrong Level of Abstraction

* Clean Code p290

Consider the following code:

```java
public interface Stack {
  Object pop() throws EmptyException;
  void push(Object o) throws FullException;
  double percentFull();

  class EmptyException extends Exception {}
  class FullException extends Exception {}
}
```

The `percentFull` function is at the wrong level of abstraction. Although there are many implementations of `Stack` where the concept of *fullness* is reasonable, there are other implementations that simply *could not know* how full they are. So the function would be better placed in a derivative interface such as `BoundedStack`.

#### Commented Out Code

* Clean Code p287

#### Dead Code

* Clean Code p292

#### Dead Function

* Clean Code p288

#### Don't Be Arbitrary

* Clean Code p303

#### Encapsulate Boundary Conditions

* Clean Code p304

#### Encapsulate Conditionals

* Clean Code p301

#### Flag Arguments

* Clean Code p288

#### Follow Standard Conventions

* Clean Code p299

#### Function Names Should Say What They Do

* Clean Code p297

#### Functions Should Do One Thing

* Clean Code p302

#### Functions Should Only Descend One Level of Abstraction

* Clean Code p304

#### Hidden Temporal Coupling

* Clean Code p302

#### Inappropriate Information

* Clean Code p286

It is inappropriate for a comment to hold information better held in a different kind of system such as your source code control system, your issue tracking system or any other kind of record-keeping system.

#### Inappropriate Static

* Clean Code p296

#### Inconsistency

* Clean Code p292

#### Incorrect Behavior at the Boundaries

* Clean Code p289

#### Keep Configurable Data at High Levels

* Clean Code p306

#### Magic Numbers

* Clean Code p300

#### Make Logical Dependencies Physical

* Clean Code p298

#### Misplaced Responsibility

* Clean Code p295

#### Multiple Languages in One Source File

* Clean Code p288

#### Negative Conditionals

* Clean Code p302

#### Obscured Intent

* Clean Code p295

#### Obvious Behavior is Unimplemented

* Clean Code p288

For example, consider a function that translates the name of a day to an `enum` that represents the day.

```java
Day day = DayDate.StringToDay(String dayName);
```

We would expect the string `"Monday"` to be translated to `Day.MONDAY`. We would also expect the common abbreviations to be translated, and we would expect the function to ignore case.

When an obvious behavior is not implemented, readers and users of the code can no longer depend on their intuition about function names. They lose their trust in the original author and must fall back on reading the details of the code.

#### Obsolete Comment

* Clean Code p286

A comment that has gotten old, irrelevant, and incorrect is obsolete.

#### Output Arguments

* Clean Code p288

Output arguments are counterintuitive.

#### Overridden Safeties

* Clean Code p289

#### Poorly Written Comment

* Clean Code p287

#### Redundant Comment

* Clean Code p286

A comment is redundant if it describes something that adequately describes itself.

```java
i++; // increment i
```

#### Selector Arguments

* Clean Code p294

#### Tests Require More Than One Step

* Clean Code p287

You should be able to run *all* the unit tests with just one command.

#### Too Much Information

* Clean Code p291

#### Understand the Algorithm

* Clean Code p297

#### Use Explanatory Variables

* Clean Code p296

#### Vertical Separation

* Clean Code p292

## Bibliography

* Fowler, Martin *et al*. *[Refactoring][refactoring]*. Addison-Wesley Professional, July 8, 1999.
* Martin, Robert C. *[Clean Code][clean-code]*. Prentice Hall, August 11, 2008.

[clean-code]: http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/
[fluent]: http://en.wikipedia.org/wiki/Fluent_interface
[refactoring]: http://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672/
[srp]: http://en.wikipedia.org/wiki/Single_responsibility_principle
