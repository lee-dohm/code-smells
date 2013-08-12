# Code Smells

[Code Smell][definition] is a term coined by Kent Beck and introduced in Martin Fowler's book, [Refactoring][refactoring]. Code Smells are patterns of code that suggest there might be a problem, that there might be a better way of writing the code or that more design perhaps should go into it. They were originally intended to be used as a guide for when to refactor code. More recently though, I have found them to be very useful in code reviews as a succinct language for when and how to clean up certain chunks of code. I wanted to document and standardize this language so as to make code reviews more valuable.

The book [Anti Patterns][antipatterns] by William J. Brown *et al* is another book that describes the same kinds of phenomena. While the Anti Patterns book came out over a year prior to Refactoring, I think the term "code smell" is better recognized. So that is what I will use as the overarching term for these degenerate code templates.

This list is specifically written with a header for each smell to enable linking. One can simply craft a link with an anchor target of the rule name in lower case with hyphens instead of spaces to link to a specific rule. For example: `https://github.com/lee-dohm/code-smells#duplicate-code`

All page numbers are from [Refactoring][refactoring] unless otherwise noted.

## Why Ruby for the Code Examples?

I chose [Ruby][ruby] for the code examples mostly because its ability to compactly express ideas will be able to quickly convey the point of the examples with a minimum of confusion. As this document grows, examples in other languages may be added as needed.

## Code Smells That Suggest Refactoring

There are different levels of code smells. The original intent of code smells was not just as a signal that something was wrong with the code, but to give specific advice on how to refactor that code. This list contains smells that are of the refactoring class.

### Alternative Classes with Different Interfaces

* p85

Classes that do similar things but have different interfaces should probably be refactored to have similar interfaces.

### Comments

* p87

> It's surprising how often you look at thickly commented code and notice that the comments are there because the code is bad. <br/>
> -- *[Refactoring][refactoring]*

Many comments aren't bad in and of themselves. But comments are often used as a crutch to allow poorly written code to remain so. If at all possible, code should be written so that the comments are not necessary.

Comments within functions should bear extra scrutiny. Comments within the body of functions are, almost without exception, unnecessary in well-written code. Well-written code consists of short, declarative functions that have good identifier names. It should be obvious *what* the code is doing from the code itself. What the code often cannot describe though is *why* the code is doing what it is doing. Here is an example from one of my projects:

```ruby
# Indicates whether `color` is a valid SVG color string.
#
# [SVG color descriptions](http://www.w3.org/TR/SVG/types.html#DataTypeColor) are one of
# the following:
#
# * RGB values
#     * `#rgb`
#     * `#rrggbb`
#     * `rgb(255, 0, 0)` - *not currently supported*
#     * `rgb(100%, 0%, 0%)` - *not currently supported*
# * [Color names](http://www.w3.org/TR/SVG/types.html#ColorKeywords)
def valid_color?(color)
  return color =~ /^#[0-9A-Fa-f]{3}([0-9A-Fa-f]{3})?$/ if color[0] == '#'

  COLOR_NAMES.include?(color)
end
```

The code by itself is quite clear in what it is doing, so long as one understands regular expressions. But one wouldn't have the extra understanding of the *why* the code is written this way, that it is validating SVG color codes, or how exactly the code could or should be modified without this extra information. One could easily see someone coming along and adding or subtracting functionality from this method and introducing bugs if they did not know that this is intended specifically to conform to the SVG definition of a color.

#### Documentation Comments

Documentation comments are somewhat contentious. Some think they are important and some consider them to be a code smell. I personally believe that documentation comments are quite useful so long as they are well written and are kept up-to-date with the code. Well written documentation comments that are used to generate developer documentation can allow one to understand a code base much more quickly than rifling through the code itself. Consider this, when you are working with your pet language; would you want to dive deep into the code for the language itself to understand how opening a file really works? Or would you rather have some documentation that tells you how to open a file for writing?

### Data Class

* p86

> These are classes that have fields, getting and setting methods for the fields, and nothing else. Such classes are dumb data holders and are almost certainly being manipulated in far too much detail by other classes. <br/>
> -- *[Refactoring][refactoring]*

One might argue that this is in direct conflict with [Primitive Obsession](#primitive-obsession). But Primitive Obsession recommends creating a class for single pieces of data that have specific boundaries or properties for which the built-in data types are not well-suited. Data Class is about creating a class that simply ties a bunch of pieces of data together and provides no other value. For example, the classic `Point` class is potentially an example:

```ruby
class Point
  attr_accessor :x
  attr_accessor :y

  def initialize(x = 0, y = 0)
    @x = x
    @y = y
  end
