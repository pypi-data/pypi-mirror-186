"""mse_lib_crypto.x25519 module."""

from typing import Tuple

from nacl.bindings.crypto_scalarmult import crypto_scalarmult
from nacl.public import PrivateKey, PublicKey


def x25519_keygen() -> Tuple[bytes, bytes]:
    """Keygen for X25519 (DH using Curve25519 in Montgomery form).

    Returns
    -------
    Tuple[bytes, bytes]
        Keypair (public_key, private_key).

    """
    private_key: PrivateKey = PrivateKey.generate()
    public_key: PublicKey = private_key.public_key

    return bytes(public_key), bytes(private_key)


def x25519(private_key: bytes, public_key: bytes) -> bytes:
    """Scalar multiplication over Curve25519.

    Parameters
    ----------
    private_key: bytes
        Scalar to be used as private key.
    public_key: bytes
        Bytes of the point on the Curve25519.

    Returns
    -------
    bytes
        Point on the Curve25519 to be used as shared secret.

    """
    return crypto_scalarmult(private_key, public_key)
