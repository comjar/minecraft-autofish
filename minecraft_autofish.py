import autopy
import time
from playsound import playsound

i=0
fishtime = int(input('enter time to fish in seconds then press enter :'))
time.sleep(3)
playsound('start sound.wav')
size = autopy.screen.size()
needle = autopy.bitmap.Bitmap.open('black.png')
start_time = time.time()
for x in range(0, fishtime*10):
    haystack =  autopy.bitmap.capture_screen()
    pos = haystack.find_bitmap(needle,0.03,((size[0]*0.4, size[1]*0.2), (size[0]*0.2,size[1]*0.5)),(size[0]*0.4, size[1]*0.2))
    if pos is None:
        autopy.mouse.click()
        time.sleep(0.1)
        autopy.mouse.click()
        time.sleep(1.2)
        i=i+1
        print("fish catched :", i)   
        elapsed_time = time.time() - start_time
        print("time elasped", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
elapsed_time = time.time() - start_time
print("time elasped :", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
playsound('end sound.wav')
autopy.alert.alert("Program ended")
