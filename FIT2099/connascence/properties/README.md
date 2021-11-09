# Properties of connnascence


> "strive for low coupling and high cohesion". 

We should **strive for code that separates tasks and doesn't rely heavily on each other**.

## Cohesiveness
Grouping together code that contribute to a single task.

> Don't try to have too many games in one package ... Individually, those each could have been good games. Together they fought with each other.

In OOP, each object should only have one responsibility. Every behaviour of that object should only do one task. Any more that that you will have a much harder time making changes to the code.

### Why high cohesion?
Highly cohesive code (organised by functionality and have only one task) is **reusable, simple, easy to understand**.

Sometimes it creates objects that are **small and focused**.

### Solution


#### Asteroid

Now let's define a ship as having behaviours of turning, moving and firing.

If we write one function it will become messy (all three behaviour at once). Instead we separate into individual functions that groups similar code together, help creating **highly cohesive code**.

```java
/*
* The ship class
*/
public class Ship() {
  /*
  * turning the ship
  */

  private void rotate() {
      //code
  }


  private void move() {
  //code
  }

  private void fire() {
      //code
  }

}

```


## Coupling
Coupling is the principle of "**separation of concerns**". 

This means that one object doesn't directly change or modify the state or behavior of another object.

### CSS and HTML
A good example of coupling is HTML and CSS. Before CSS, HTML was used for both markup and presentation. This created bloated code that was hard to change and difficult to maintain. 

With the advent of CSS, HTML became used just for markup, and CSS took over for presentation. 

This made the code fairly clean and easily changeable. The concerns of presentation and markup were separated.


### Why low coupling
Loose coupling lets the **code be more flexible, more changeable, and easier to work** with.

Objects that rely **on other objects and can modify the states of other objects** are said to be tightly coupled. 

Tight coupling creates situations where modifying the code of one object also requires changing the code of other objects (also known as a ripple effect). **Tightly coupled code is also harder to reuse** because it can't be separated.

### Solution

In Asteroids, a ship can fire a bullet, a bullet can hit an asteroid and a flying saucer, and an asteroid and a flying saucer can hit the ship. Our relations diagram then looks as follows:

### Tightly coupled 
![Alt Text](pic1.png) 

### Less coupled with intermediary class
![Alt Text](pic2.png) 

This relations diagram looks a lot better and creates a very loosely coupled system. In this system, if we were to add an object, such as a meteor, we could easily do so without having to change how the ship or bullet objects function - we'd just let our **intermediary class** take care of it all.

## Strength
The strength of a form of connascence is determined by the **ease with which that type of coupling can be refactored**. 

For example, connascence of name is a weak form of connascence because renaming entities across a codebase is usually reasonably trivial. However, connascence of meaning is considered a stronger form of connascence since semantic meaning is harder to find across an entire codebase.

**Static connascences are considered to be weaker than dynamic connascences**, since static connascences can be determined simply by examining the source code. **Dynamic connascences require knowledge of run-time behavior**, and thus are harder to reason about.

**Strength and locality should be considered together. Stronger forms of connascence are often found within the same function, class, or module where their impact can be more easily observed.
**

## Locality

The locality of an instance of connascence is how close the two entities are to each other. 

Code that is **close together** (in the same module, class, or function) should typically have more, and higher forms of connascence than code that is far apart (in separate modules, or even codebases). 

**Many of the stronger forms of connascence that can be devastating to the readability and maintainability of a codebase when they appear far apart are innocuous when close together.
**

Locality matters! Stronger connascences are more acceptible within a module. Weaker connascences should be used between entities that are far apart (in separate modules or even codebases).

![Alt Text](pic3.png) 

## Degree
The degree of a piece of connascence is related to the **size of its impact. Does the coupling in question affect 2 entities, or 200**?
