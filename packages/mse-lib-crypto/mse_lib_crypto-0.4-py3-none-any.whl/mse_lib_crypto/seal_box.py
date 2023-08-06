"""mse_lib_crypto.seal_box module."""

from nacl.public import PrivateKey, PublicKey, SealedBox


def seal(data: bytes, recipient_public_key: bytes) -> bytes:
    """Seal with seal box of libsodium (X25519 and XSalsa20-Poly1305).

    Parameters
    ----------
    data : bytes
        The data to be sealed.
    recipient_public_key : bytes
        Recipent X25519 public key (32 bytes).

    Returns
    -------
    bytes
        `data` sealed for `recipient_public_key`.


    Notes
    -----
    ephemeral_pk ‖ box(m,
                       recipient_pk,
                       ephemeral_sk,
                       nonce=blake2b(ephemeral_pk ‖ recipient_pk))

    """
    box = SealedBox(PublicKey(recipient_public_key))

    return box.encrypt(data)


def unseal(encrypted_data: bytes, private_key: bytes) -> bytes:
    """Unseal with seal box of libsodium (X25519 and XSalsa20-Poly1305).

    Parameters
    ----------
    encrypted_data : bytes
        The encrypted data to be unsealed:
        ephemeral_pk (32 bytes) || MAC (16 bytes) || box(data) (var).
    private_key : bytes
        X25519 private key (32 bytes).

    Returns
    -------
    bytes
        cleartext data if success.

    """
    box = SealedBox(PrivateKey(private_key))

    return box.decrypt(encrypted_data)
