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
dynabyte.core

- Classes providing the core functionality of Dynabyte
"""
import hashlib
import os
import base64
from dynabyte import utils
from dynabyte import operations as ops


__all__ = ["Array", "File"]


class DynabyteBase:
    """Base class for dynabyte objects
    
    Provides operation methods for dynabyte.core.Array and dynabyte.core.File
    """        
    def run(self, callback, *, cb_type="full", output=None, count=1):
        """Execute operations defined in a callback function upon data. Gives access to offset.
        
        Must be overriden by subclass
        
        :param callback: Callback function: func(byte, offset) -> byte
        :param cb_type: 'full' (recieves all data) or 'offset' (recieves byte and its offset)
        :type cb_type: str
        :param output: Output file path (optional)
        :type output: str
        :param count: Number of times to run array though callback function
        :type count: int
        """
        raise NotImplementedError
    
    def XOR(self, value=0, *, count=1):
        """XOR each byte of the current instance against 'value', 'count' times
        
        If value is anything other than int, data will be XOR'd against
        the value sequentially (like a key).
        
        :param value: Value to XOR array against (int, str, list, bytes, or bytearray)
        :param count: Number of times to XOR array against value
        :type count: int
        """
        return self.run(callback=lambda data: ops.XOR(data, value), count=count)
        
    def __xor__(self, value):
        return self.XOR(value)
        
    def SUB(self, value=0, *, count=1):
        """Subtract 'value' from each byte of the current instance, 'count' times
         
        :param value: Value to subtract from each byte of array
        :type value: int
        :param count: Number of times to subtract value from array
        :type count: int
        """
        return self.run(callback=lambda data: ops.SUB(data, value), count=count)
        
    def __sub__(self, value):
        return self.SUB(value)
        
    def ADD(self, value=0, *, count=1):
        """"Add 'value' to each byte of the current instance, 'count' times
        
        :param value: Value to add to each byte of array
        :type value: int
        :param count: Number of times to add value to array
        :type count: int
        """
        return self.run(callback=lambda data: ops.ADD(data, value), count=count)
        
    def __add__(self, value):
        return self.ADD(value)
        
    def ROL(self, value=0, *, count=1):
        """Circular rotate shift left each byte of the current instance by 'value' bits, 'count' times
        
        :param value: Number of places to shift array
        :type value: int
        :param count: Number of times to run ROL
        :type count: int
        """
        return self.run(callback=lambda data: ops.ROL(data, value), count=count)
        
    def __lshift__(self, value):
        return self.ROL(value)
        
    def ROR(self, value=0, *, count=1):
        """Circular rotate shift right each byte of the current instance by 'value' bits, 'count' times
        
        :param value: Number of places to shift array
        :type value: int
        :param count: Number of times to run ROR
        :type count: int
        """
        return self.run(callback=lambda data: ops.ROR(data, value), count=count)
        
    def __rshift__(self, value):
        return self.ROR(value)
        
    def RC4(self, key, *, count=1):
        """Encrypt/decrypt data with key using RC4

        :param key: Key to encrypt data with (str, list, bytes, bytearray, int)
        :param count: Number of times to run RC4
        :type count: int
        """
        return self.run(callback=lambda data: ops.RC4(data, key), count=count)
        
    def AESEncrypt(self, key):
        """Encrypt/decrypt data using AES
        
        :param key: Key to encrypt data with (str, list, bytes, bytearray, int) ! Must be 16 bytes !
        """
        return self.run(callback=lambda data: ops.AESEncrypt(data, key))
        
    def AESDecrypt(self, key, *, nonce=None, tag=None):
        """Encrypt/decrypt data using AES
        
        :param key: Key to encrypt data with (str, list, bytes, bytearray, int) ! Must be 16 bytes !
        """
        return self.run(callback=lambda data: ops.AESDecrypt(data, key, nonce=nonce, tag=tag))
        
    def b64encode(self):
        """Encode data using base64
        """
        return self.run(callback=lambda data: base64.b64encode(data))
        
    def b64decode(self):
        """Decode data using base64
        """
        return self.run(callback=lambda data: base64.b64decode(data))
        
    def reverse(self):
        """Reverse the order of data
        
        If using on a file or particularly large string, be aware of the buffersize
        """
        return self.run(callback=lambda data: ops.reverse(data))


class Array(DynabyteBase):
    """Dynabyte class for interacting with arrays
    
    For use with string/list/byte/bytearray objects
    """
    delim = ", " # Default delimiter when printing instance data
    hex = True # Print bytes in hex form, or int
    
    def __init__(self, data, *, encoding="utf-8"):
        self.encoding = encoding # Default encoding when encoding/decoding data
        if type(data) is type(self): # For accepting data from dynabyte.core.Array objects
            self.data = data.data
            self.encoding = data.encoding # Transfer encoding between instances
        else:
            self.data = utils.getbytearray(data, encoding=self.encoding)
    
    def __str__(self):
        """Returns string representation of data when object pass to str()
        """
        return format(self, "str")
        
    def __iter__(self):
        """Makes object iterable
        
        Also allows object to be converted with bytes(), list(), etc.
        """
        for byte in self.data:
            yield byte
            
    def __getitem__(self, pos):
        """Allows items to be retreived from data array
        """
        return self.data[pos]
        
    def __setitem__(self, pos, value):
        """Allows values in data array to be changed
        
        Accepts int and str only
        """
        if type(value) is int:
            self.data[pos] = value
        elif type(value) is str:
            self.data[pos] = ord(value) # Error pops if its more than one letter
        else:
            raise ValueError(str(value))
        
    def __format__(self, style=None):
        """Returns various representations of instance data when used with format() built-in
        
        C-style array, Python list, string, or delimited hex values (default)
        
        :param spec: C, list, str, or None (hex bytes) format styles
        :type style: str      
        """       
        try:
            style = style.lower()
        except AttributeError:
            pass
        
        if self.hex:
            array = self.delim.join(hex(byte) for byte in self.data)
        else:
            array = self.delim.join(str(byte) for byte in self.data)
        
        if style == "c":
            array = f"unsigned char byte_array[] = {{ {array} }};"
        elif style == "list":
            array = f"byte_array = [{array}]"
        elif style == "str":
            array = self.data.decode(self.encoding, errors='ignore')
        return array
        
    def gethash(self, hash="sha256"):
        """Return hash of current instance data
        
        :param hash: Hash type (Default: sha256)
        :type hash: str
        :rtype: str
        """
        hash_obj = hashlib.new(hash)
        hash_obj.update(self.data)
        return hash_obj.hexdigest()
                
    def run(self, callback, *, cb_type="full", output=None, count=1):
        """Execute operations defined in a callback function upon data. 
        
        Callback type 'full' gives the callback function full control over
        the data. Callback type 'offset' passes the data 1 byte at time to
        the callback function, along with the global offset.
        
        :param callback: Callback function: offset_func(byte, offset) -> byte OR full_func(data) -> bytes
        :param cb_type: 'full' (recieves all data) or 'offset' (recieves byte and its offset)
        :type cb_type: str
        :param output: Output file path (optional)
        :type output: str
        :param count: Number of times to run array though callback function
        :type count: int
        """
        callback_function = callback if cb_type.lower() == "full" else OffsetCallback(callback)
        for _ in range(count):
            self.data = callback_function(self.data)
        if output:
            with open(output, 'wb') as file:
                file.write(self.data)
        self.data = bytearray(self.data)
        return self
        

class File(DynabyteBase):
    """Dynabyte class for interacting with files"""
    def __init__(self, path, *, buffersize=8192):
        self.path = path
        self.buffersize = buffersize
        
    def __str__(self):
        return self.path
        
    def getsize(self):
        """Return size of current instance file in bytes
        
        :rtype: int
        """
        return os.stat(self.path).st_size

    def gethash(self, hash="sha256"):
        """Return hash of current instance file
        
        :param hash: Hash type (Default: sha256)
        :type hash: str
        :rtype: str
        """
        hash_obj = hashlib.new(hash)
        with open(self.path, "rb") as reader:
            chunk = reader.read(self.buffersize)
            while chunk:
                hash_obj.update(chunk)
                chunk = reader.read(self.buffersize)
        return hash_obj.hexdigest()
        
    def delete(self):
        """Delete input file"""
        if os.path.exists(self.path):
            os.remove(self.path)
        
    def getbytes(self, buffer=-1, encoding="utf-8"):
        """Retrieve all bytes from file, return in a dynabyte Array
        
        Beware hella large files
        
        :param buffer: Number of bytes to read from file (Default: all)
        :type buffer: int
        :returns Array: Array object initialized with file bytes
        :rtype: dynabyte.core.Array
        """
        data = None
        try:
            with open(self.path, "rb") as fileobj:
                data = Array(file.read(buffer), encoding=encoding)
        except FileNotFoundError:
            pass
        return data 
        
    def run(self, callback, *, cb_type="full", output=None, count=1):
        """Execute operations defined in a callback function upon data within given file. 
        
        Callback type 'full' gives the callback function full control over
        the data. Callback type 'offset' passes the data 1 byte at time to
        the callback function, along with the global offset. 
        Returns self, or instance created from output file.
        
        :param callback: Callback function: func(byte, offset) -> byte
        :param output: Output file path (optional)
        :type output: str
        :param count: Number of times to run file though callback function
        :type count: int
        """
        input_path = self.path # Running count > 1 and outputting a file at the same time breaks if I don't do this
        for _ in range(count):
            callback_function = callback if cb_type.lower() == "full" else OffsetCallback(callback)
            with DynabyteFileManager(input_path, output, self.buffersize) as file_manager:
                for chunk in file_manager: 
                    file_manager.write(callback_function(chunk))
            if output:
                input_path = output # On the 2nd cycle it'll continue reading from the original (not up to date) file
                output = None
        return self
    

class DynabyteFileManager:
    """Context manager for file objects, can be iterated over to retrieve buffer of file bytes.
    
    Handles the input/output of one or two files.
    If no output path is given, the input will be overwritten
    """
    start_position = 0    
    def __init__(self, input: str, output: str, buffersize: int): 
        self.input_file = input
        self.output_file = output
        self.buffersize = buffersize
        self.last_position = self.start_position      

    def write(self, chunk: bytes) -> None:
        """Write bytes to file"""
        self.writer.seek(self.last_position)
        self.writer.write(chunk)

    def __enter__(self):
        if self.output_file is None:
            self.reader = self.writer = open(self.input_file, "rb+")  # reader/writer will use the same file handle if no output given
        else:
            self.reader = open(self.input_file, "rb")
            self.writer = open(self.output_file, "wb")
        return self

    def __exit__(self, type, val, traceback):
        self.reader.close()
        self.writer.close()
           
    def __iter__(self):
        return self

    def __next__(self) -> bytes:
        self.last_position = self.reader.tell() 
        chunk = self.reader.read(self.buffersize)
        if self.reader is None or chunk == b"":
            raise StopIteration
        else:
            return chunk


class OffsetCallback:
    """Offset Callback function handler, runs bytes through given function.
    
    When called, passes 1 byte of data at a time to callback function, along
        with global offset
    """
    def __init__(self, function):
        self.callback = function
        self.global_offset = 0
        
    def __call__(self, chunk: bytes) -> bytes:
        """Returns bytes after being processed through callback function
        
        :param chunk: Data/chunk to be processed
        :type chunk: bytes
        :rtype: bytes
        """
        buffer = bytearray(len(chunk))
        for chunk_offset, byte in enumerate(chunk):
            buffer[chunk_offset] = (self.callback(byte, self.global_offset) & 0xff)
            self.global_offset += 1
        return bytes(buffer)


if __name__ == "__main__":
    pass
