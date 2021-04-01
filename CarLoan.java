public class CarLoan {
	public static void main(String[] args) {
    int carLoan = 10000;
    int loanLength = 3;// Years
    int interestRate = 5;// Percentage
    int downPayment = 2000;
    // Checking for errors where No. of years or Interest Rate cannot be less than or equal to zero.
    if (loanLength <= 0 || interestRate <= 0) {
      System.out.println("Error! You must take out a valid car loan.");
    }
    // Check if car can be paid in full.
    else if (downPayment >= carLoan) {
      System.out.println("The car can be paid in full.");
    }
    // If everything else is false this block of code gets executed.
    else {
      int remainingBalance = carLoan - downPayment;
      int months = loanLength * 12;
      int monthlyBalance = remainingBalance / months;
      int interest = ( monthlyBalance * interestRate ) / 100;
      int monthlyPayment = monthlyBalance + interest;
      System.out.println(monthlyPayment);
    }
	}
}
