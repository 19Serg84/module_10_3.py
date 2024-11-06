import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Блокировка

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайная сумма для пополнения
            with self.lock:
                self.balance += amount  # Пополнение баланса
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)  # Имитация скорости выполнения пополнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайная сумма для снятия
            print(f"Запрос на {amount}")

            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount  # Снятие средств
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")

            time.sleep(0.001)  # Имитация скорости выполнения снятия


# Главный блок для запуска программы
if __name__ == "__main__":
    bk = Bank()

    # Создание потоков для методов deposit и take
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    # Запуск потоков
    th1.start()
    th2.start()

    # Ожидание завершения потоков
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')