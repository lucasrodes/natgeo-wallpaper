# natgeo-wallpaper

This project was started motivated by this [post](http://miquel.ml/wallpaperoftheday/),
where the [Photo of the Day](https://www.nationalgeographic.com/photography/photo-of-the-day/)
from National Geographic is set as the destkop wallpaper every day automatically. 

This project has been tested on CentOS 7.5.1804 and GNOME Shell 3.25.4.

## Getting started

To make it work you need to follow this simple steps:

0. Install python dependencies: 
	```
	$ pip3 install bs4 pillow lxml --user
	```
1. Change the paths in the shell script [wallpaper.sh](wallpaper.sh).
2. Add the shell script to cronetab to ensure that it is executed daily. Type 
    `sudo crontab -e`. This will open a file, insert the following line 
    
    ```
    30 8 * * * <path to natgeo-wallpaper repo>/wallpaper.sh > <path to natgeo-wallpaper repo>/wallpaper.log 2>&1
    ```
3. Type `gnome-tweak-tools` in the terminal and go to Desktop -> Background 
    Location and select the file `<path to repository>/pics/wallpaper.jpg` 
    (create file if not already there).