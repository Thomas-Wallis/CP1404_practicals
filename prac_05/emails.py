def main():
    """Dictionary of emails to names"""
    email_names = {}
    email = input("Email: ")
    while email != "":
        name = get_email_name(email)
        verify_name = input("Is your name {}? (Y/n)".format(name))
        if verify_name.upper() != "Y" and verify_name != "":
            name = input("Name: ")
        email_names[email] = name
        email = input("Email: ")
    for email, name in email_names.items():
        print("{} ({})".format(name, email))


def get_email_name(email):
    """Takes excepted name from email"""
    expected_name_half = email.split('@')[0]
    parts = expected_name_half.split('.')
    expected_name = " ".join(parts).title()
    return expected_name


main()