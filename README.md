# MotorCape from GHI and BeagleBoard.org

Some ideas for the MotorCape from GHI and BBB.io persons...

...

First off...attach that MotorCape. Make sure, if you are using the Cape w/ a BBBW, to get P8 on the Cape w/ P8 on the BBBW and the same for header P9. 

...

# Making stuff move around...

...

You can look to MotoCape.py and boboJackson.html in the templates directory for a quick software example. As you can tell, I am using motorOne and motorThree only. Please keep in mind that when applying power to the MotorCape, the motors will only move if the BBB, BBG, BBGW, BBBW are all plugged in via barrel jack (vdd_5v).

...

You can set up Adafruit_BBIO by following this site on this site: https://github.com/adafruit/adafruit-beaglebone-io-python. Setting up PWM and GPIO on the BBBW, in my case, was close to simple. I installed, w/ pip, Adafruit_BBIO, understood the schematic finally, and then looked to making some software examples to get going.

# GO!

...

Please keep in mind that people are around that have produced nice items w/ their BBB and variations. Do not discredit this little board.

I thought I was getting the shaft at first and it was b/c of me, my lack of knowledge on the subject matter, and b/c I did not have enough time to promote ideas after learning.

But...in time, I found time and fondness of this board and others like it in the same family.

...

Anyway...back to it. So, got Adafruit_BBIO yet? Good! Now, we need to install flask w/ sudo pip install flask. It should install dependencies also.

...

Use that software and your new Cape to make that motion from two motors. 

Seth

P.S. I think this is all for now!
