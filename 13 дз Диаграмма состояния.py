from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def select_ticket(self, machine):
        pass

    @abstractmethod
    def insert_money(self, machine, amount):
        pass

    @abstractmethod
    def dispense_ticket(self, machine):
        pass

    @abstractmethod
    def cancel_transaction(self, machine):
        pass



class TicketMachine:
    def __init__(self):
        self.ticket_price = 10
        self.amount_inserted = 0
        self.state = IdleState()  # начальное состояние

    # Методы для взаимодействия
    def select_ticket(self):
        self.state.select_ticket(self)

    def insert_money(self, amount):
        self.state.insert_money(self, amount)

    def dispense_ticket(self):
        self.state.dispense_ticket(self)

    def cancel_transaction(self):
        self.state.cancel_transaction(self)



class IdleState(State):
    def select_ticket(self, machine):
        print("Билет выбран. Ожидание внесения денег...")
        machine.state = WaitingForMoneyState()

    def insert_money(self, machine, amount):
        print("Сначала выберите билет!")

    def dispense_ticket(self, machine):
        print("Сначала выберите билет!")

    def cancel_transaction(self, machine):
        print("Нет активной транзакции.")



class WaitingForMoneyState(State):
    def select_ticket(self, machine):
        print("Билет уже выбран. Внесите деньги.")

    def insert_money(self, machine, amount):
        machine.amount_inserted += amount
        print(f"Внесено: {machine.amount_inserted}")
        if machine.amount_inserted >= machine.ticket_price:
            machine.state = MoneyReceivedState()

    def dispense_ticket(self, machine):
        print("Недостаточно денег.")

    def cancel_transaction(self, machine):
        print("Транзакция отменена.")
        machine.amount_inserted = 0
        machine.state = TransactionCanceledState()



class MoneyReceivedState(State):
    def select_ticket(self, machine):
        print("Билет уже выбран и деньги внесены.")

    def insert_money(self, machine, amount):
        machine.amount_inserted += amount
        print(f"Дополнительно внесено: {amount}")

    def dispense_ticket(self, machine):
        print("Билет выдан. Спасибо за покупку!")
        machine.amount_inserted = 0
        machine.state = TicketDispensedState()

    def cancel_transaction(self, machine):
        print("Транзакция отменена. Возврат денег.")
        machine.amount_inserted = 0
        machine.state = TransactionCanceledState()



class TicketDispensedState(State):
    def select_ticket(self, machine):
        print("Начните новую транзакцию.")

    def insert_money(self, machine, amount):
        print("Начните новую транзакцию.")

    def dispense_ticket(self, machine):
        print("Билет уже выдан.")

    def cancel_transaction(self, machine):
        print("Невозможно отменить. Билет уже выдан.")


class TransactionCanceledState(State):
    def select_ticket(self, machine):
        print("Начинаем новую транзакцию...")
        machine.state = IdleState()

    def insert_money(self, machine, amount):
        print("Транзакция отменена. Сначала выберите билет.")

    def dispense_ticket(self, machine):
        print("Транзакция отменена. Невозможно выдать билет.")

    def cancel_transaction(self, machine):
        print("Транзакция уже отменена.")



if __name__ == "__main__":
    machine = TicketMachine()

    machine.select_ticket()       # Выбираем билет
    machine.insert_money(5)       # Вносим часть суммы
    machine.insert_money(5)       # Вносим оставшуюся сумму
    machine.dispense_ticket()     # Получаем билет
    machine.select_ticket()       # Начинаем новую транзакцию
