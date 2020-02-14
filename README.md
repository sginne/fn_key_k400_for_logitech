# FN disabler for Logitech k400+

This product:
https://www.logitech.com/en-us/product/wireless-touch-keyboard-k400-plus?crid=27

has a bad habbit of function keys being disabled by default.

So, here is ad hoc solution working with /dev/hidraw*

Since it is just small script for my convenience, it iterates:
/dev/hidraw0
/dev/hidraw1
/dev/hidraw2

And it it finds suitable product, sends message to device, after which function keys start to work properly 

One can uncomment
>#fkeys 
string to enable pressing FN key back

and enhance 
>for i in ['0','1','2']:

with addtitional numbers that are added to /dev/hidraw[i]

since I have feeling, script catches ReadWrite exceptions, this is also place to put proper values there.

Suitable devices can be listed with
>ls /dev/hidraw*