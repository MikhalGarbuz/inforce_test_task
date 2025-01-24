from src.generate_data import is_valid_email, _format_date, get_email_domain


def test_format_date():
    assert _format_date("2021-10-01 12:00:00") == "2021-10-01"
    
    
def test_is_valid_email():
    assert is_valid_email("test@gmail.com") is True
    assert is_valid_email("t@yahoo.com") is True
    assert is_valid_email("user.name+tag+sorting@gmail.com") is True
    assert is_valid_email("user.name@example.co.uk") is True
    assert is_valid_email("plainaddress") is False
    assert is_valid_email("@missingusername.com") is False
    assert is_valid_email("username@.com") is False
    assert is_valid_email("username@com") is False
    assert is_valid_email("username@.com.") is False
    assert is_valid_email("username@gmail..com") is False


def test_get_email_domain():
    assert get_email_domain("test@gmail.com") == "gmail.com"
    assert get_email_domain("user@yahoo.com") == "yahoo.com"
    assert get_email_domain("user.name+tag+sorting@gmail.com") == "gmail.com"
    assert get_email_domain("user@subdomain.example.com") == "subdomain.example.com"