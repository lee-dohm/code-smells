# Coding practices


## Avoid use of literals (magic numbers and variables)
>Numerical constants (literals) should not be coded directly, **except for -1, 0, and 1, which can appear in a for loop as counter values. ** <br />

Not really exclusive to OOP.

### Static final fields
The solution to these issues is to give such literals a name and type which are declared once (DRY), and can never change.

 * Used to represent a constant
 * Common to all instances of the class and never changes.
 * Declared once and never changes (DRY principle adhered)

```java
public class Watch3 extends Watch {
  ...
  static final int MAX_HOURS = 24;
  static final int MAX_MINUTES = 60;
  static final int MAX_SECONDS = 60;

  public Watch3() {
    hours = new MaxCounter(MAX_HOURS);
    this.addCounter(hours);
    minutes = new LinkedCounter(MAX_MINUTES, hours);
    this.addCounter(minutes);
    seconds = new LinkedCounter(MAX_SECONDS, minutes);
    this.addCounter(seconds);
    }

}
```

#### Does not need **private** modifier for final fields
**Static final fields can’t be modified after creation**, so there is no danger of unauthorised modification as there is with non-final fields (which should all be private). 

## Reduce dependencies whenever possible! (ReD)

### Direct dependencies
* Obvious dependencies we can see at the level of particular attributes or methods. A compiler can see these dependencies, and thus tools exist that can help us find and manage them. We can call these direct dependencies.


### Indirect dependencies
They exist because of the meaning of various elements of the code to humans, and **only a human programmer can know they exist**. For example, the values of variables or literals in different parts of the program can be related to each other, and **must be changed simultaneously if correctness is to be maintained** (connnascence of value, could occur at low locality (different classes or packages)).

These types of dependencies must be **carefully documented or even eliminated**.

