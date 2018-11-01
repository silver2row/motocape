# MotorCape from GHI and BeagleBoard.org

Some ideas for the MotorCape from GHI and BBB.io persons...

http://beagleboard.org/black-wireless, http://octavosystems.com/octavo_products/osd335x/, and https://www.mouser.com/ProductDetail/GHI-Electronics/MRTCPE-BBBCAPE?qs=lYGu3FyN48fyjZuUoploBg%3d%3d
will show some ideas on the BBBW, which I am using, the SiP on the BBBW, and the MotorCape which can be purchased from Mouser.com.

Just to mention ideas, please read this page: https://beagleboard.org/logo. This will give you some ideas on their Logo, the dog which name evades me now, the license for their open source
attitudes and beliefs, and how to prepare specific ideas if dealing w/ them. Anyway, enough of policy. Here goes it!

...

First off...attach that MotorCape. Make sure, if you are using the Cape w/ a BBBW, to get P8 on the Cape w/ P8 on the BBBW and the same for header P9. 

Okay, once attached is when we can start development. We will need to make service by way of a .service file, a couple of software examples, and use systemctl to make our service run on boot.
For the service file, go to /etc/systemd/system. Make a .service file by using your favorite editor, nano for instance, and use this idea for a .py file named MotoCape.py:

    [Unit]
    Description=Whatever You Would Like to Describe about Your File

    [Service]
    ExecStart=/The/Path/To/Your/File.py

    [Install]
    WantedBy=multi-user.target

Once we have our file/.service file, save it and exit. Notice in the [Unit] section...there is a Description directive. I described what you should put there but have at it. 
The best way to add content to the Description= line is to make your description as well understood as possible. Just nothing all that vague should do.

In the [Service] section after ExecStart=, the PATH to your file, whatever type of file it may be at this point, should start w/ your working directory and end w/ the file being run on boot.

On the [Install] section after WantedBy=, type multi-user.target. This is a cop out but is should work no matter what. There are many recommendations on what to read and where to read it. I have found
this site to be the online page w/ the most info: https://www.freedesktop.org/wiki/Software/systemd/. I know MAN pages rule, too. 
...

# Making stuff move around...

You can look to MotoCape.py and bobo.html in the templates directory for a quick software example. As you can tell, I am using motorOne and motorThree only. 
Please keep in mind that when applying power to the MotorCape, the motors will only move if the BBB, BBG, BBGW, BBBW are plugged in via barrel jack (vdd_5v).

You can still use the USB (sys_5v) connection to debug and create software for your Cape on your BBB/variation.
...

You can set up Adafruit_BBIO by following this site on this site: https://github.com/adafruit/adafruit-beaglebone-io-python. Setting up PWM and GPIO on the BBBW, in my case, was close to simple. 
I installed w/ pip, Adafruit_BBIO like so: sudo pip install Adafruit_BBIO. Understanding the schematic finally, helped me make some software examples to get going.

# GO!

...

    If you need rations or supplies of help, ask away. I should be knowledgeable by that point in time. 

    I added a new bunch of software I got from adding, making additions, and reading. Some are from www.w3schools.com, a book I already mentioned, and a person from Freenode at #beagle!

Seth

P.S. I think this is all for now! Oh and I reviewed this info. from a book w/ my changes. Here is the book and page number in case you are wondering, "BeagleBone By Example," (Prabakar).
Page 235 of the book is where I got some ideas and reinvented the idea on his subjects. If you need additional info, please do not hesitate to ask.
