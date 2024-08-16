Raspberry Pi OS Image Setup
===========================

Next we will flash the Operating System onto the Raspberry Pi, which will serve
as the high-level "brains" for Jubilee.

We'll be installing a *headless* setup without a desktop as `strongly recommended <https://www.klipper3d.org/Installation.html#installing-via-kiauh>`_ by *Klipper*, the firmware we'll be using to manage the machine's motors and sensors.
Don't worry, though. We will ultimately still be able to control the machine through a graphical user interface using a web browser, or through Python directly.


You will need
-------------

* a MicroSD card
* an SD card-to-USB adapter (if you cannot)
* a PC or laptop


Instructions
------------

Plug the MicroSD card into your PC.

Download, install, and launch `RPi Imager <https://www.raspberrypi.com/software/>`_.

From the *Choose OS* option, select *Raspberry Pi OS (Other)*, and select *Raspberry Pi OS Lite (64bit)*.

.. grid:: 2

   .. grid-item::
      :padding: 0 0 1 1

      .. figure:: pics/rpi_imaging/rpi_imager.avif
         :width: 600
         :class: dark-light
         :align: center

   .. grid-item::
      :padding: 0 0 1 1

      .. figure:: pics/rpi_imaging/rpi_os_lite_64.avif
         :width: 600
         :class: dark-light
         :align: center

In the *Choose Storage* option, select your SD card; then select *Next*.

Decide on a name for your machine that will be unique to the network you install it on.
Your machine will appear on your network as :code: `<machine_name>.local`.
If your are planning to connect to this machine over Wi-Fi, enter the network name and password now.
(Double-check this!)

In the next pane check *Enable SSH*.
This will be the primary way we connect to Jubilee and install packages before installing supplementary GUIs.
