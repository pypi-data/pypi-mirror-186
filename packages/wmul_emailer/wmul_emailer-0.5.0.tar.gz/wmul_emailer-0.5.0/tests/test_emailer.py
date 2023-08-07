"""
@Author = 'Mike Stanley'

============ Change Log ============
2023-Jan-17 = Refactor to reduce unnecessary code duplication. Change license
              from GPLv2 to GPLv3.

2023-Jan-13 = Added tests for when the e-mail addresses are missing from both 
              the constructor and the function. Added/Modified tests for when 
              a single destination e-mail address is passed in. Re-wrote tests 
              to make use of wmul_test_utils.make_namedtuple. 

2022-May-06 = Changed License from MIT to GPLv2.

2018-May-18 = Created.

============ License ============
Copyright (c) 2018-2023 Michael Stanley

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
import contextlib
import pytest
import wmul_emailer
from wmul_test_utils import make_namedtuple, \
    generate_true_false_matrix_from_list_of_strings, assert_has_only_these_calls


setup_send_email_params, setup_send_email_ids = \
    generate_true_false_matrix_from_list_of_strings(
        "setup_send_email_options", 
        ["use_tuple_of_addresses"]
    )

@pytest.fixture(scope="function", params=setup_send_email_params, 
                ids=setup_send_email_ids)
def setup_send_email(mocker, request):
    use_tuple_of_addresses = request.param.use_tuple_of_addresses
    mock_server = mocker.Mock()

    @contextlib.contextmanager
    def mock_server_function(host, port):
        yield mock_server

    mock_smtp = mocker.Mock(side_effect=mock_server_function)
    mocker.patch("wmul_emailer.SMTP", mock_smtp)

    def mock_mimetext_function(data):
        mimetext_contents = {"Body": data}
        return mimetext_contents

    mock_mimetext = mocker.Mock(side_effect=mock_mimetext_function)
    mocker.patch(
        "wmul_emailer.MIMEText",
        mock_mimetext
    )

    mock_body = "mock_body"
    mock_subject = "mock_subject"

    mock_destination_email_addresses = ["foo@example.com", "bar@example.com"]
    if use_tuple_of_addresses:
        mock_destination_email_addresses = \
            tuple(mock_destination_email_addresses)
    mock_host = "mock_host"
    mock_port = "mock_port"
    mock_username = "mock_username"
    mock_password = "mock_password"
    mock_from_address = "mock_from_email_address"

    return make_namedtuple(
        "setup_send_email",
        mock_server=mock_server, 
        mock_smtp=mock_smtp, 
        mock_destination_email_addresses=mock_destination_email_addresses, 
        mock_host=mock_host, 
        mock_port=mock_port, 
        mock_username=mock_username,
        mock_password=mock_password, 
        mock_from_address=mock_from_address,
        mock_body=mock_body,
        mock_subject=mock_subject,
        mock_mimetext=mock_mimetext
    )


def test_send_email_dest_addresses_not_a_list_tuple_or_str(setup_send_email):
    with pytest.raises(TypeError):
        emailer = wmul_emailer.EmailSender(
            destination_email_addresses=object(),
            server_host=setup_send_email.mock_host,
            port=setup_send_email.mock_port,
            user_name=setup_send_email.mock_username,
            password=setup_send_email.mock_password,
            from_email_address=setup_send_email.mock_from_address
        )

    confirm_mocks_not_called(setup_send_email)


def confirm_mocks_not_called(mocks_not_called_args):
    mocks_not_called_args.mock_smtp.assert_not_called()
    mocks_not_called_args.mock_server.assert_not_called()
    mocks_not_called_args.mock_mimetext.assert_not_called()
    mocks_not_called_args.mock_server.login.assert_not_called()
    mocks_not_called_args.mock_server.send_message.assert_not_called()


@pytest.fixture(scope="function")
def setup_send_email_correctly_created(setup_send_email):
    emailer = wmul_emailer.EmailSender(
        destination_email_addresses=\
            setup_send_email.mock_destination_email_addresses,
        server_host=setup_send_email.mock_host,
        port=setup_send_email.mock_port,
        user_name=setup_send_email.mock_username,
        password=setup_send_email.mock_password,
        from_email_address=setup_send_email.mock_from_address
    )

    return make_namedtuple(
        "setup_send_email_correctly_created",
        emailer=emailer, 
        setup_send_email=setup_send_email
    )


def test_send_email_called_correctly_normal_path(
        mocker, 
        setup_send_email_correctly_created
    ):
    
    setup_send_email = setup_send_email_correctly_created.setup_send_email

    setup_send_email_correctly_created.emailer.send_email(
        setup_send_email.mock_body,
        setup_send_email.mock_subject
    )

    confirm_mocks_called_correctly(
        make_namedtuple(
            "correct_call_args",
            mock_smtp=setup_send_email.mock_smtp,
            mock_host=setup_send_email.mock_host,
            mock_port=setup_send_email.mock_port,
            mock_server=setup_send_email.mock_server,
            mock_username=setup_send_email.mock_username,
            mock_password=setup_send_email.mock_password,
            mock_destination_email_addresses=\
                setup_send_email.mock_destination_email_addresses,
            mock_body=setup_send_email.mock_body,
            mock_subject=setup_send_email.mock_subject,
            mock_from_address=setup_send_email.mock_from_address,
            mocker=mocker
        )
    )


def confirm_mocks_called_correctly(correct_call_args):
    correct_call_args.mock_smtp.assert_called_once_with(
        correct_call_args.mock_host, 
        port=correct_call_args.mock_port
    )

    correct_call_args.mock_server.login.assert_called_once_with(
        user=correct_call_args.mock_username, 
        password=correct_call_args.mock_password
    )

    expected_send_message_calls = []

    for this_email_address in \
                            correct_call_args.mock_destination_email_addresses:
        this_message = {
            "Body": correct_call_args.mock_body,
            "Subject": correct_call_args.mock_subject,
            "From": correct_call_args.mock_from_address,
            "To": this_email_address
        }
        expected_send_message_calls.append(
            correct_call_args.mocker.call(this_message)
        )

    assert_has_only_these_calls(
        correct_call_args.mock_server.send_message,
        expected_send_message_calls
    )


def test_send_email_called_correctly_different_from_address(
        mocker, 
        setup_send_email_correctly_created
    ):

    setup_send_email = setup_send_email_correctly_created.setup_send_email

    new_mock_from_address = "new_mock_from_address"

    setup_send_email_correctly_created.emailer.send_email(
        setup_send_email.mock_body,
        setup_send_email.mock_subject,
        from_email_address=new_mock_from_address
    )

    confirm_mocks_called_correctly(
        make_namedtuple(
            "correct_call_args",
            mock_smtp=setup_send_email.mock_smtp,
            mock_host=setup_send_email.mock_host,
            mock_port=setup_send_email.mock_port,
            mock_server=setup_send_email.mock_server,
            mock_username=setup_send_email.mock_username,
            mock_password=setup_send_email.mock_password,
            mock_destination_email_addresses=\
                setup_send_email.mock_destination_email_addresses,
            mock_body=setup_send_email.mock_body,
            mock_subject=setup_send_email.mock_subject,
            mock_from_address=new_mock_from_address,
            mocker=mocker
        )
    )


def test_send_email_called_correctly_different_destination_address(
        mocker, 
        setup_send_email_correctly_created
    ):

    setup_send_email = setup_send_email_correctly_created.setup_send_email

    new_mock_destination_addresses = [
        "new_mock_destination_address_1", 
        "new_mock_destination_address_2"
    ]

    setup_send_email_correctly_created.emailer.send_email(
        setup_send_email.mock_body,
        setup_send_email.mock_subject,
        destination_email_addresses=new_mock_destination_addresses
    )

    confirm_mocks_called_correctly(
        make_namedtuple(
            "correct_call_args",
            mock_smtp=setup_send_email.mock_smtp,
            mock_host=setup_send_email.mock_host,
            mock_port=setup_send_email.mock_port,
            mock_server=setup_send_email.mock_server,
            mock_username=setup_send_email.mock_username,
            mock_password=setup_send_email.mock_password,
            mock_destination_email_addresses=new_mock_destination_addresses,
            mock_body=setup_send_email.mock_body,
            mock_subject=setup_send_email.mock_subject,
            mock_from_address=setup_send_email.mock_from_address,
            mocker=mocker
        )
    )


def test_send_email_called_correctly_different_from_and_destination_address(
        mocker, 
        setup_send_email_correctly_created
    ):

    setup_send_email = setup_send_email_correctly_created.setup_send_email

    new_mock_from_address = "new_mock_from_address"
    new_mock_destination_addresses = [
        "new_mock_destination_address_1", 
        "new_mock_destination_address_2"
    ]

    setup_send_email_correctly_created.emailer.send_email(
        setup_send_email.mock_body,
        setup_send_email.mock_subject,
        from_email_address=new_mock_from_address,
        destination_email_addresses=new_mock_destination_addresses
    )

    confirm_mocks_called_correctly(
        make_namedtuple(
            "correct_call_args",
            mock_smtp=setup_send_email.mock_smtp,
            mock_host=setup_send_email.mock_host,
            mock_port=setup_send_email.mock_port,
            mock_server=setup_send_email.mock_server,
            mock_username=setup_send_email.mock_username,
            mock_password=setup_send_email.mock_password,
            mock_destination_email_addresses=new_mock_destination_addresses,
            mock_body=setup_send_email.mock_body,
            mock_subject=setup_send_email.mock_subject,
            mock_from_address=new_mock_from_address,
            mocker=mocker
        )
    )


def test_send_email_called_correctly_str_destination_address(
        setup_send_email_correctly_created,
        mocker
    ):

    setup_send_email = setup_send_email_correctly_created.setup_send_email

    new_mock_from_address = "new_mock_from_address"
    new_mock_destination_address = "new_mock_destination_address_1"

    setup_send_email_correctly_created.emailer.send_email(
        setup_send_email.mock_body,
        setup_send_email.mock_subject,
        from_email_address=new_mock_from_address,
        destination_email_addresses=new_mock_destination_address
    )

    confirm_mocks_called_correctly(
        make_namedtuple(
            "correct_call_args",
            mock_smtp=setup_send_email.mock_smtp,
            mock_host=setup_send_email.mock_host,
            mock_port=setup_send_email.mock_port,
            mock_server=setup_send_email.mock_server,
            mock_username=setup_send_email.mock_username,
            mock_password=setup_send_email.mock_password,
            mock_destination_email_addresses=[new_mock_destination_address],
            mock_body=setup_send_email.mock_body,
            mock_subject=setup_send_email.mock_subject,
            mock_from_address=new_mock_from_address,
            mocker=mocker
        )
    )


def test_send_email_no_destination_email_addresses(setup_send_email):
    emailer = wmul_emailer.EmailSender(
        server_host=setup_send_email.mock_host,
        port=setup_send_email.mock_port,
        user_name=setup_send_email.mock_username,
        password=setup_send_email.mock_password,
        from_email_address=setup_send_email.mock_from_address
    )

    with pytest.raises(ValueError) as ve:
        emailer.send_email(
            email_body=setup_send_email.mock_body,
            email_subject=setup_send_email.mock_subject
        )
        assert "destination_email_addresses must be provided to either the " \
            "constructor or to the send_email function" in str(ve)

    confirm_mocks_not_called(setup_send_email)


def test_send_email_no_from_email_address(setup_send_email):
    emailer = wmul_emailer.EmailSender(
        destination_email_addresses=\
            setup_send_email.mock_destination_email_addresses,
        server_host=setup_send_email.mock_host,
        port=setup_send_email.mock_port,
        user_name=setup_send_email.mock_username,
        password=setup_send_email.mock_password
    )

    with pytest.raises(ValueError) as ve:
        emailer.send_email(
            email_body=setup_send_email.mock_body,
            email_subject=setup_send_email.mock_subject
        )
        assert "from_email_address must be provided to either the constructor "\
            "or to the send_email function." in str(ve)

    confirm_mocks_not_called(setup_send_email)


def test_send_email_no_from_and_no_destination_email_address(setup_send_email):
    emailer = wmul_emailer.EmailSender(
        server_host=setup_send_email.mock_host,
        port=setup_send_email.mock_port,
        user_name=setup_send_email.mock_username,
        password=setup_send_email.mock_password
    )

    with pytest.raises(ValueError) as ve:
        emailer.send_email(
            email_body=setup_send_email.mock_body,
            email_subject=setup_send_email.mock_subject
        )
        assert "must be provided to either the constructor or to the "\
            "send_email function." in str(ve)

    confirm_mocks_not_called(setup_send_email)
