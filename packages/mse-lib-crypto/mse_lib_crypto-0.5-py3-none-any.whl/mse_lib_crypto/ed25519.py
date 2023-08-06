"""mse_lib_crypto.ed25519 module."""

import hashlib
from typing import Tuple

from nacl.bindings import (crypto_sign_keypair, crypto_sign_seed_keypair,
                           crypto_sign_SEEDBYTES)
from nacl.bindings.crypto_scalarmult import (
    crypto_scalarmult_ed25519_SCALARBYTES)
from nacl.signing import SigningKey, VerifyKey


def ed25519_keygen() -> Tuple[bytes, bytes, bytes]:
    """Keygen for Ed25519 (EdDSA using edwards25519).

    Returns
    -------
    Tuple[bytes, bytes, bytes]
        Triple (public_key, seed, private_key).

    """
    public_key, sk = crypto_sign_keypair()  # type: bytes, bytes
    seed: bytes = sk[:crypto_sign_SEEDBYTES]
    private_key: bytes = hashlib.sha512(
        seed).digest()[:crypto_scalarmult_ed25519_SCALARBYTES]

    return public_key, seed, private_key


def ed25519_seed_keygen(seed: bytes) -> Tuple[bytes, bytes, bytes]:
    """Seeded keygen for Ed25519 (EdDSA using edwards25519).

    Returns
    -------
    Tuple[bytes, bytes, bytes]
        Triple (public_key, seed, private_key).

    """
    public_key, sk = crypto_sign_seed_keypair(seed)

    assert seed == sk[:crypto_sign_SEEDBYTES]

    private_key: bytearray = bytearray(
        hashlib.sha512(seed).digest()[:crypto_scalarmult_ed25519_SCALARBYTES])

    # see: src/libsodium/crypto_sign/ed25519/ref10/keypair.c#L19
    private_key[0] &= 248
    private_key[31] &= 127
    private_key[31] |= 64

    return public_key, seed, bytes(private_key)


def sign(data: bytes, private_key: bytes) -> bytes:
    """Sign `data` with `private_key` using Ed25519.

    Parameters
    ----------
    data : bytes
        Data to be signed.
    private_key : bytes
        Private key used to sign data.

    Returns
    -------
    bytes
        64 bytes Ed25519 signature.

    """
    signing_key: SigningKey = SigningKey(private_key)

    return signing_key.sign(data).signature


def verify(data: bytes, sig: bytes, public_key: bytes) -> bytes:
    """Verify `sig` with `data` and `public_key` using Ed25519.

    Parameters
    ----------
    data : bytes
        Data which has been signed.
    sig : bytes
        64 bytes signature.
    public_key : bytes
        Public key used to verify the signature.

    Returns
    -------
    bytes
        Original bytes of the message if the verification succeeded.

    """
    verify_key: VerifyKey = VerifyKey(public_key)

    return verify_key.verify(data,
                             sig)  # raise nacl.exceptions.BadSignatureError
