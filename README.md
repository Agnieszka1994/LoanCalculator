# LoanCalculator
This repository contains the Loan Calculator that calculates real loan parameters using Python’s mathematical capabilities. 
The calculator is able to work with different types of payment and accept command-line arguments.

## Objectives
- **Calculation of differentiated payments.** To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
- **Ability to calculate the values for annuity payment** (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter is unknown. This is the value the user wants to calculate.
- Handling of invalid parameters.

### Sample usage
The greater-than symbol followed by a space (> ) represents the user input from the command-line. \
**Example 1: calculating differentiated payments:**
```
> python creditcalc.py --type=diff --principal=2000000 --periods=12 --interest=9
Month 1: payment is 181667
Month 2: payment is 180417
Month 3: payment is 179167
Month 4: payment is 177917
Month 5: payment is 176667
Month 6: payment is 175417
Month 7: payment is 174167
Month 8: payment is 172917
Month 9: payment is 171667
Month 10: payment is 170417
Month 11: payment is 169167
Month 12: payment is 167917

Overpayment = 97504
```
**Example 2: calculate the annuity payment for a 62-month loan with a principal amount of 1,000,000 at 5.5% interest**
```
> python LoanCalc.py --type=annuity --principal=1000000 --periods=62 --interest=5.5
Your annuity payment = 18566!
Overpayment = 151092!
```
**Example 3: fewer than four arguments are given**
```
> python LoanCalc.py --type=annuity --principal=1000000 --periods=62
Incorrect parameters.
```
**Example 4: calculate differentiated payments given a principal of 450,000 over 10 months at an interest rate of 8.2%**
```
> python LoanCalc.py --type=diff --principal=450000 --periods=10 --interest=8.2
Month 1: payment is 48075
Month 2: payment is 47768
Month 3: payment is 47460
Month 4: payment is 47153
Month 5: payment is 46845
Month 6: payment is 46538
Month 7: payment is 46230
Month 8: payment is 45923
Month 9: payment is 45615
Month 10: payment is 45308

Overpayment = 16915
```
**Example 5: calculate the principal for a user paying 8,755 per month for 120 months (10 years) at 5.7% interest**
```
> python LoanCalc.py --type=annuity --payment=8755 --periods=120 --interest=5.7
Your loan principal = 799397!
Overpayment = 251203!
```
**Example 6: calculate how long it will take to repay a loan with 500,000 principal, monthly payment of 15,000, and 6.8% interest**
```
> python LoanCalc.py --type=annuity --principal=500000 --payment=15000 --interest=6.8
It will take 3 years and 2 months to repay this loan!
Overpayment = 70000!
```

