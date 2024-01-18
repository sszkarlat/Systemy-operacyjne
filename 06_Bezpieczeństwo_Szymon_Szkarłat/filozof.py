import threading
import time
import random

class DiningPhilosophers:
    def __init__(self, n, typ):
        self.n = n
        self.typ = typ
        self.forks = [threading.Semaphore(1) for _ in range(n)]
        self.eating_semaphore = threading.Semaphore(n // 2) # Maksymalnie polowa filozofow moze jesc w tym samym czasie
        self.philosophers = [threading.Thread(target=self.philosopher, args=(i,)) for i in range(n)]
        self.running = True

    def start(self):
        for philosopher in self.philosophers:
            philosopher.start()

    def stop(self):
        self.running = False
        for philosopher in self.philosophers:
            philosopher.join()

    def philosopher(self, i):
        while self.running:
            time.sleep(random.randint(1, 10))  # czas myslenia

            if self.typ == 1:
                if i % 2 == 0:
                    self.eat_even(i)
                else:
                    self.eat_odd(i)
            elif self.typ == 2:
                if i % 2 == 0:
                    self.eat_even_reversed(i)
                else:
                    self.eat_odd_reversed(i)

    def can_eat(self, left_fork, right_fork):
        return self.forks[left_fork]._value > 0 and self.forks[right_fork]._value > 0

    def eat_even(self, i):
        left_fork = i
        right_fork = (i + 1) % self.n

        with self.eating_semaphore:
            if self.can_eat(left_fork, right_fork):
                with self.forks[left_fork], self.forks[right_fork]:
                    print(f"Filozof {i} je.")

                    time.sleep(random.randint(1, 10))  # czas jedzenia

                    print(f"Filozof {i} odlozyl sztucce.")

    def eat_odd(self, i):
        right_fork = i
        left_fork = (i + 1) % self.n

        with self.eating_semaphore:
            if self.can_eat(left_fork, right_fork):
                with self.forks[right_fork], self.forks[left_fork]:
                    print(f"Filozof {i} je.")

                    time.sleep(random.randint(1, 10))  # czas jedzenia

                    print(f"Filozof {i} odlozyl sztucce.")

    def eat_even_reversed(self, i):
        left_fork = i
        right_fork = (i + 1) % self.n

        with self.eating_semaphore:
            if self.can_eat(left_fork, right_fork):
                # Zmiana kolejnosci podnoszenia sztuccow dla parzystych filozofow
                with self.forks[right_fork], self.forks[left_fork]:
                    print(f"Filozof {i} je.")

                    time.sleep(random.randint(1, 10))  # czas jedzenia

                    print(f"Filozof {i} odlozyl sztucce.")

    def eat_odd_reversed(self, i):
        right_fork = i
        left_fork = (i + 1) % self.n

        with self.eating_semaphore:
            if self.can_eat(left_fork, right_fork):
                # Zmiana kolejnosci podnoszenia sztuccow dla nieparzystych filozofow
                with self.forks[left_fork], self.forks[right_fork]:
                    print(f"Filozof {i} je.")

                    time.sleep(random.randint(1, 10))  # czas jedzenia

                    print(f"Filozof {i} odlozyl sztucce.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Uzycie: python filozof.py <typ> <n>")
        sys.exit(1)

    typ = int(sys.argv[1])
    n = int(sys.argv[2])

    if typ not in [1, 2] or n < 2 or n > 10:
        print("Bledne dane wejsciowe")
        sys.exit(1)

    dining_philosophers = DiningPhilosophers(n, typ)

    try:
        dining_philosophers.start()
        time.sleep(60)  # Czas trwania symulacji
    finally:
        dining_philosophers.stop()
