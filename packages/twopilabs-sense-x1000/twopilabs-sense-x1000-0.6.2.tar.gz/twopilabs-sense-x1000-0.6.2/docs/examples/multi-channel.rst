.. _examples-multi-channel:

Retrieving Data from Multiple Channels
--------------------------------------
In this example we retrieve radar data from multiple hardware channels (if available) by using the `trace` concept.

In the context of the radar system, a trace is a simple representation of multiple data points, similar to a trace on an oscilloscope, where each sweep within an acquisition can contain multiple traces.
When the radar is configured for raw data access (i.e. no processing is done on the device, which is the default setting), the traces directly map to the raw data of the available hardware channels.

.. note::

   Not all hardware variants have support for multiple hardware channels.


.. code-block:: python

   from twopilabs.sense.x1000 import SenseX1000
   import matplotlib.pyplot as plt

   # Look for X1000 series devices
   devices = SenseX1000.find_devices()

   if len(devices) == 0:
       raise SystemExit("No Sense X1000 series devices found")

   # Open the first device found, manually set the timeout if you expect data transfers over longer periods of time
   with SenseX1000.open_device(devices[0], timeout=30) as device:
       # This resets the device configuration state to their default values
       device.core.rst()

       # Set start and stop frequency of the FMCW sweep in Hertz and the sweep time (duration) in seconds.
       device.sense.frequency_start(182E9);
       device.sense.frequency_stop(126E9);
       device.sense.sweep_time(8E-3);
       device.sense.sweep_count(1);

       # By default, only trace 0 is enabled. A list of traces that should be enabled can be set using the calc.trace_list command
       # This activates trace 0 and trace 2 (center and right/left channel)
       device.calc.trace_list([0,2]);

       # Perform acquisition and read all data
       acq = device.initiate.immediate_and_receive()
       data = acq.read()

       # Plot data for all traces of the first and only sweep
       plt.figure(figsize=(15, 10))
       plt.plot(data.array[0,:,:].T);

   # Generated axes label, legend and show plot
   plt.xlabel('ADC Sample Points');
   plt.ylabel('Amplitude (16-bit Signed Integer)');
   plt.legend([f'Trace {trace}' for trace in data.trace_list])
   plt.show()
