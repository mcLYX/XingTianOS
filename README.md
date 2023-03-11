# XingTianOS 
A ugly  os-like UI launcher(???)  for .py files in MicroPython.


XtOS
![](https://s3.bmp.ovh/imgs/2022/07/23/b43d760b5a924ce1.webp)


# 换带psram的s2-mini了，真香，请到main-s2分支，这里不咋更了

此OS非传统意义上的OS，该OS是“Oh Sh*t的缩写”。

ESP32C3的板子直接上传就完事，可能要在$LIB$文件夹补上mpy官方的ssd1306.py和urequests.py

只适配了12864 OLED（ssd1306/1315）和128*160 TFT彩屏（st7735）

其他的改下/$LIB$/PRECONFIG.py以及一大堆东西

写着玩的东西，内存占用巨大，比ESP8266EX还烂（指RAM更小）的MCU基本别想用了，如果要8266的话只能用12864 OLED屏




草原来这玩意是MarkDown🐎
