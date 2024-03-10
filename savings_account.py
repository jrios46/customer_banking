"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE

from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    account = Account(balance,interest_rate)
    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_earned = balance * (interest_rate/100) ** (months/12)
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account.set_balance(updated_balance)
    #print (f"Balance {account.set_balance(balance)}")
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account.set_interest(interest_earned)
    #print (f"Balance {account.interest}")
    # Return the updated balance and interest earned.
    return  updated_balance, interest_earned  # ADD YOUR CODE HERE

   
    