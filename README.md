# swfpng
一个基于swfrender的swf文件png图片提取




## swfrender

```
C:swf2png>swfrender.exe

Usage: swfrender.exe file.swf [-options]

-h , --help                    Print short help message and exit
-l , --legacy                  Use old rendering framework
-o , --output                  Output file, suffixed for multiple pages (default: output.png)
-p , --pages range             Render pages in specified range e.g. 9 or 1-20 or 1,4-6,9-11 (default:
-r , --resolution dpi          Scale width and height to a specific DPI resolution, assuming input is
-X , --width width             Scale output to specific width (proportional unless height specified)
-Y , --height height           Scale output to specific height (proportional unless width specified)
```



对于python提取swf中的png图片先看看git上别人是怎么做的

** [szebenyib/swf_to_pdf](https://github.com/szebenyib/swf_to_pdf)**

![](https://raw.githubusercontent.com/Hatcat123/GraphicBed/master/Img/20190322192718.png)

** [klujanrosas/PearsonRipper](https://github.com/klujanrosas/PearsonRipper)**

![](https://raw.githubusercontent.com/Hatcat123/GraphicBed/master/Img/20190322194539.png)

** [Ation/extract_mages_swf](https://github.com/Ation/extract_mages_swf)**

![](https://raw.githubusercontent.com/Hatcat123/GraphicBed/master/Img/20190322204233.png)


** [FafnerKeyZee/swf2pdf/](https://github.com/FafnerKeyZee/swf2pdf/) **

![](https://raw.githubusercontent.com/Hatcat123/GraphicBed/master/Img/20190322204417.png)

无疑最简单的方法是调用swfrender工具


当我使用swfender的时候，发现如果dpi提升太高，则会导致产生内存溢出的错误，大概在500p的时候得到较高质量的图片，但是转换响应的时间也会增加。对于此demo.swf选择200p的情况能做到较好的中和度。

```

C:\swf2png>swfrender.exe .\demo\demo.swf -o high_p.png -r 800
FATAL: Out of memory (while trying to claim 187088000 bytes)


```

如何使用脚本来执行

bash版本：

```
for x in *.swf; do
    swfrender ${x} -o ${x%.swf}.png
done

```

python版本

```

import os
for i in range(0,10):
    os.system("swfrender file%02d.swf -o output.png" % i)

```



如果您需要比从swfrender获得的分辨率更高的分辨率，您可以试用Karim Beyrouti 的免费Adobe AIR应用程序 Kurst SWF Renderer 1.0，或商业SWF Renderer 2.0