def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        print("Insufficient balance")
        return balance


if __name__ == "__main__":

    balance = int(input("Enter initial balance: "))

    amt = int(input("Enter deposit amount: "))
    balance = deposit(balance, amt)

    amt = int(input("Enter withdrawal amount: "))
    balance = withdraw(balance, amt)

    print("Balance:", balance)