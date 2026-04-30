class Wallet:
    def __init__(self, owner, pin, starting_balance=0):
        self.owner = owner
        self._balance = 0
        self._pin = pin
        self._failed_attempts = 0
        self._is_blocked = False
        self.deposit(starting_balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit harus lebih dari 0")
        self._balance += amount

    def withdraw(self, amount, input_pin):
        # Fitur 2: Cek apakah akun terblokir
        if self._is_blocked:
            raise PermissionError("Akun terblokir karena 3x salah PIN.")

        # Fitur 1: Validasi PIN
        if input_pin != self._pin:
            self._failed_attempts += 1
            if self._failed_attempts >= 3:
                self._is_blocked = True
                raise PermissionError("PIN salah 3x. Akun diblokir!")
            raise ValueError("PIN salah.")

        # Validasi Saldo
        if amount <= 0:
            raise ValueError("Jumlah withdraw tidak valid.")
        if amount > self._balance:
            raise ValueError("Saldo tidak mencukupi.")

        # Reset attempt jika berhasil dan kurangi saldo
        self._failed_attempts = 0
        self._balance -= amount
        return f"Berhasil menarik {amount}"
    
# Contoh Eksekusi Edge Case
dompet = Wallet("Andi", "1234", 1000)

# Edge Case 1: Tarik semua saldo
dompet.withdraw(1000, "1234")
print(f"Saldo setelah dikosongkan: {dompet.balance}") # Output: 0

# Edge Case 2: Salah PIN 2x lalu benar 1x
dompet.deposit(500)
try:
    dompet.withdraw(100, "9999") # Salah 1
except ValueError: pass
try:
    dompet.withdraw(100, "8888") # Salah 2
except ValueError: pass

print(dompet.withdraw(100, "1234")) # Berhasil, tidak terblokir