end
```

But perhaps we calculate the distance of two points from each other (or from the origin) in a few places. We should then refactor that to:

```ruby
class Point
  attr_accessor :x
  attr_accessor :y

  def initialize(x = 0, y = 0)
    @x = x
    @y = y
  end

  def distance(point = Point.new)
    Math.sqrt((@x - point.x) ** 2 + (@y - point.y) ** 2)
  end
end
```

So what really makes this a code smell is that, very often, a Data Class has regular operations performed on it spread around the code base that should be merged into the class itself.

### Data Clumps

* p81

> Data items tend to be like children; they enjoy hanging around in groups together. Often you'll see the same three or four data items together in lots of places: fields in a couple of classes, parameters in many method signatures. Bunches of data that hang around together really ought to be made into their own object. <br/>
> -- *[Refactoring][refactoring]*

A simple example would be a graphics library that takes `x` and `y` coordinate parameters all over the place:

```ruby
def draw_line(start_x, start_y, end_x, end_y)
  # snip
end

def draw_circle(x, y, radius)
  # snip
end

# etc
```

when it should just have a `Point` class:

```ruby
class Point
  # details removed
end

def draw_line(start, end)
  # snip
end

def draw_circle(center, radius)
  # snip
end
```

### Disjointed API

* [Refactoring: Ruby Edition][refactoring-ruby]

> Libraries are often written with flexibility as the number one priority. The author needs to build in this flexibility so that her library can be used by many different people in many different ways. This flexibility often presents itself as a relatively fine-grained, disjointed API, with many configuration options. <br/>
> -- *[Refactoring: Ruby Edition][refactoring-ruby]*

### Divergent Change

* p79

> Divergent change occurs when one class is commonly changed in different ways for different reasons. If you look at a class and say, "Well, I will have to change these three methods every time I get a new database; I have to change these four methods every time there is a new financial instrument," you likely have a situation in which two objects are better than one. That way each object is changed only as a result of one kind of change. <br/>
> -- *[Refactoring][refactoring]*

*See [Single Responsibility Principle][srp]*

### Duplicate Code

* p76

> If you see the same code structure in more than one place, you can be sure that your program will be better if you find a way to unify them. <br/>
> -- *[Refactoring][refactoring]*

By far the most common code smell, Duplicate Code comes in many shapes and sizes. There are the obvious instances where chunks of code are simply copy and pasted around the code base. But there are also more subtle instances too where chunks of code are parameterized to one extent or another. Figuring out that bits of code are duplicates of each other and how to remove that duplication is what separates beginning developers from intermediate and advanced developers.

*See [Don't Repeat Yourself][dry]*

### Feature Envy

* p80

> A method that seems more interested in a class other than the one it actually is in. The most common focus of the envy is the data. We've lost count of the times we've seen a method that invokes half-a-dozen getting methods on another object to calculate some value. <br/>
> -- *[Refactoring][refactoring]*

This is the function-level version of [Middle Man](#middle-man).

### Inappropriate Intimacy

* p85

> Sometimes classes become far too intimate and spend too much time delving in each others' private parts. We may not be prudes when it comes to people, but we think our classes should follow strict, puritan rules. <br/>
> -- *[Refactoring][refactoring]*

### Incomplete Library Class

* p86

### Large Class

* p78

Typically a catch-all class that all the functionality that doesn't go anywhere else is placed in.

*See [Single Responsibility Principle][srp]*

### Lazy Class

* p83

> Each class you create costs money to maintain and understand. A class that isn't doing enough to pay for itself should be eliminated. <br/>
> -- *[Refactoring][refactoring]*

While [Data Class](#data-class) and [Primitive Obsession](#primitive-obsession) are examples of classes not being powerful enough or simply not written, a Lazy Class is powerful enough to stand on its own. It simply isn't used much or at all. If a class just isn't used much, then perhaps its functionality needs to go someplace else.

Striking the right balance between Lazy Class and [Feature Envy](#feature-envy) is sometimes challenging.

### Long Method

* p76

The longer a function is, the more difficult it is to understand.

### Long Parameter List

* p78

More than three arguments to a function is generally an issue.

### Message Chains

* p84

You see message chains when a client asks one object for another object, which the client then asks for yet another object, which the client then asks for yet another another object, and so on.

```ruby
# Message Chain
salary = database.get_company(company_name).
                  get_manager(manager_name).
                  get_team_member(employee_name).
                  salary

# Better
salary = database.get_employee_by_name(employee_name).salary
```

In the above example, the function calling the message chain has to understand that it needs to go to the database, get the company object, get the manager object from that, get the individual employee's object from there and finally get the salary. If the structure of how employees are stored changes, this code will break. It would be better to simply ask the database for the employee by name and then ask that for its salary, then the structure of how employees are stored can change and the code will continue to work.

Message Chains are distinct from [fluent interfaces][fluent] in that with fluent interfaces all of the functions in the chain are essentially called on the first object.

```ruby
# Fluent Interface
canvas.draw_line(from, to).
       draw_circle(center, radius).
       draw_text(upperLeft, someText)
