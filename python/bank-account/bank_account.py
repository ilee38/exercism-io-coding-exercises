import threading

class BankAccount:
    def __init__(self):
        self._acct_balance = 0
        self._acct_is_open = False
        self._transac_lock = threading.Lock()

    def get_balance(self):
        if not self._acct_is_open:
            raise ValueError("This account is not open")
        else:
            return self._acct_balance

    def open(self):
        if self._acct_is_open:
            raise ValueError("This account is already open")
        else:
            self._acct_is_open = True

    def deposit(self, amount):
        with self._transac_lock:
            if not self._acct_is_open:
                raise ValueError("This account is not open")
            if amount <= 0:
                raise ValueError("Amount entered is incorrect")
            else:
                self._acct_balance += amount

    def withdraw(self, amount):
        with self._transac_lock:
            if not self._acct_is_open:
                raise ValueError("This account is not open")
            if self._acct_balance < amount:
                raise ValueError("Withdrawal amount exceeds current balance")
            elif amount < 0:
                raise ValueError("Cannot withdraw a negative ammount")
            else:
                self._acct_balance -= amount

    def close(self):
        if not self._acct_is_open:
            raise ValueError("This account is already closed")
        else:
            self._acct_balance = 0
            self._acct_is_open = False
