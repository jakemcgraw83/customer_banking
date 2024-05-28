# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERe
from savings_account.py import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
savings_balance = input('Enter your savings balance')
savings_interest = input('Enter the interest rate')
savings_maturity = input('Enter the # of months')
    # Call the create_savings_account function and pass the variables from the user.
updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print('Here is your updated savings balance')
print(f"Updated Balance: {create_savings_accounts.updated_savings_balance()} ")
print(f"Interest Earned: {create_savings_account.interest_earned} ")
print(f"over {create_savings_account.months} months ")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
cd_balance = input('Enter your checking balance')
cd_interest = input('Enter the interest rate')
months = input('Enter the # of months')
    # Call the create_cd_account function and pass the variables from the user.
updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print('Here is your updated savings balance')
print(f"Updated Balansce: {create_cd_accounts.updated_savings_balance()} ")
print(f"Interest Earned: {create_cd_account.interest_earned} ")
print(f"over {create_cd_account.months} months ")

    # Call the main function
if __name__ == "__main__":
    main()