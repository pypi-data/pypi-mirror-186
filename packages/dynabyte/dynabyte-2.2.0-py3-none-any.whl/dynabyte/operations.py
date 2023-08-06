#
# Copyright (C) 2023 LLCZ00
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.  
#

""" 
dynabyte.operations

- Operation function used by dynabyte's Array and File class
    - Can also be used independently
"""
import os
import hashlib
from Crypto.Cipher import AES
from dynabyte import utils


__all__ = ["ROL", "ROR", "XOR",
           "ADD", "SUB", "RC4",
           "AESEncrypt", "AESDecrypt",
           "reverse"]


# Helper functions #

def RotateLeft(x, n):
    """Circular rotate shift byte 'x' left by 'n' bits
    
    Performs ROL on single byte.
    Included for convenience, not inherited by anything.
    
    :param x: Byte to rotate
    :type x: int
    :param n: Number of bits to shift by
    :type n: int
    :rtype: int
    """
    return ((x << n % 8) & 255) | ((x & 255) >> (8 - (n % 8)))


def RotateRight(x, n):
    """Circular rotate shift byte 'x' right by 'n' bits
    
    Performs ROR on single byte.
    Included for convenience, not inherited by anything.
    
    :param x: Byte to rotate
    :type x: int
    :param n: Number of bits to shift by
    :type n: int
    :rtype: int
    """
    return ((x & 255) >> (n % 8)) | (x << (8 - (n % 8)) & 255)


# Standalone operation functions #

def ROL(data, value=0, *, count=1):
    """Circular rotate shift 'data' left by 'value' bits
    
    :param data: Data to perform operation on (str, list, bytes, bytearray, int)
    :param value: Number of bits to rotate
    :type value: int
    :param count: Number of times to perform function
    :type count: int
    :rtype: bytes
    """
    data = utils.getbytearray(data)
    for _ in range(count):
        for offset, byte in enumerate(data):
            data[offset] = ((((byte << value % 8) & 255) | ((byte & 255) >> (8 - (value % 8)))) & 0xff)        
    return bytes(data)


def ROR(data, value=0, *, count=1):
    """Circular rotate shift 'data' right by 'value' bits
    
    :param data: Data to perform operation on (str, list, bytes, bytearray, int)
    :param value: Number of bits to rotate
    :type value: int
    :param count: Number of times to perform function
    :type count: int
    :rtype: bytes
    """
    data = utils.getbytearray(data)
    for _ in range(count):
        for offset, byte in enumerate(data):
            data[offset] = ((((byte & 255) >> (value % 8)) | (byte << (8 - (value % 8)) & 255)) & 0xff)        
    return bytes(data)
    

def XOR(data, value=0, *, count=1):
    """XOR 'data' against 'value', 'count' times
    
    If value is anything other than int, data will be XOR'd against
    the value sequentially (like a key).
     
    :param data: Data to perform operation on (str, list, bytes, bytearray, int)
    :param value: Value to XOR array against (str, list, bytes, bytearray, int)
    :param count: Number of times to perform function
    :type count: int
    :rtype: bytes
    """
    data = utils.getbytearray(data)
    value = utils.getbytearray(value)
    for _ in range(count):
        for offset, byte in enumerate(data):
            data[offset] = ((byte ^ value[offset % len(value)]) & 0xff)
    return bytes(data)


def SUB(data, value=0, *, count=1):
    """Subtract 'value' from each byte in 'data', 'count' times
     
    :param data: Data to perform operation on (str, list, bytes, bytearray, int)
    :param value: Value to subtract
    :type value: int
    :param count: Number of times to perform function
    :type count: int
    :rtype: bytes
    """
    data = utils.getbytearray(data)
    for _ in range(count):
        for offset, byte in enumerate(data):
            data[offset] = ((byte - value) & 0xff)
    return bytes(data)


def ADD(data, value=0, *, count=1):
    """Add 'value' to each byte in 'data', 'count' times
     
    :param data: Data to perform operation on (str, list, bytes, bytearray, int)
    :param value: Value to add
    :type value: int
    :param count: Number of times to perform function
    :type count: int
    :rtype: bytes
    """
    data = utils.getbytearray(data)
    for _ in range(count):
        for offset, byte in enumerate(data):
            data[offset] = ((byte + value) & 0xff)
    return bytes(data)
    
    
def RC4(data, key):
    """Encrypt/decrypt data with key using RC4

    :param data: Data to encrypt (str, list, bytes, bytearray, int)
    :param key: Key to encrypt data with (str, list, bytes, bytearray, int)
    :rtype: bytes
    """
    data = utils.getbytearray(data)
    key = utils.getbytearray(key)   
    # Key-scheduling algorithm
    key_schedule = bytearray([byte for byte in range(256)]) # Populate array with every possible byte (0-255)
    key_length = len(key)    
    i = 0
    j = 0
    tmp = 0    
    while i < 256:
        j = (j + key_schedule[i] + key[i % key_length]) % 256        
        tmp = key_schedule[j]
        key_schedule[j] = key_schedule[i] # Swap i and j
        key_schedule[i] = tmp
        i += 1
    # Pseudo-random generation algorithm (PRGA)   
    i = 0
    j = 0
    n = 0
    ciphertxt = bytearray()
    while n < len(data):
        i = (i + 1) % 256
        j = (j + key_schedule[i]) % 256
        
        tmp = key_schedule[j]
        key_schedule[j] = key_schedule[i] # Swap i and j
        key_schedule[i] = tmp
        
        key_stream = key_schedule[(key_schedule[i] + key_schedule[j]) % 256]
        ciphertxt.append(data[n] ^ key_stream)
        n += 1        
    return bytes(ciphertxt)
    

def AESEncrypt(data, key, mode=AES.MODE_EAX):
    """Encrypt data using AES
    
    :param data: Data to encrypt (str, list, bytes, bytearray, int)
    :param key: Key to encrypt data with (str, list, bytes, bytearray, int) ! Must be 16 bytes !
    :rtype: bytes
    """
    data = utils.getbytearray(data)
    key = utils.getbytearray(key) 
    
    cipher = AES.new(key, mode)
    return cipher.encrypt_and_digest(data)[0]
    
    
def AESDecrypt(data, key, *, nonce=None, tag=None, mode=AES.MODE_EAX):
    """Encrypt data using AES
    
    :param data: Data to encrypt (str, list, bytes, bytearray, int)
    :param key: Key to encrypt data with (str, list, bytes, bytearray, int) ! Must be 16 bytes !
    :rtype: bytes
    """
    data = utils.getbytearray(data)
    key = utils.getbytearray(key) 
    tag = utils.getbytearray(tag)
    nonce = utils.getbytearray(nonce)
    
    cipher = AES.new(key, mode, nonce)
    return cipher.decrypt_and_verify(data, tag)
    
    
def reverse(data):
    """Reverse the order of data
    
    :param data: Data to reverse (str, list, bytes, bytearray, int)
    :rtype: bytes
    """
    data = utils.getbytearray(data)
    r_data = list(reversed(list(data)))
    return bytes(r_data)
        