# L3 // Projet QR Code
Creation of a new graphic communication tool

The objective of this lab is to design a "graphical" communication protocol. An example of a graphical communication protocol is the QR-CODE.
Ideally, the goal of our project would be to be able to create a graphical code for any string of characters with automatic 
detection and correction of the various errors.

I have created two versions of my graphic communication medium:

First, following my basic idea, which respects the constraints of distortion, direction and inversion. We can, thanks to this means of communication, write any message thanks to the binary code of the Unicode code of each character. The code is read from left to right and is composed of a set of "bars", each composed of 8 full points or not, depending on the corresponding binary code. Then we have a correction of each given constraint: On the one hand, the direction is given by a bar present on the left of the graphic code. Then the management of the distortion is managed by the central drawing on each "bar", but also by each square below them.

The other means of communication follows much more the idea of the QRcode in its visual aspect. 

It follows the same logic of binary according to the unicode of each character. Our code is restricted to the shape of a square formed by bars. Each bar corresponds to a character. Our message is printed from top to bottom and it ends with a line of 8 rectangles giving both the distortion and the direction.
