import logging
from Roles import Tailor, HajiFirooz
from Threads import *


def read_data():
    sons_number = 4  # input("inter number of hajiFirooz sons: ")
    file = open("./data.txt", "r")
    number_of_orders = int(file.readline())
    khayats = sons_number + 1  # 1 is Hajifirooz
    order_peer_khayat = number_of_orders // khayats

    customers_list = [d.split("\n") for d in file]
    # remove empty columns
    for f in customers_list:
        try:
            f.remove('')
        except:
            print("")
    #########

    # print(customers_list)

    monshi_tagsim_kon(customers_list, order_peer_khayat)
    logging.info("Secretary completes his task.")

    end_threads()


def monshi_tagsim_kon(customers_list: list, order_peer_khayat: int):

    customers = spit_customres_for_each_khayat(
        customers_list, order_peer_khayat)

    Haji = False
    son_index = 1
    global threads
    for each_khayat_list in customers:
        if not Haji:
            khayat = HajiFirooz(each_khayat_list)
            Haji = True
        else:
            son_name = "Tailor"+str(son_index)
            khayat = Tailor(son_name, each_khayat_list)
            son_index = son_index + 1

        start_thread(khayat)


def spit_customres_for_each_khayat(customers_list2D, order_peer_khayat):
    count = 0
    t = []
    customers = []
    for j in customers_list2D:
        for i in j:
            if not count < order_peer_khayat:
                customers.append(t)
                t = []
                count = 0

            t.append(i)
            count = count + 1
    
    customers.append(t)
    return customers


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    read_data()
