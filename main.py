import ReactiveLayer
import DeliberativeLayer
# import MediativeLayer

import threading
import time

# Constants
IP_ONE = 'x'
IP_TWO = 'x'
MAP_FILE = 'x.txt'

botOne = ReactiveLayer.ReactiveLayer(1, IP_ONE)
botTwo = ReactiveLayer.ReactiveLayer(2, IP_TWO)
medLayer = MediativeLayer.MediativeLayer()
dLayer = DeliberativeLayer.DeliberativeLayer(MAP_FILE)

reactiveThreadOne = threading.Thread(target=botOne.RunLayer)
reactiveThreadTwo = threading.Thread(target=botTwo.RunLayer)
mediativeThread = threading.Thread(target=medLayer.RunLayer, args=(botOne, botTwo))
deliberativeThread = threading.Thread(target=dLayer.RunLayer, args=(medLayer))

reactiveThreadOne.start()
reactiveThreadTwo.start()
mediativeThread.start()
deliberativeThread.start()

reactiveThreadOne.join()
reactiveThreadTwo.join()
mediativeThread.join()
deliberativeThrad.join()
