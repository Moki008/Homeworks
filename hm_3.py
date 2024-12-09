class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu(self):
         return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_compulations(self):
        addition = self.__cpu + self.__memory
        subtraction = self.__cpu - self.__memory
        multiplication = self.__cpu * self.__memory
        division = self.__cpu / self.__memory
        return addition, subtraction, multiplication, division

    def __str__(self):
        return f'CPU: {self.__cpu}, Memory: {self.__memory}'

    def __lt__(self, other):
        return self.memory < other.memory
    def __gt__(self, other):
        return self.memory > other.memory
    def __le__(self, other):
        return self.memory <= other.memory
    def __ge__(self, other):
        return self.memory >= other.memory
    def __eq__(self, other):
        return self.memory == other.memory
    def __ne__(self, other):
        return self.memory != other.memory

class Phone:
    def __init__(self):
        self.__sim_cards = []

    def get_sim(self):
        return self.__sim_cards
    def add_sim(self, sim_card):
        self.__sim_cards.append(sim_card)
    def remove_sim(self, sim_card):
        self.__sim_cards.remove(sim_card)

    def call(self,sim_card_number, call_to_number= 911):
        self.call_to_number = call_to_number
        sim_card_number = sim_card_number-(len(self.__sim_cards)+1)
        print(f"Идет звонок на номер {call_to_number},"
              f"c cим-карты - 1: {self.__sim_cards[sim_card_number]}")

    def __str__(self):
        return f"Number: {self.call_to_number}, Sim Card: {self.__sim_cards}"

class Smartphone(Phone, Computer):
    def use_gps(self, location):
        self.location = location
        print(f'Маршрут на локацию: {location} построен. ')

    def __str__(self):
        return f"Location: {self.location}"

Pc = Computer(40, 500)
Phone1 = Phone()
Phone1.add_sim('Beeline')
Phone1.call(1)
Smartphone1 = Smartphone()
Smartphone1.use_gps(1)
Smartphone2 = Smartphone()
Smartphone2.use_gps(2)

print(Pc)
print(Phone1)
print(Smartphone1)

"""Computer"""
Pc.make_compulations()
print(Pc.make_compulations())

"""Phone"""
Phone1.add_sim("beeline")
Phone1.call(1)
Phone1.get_sim()
Phone1.remove_sim("beeline")

"""Smartphone"""
Smartphone2.use_gps("Gym")




