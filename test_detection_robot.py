import time
from ReactiveLayer import ReactiveLayer
from robobopy.utils.Color import Color

bot = ReactiveLayer(1, "192.168.1.87")

print("Vision System Warm-up...")
bot.robot.setActiveBlobs(True, True, True, False)
bot.robot.moveTiltTo(90, 5)
time.sleep(2)

print("Searching for ANY color blob...")
try:
    while True:
            blob = bot.robot.readColorBlob(Color.BLUE)
            if blob and blob.size > 0:
                print(f"I see the screen! Size: {blob.size} at x: {blob.x}")
            else:
                print("I can't see nothing")
            time.sleep(0.5)
  
except KeyboardInterrupt:
    bot.stop_robot()