# Process for Assebling Case for Camera

## Parts

The parts are:
  1. Body - as in Arducam-Body.obj
  2. Front - as in Arducam-Front.obj

Both were made using FreeCAD.

## Significance

The front is the main front-facing side that has the slot for the camera lense and holes for the screws to go through.
The back is the other 5 sides and has a coin-like slot that is used to insert the ribbon cable.

## Procedure

### Before starting

Be sure to have connected your Arducam to the pi once and used libcamera commands to verify it works.

### Procedure

1. Place Front bottom-up flat on the floor
2. Insert your arducam so that the lenses goes inside the hole and the mounting holes align
3. Carefully put the ribbon cable through the thin coin-like ribbon cable hole at the bottom of Body
4. Place Front and the camera, now connected, on top of Body, making sure the mounting holes align
5. Put the M2 Screw through the mounting hole, repear for the other 3 screws
6. Twist the M2 Nut onto the back of the M2 Screw, repeat for the other 3 nuts
7. Align everything so that Front is facing towards you and ensure that the camera is firm
8. Attach the other end of the cable back onto the pi

## Test

Confirm lib-camera commands work again
