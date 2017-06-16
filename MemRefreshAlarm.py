import time
import webbrowser

condition=0

print("The program Started on " + time.ctime())
while condition<3 :
 time.sleep(5)
 webbrowser.open("https://www.youtube.com/watch?v=muHdlKxV45U")
 condition=condition+1
 
