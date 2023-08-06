.. _section-examples:

Examples
========
This section contains a list of examples that focus on various aspects of using your 2πSENSE X1000 series device.
The example scripts shown here are directly runnable by a python system where the required packages (see :ref:`section-introduction`) are installed.

.. toctree::
   :hidden:

   alternating-sweeps
   multi-channel
   live-plot
   fast-plot
   range-doppler

* :ref:`examples-alternating-sweeps`

  This example shows how the device can be used to perform multiple sweeps by a single trigger event with alternating sweep slopes.
  The generator syntax method is used to receive and process the data in pairs of 2 consecutive sweeps.

* :ref:`examples-multi-channel`

  Depending on the physical configuration, 2πSENSE X1000 series device can support multiple receive channels. 
  This example shows how data can be received from multiple channels by enable additional `traces`.

* :ref:`examples-live-plot` 

  A simple live plotting demo with basic fft processing and axis calculation. 
  Plotting is handled by ``matplotlib`` and sweep parameters can be customized from command-line

* :ref:`examples-fast-plot`

  An improved version of the live-plot demonstrating a very responsive Qt+PyQtGraph GUI with peak detection and range history.

* :ref:`examples-range-doppler`

  The Range-Dopppler example shows how the 2πSENSE X1000 series devices can be used to perform FMCW sweeps with very precise and reliable timing.
  An entire acquisition of multiple sweeps is processed using a range-doppler algorithm providing a 2D color-coded live image of both distance and recession velocity.
