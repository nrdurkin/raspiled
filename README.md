# raspiled
This project is a raspberry pi network based controller for a ws2182b led strip. The raspberry pi controls the led strip, and hosts a server to offer control from any wifi connected device. The server is hosted on port 8000 of the raspberry pi.

Current supported modes:
Block Color - set the entire strip to one color
Fade - Slowly crossfade between different colors
Fairy - lights will twinkle based on the settings
Stripe - Choose several colors and a time interval. The colors will move down the strip.
