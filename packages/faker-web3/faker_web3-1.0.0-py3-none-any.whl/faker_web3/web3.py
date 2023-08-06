import secrets

from faker.providers import BaseProvider


class Web3Provider(BaseProvider):
    def web3_private_key(self) -> str:
        """Returns a random private key.

        Returns:
            str: Private key
        """
        private_key = secrets.token_hex(32)
        return "0x" + private_key
