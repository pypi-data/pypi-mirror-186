"""mse_lib_crypto.aead module."""

import shutil
from pathlib import Path
from typing import List, Optional, Dict

import nacl.utils
from nacl.secret import SecretBox

KEY_LENGTH: int = nacl.secret.SecretBox.KEY_SIZE
NONCE_LENGTH: int = nacl.secret.SecretBox.NONCE_SIZE


def random_key() -> bytes:
    """Generate a random symmetric key for XSalsa20-Poly1305.

    Returns
    -------
    bytes
        Random symmetric key of length AEAD_KEY_LENGHT.

    """
    return nacl.utils.random(KEY_LENGTH)


def encrypt(data: bytes, key: bytes, nonce: Optional[bytes] = None) -> bytes:
    """Encrypt bytes `data` using XSalsa20-Poly1305.

    Parameters
    ----------
    data : bytes
        Data to be encrypted.
    key : bytes
        Symmetric key used for encryption.
    nonce : Optional[bytes]
        Arbitrary number that can be used just once. Randomly
        generated if not provided.

    Returns
    -------
    bytes
        Ciphertext of `data` using `key`.

    """
    box: SecretBox = SecretBox(key)

    return box.encrypt(data, nonce)


def encrypt_file(path: Path,
                 key: bytes,
                 nonce: Optional[bytes] = None,
                 ext: str = ".enc") -> Path:
    """Encrypt file `path` using XSalsa20-Poly1305.

    Parameters
    ----------
    path : Path
        Path to the data to be encrypted.
    key : bytes
        Symmetric key used for encryption.
    nonce : Optional[bytes]
        Arbitrary number that can be used just once. Randomly
        generated if not provided.
    ext : str
        Extension for the encrypted file.

    Returns
    -------
    Path
        Path to the encrypted file `path`.

    """
    if not path.is_file():
        raise FileNotFoundError

    out_path: Path = path.with_suffix(f"{path.suffix}{ext}")
    out_path.write_bytes(encrypt(path.read_bytes(), key, nonce))

    return out_path


def encrypt_directory(dir_path: Path, patterns: List[str], key: bytes,
                      nonces: Optional[Dict[str, bytes]], exceptions: List[str],
                      dir_exceptions: List[str],
                      out_dir_path: Path) -> Dict[str, bytes]:
    """Encrypt the content of directory `dir_path` using XSalsa20-Poly1305.

    Parameters
    ----------
    dir_path : Path
        Path to the directory to be encrypted.
    patterns: List[str]
        List of patterns to be matched in the directory.
    key : bytes
        Symmetric key used for encryption.
    nonces : Optional[Dict[str, bytes]]
        Map of string path to nonce. Randomly generated if None.
    exceptions: List[str]
        List of files which won't be encrypted.
    dir_exceptions: List[str]
        List of directories which won't be encrypted recursively.
    out_dir_path: Path
        Output directory path. Will be removed if already exists.

    Returns
    -------
    Dict[str, bytes]
        Map of path string to nonce used to encrypt.

    """
    if not dir_path.is_dir():
        raise NotADirectoryError

    if out_dir_path.exists():
        shutil.rmtree(out_dir_path)

    shutil.copytree(dir_path, out_dir_path)

    nonce_map: Dict[str, bytes] = {}

    for pattern in patterns:  # type: str
        for path in out_dir_path.rglob(pattern):  # type: Path
            if path.is_file() and path.name not in exceptions and all(
                    directory not in path.parts
                    for directory in dir_exceptions):
                relpath: Path = path.relative_to(out_dir_path)
                if nonces is not None and f"{relpath}" not in nonces:
                    raise Exception(
                        f"Path '{relpath}' not found in nonces: {nonces}")
                nonce: bytes = (nonces[f"{relpath}"] if nonces is not None else
                                nacl.utils.random(NONCE_LENGTH))
                nonce_map[f"{relpath}"] = nonce
                encrypt_file(path, key, nonce)
                path.unlink()

    return nonce_map


def decrypt(encrypted_data: bytes,
            key: bytes,
            nonce: Optional[bytes] = None) -> bytes:
    """Decrypt bytes `encrypted_data` using XSalsa20-Poly1305.

    Parameters
    ----------
    encrypted_data : bytes
        Encrypted data to be decrypted.
    key : bytes
        Symmetric key used for encryption.
    nonce : Optional[bytes]
        Arbitrary number that can be used just once. Part of the
        ciphertext when omitted.

    Returns
    -------
    bytes
        Cleartext of `encrypted_data`.

    """
    box: SecretBox = SecretBox(key)

    return box.decrypt(encrypted_data, nonce)


def decrypt_file(path: Path,
                 key: bytes,
                 nonce: Optional[bytes] = None,
                 ext: str = ".enc",
                 out_dir_path: Optional[Path] = None) -> Path:
    """Decrypt file `path` using XSalsa20-Poly1305.

    Parameters
    ----------
    path : Path
        Path to the data to be decrypted.
    key : bytes
        Symmetric key used for decryption.
    nonce : Optional[bytes]
        Arbitrary number that can be used just once. Part of the
        ciphertext when omitted.
    ext : str
        Extension of encrypted file.
    out_dir_path : Optional[Path]
        Output directory path if different from `path` parent directory.

    Returns
    -------
    Path
        Path to the decrypted file `path`.

    """
    if not path.is_file():
        raise FileNotFoundError

    if ext != path.suffix:
        raise Exception(f"Extension {ext} not found in {path}")

    filename: str = path.with_suffix("").name
    out_path: Path = (path.parent /
                      filename if out_dir_path is None else out_dir_path /
                      filename)
    out_path.write_bytes(decrypt(path.read_bytes(), key, nonce))

    return out_path


def decrypt_directory(dir_path: Path,
                      key: bytes,
                      ext: str = ".enc",
                      out_dir_path: Optional[Path] = None) -> bool:
    """Decrypt the content of directory `dir_path` using XSalsa20-Poly1305.

    Parameters
    ----------
    dir_path : Path
        Path to the directory to be decrypted.
    key : bytes
        Symmetric key used for decryption.
    ext : str
        File extension of encrypted files.
    out_dir_path : Optional[Path]
        Output directory path if different from `dir_path`.

    Returns
    -------
    bool
        True if success, raise an exception otherwise.

    """
    if not dir_path.is_dir():
        raise NotADirectoryError

    for path in dir_path.rglob(f"*{ext}"):  # type: Path
        if path.is_file():
            decrypt_file(path, key, None, ext, out_dir_path)
            path.unlink()

    return True