```

### Metaprogramming Madness

* [Refactoring: Ruby Edition][refactoring-ruby]

> While in most cases Ruby's dynamic nature provides great benefits, it can be misused. Some metaprogramming techniques can result in obfuscated code. The `method_missing` hook, for example, often results in code that is difficult to understand. <br/>
> -- *[Refactoring: Ruby Edition][refactoring-ruby]*

### Middle Man

* p85

> You look at a class' interface and find half the methods are delegating to this other class. <br/>
> -- *[Refactoring][refactoring]*

This is the class-level version of [Feature Envy](#feature-envy).

### Parallel Inheritance Hierarchies

* p83

> Parallel inheritance hierarchies is really a special case of shotgun surgery. In this case, every time you make a subclass of one class, you also have to make a subclass of another. <br/>
> -- *[Refactoring][refactoring]*

### Primitive Obsession

* p81

> People new to objects usually are reluctant to use small objects for small tasks, such as money classes that combine number and currency, ranges with an upper and a lower, and special strings such as telephone numbers and ZIP codes. <br/>
> -- *[Refactoring][refactoring]*

Primitive Obsession is an over-reliance on the built-in simple data types in a language such as integers, floating-point numbers, strings and the like. For example, a string can hold an hexadecimal color code such as `C0C0C0`. But even a simple `Color` class can help reduce bugs:

```ruby
class Color
  attr_reader :code

  def initialize(code)
    @code = validate(code)
  end

  def to_s
    @code.to_s
  end

  private

  def validate(code)
    raise InvalidColorError unless code =~ /[0-9A-Fa-f]{6}/

    code
  end
end
```

### Refused Bequest

* p87

A class that inherits from another, but hides or removes a lot of the functionality of the parent class.

### Repetitive Boilerplate

* [Refactoring: Ruby Edition][refactoring-ruby]

> One of the easiest ways to remove duplication is [the Extract Method refactoring]. Extract the method and call it from multiple places. Some kinds of methods become so commonplace that we can go even further. Take for example attr_reader in Ruby. Implementing attribute readers is so common in object-oriented languages that the author of Ruby decided to provide a succinct way to declare them. <br/>
> -- *[Refactoring: Ruby Edition][refactoring-ruby]*

### Shotgun Surgery

* p80

> [Shotgun Surgery] is similar to [the Divergent Change code smell] but is the opposite. You whiff this when every time you make a kind of change, you have to make a lot of little changes to a lot of different classes. When the changes are all over the place, they are hard to find, and it's easy to miss an important change. <br/>
> -- *[Refactoring][refactoring]*

### Speculative Generality

* p83

> You get it when people say, "Oh, I think we need the ability to do this kind of thing someday" and thus want all sorts of hooks and special cases to handle things that aren't required. The result often is harder to understand and maintain. If all this machinery were being used, it would be worth it. But if it isn't, it isn't. The machinery just gets in the way, so get rid of it. <br/>
> -- *[Refactoring][refactoring]*

*See [You Ain't Gonna Need It][yagni]*

### Switch Statements

* p82

> Often you find the same switch statement scattered about a program in different places. If you add a new clause to the switch, you have to find all these switch statements and change them. <br/>
> -- *[Refactoring][refactoring]*

### Temporary Field

* p84

> Sometimes you see an object in which an instance variable is set only in certain circumstances. Such code is difficult to understand, because you expect an object to need all of its variables. <br/>
> -- *[Refactoring][refactoring]*

## Bibliography

* Fields, Jay *et al*. *[Refactoring: Ruby Edition][refactoring-ruby]*. Addison-Wesley Professional, October 25, 2009.
* Fowler, Martin *et al*. *[Refactoring][refactoring]*. Addison-Wesley Professional, July 8, 1999.
* Martin, Robert C. *[Clean Code][clean-code]*. Prentice Hall, August 11, 2008.

[antipatterns]: http://www.amazon.com/AntiPatterns-Refactoring-Software-Architectures-Projects/dp/0471197130/
[clean-code]: http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/
[definition]: http://martinfowler.com/bliki/CodeSmell.html
[dry]: http://en.wikipedia.org/wiki/Don%27t_Repeat_Yourself
[fluent]: http://en.wikipedia.org/wiki/Fluent_interface
[refactoring]: http://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672/
[refactoring-ruby]: http://www.amazon.com/Refactoring-Ruby-Edition-Jay-Fields/dp/0321603508/
[ruby]: http://www.ruby-lang.org
[srp]: http://en.wikipedia.org/wiki/Single_responsibility_principle
[yagni]: http://en.wikipedia.org/wiki/YAGNI
