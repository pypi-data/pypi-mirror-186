from __future__ import annotations
import logging
import os
from time import sleep, time

import cups

logger = logging.getLogger(__name__)

class PrinterError(Exception):
    """Exception raised for errors during login."""

    def __init__(self, message):
        super().__init__(message)

class PrintHost():
    """Object used to interact with a printer using cups, such as storing printer data and creating
    a print job."""

    def __init__(self, *, print_host_url: str, printer: str=None, job_timeout: int=120):
        self.print_host_url = print_host_url
        self.print_host = None
        self.printer = printer
        self.job_timeout = job_timeout
    
    def create_print_job(self, file_path: str) -> PrintJob:
        return PrintHost.PrintJob(self, file_path)

    def connect(self):
        # connect to cups host
        try:
            self.print_host = cups.Connection(self.print_host_url)
            logger.debug("connected to print host")
            if not self.printer:
                self.printer = self.print_host.getDefault()
        except RuntimeError as err:
            raise PrinterError(f"could not connect to cups host on {self.print_host_url}") from err

    """
    # where is this used? does not seem to match the printjob class.
    def print(self, *, file_path: str, printer=None):
        print_job = self.PrintJob(file_path)
        print_job.print(print_host=self.print_host, printer=printer)
        """


    class PrintJob():
        """Object used to store print job data and trigger the printing."""

        # Job states retrieved from https://tools.ietf.org/html/rfc2911#section-4.3.7
        JOB_STATES = {
            3: 'PENDING',
            4: 'PENDING-HELD',
            5: 'PROCESSING',
            6: 'PROCESSING-STOPPED',
            7: 'CANCELLED',
            8: 'ABORTED',
            9: 'COMPLETED'
        }
        TERMINAL_STATES = [7, 8, 9]
        SUCCESS_STATES = [9]

        def __init__(self, print_host: PrintHost, file_path: str):
            self.print_host = print_host
            self.file_path = file_path
            self.job_state = None

        def print(self):
            """Start the printing and monitor the job state. An error will be raised if the print 
            was not successful."""
            try:
                file_name = os.path.basename(self.file_path)
                logger.debug(f"printing {file_name} ...")
                job_id = self.print_host.print_host.printFile(self.print_host.printer, self.file_path, file_name, {})
                job_start_time = time()
                while self.job_state not in self.TERMINAL_STATES:
                    self.job_state = self.print_host.print_host.getJobAttributes(job_id).get('job-state')
                    sleep(1)
                    if (time() - job_start_time) > self.print_host.job_timeout:
                        break
            except (cups.IPPError, cups.HTTPError) as err:
                raise PrinterError("Printer communication error") from err
            
            if self.job_state in self.SUCCESS_STATES:
                logger.debug("print success!")
                return
            if self.job_state in self.TERMINAL_STATES:
                logger.warning(f"Print error: {self.job_state}': {self.JOB_STATES.get(self.job_state)}")
                raise PrinterError(f"{self.JOB_STATES.get(self.job_state)}")
            logger.warning(f"Print timeout: '{self.job_state}': {self.JOB_STATES.get(self.job_state)}")
            raise PrinterError(f"TIMEOUT/{self.JOB_STATES.get(self.job_state)}")

