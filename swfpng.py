
import os
for i in range(0,10):
    os.system("swfrender file%02d.swf -o output.png" % i)