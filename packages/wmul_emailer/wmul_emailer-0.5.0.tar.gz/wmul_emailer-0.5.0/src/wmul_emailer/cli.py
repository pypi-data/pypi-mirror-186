"""
@Author = 'Mike Stanley'

A cli is provided to test that the credentials are functional and that the 
system can send e-mails.

============ Change Log ============
01/17/2023 = Changed License from GPLv2 to GPLv3.

01/13/2023 = Added documentation.

08/10/2022 = Created.

============ License ============
Copyright (c) 2022-2023 Michael Stanley

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
import click
import wmul_emailer
from wmul_click_utils import RequiredUnless


@click.command()
@click.version_option()
@click.option("--email", type=str, multiple=True, cls=RequiredUnless, 
              required_unless=["license"],
              help="The e-mail address to which the results should be sent.")
@click.option("--server", type=str, cls=RequiredUnless, 
              required_unless=["license"], 
              help="The hostname or ip address of the smtp server.")
@click.option("--port", type=int, default=25,  
              help="The port number on which the smtp server resides.")
@click.option("--username", type=str, cls=RequiredUnless, 
              required_unless=["license"],
              help="The username to authenticate with the smtp server.")
@click.option("--password", type=str, cls=RequiredUnless, 
              required_unless=["license"],
              help="The password to authenticate with the smtp server.")
@click.option("--from_address", type=str, cls=RequiredUnless, 
              required_unless=["license"],
              help="The 'from' e-mail address.")
@click.option("--license", is_flag=True, 
              help="Display the abbreviated license information.")
def send_test_email(email, server, port, username, password, from_address, 
                    license):
    if license:
        print("wmul_emailer Copyright (C) 2017-2023  Michael Stanley \nThis "
              "program is licensed under the GPL version 3.\nThis program "
              "comes with ABSOLUTELY NO WARRANTY. This is free software, and "
              "you are welcome to redistribute it under certain conditions; "
              "see https://www.gnu.org/licenses/gpl-3.0.txt for details.")
    else:
        emailer = wmul_emailer.EmailSender(
            server_host=server,
            port=port,
            user_name=username,
            password=password,
            destination_email_addresses=email,
            from_email_address=from_address
        )

        emailer.send_email(
            email_body="This is the test e-mail from wmul_emailer.py. "
                    "If you are reading this, the software is configured correctly.",
            email_subject="Test e-mail from wmul_emailer"
        )
