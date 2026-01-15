import ReactiveLayer
import MediativeLayer
import DeliberativeLayer
# import MediativeLayer

import threading
import time

# Constants
IP_ONE = 'localhost'
IP_TWO = 'localhost'
MAP_FILE = 'map_simple.txt'

botOne = ReactiveLayer.ReactiveLayer(1, IP_ONE)
botTwo = ReactiveLayer.ReactiveLayer(2, IP_TWO)
medLayer = MediativeLayer.MediativeLayer()
dLayer = DeliberativeLayer.DeliberativeLayer(MAP_FILE)

reactiveThreadOne = threading.Thread(target=botOne.RunLayer)
reactiveThreadTwo = threading.Thread(target=botTwo.RunLayer)
mediativeThread = threading.Thread(target=medLayer.RunLayer, args=(botOne, botTwo))
deliberativeThread = threading.Thread(target=dLayer.RunLayer, args=(medLayer,))

reactiveThreadOne.start()
reactiveThreadTwo.start()
mediativeThread.start()
deliberativeThread.start()

reactiveThreadOne.join()
reactiveThreadTwo.join()
mediativeThread.join()
deliberativeThrad.join()
