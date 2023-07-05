# Demostracion de cola eficiente.
#  Se debe de colocar self.ram_pool = lambda: 10 
# # psutil.virtual_memory().available en RamLocker.__init__

from time import sleep
from celaut_framework.resource_manager.resourcemanager import ResourceManager, mem_manager
from threading import Thread, Lock

RAM_POOL = 5


class NodeResourcesManagerSimulator:
    def __init__(self) -> None:
        self.ram_pool = RAM_POOL
        self.lock = Lock()

    def modify_resources(self, l: dict):
        with self.lock:
            print('\n ei mai friend, yu want to change the ram, ok, i change it. ->  ', l, '\n')
            self.ram_pool = l['max']
        return self.ram_pool


def p0():
    with mem_manager(len=RAM_POOL):
        while True:
            sleep(1)


def p1():
    with mem_manager(len=700):
        print(1)


def p2():
    with mem_manager(len=900):
        sleep(7)
        print(2)


def p3():
    with mem_manager(len=300):
        print(3)


# ResourceManager(ram_pool_method= lambda: psutil.virtual_memory().total) Simulacion de uso de la librería en nodo.

nrms = NodeResourcesManagerSimulator()
ResourceManager(
    ram_pool_method=lambda: RAM_POOL,
    modify_resources=lambda l: nrms.modify_resources(l)
)

Thread(target=p0).start()
sleep(2)
Thread(target=p1).start()
sleep(2)
Thread(target=p2).start()
sleep(2)
Thread(target=p3).start()
