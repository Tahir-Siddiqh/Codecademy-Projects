public class Calculator{
  // Constructor for class Claculator
  public Calculator(){
  }
  // add method adds two integers
  public int add(int a, int b){
    int add = a + b;
    return add;
  }
  // subtract method subtracts two integers
  public int subtract(int a, int b){
    int subtract = a - b;
    return subtract;
  }
  // multiply method multiplies two integers
  public int multiply(int a, int b){
    int multiply = a * b;
    return multiply;
  }
  // divide method divides two integers
  public int divide(int a, int b){
    int divide = a / b;
    return divide;
  }
  // modulo method find modulos of two integers
  public int modulo(int a, int b){
    int modulo = a % b;
    return modulo;
  }
  // main
  public static void main(String[] args){
    Calculator myCalculator = new Calculator();
    System.out.println(myCalculator.add(5,7));
    System.out.println(myCalculator.subtract(45,11));
  }
}
