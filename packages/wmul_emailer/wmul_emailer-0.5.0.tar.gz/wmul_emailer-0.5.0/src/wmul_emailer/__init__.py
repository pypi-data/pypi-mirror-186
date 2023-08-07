"""
@Author = 'Mike Stanley'

Utility to send an email to multiple addresses. Primarily intended for cli 
applications. The various fields such as server host, username, etc. are 
entered at the command line, used to construct a wmul_emailer.EmailSender 
object, and that object is passed into the main part of the script. 
The main part of the script can use it as needed to report errors or results 
without having to worry about the e-mail details.

============ Change Log ============
2023-Jan-17 = Changed License from GPLv2 to GPLv3. 

2023-Jan-13 = Added documentation. Allow caller to defer providing 
              from_email_address and destination_email_addresses until 
              send_email is called.

2022-May-06 = Changed License from MIT to GPLv2.

2018-May-23 = Reworked API to be class based.

2018-May-18 = Imported from Titanium_Monticello

              Fresh start, so no longer need two API endpoints for one function.

2017-Nov-15 = Bugfix for the destination email addresses not being a list.

2017-Nov-14 = Added SendEmailArguments to encapsulate the arguments and 
              send_email2 to consume those arguments.

2017-Jun-27 = Created.

============ License ============
Copyright (c) 2017-2023 Michael Stanley

This file is part of wmul_emailer.

wmul_emailer is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later 
version.

wmul_emailer is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR 
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
wmul_emailer. If not, see <https://www.gnu.org/licenses/>. 
"""
from email.mime.text import MIMEText
from smtplib import SMTP

__version__ = "0.5.0"


__all__ = ["EmailSender"]


class EmailSender:

    def __init__(self, server_host, port, user_name, password, from_email_address=None, destination_email_addresses=None):
        if destination_email_addresses:
            if not _destination_emails_correct_type(destination_email_addresses):
                raise TypeError("destination_email_addresses must be a list, tuple, or str.")
            if isinstance(destination_email_addresses, str):
                destination_email_addresses = [destination_email_addresses]

        self.server_host = server_host
        self.port = port
        self.user_name = user_name
        self.password = password
        self.from_email_address = from_email_address
        self.destination_email_addresses = destination_email_addresses

    def send_email(self, email_body, email_subject, from_email_address=None, destination_email_addresses=None):
        if destination_email_addresses:
            if not _destination_emails_correct_type(destination_email_addresses):
                raise TypeError("destination_email_addresses must be a list, tuple, or str.")
            if isinstance(destination_email_addresses, str):
                destination_email_addresses = [destination_email_addresses]
        elif not self.destination_email_addresses:
            raise ValueError("destination_email_addresses must be provided to either the constructor or to the send_email function")
        else:
            destination_email_addresses = self.destination_email_addresses

        if not from_email_address:
            if not self.from_email_address:
                raise ValueError("from_email_address must be provided to either the constructor or to the send_email function.")
            else:
                from_email_address = self.from_email_address

        with SMTP(self.server_host, port=self.port) as server:
            server.login(user=self.user_name, password=self.password)
            for email_address in destination_email_addresses:
                msg = MIMEText(email_body)
                msg['Subject'] = email_subject
                msg['From'] = from_email_address
                msg['To'] = email_address
                server.send_message(msg)


def _destination_emails_correct_type(destination_email_addresses):
    return (
        isinstance(destination_email_addresses, list) or 
        isinstance(destination_email_addresses, tuple) or
        isinstance(destination_email_addresses, str)
    )
