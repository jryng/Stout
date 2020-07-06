# Stout
Display the status of a CUPS-based printer (and, if printing, of a print job) on an I2C LCD module.

This program has been tested on a Pi 3 B+ and a Pi Zero W, and was written for a 16x2 display, but should work on any Pi as long as there is a 5V source available for the display.

# Installing and Running
Stout requires pycups to run. This can be acquired via pip, which in turn requires the libcups2 package. python3-smbus is also required, due to the LCD driver.

After meeting all requirements, plug in your display module and run lcd_install.sh to prepare the driver. By default, Stout will get the default printer name and job info from the locally-running instance of CUPS. To change this, modify stout.py to connect to the IP and port of your print server.

Now, run python3 stout.py and Stout should run as intended.

# Todo
Maybe create an install script that handles everything else. Create alternate versions for 20x4 and OLED display modules. Add easy customization to the script, namely to change how status messages are shown. Add alternate display modes either via a command or GPIO input.
