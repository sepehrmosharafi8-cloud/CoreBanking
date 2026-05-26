from database import create_tables
from models import Account
def main():
    print("___CoreBanking System___")

    create_tables()

    print("\nCreating a new account...")
    account1 = Account.create_account("Ali Rezaei", 1000.0)

    account2 = Account.create_account("Zahra Ahmadi", 500.0)

    print("\nFetching account details...")
    fetched_account = Account.get_account_by_id(account1.account_id)
    if fetched_account:
        print(f"Fetched: {fetched_account}")

    print("\nPerforming withdrawal...")
    if account1:
        account1.withdraw(150.0)
        print(f"After withdraw: {Account.get_account_by_id(account1.account_id)}")

    print("\nAttempting to overdraw...")
    if account1:
        account1.withdraw(2000.0)

    print("\n--- System End ---")
    if __name__ == "__main__":
        main()