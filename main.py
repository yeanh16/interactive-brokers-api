from pprint import pprint
from configparser import ConfigParser
from ibc.client import InteractiveBrokersClient

# Initialize the Parser.
config = ConfigParser()


# Initialize the client.
ibc_client = InteractiveBrokersClient(
    account_number="hi",
    password="gy"
)

# Grab the Auth Service.
auth_service = ibc_client.authentication

# Login
# auth_service.login()

# check if we are authenticated.
pprint(
    auth_service.is_authenticated()
)
