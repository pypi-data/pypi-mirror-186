from __future__ import annotations
import logging
import os
import re
from pathlib import Path

from PyPDF2 import PdfFileWriter, PdfFileReader

from .mailbox import MailBox
from .printer import PrintHost, PrinterError

logger = logging.getLogger(__name__)

class Processor():
    """Object used to process incoming emails by printing them and sending confirmation emails
    afterward. This class contains the processing 'business logic'."""

    def __init__(self, mailbox: MailBox, print_host: PrintHost, temp_dir: str="/tmp/ninjaprinter"):
        self.mailbox = mailbox
        self.print_host = print_host
        self.temp_dir = temp_dir

    def process(self, *, 
                from_folder: str="INBOX",
                to_folder: str="printed",
                error_folder: str="error",
                unsupported_folder: str="unsupported",
                file_extensions: list=["pdf"],
                page_limit: int=5,
                payment_url: str=None
    ) -> None:
        # if target folder does not exist in mailbox, create it
        for target_folder in [from_folder, to_folder, error_folder, unsupported_folder]:
            if not self.mailbox.imap.folder.exists(target_folder):
                logger.debug(f"{target_folder} folder did not exist in mailbox, creating folder...")
                self.mailbox.imap.folder.create(target_folder)
                logger.debug("folder creation successful")

        # load mails in from_folder
        self.mailbox.imap.folder.set(from_folder)
        logger.debug(f"loading mails in {from_folder}...")
        messages = list(self.mailbox.imap.fetch(bulk=True))
        logger.info(f"{len(messages)} unprocessed mails in {from_folder}")

        # process each mail
        for msg_nr, msg in enumerate(messages):
            msg_total = len(messages)
            msg_nr = msg_nr + 1
            logger.info(f"[mail {msg_nr}/{msg_total}] from: {msg.from_}, subject: {msg.subject}")
        
            if not msg.attachments:
                logger.info(f"no attachments, moving to {unsupported_folder}")
                self.mailbox.imap.move(msg.uid, unsupported_folder)
                self.mailbox.imap.delete(msg.uid)
                continue

            # print attachments
            process_job = self.ProcessJob(self, msg.attachments, file_extensions, page_limit)
            process_job.process()
           
            # archive email and send confimration
            mail_data = {
                "recipient": msg.from_.split("@")[0],
                "print_items": process_job.print_items,
                "payment_url": payment_url,
                "file_extensions": ", ".join(file_extensions),
                "page_limit": page_limit
            }
            if process_job.status == "Printed":
                logger.info(f"print successful, moving to {to_folder}")
                destination_folder = to_folder
                mail_template = 'success.html'
                mail_subject = "Print Success"
            elif process_job.status == "Partial":
                logger.info(f"print partial, moving to {to_folder}")
                destination_folder = error_folder
                mail_template = 'partial.html'
                mail_subject = "Partial Print"
            elif process_job.status == "Error":
                logger.info(f"print error, moving to {error_folder}")
                destination_folder = error_folder
                mail_template = 'error.html'
                mail_subject = "Print Error"
            elif process_job.status == "Unsupported":
                logger.info(f"unsupported file(s), moving to {unsupported_folder}")
                destination_folder = unsupported_folder
                mail_template = 'error.html'
                mail_subject = "Unsupported files"
            else:
                logger.info(f"unexpected print status, moving to {error_folder}")
                destination_folder = error_folder
                mail_template = 'error.html'
                mail_subject = "Print Error"

            self.mailbox.imap.move(msg.uid, destination_folder)
            self.mailbox.imap.delete(msg.uid)
            self.mailbox.send_mail(mail_template, msg.from_, mail_subject, mail_data)

    class ProcessJob():
        """Object used to store process job data and trigger the processing and to monitor its 
        progress."""

        def __init__(self, processor: Processor, attachments: list, file_extensions: list, page_limit: int) -> None:
            self.processor = processor
            self.file_extensions = file_extensions
            self.page_limit = int(page_limit)
            self.print_items = []
            for attachment in attachments:
                if not attachment.filename: continue
                file_path = self.create_file(attachment.payload, processor.temp_dir, attachment.filename)
                self.print_items.append(self.PrintItem(self, file_path))
        
        @staticmethod
        def create_file(data: bytes, folder_path: str, file_name: str) -> str:
            folder_path = Path(folder_path)
            folder_path.mkdir(parents=True, exist_ok=True)
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'wb') as file_to_print:
                file_to_print.write(data)
            return file_path
        
        def process(self) -> None:
            for print_item in self.print_items:
                print_item.print()
        
        @property
        def status(self) -> str:
            statuses = []
            for print_item in self.print_items:
                statuses.append(print_item.status)
            
            if "Printing" in statuses:
                return "Printing"
            if "Printed" in statuses and ("Error" in statuses or "Unsupported" in statuses):
                return "Partial"
            if "Error" in statuses:
                return "Error"
            if "Unsupported" in statuses:
                return "Unsupported"
            else:
                return "Printed"

    
        class PrintItem():
            """Object used to store individual to be printed attachment and to trigger the printing. 
            This class contains the supported files check and limits the number of pages."""

            def __init__(self, process_job: Processor.ProcessJob, file_path: str) -> None:
                self.process_job = process_job
                self.file_path = file_path
                self.print_job = None
                self.comment = None
                
                # check if file extension is supported
                if any(re.search(f".*\.{file_extension}$", file_path, re.IGNORECASE) for file_extension in self.process_job.file_extensions):
                    self.print_job = self.process_job.processor.print_host.create_print_job(file_path)
                    self.status = "Created"
                else:
                    self.status = "Unsupported"
                    self.comment = f"File extension {os.path.splitext(file_path)[-1]} is not supported"
                    return
                
                # reduce nr of pages if page limit is exceeded
                if re.search(".*\.pdf$", file_path, re.IGNORECASE):
                    input_file = PdfFileReader(file_path, "rb")
                    nr_pages = input_file.getNumPages()
                    if  nr_pages > self.process_job.page_limit:
                        logger.info(f"pdf file exceed page limit of {self.process_job.page_limit}: {nr_pages} pages were reduced to {self.process_job.page_limit} pages")
                        output_file = PdfFileWriter()
                        for i in range(self.process_job.page_limit):
                            page = input_file.getPage(i)
                            output_file.addPage(page)
                        with open(file_path, 'wb') as file:
                            output_file.write(file)
            
            def print(self) -> None:
                try:
                    if self.print_job:
                        self.status= "Printing"
                        self.print_job.print()
                        self.status = "Printed"
                        logger.debug("print success")
                except PrinterError as err:
                    logger.debug(f"print error: {err}")
                    self.status = "Error"
                    self.comment = err
                os.unlink(self.file_path)
            
            @property
            def file_name(self) -> str:
                return os.path.basename(self.file_path)

            
