# Encapsulation
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Encapsulation](#encapsulation)
    - [Packages](#packages)
        - [Reduce dependencies as much as possible.](#reduce-dependencies-as-much-as-possible)
        - [Group elements that must depend on each other together inside an encapsulation boundary](#group-elements-that-must-depend-on-each-other-together-inside-an-encapsulation-boundary)
    - [Minimise dependencies that cross encapsulation boundaries](#minimise-dependencies-that-cross-encapsulation-boundaries)
    - [Declare things in the tightest possible scope](#declare-things-in-the-tightest-possible-scope)
    - [Declare things in the tightest possible scope](#declare-things-in-the-tightest-possible-scope-1)

<!-- markdown-toc end -->

## What is encapsulation?

The realisation and the access to the names, meanings, values, and responsibilities of a class is entirely separated.
* A software development technique
* Isolate a system function or a set of data and operations on those data within a module and providing precise specifications for the module.

| Within encapsulation boundary      | Outside encapsulation boundary        |
| :-:                                | :-:                                   |
| External interface (preconditions) | Internal implementations              |
| set of data                        | realisation                           |
| operations on the data             | precise specifications for the module |
| names                              | Methods (setters getters)             |
| meanings                           |                                       |
| values                             |                                       |
| responsibilities                   |                                       |
| **Private** variable               |                                       |

## Why encapsulate?
* Code is simplier as you don't have to know every little single detail of every module. Only need to know the interface
* Avoids unnecessary connascence, coupling as well as degree
* Reducing Dependencies (**ReD**)

## Information hiding
* Every module is characterised by its **Knowldege of a *design decision* which hides from all others**
* Interface or definition chosen to reveal as little has possible about it's inner workings: 
    * **inside single module**
    * Data structures
    * Internal linings
    * Accessing procedures
    * modifying procedures

## Encapsulation boundaries
* the class
* the package
* the module
* even the **scope defined within methods** by curly braces {}

It is ideal to **minimise access across classes or packages**

## Encapsulation in java

Reducing connascence using encapsulation
  * [ ] Avoid public attributes, only make them public, protected or none where necessary

  * [ ] Keep the class package-private if not needed

Basic unit of Java programs is the class

  * [ ] can group classes into packages

  * [ ] can group packages into modules (as of Java 9)

  * [ ] Can restrict access to anything in the class to:

    * [ ] within the class only (private)

    * [ ] within the package only (no access modifier - default)

    * [ ] only to sub classes and within the package (protected)

    * [ ] no restrictions (public)

Always make variable private when not sure

| **Modifier** | Class | Package | Subsclass | World |
| :-:          | :-:   | :-:     | :-:       | :-:   |
| public       | yes   | yes     | yes       | yes   |
| protected    | yes   | yes     | yes       | no    |
| no modifier* | yes   | yes     | no        | no    |
| private      | yes   | no      | no        | no    |


## Modules

A **collection of Java packages organised in the usual way**

Includes a **module descriptor file** (**module-info.java**) that specifies:
* the **name** of the module
* any other modules that this module **depends on**
* which packages are **public**
* any **services** this module offers
* which services this module **consumes**
e which other classes may apply **reflection** to packages in this module

```java
module my-module {
  requires javafx.controls; // dependencies. Javafx.controls is read by my-module
  exports my.program.package; // make package visible publicly
  exports my.program.package
    to other-module; // make package only visible to other-module
  provides someInterface // implements this interface
  with my.program.Implementation;
}
```

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

## Minimising APIs

Application programming interface: that part of a class/package/module that is accessible from outside aka public interface

The **smaller and less complicated the interface is, the fewer opportunities for connascence** there are 

## Defensive copy

When getters return a reference to a private object that is **mutable** i.e. with public attributes or mutator methods (setters) other than constructor.

You should make a copy and return that Otherwise, you lose benefit of encapsulation this is called a **privacy leak**

Lose control of connascence?

## Privacy leaks

```java
public class GasTank {
    private Fraction fuel;
    public gasTank() {
        fuel = new Fraction(1,1);
    }

    public Fraction getFuel() {
         return fuel;
    }

    public void setFuel(Fraction f) {
        (if f.asDouble <= 1) {
            fuel = f;
        }
    }

}

// Privacy leak:

/**
/* What happens here is the tank variable points to the memory address of the tank's fuel
/* fuelread points to tank's fuel which points to the same memory address.
/* Hence modifying fuelRead also modifies tank's fuel on the stack.
*/

GasTank tank = new GasTank();
Fraction fuelRead = tank.getFuel();

fuelRead.setNumerator(2);

```
