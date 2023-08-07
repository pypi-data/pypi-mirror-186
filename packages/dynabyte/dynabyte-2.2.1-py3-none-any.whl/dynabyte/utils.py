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
dynabyte.utils

- Dynabytes utility/helper functions. 
"""

import os
from random import randint


def getbytearray(data, *, encoding="utf-8"):
    """Convert string, list, bytes, or int objects to bytearray
    
    List-type input data can be a combination of any
    valid input type (int, str, list, byte, bytearray).
    Strings will be encoded using the given codec.
    
    :param data: string, list, bytes, or int objects
    :param encoding: Codec to use for encoding if string given
    :type encoding: str
    :rtype: bytearray
    """
    if type(data) is bytearray:
        return data    
    elif type(data) is str:
        return bytearray(data.encode(encoding))    
    elif type(data) is bytes:
        return bytearray(data)
    elif type(data) is int:
        return bytearray([data])
    elif type(data) is type(None):
        return bytearray([])
    elif type(data) is list:
        array = bytearray([])
        for item in data:
            if type(item) is int:
                array.append(item)                
            else:
                array.extend(getbytearray(item))
        return array
    
    else:
        raise TypeError(data)
        

def bprint(data, style=None, *, encoding="utf-8", delim=", "):
    """Print data as Python list, C-style array, string, or delimited hex
    
    Default: Comma-deliminated hex representation
    
    :param data: string, list, bytes, bytearray, or int objects
    :param style: C, list, str, or None (hex bytes) array format
    :type style: str
    :param encoding: Codec to decode string with
    :type encoding: str
    :param delim: Delimiter between hex values
    :type delim: str
    :rtype: None 
    """
    try:
        style = style.lower()
    except AttributeError:
        pass
    data = getbytearray(data)
    array = delim.join(hex(byte) for byte in data)    
    if style == "c":
        array = f"unsigned char byte_array[] = {{ {array} }};"
    elif style == "list":
        array = f"byte_array = [{array}]"
    elif style == "str":
        array = data.decode(encoding, errors='ignore')      
    print(array)


def random_key(length=10, lower=33, upper=126, string=True, encoding="utf-8"):
    """Return random assortment of characters in given length.
    
    By default, the key will be generated from readable ascii characters.
    
    :param length: Length, in characters, of key to return
    :type length: int
    :param lower: Lower limit of values to generate (Default: 33/'!')
    :type lower: int
    :param lower: Upper limit of values to generate (Default: 126/'~')
    :type lower: int
    :param string: Return string representation if True, otherwise return bytes object
    :type string: bool
    :param encoding: Encoding scheme for returned string
    :type encoding: str
    :rtype: str
    """
    key = getbytearray([randint(lower, upper-1) for _ in range(length)])
    if string:
        return key.decode(encoding, errors='ignore')
    return bytes(key)
    

def comparefilebytes(path1, path2, verbose=True):
    """Compare the bytes of the two given files.
    
    :param path1: Path to file
    :type path1: str
    :param path2: Path to second file
    :type path2: str
    :param verbose: Print filesize message
    :type verbose: bool
    :rtype: bool
    """
    name1 = os.path.basename(path1)
    name2 = os.path.basename(path2)
    deviants = []
    offset = 0
    with open(path1, "rb") as file1, open(path2, "rb") as file2:
        chunk1 = file1.read(8192)
        chunk2 = file2.read(8192)
        while chunk1 and chunk2:
            for byte1, byte2 in zip(chunk1, chunk2):
                if byte1 != byte2:
                    deviants.append(f"Offset {hex(offset)}: {hex(byte1)} -> {hex(byte2)}")
                offset += 1
            chunk1 = file1.read(8192)
            chunk2 = file2.read(8192)
    if deviants:
        if verbose:
            print(f"{len(deviants)} errors found.")
        return deviants
    if verbose:
        print(f"No discrepancies found between {name1} and {name2}")
    return None



if __name__ == "__main__":
    pass
