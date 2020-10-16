import math
import argparse


def error_msg() -> int:
    print("Incorrect parameters.")
    return 0


def validate_params(arg) -> int:
    if arg.interest is None:
        return error_msg()
    if arg.payment is not None and arg.type == 'diff':
        return error_msg()
    if args.payment is None:
        if args.type == 'diff':
            return 1
        elif args.type == 'annuity':
            return 2
        else:
            return error_msg()
    elif args.principal is None:
        if arg.type == 'annuity' and arg.payment is not None and arg.periods is not None:
            return 3  # the principal will be calculated
        else:
            return error_msg()
    elif args.periods is None:
        if arg.type == 'annuity' and arg.payment is not None and arg.principal is not None:
            return 4  # the principal will be calculated
        else:
            return error_msg()


def number_of_monthly_payments(principal, monthly_payment, interest):
    to_print = ''
    nominal = interest / (12 * 100)
    num_of_months = math.ceil(math.log(monthly_payment
                                       / (monthly_payment - nominal * principal),
                                       1 + nominal))
    if num_of_months != 1:
        if num_of_months < 12:
            print('It will take ' + str(num_of_months) + ' months to repay this loan!')
        else:
            years = num_of_months // 12
            months = num_of_months % 12
            if years == 1:
                if months == 0:
                    to_print = '1 year'
                elif months == 1:
                    to_print = '1 year and 1 month'
                else:
                    to_print = '1 year and ' + str(months) + ' months'
            elif months == 1:
                to_print = str(years) + ' years and 1 month'
            elif months == 0:
                to_print = str(years) + ' years'
            else:
                to_print = str(years) + " years and " + str(months) + ' months'
    else:
        to_print = '1 month'

    print(f'It will take {to_print} to repay this loan!')
    print(f'Overpayment = {(monthly_payment * num_of_months - principal)}!')


def calc_annuity_payment(principal, periods, interest):
    nominal = interest / (12 * 100)
    annuity_pmt = principal * (nominal * pow((1 + nominal), periods)) / (pow((1 + nominal), periods) - 1)
    print(f'Your annuity payment = {math.ceil(annuity_pmt)}!')
    print(f'Overpayment = {(math.ceil(annuity_pmt) * periods - principal)}!')


def calculate_principal(payment, periods, interest):
    nominal = interest / (12 * 100)
    principal = payment / ((nominal * pow((1 + nominal), periods)) / (pow((1 + nominal), periods) - 1))
    print(f'Your loan principal = {math.floor(principal)}!')
    print(f'Overpayment = {(periods * payment - math.floor(principal))}!')


def calculate_diff_pmt(principal, periods, interest):
    nominal = interest / (12 * 100)
    total_pmt = 0
    for i in range(1, periods + 1):
        to_add = nominal * (principal - ((principal * (i - 1)) / periods))
        pmt = principal / periods + to_add
        total_pmt += math.ceil(pmt)
        print(f'Month {i}: payment is {math.ceil(pmt)}')
    print()
    print(f'Overpayment = {total_pmt - principal}')


parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
parser.add_argument('--payment')
args = parser.parse_args()

parameter_to_count = validate_params(args)

if parameter_to_count == 1:
    calculate_diff_pmt(int(args.principal), int(args.periods), float(args.interest))
if parameter_to_count == 2:
    calc_annuity_payment(int(args.principal), int(args.periods), float(args.interest))
if parameter_to_count == 3:
    # calculate the principal
    calculate_principal(int(args.payment), int(args.periods), float(args.interest))
if parameter_to_count == 4:
    # if parameter == 4 - calculate how long it will take to repay the loan
    number_of_monthly_payments(int(args.principal), int(args.payment), float(args.interest))
