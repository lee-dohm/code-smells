# DRY (Do not repeat yourself):

Cut and pasted code is not good programming practice because this is a sign of shared responsibility within the code (violating SRP)

This can lead to poor abstraction and cognitive capacity being overloaded so it is hard to maintain and understand. Also, there would be more connascence of algorithm or value because if there is changes to a certain area of code, all cut-and-pasted might need to be changed as well, so it is harder to test and maintain. Also this is a code smell so it is a technical debt that needs refactoring

Repeated code is harder to maintain
Repeated code is a source of technical debt
Repeated code is harder to test because it is no longer modular. Each separate repeated code need to be tested
If the developer copy and pasted the code, there might be lack of understanding in the code leading to incorrect results.

Sometimes there could be static polymophism with if and elsif statements for differnet classes, this could violate the open close principle because most of the code is repeated in the if blocks. Also when new change is introduced, more statements must be added manually and could be copy and pasted as well

Fix:

Refactor:

Extract the repeated group of code the repeated code into a separate method.

Inherentence: Create abstract classes or interfaces containing methods for the repeated code. Form design by contract where the repeated code can be reused in other classes using liskov subsitution princple. **Move repeated code from subclass to superclass.**

Static final variables and avoid literals in classes.


**Generics: If the repeated code handle different input types, may be possible to make the type a parameter**

Proposal A:

Liskov substitution principles has to be met. The precondition for myInteger is stronger than myRational and the post condition for myInteger is also weaker in postcondition so this this case myInteger should be a superclass to myRational.

By liskov subsitution principle, proposal B is more is correct because you can represent or substitue a insteger with a rational number but not vice versa.

However there could be a issue with design by contract because integer has a stronger preondition than myRational and weaker postcondition than myRational.

You cannot replace the contract with myRational with myInteger

because in order to meet design by contract: precondition must be no stronger and postcondition must be no weaker.

So basically integer cannot replace the contract of myRational

Precondition:

myRational: 

must be a integer

myInteger:
must be an integer
must be whole number

Post condition:

My Rational:

- nominator
- denominator

myInteger:

- one value

Static polymorphism and O/C principle

class myNumber {

  protected Integer num;
  public myNumber(Integer num ) {
      this.num = num;
  }

}

class myInteger extends myNumber {

    public myInteger(Integer num) {
        super((num));
    }
}

class myRational extends myNumber {

    private Integer denominator;

    public myRational(Integer nominator, Integer denom) {
        super(nominator);
        this.denominator = denom; 
    }

    public getRational() {
        return num/this.demoninator; 
    }
}
