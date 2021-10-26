# FIT2099 Exam

## Code Revision Example
```java
public interface Shape {
  public void draw();
  public double getArea();
}
```

You have been asked to write the code to calculate the area of two shapes:
Circle and Triangle. Please, create two classes using the Shape interface and
following the next requirements:
• The area of a Circle is pi times the radius squared (hint: use Math.PI to get
the value of PI).
• The area of a Trinagle is the product of the height and width of the triangle
divided by 2.
• You don’t have to code the logic for drawing the shapes, you can simply print
a message using System.out.println("some text");

### Circle
```java

public Circle implements Shape() {
   
   private double radius;
    
    public Circle(radius) {
        this.radius;
    }

    @Override
    public void draw() {
        System.out.println("Draw the circle");
    }
    
    @Override
    public double getArea() {
        return radius^2*Math.PI;
    }
    
}

```

### Triangle
```java

public Triangle implements Shape() {
   
    private double width;
    private double height;

   
    public Triangle(width, height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public void draw() {
        System.out.println("Draw the triangle");
    }
        
    @Override
    public double getArea() {
        return 0.5*width*height;
    }
    
}

```
