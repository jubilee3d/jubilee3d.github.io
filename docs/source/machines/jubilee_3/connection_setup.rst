Network Setup
=============

Wired Setup
-----------

Windows
~~~~~~~

Install `Bonjour Print Services for Windows <https://support.apple.com/en-us/106380>`_.
Bonjour, aka *Zeroconf*, dramatically simplifies the way the machine will appear on your PC when both are connected to the same network.

To share the host PC's internet with the Rasbperry Pi,


Ubuntu Linux
~~~~~~~~~~~~

Plug in your USB-to-Ethernet adapter.
Under *Settings → Network*, click on option that appears under *USB Ethernet*.

.. grid:: 2

   .. grid-item::
      :padding: 0 0 1 1

      .. figure:: pics/linux_wired_setup_dhcp1.avif
         :width: 600
         :class: dark-light
         :align: center

   .. grid-item::
      :padding: 0 0 1 1

      .. figure:: pics/linux_wired_setup_dhcp2.avif
         :width: 600
         :class: dark-light
         :align: center

Under the *IPv4* tab, click *Shared to Other Computers*.
That's it!


Wireless Setup
--------------


Wired and Wireless Setup
------------------------

It's possible to setup *both* wired and wireless connections.
If you do so, and you want to login into the Pi over a specific connection, you
will need to know the IP address.


Test the Connection
~~~~~~~~~~~~~~~~~~~


Windows
~~~~~~~

Ubuntu Linux
~~~~~~~~~~~~

After configuring the network and powering on the Pi for the first time, note that it may take up to 90 seconds for the device to appear.

Ping the device from your PC with:

.. code:: bash

  ping raspberrypi.local

(You may have to try this a few times if this is your first time booting the device or connecting to it.)

Log into the Pi
---------------


Windows
~~~~~~~
