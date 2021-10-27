# Refactoring

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Refactoring](#refactoring)
    - [Why do we need to refactor?](#why-do-we-need-to-refactor)
    - [How to refactor?](#how-to-refactor)
    - [Refactoring code smells](#refactoring-code-smells)
        - [Long methods](#long-methods)
        - [Wrong variable names](#wrong-variable-names)
        - [Method doesn't use anything class containing it. Feature envy](#method-doesnt-use-anything-class-containing-it-feature-envy)
        - [Temporary Variables](#temporary-variables)
        - [Getting rid of the formatter](#getting-rid-of-the-formatter)
    - [Simple vs complex refactoring](#simple-vs-complex-refactoring)
    - [Switch statements](#switch-statements)

<!-- markdown-toc end -->


## Why do we need to refactor?
* Refactoring makes changes easier to make.

* The client has additional requirements
    * they would like to be able to get more things done.
    * they plan to add further types

**Example:** 
A habit tracking application that allows user to keep track of habits they need to follow as a list of habits. A new time functionality that stores the time and alerts the user to perform a certain habit like exercise.


**Example:** 
A habit tracking application that allows user to keep track of habits they need to follow as a list of habits. New templates like habits scoreboard, implementations intentions, habit stacking, habit tracker, habit contract.

## How to refactor?

**Note:** You can perform multiple refactoring methods for one code smell

* Identify a code smell
* Identify a refactoring that will fix the code smell
* Apply the refactoring
* Test that the code still works
    * if not, fix it
    * if so, commit the refactored code
* Keep doing this until code quality is acceptable

## Refactoring code smells

### Long methods

* Extract method refactor
    * Extracting parts of the method
    * IDE can do this for you

### Wrong variable names

* rename variable refactor
    * This makes sure that everything still makes sense even if it's in a new context

### Method doesn't use anything class containing it. Feature envy

* Move instance method refactor
    * move method across to a different class.

### Temporary Variables


* Replace temporary variables with query
  * accessible to any method in the class (class field variables)
  * only useful within their own routine
  * easy to lose track of


### Getting rid of the formatter
**Example:** We have a formatter to format number amounts (stored in cents) to Australian dollars Note the repeated code including division by 100

* Can extract that into a method
  * gets rid of another local variable
  * reduces duplicate code

## Simple vs complex refactoring
These refactorings were pretty simple
Not so simple that we could just get a machine to do them…
But I didn't have to think about them much

## Switch statements

* Classes using switch states for different types can be solved with **polymorphism**

* Create abstract class and override methods in subclasses. Subclasses are different types.
