#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0111,C0103

import os
from Crypto.Cipher import AES

AES_KEY_SIZE = 128 # bit

def pad(bytestring, k=AES.block_size):
    l = len(bytestring)
    val = k - (l % k)
    return bytestring + bytearray([val] * val)

def unpad(bytestring, k=AES.block_size):
    val = bytestring[-1]
    if val > k:
        raise ValueError('Input is not padded or padding is corrupt')
    l = len(bytestring) - val
    return bytestring[:l]

def Encrypt(Source):
    """ AES ECB encrypt.

    Args:
        Source (bytes): The data to encrypt.

    Returns:
        Key (128 bit) + Encrypted data.

    """
    key = os.urandom(AES_KEY_SIZE // 8)
    cipher = AES.new(key, AES.MODE_ECB)
    output = cipher.encrypt(pad(Source))
    return key + output

def Decrypt(Code):
    """ AES ECB decrypt.

    Args:
        Code (bytes): Key (128 bit) + Encrypted data.

    Returns:
        Decrypted data.

    Raises:
        ValueError: If `code` is too short.
    """
    key_length = AES_KEY_SIZE // 8
    if len(Code) <= key_length:
        raise ValueError('Code too short')
    key = Code[:key_length]
    cipher = AES.new(key, AES.MODE_ECB)
    realCode = Code[key_length:]
    output = cipher.decrypt(realCode)
    return unpad(output)
