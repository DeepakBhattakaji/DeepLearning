import webbrowser
import time

total_breaks=3
break_count=0

print("This Program started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(10) #10 Seconds
   # time.sleep(2*60*60) #2 hours
    webbrowser.open("facebook.com")
    break_count=break_count+1
