## Confusing abstraction with abstract

|                              | Abstract class                                               | Interfaces                                     |
| :-:                          | :-:                                                          | :-:                                            |
| Types of variable            | Static and non-static                                        | Final by default                               |
| Access modifiers for members | All                                                          | Public by default                              |
| Subclasses                   | **extends** abstract class                                   | implements interface                           |
| Subclasses                   | Can extend only one abstract class                           | Can implement multiple interfaces              |
| Methods                      | Can be implemented and also have 0 or more abstract methods  | Implicitly abstract and cannot be instantiated |
| Instantiated                 | Cannot be instantiated but can be invoked if a main() exists | Cannot be instantiated                         |
| Speed                        | Fast                                                         | Slow                                           |


