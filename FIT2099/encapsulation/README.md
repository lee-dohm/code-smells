# Encapsulation

## Packages
Grouping several classes together by packages.

* It makes it easier to find	related	classes
* It gives	us	a mechanism	to **prevent name clashes**. For example, the name Counter is quite	common.	It	is	likely	that someone else somewhere	has	used that name. Placing	our	counter	classes	in a package with a	very specific name means that we can distinguish them from any other classes elsewhere with	the	**same class names**.
• Often	**related	classes	necessarily	depend on each other**. When we can’t eliminate dependencies, we want to place the elements that must depend on	each other together inside an **encapsulation boundary**.

### Reduce dependencies as much as possible.

### Group elements that must depend on each other together inside an encapsulation boundary

## Minimise dependencies that cross encapsulation boundaries

## Declare things in the tightest possible scope

Can be achieve by language constructs that make it impossible to create dependencies that cross boundaries. 

For example, in Java we can **declare attributes and operations to be private to a class**. 

If no access level modifier is used, the default visibility level in Java is **package-private**.


## Declare things in the tightest possible scope

The tighter the scope in which something is visible, the **less risk there is that something written can depend on it**, and thus the less the risk that it will be a future point of failure when it is changed. 

So, for example: **declare local variables** in the loops where they are used, rather than at the beginning of a method; use local variables rather than attributes whenever possible; keep members that implement an abstraction together inside a class; keep classes that work together inside packages, and so on.


