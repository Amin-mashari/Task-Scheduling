import logging
import time
from Dress import Dress, Cost
from Threads import start_thread


class Tailor():

    def __init__(self, name, customers_list: list):
        self.shalvar_time = 0.8
        self.pirahan_time = 0.9
        self.kot_time = 1
        self.name = name
        self.customer_cost = 0
        self.customers_list = customers_list

    def add_customer_cost(self, cost: int):
        self.customer_cost = self.customer_cost + cost

    def getName(self) -> str:
        return self.name

    def run(self):
        logging.info("%s gets orders.", self.name)
        for customer_li in self.customers_list:
            customer = customer_li.split(" ")
            customer_name = customer.pop(0)
            customer_orders = []
            for lebas_name in customer:
                customer_orders.append(lebas_name)
                match lebas_name:
                    case Dress.shalvar.value:
                        time.sleep(self.shalvar_time)
                        self.add_customer_cost(Cost.shalvar.value)
                    case Dress.pirahan.value:
                        time.sleep(self.pirahan_time)
                        self.add_customer_cost(Cost.pirahan.value)
                    case Dress.kot.value:
                        time.sleep(self.kot_time)
                        self.add_customer_cost(Cost.kot.value)

            logging.info("%s prepares order of %s.", self.name, customer_name)
            self.create_customer(customer_name, customer_orders)

        logging.info("%s completes his task.", self.name)

    def create_customer(self, customer_name, customer_orders):
        customer = Customer(customer_name,
                            self.customer_cost, customer_orders)
        start_thread(customer)


class HajiFirooz():

    def __init__(self, customers_list: list):

        self.name = "HajiFirooz"
        self.shalvar_time = 0.7
        self.pirahan_time = 0.85
        self.kot_time = 0.9
        self.customer_cost = 0
        self.customers_list = customers_list

    def getName(self) -> str:
        return self.name

    def add_customer_cost(self, cost: int):
        self.customer_cost = self.customer_cost + cost

    def run(self):
        logging.info("%s gets orders.", self.name)
        for customer_li in self.customers_list:
            customer = customer_li.split(" ")
            customer_name = customer.pop(0)
            customer_orders = []
            for lebas_name in customer:
                customer_orders.append(lebas_name)

                match lebas_name:
                    case Dress.shalvar.value:
                        time.sleep(self.shalvar_time)
                        self.add_customer_cost(Cost.shalvar.value)
                    case Dress.pirahan.value:
                        time.sleep(self.pirahan_time)
                        self.add_customer_cost(Cost.pirahan.value)
                    case Dress.kot.value:
                        time.sleep(self.kot_time)
                        self.add_customer_cost(Cost.kot.value)

            logging.info("%s prepares order of %s.", self.name, customer_name)
            self.create_customer(customer_name, customer_orders)

        logging.info("%s completes his task.", self.name)

    def create_customer(self, customer_name, customer_orders):
        customer = Customer(customer_name,
                            self.customer_cost, customer_orders)
        start_thread(customer)


class Customer():

    def __init__(self, name, cost, orders):

        self.shalvar_time = 0.4
        self.pirahan_time = 0.4
        self.kot_time = 0.5
        self.name = name
        self.cost = cost
        self.orders = orders

    def getName(self) -> str:
        return self.name

    def run(self):
        for lebas_name in self.orders:
            # logging.info("starting: %s is prooing %s",
            #              self.name, lebas_name)
            match lebas_name:
                case Dress.shalvar:
                    time.sleep(self.shalvar_time)
                case Dress.pirahan:
                    time.sleep(self.pirahan_time)
                case Dress.kot:
                    time.sleep(self.kot_time)
            # logging.info("finishing: %s prooing %s",
            #              self.name, lebas_name)
        logging.info("%s puts %d in dressing room and Exit.",
                     self.name, self.cost)
