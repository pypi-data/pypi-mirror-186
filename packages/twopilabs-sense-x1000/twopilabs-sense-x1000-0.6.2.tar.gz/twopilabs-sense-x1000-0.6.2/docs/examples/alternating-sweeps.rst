.. _examples-alternating-sweeps:

Running Alternating Sweeps
--------------------------
In some application scenarios it might be desirable to run multiple sweeps during one acquisition (i.e. one trigger event), where however the sweep direction alternates between upchirps and downchirps.
This includes scenarios where a doppler shift compensation or other kind of compensations are used. 

The following example shows how to set up the device to perform this measurement and receive the acquired raw data in one or multiple pairs.

.. code-block:: python

   from twopilabs.sense.x1000 import SenseX1000
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(15, 10))
   ax = fig.add_subplot(1, 1, 1)


   # Look for X1000 series devices
   devices = SenseX1000.find_devices()

   if len(devices) == 0:
       raise SystemExit("No Sense X1000 series devices found")

   # Open the first device found, manually set the timeout if you expect data transfers over longer periods of time
   with SenseX1000.open_device(devices[0], timeout=30) as device:
       # This resets the device configuration state to their default values
       device.core.rst()

       # Set start and stop frequency of the FMCW sweep in Hertz and the sweep time (duration) in seconds.
       device.sense.frequency_start(182E9)
       device.sense.frequency_stop(126E9)
       device.sense.sweep_time(8E-3)
       device.sense.sweep_count(4)
       device.sense.sweep_period(60E-3)

       # This configuration will begin with the configured downchirp and will alternate the chirp direction after every sweep
       device.sense.sweep_mode(SenseX1000.SweepMode.ALTERNATING)

       # Initiate for one cycle, automatically triggers the acquisition by default
       acq = device.initiate.immediate_and_receive()

       # For this example we would like to iteratively process one upchirp and downchirp pair as a group.
       # This can be easily done using the generator syntax:
       for data in acq.data(n_sweeps=2):
           # data will now contain 2 consecutive sweeps and the for loop will run until acquisition is done
           # Plot data and generate some descriptive labels for the legend
           plots = ax.plot(data.array[:,0,:].T)
           for plot, seq_num, sweep_dir in zip(plots, data.seq_nums, data.sweep_dirs):
               plot.set_label(f'Seq. Num {seq_num}, Sweep Dir {SenseX1000.SweepDirection(sweep_dir).name}')

   # Generate legend and show the plot
   plt.legend()
   plt.show()
