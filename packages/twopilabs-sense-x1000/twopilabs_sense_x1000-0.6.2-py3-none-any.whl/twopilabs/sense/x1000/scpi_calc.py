from twopilabs.utils.scpi import *
from .x1000_base import SenseX1000Base


class ScpiCalc(object):
    """Class containing SCPI commands concerning CALCULATE subsystem"""

    def __init__(self, device: ScpiDevice):
        self.device = device

    def trace_list(self, traces: Optional[List[int]] = None) -> List[int]:
        """Sets or gets the list of selected traces that are processed and for which CALC data is available"""
        if traces is not None:
            self.device.execute('CALCULATE:TRACE:LIST', param=ScpiNumList(traces))
        else:
            traces = self.device.execute('CALCULATE:TRACE:LIST?', result=ScpiNumList).as_list()

        self.device.raise_error()
        return traces

    def data(self) -> SenseX1000Base.Acquisition:
        stream = self.device.execute("CALC:DATA?", result=ScpiArbStream)
        return SenseX1000Base.Acquisition._from_stream(stream)