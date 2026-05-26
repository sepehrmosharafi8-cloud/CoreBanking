from database import get_db_connection
class Account:
    def __init__(self,account_id=None, owner_name=None,balance=0.0):
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = balance

    @staticmethod
    def create_account(owner_name, initial_deposit=0.0):
        """Create new Bank account"""
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO accounts (owner_name, balance) VALUES (?,?)", (owner_name, initial_deposit))
            conn.commit()
            print(f"Account created successfully for {owner_name} with ID: {account_id}")
            return Account(account_id=account_id, owner_name=owner_name, balance=initial_deposit)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            return None
        finally:
            conn.close()

    @staticmethod
    def get_account_by_id(account_id):
        """Get account by ID"""
        conn = get_db_connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE account_id = ?", (account_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Account(account_id=row['account_id'], owner_name=row['owner_name'], balance=row['balance'])
        return None
    def deposit(self, amount):
        """Deposit amount"""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            self.balance += amount
            cursor.execute("UPDATE accounts SET balance = ? WHERE account_id = ?", (self.balance, self.account_id))
            conn.commit()
            print(f"Deposited {amount}. New balance: {self.balance}")
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()

    def withdraw(self, amount):
        """Withdraw amount"""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            self.balance -= amount("UPDATE accounts SET balance = ? WHERE account_id = ?", (self.balance, self.account_id))
            conn.commit()
            print(f"Withdrew {amount}. New balance: {self.balance}")
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()

    def __str__(self):
        return f"Account(ID: {self.account_id}, Owner: {self.owner_name}, Balance: {self.balance:2f})"
