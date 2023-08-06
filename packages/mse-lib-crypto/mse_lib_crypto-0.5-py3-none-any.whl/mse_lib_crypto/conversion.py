"""mse_lib_crypto.conversion module."""

from typing import Tuple

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey, Ed25519PublicKey)
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.serialization import (Encoding,
                                                          NoEncryption,
                                                          PrivateFormat,
                                                          PublicFormat)
from nacl.bindings import (crypto_sign_ed25519_pk_to_curve25519,
                           crypto_sign_ed25519_sk_to_curve25519,
                           crypto_scalarmult_ed25519_base)


def ed25519_pk_from_sk_(private_key: bytes) -> bytes:
    """Recover public key from private key created for Ed25519.

    Parameters
    ----------
    private_key: bytes
        Bytes of the Ed25519 private key.

    Returns
    -------
    bytes
        Bytes of the Ed25519 public key corresponding to `private_key`.

    """
    return crypto_scalarmult_ed25519_base(private_key)


def ed25519_to_x25519_keypair_(public_key: bytes,
                               seed: bytes) -> Tuple[bytes, bytes]:
    """Map edwards25519 keypair to curve25519 keypair.

    Parameters
    ----------
    public_key: bytes
        Bytes of the Ed25519 public key.
    seed : bytes
        Bytes of the Ed25519 seed.

    Returns
    -------
    Tuple[bytes, bytes]
        Keypair (pk, sk) for X25519

    """
    x25519_privkey: bytes = crypto_sign_ed25519_sk_to_curve25519(seed +
                                                                 public_key)
    x25519_pubkey: bytes = crypto_sign_ed25519_pk_to_curve25519(public_key)

    return x25519_pubkey, x25519_privkey


def ed25519_to_x25519_pk_(public_key: bytes) -> bytes:
    """Map edwards25519 point to curve25519 point.

    Parameters
    ----------
    public_key: bytes
        Bytes of the Ed25519 public key.

    Returns
    -------
    bytes
        Public key for X25519.

    """
    return crypto_sign_ed25519_pk_to_curve25519(public_key)


def ed25519_to_x25519_sk(private_key: Ed25519PrivateKey) -> X25519PrivateKey:
    """Map Ed25519 private key to X25519 private key.

    Parameters
    ----------
    private_key : Ed25519PrivateKey
        Ed25519 private key.

    Returns
    -------
    X25519PrivateKey
        X25519 private key corresponding to `private_key`.

    """
    pk = private_key.public_key().public_bytes(encoding=Encoding.Raw,
                                               format=PublicFormat.Raw)
    seed = private_key.private_bytes(encoding=Encoding.Raw,
                                     format=PrivateFormat.Raw,
                                     encryption_algorithm=NoEncryption())
    x25519_sk: bytes = crypto_sign_ed25519_sk_to_curve25519(seed + pk)

    return X25519PrivateKey.from_private_bytes(x25519_sk)


def ed25519_to_x25519_pk(public_key: Ed25519PublicKey) -> bytes:
    """Map Ed25519 public key to X25519 public key.

    Parameters
    ----------
    public_key: Ed25519PublicKey
        Ed25519 public key.

    Returns
    -------
    bytes
        Bytes of the X25519 public key corresponding to `public_key`.

    """
    return ed25519_to_x25519_pk_(
        public_key.public_bytes(encoding=Encoding.Raw, format=PublicFormat.Raw))
