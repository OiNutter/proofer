Proofer
=======

Simple python app with GUI for running on a RaspberryPI and controlling a dough
proofing box.

Setup
-----

First, you need to build your box, this is what I used:

* 1 x [Polystyrene Box](https://www.amazon.co.uk/slp/polystyrene-boxes/df2ypw48d236qz8).
I got mine from my wife's work but you can find them online
* 1 x [RaspberryPi](https://thepihut.com/collections/raspberry-pi/products/raspberry-pi-3-model-b-plus).
Any spec will do but if you want a gui you'll need one that
supports a touchscreen. Mine's an older one without wifi so I needed a dongle but
I think most newer ones have wifi built in. You only really need wifi for debugging
* 1 x Touchscreen for RaspberryPi. I used the [PiTFT](https://thepihut.com/products/adafruit-pitft-plus-320x240-2-8-tft-capacitive-touchscreen) which fit quite nicely, gave me plenty of screen real estate and came with some physical buttons which I could assign extra functions to.
* 1 x RaspberryPi Case. I used this one which gave access
to the PiTFT screen, came with buttons to go with the
screens buttons and had a decent sized opening to take the
GPIO cables out of.
* 1 x [Temperature Probe](https://thepihut.com/products/waterproof-ds18b20-sensor-kit?ref=isp_rel_prd&isp_ref_pos=2). This one comes with the breakout board and gpio pins to make wiring it easy.
* 1 x [Relay Board](https://thepihut.com/products/raspberry-pi-relay-board). This will let you turn the heat pad on and off.
* 1 x 9v/12v power adaptor. If you don't want to sacrifice the plug off the end you could also get this [adaptor](https://thepihut.com/products/female-dc-power-adapter-2-1mm-jack-to-screw-terminal-block) to convert between the adaptor and the wired heatmat.
* 1 x Heat Mat. I used one of [these](https://thepihut.com/products/electric-heating-pad-14cm-x-5cm) but it may also be worth looking at [these silicone covered ones](https://uk.rs-online.com/web/c/automation-control-gear/temperature-control-process-heating/silicone-heater-mats/) for a bit more safety
* 1 x Cardboard or Plastic Box. This will store the spare cable and the relay board. Needs to be able to have holes drilled in the side.
* 1 x Length of electrical cable with live and neutral wires
* 1 x [Pack of GPIO cables](https://thepihut.com/products/thepihuts-jumper-bumper-pack-120pcs-dupont-wire). This will give you way more than you need.
* 1 x Length of cable trunking (this will depend on the size of your box and
  where you situate all the electronics)
