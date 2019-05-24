import time
import webbrowser
total_breaks = 5
break_count =0
print("This program started on "+time.ctime())
while(break_count < total_breaks):
    webbrowser.open("https://youtu.be/8aRor905cCw")
    break_count = break_count + 1
    time.sleep(213)
