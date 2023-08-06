import ctypes as C
#import cached_table
from .aes import AESCipher

from typing import Union

class Ht_Item(C.Structure):
    _fields_ = [
                    ("key", C.c_char_p),
                    ("value", C.c_char_p)
                ]

class Linked_List(C.Structure):
    pass
    
class Linked_List(C.Structure):
    _fields_ = [
                    ("item", C.POINTER(Ht_Item)),
                    ("next", C.POINTER(Linked_List))
                ]
                
class Hash_Table(C.Structure):
    _fields_ = [
                    ("items", C.POINTER(C.POINTER(Ht_Item))),
                    ("overflow_buckets", C.POINTER(C.POINTER(Linked_List))),
                    ("size", C.c_int),
                    ("count", C.c_int)
                ]
                
class Cached_Table:    
    def __init__(self, table_size: int = 50000, table_name: str = "Cached Key-Value Storage Database"):            
        self.loaded_shared_library = C.CDLL("./cached_table.so")
        
        self.create_table = self.loaded_shared_library.create_table
        create_table_tok = {"argtypes": [C.c_int], "restype": C.POINTER(Hash_Table), "func": self.create_table}
        
        self.ht_insert = self.loaded_shared_library.ht_insert
        ht_insert_tok = {"argtypes": [C.POINTER(Hash_Table), C.c_char_p, C.c_char_p], "restype": C.c_void_p, "func": self.ht_insert}
        
        self.ht_delete = self.loaded_shared_library.ht_delete
        ht_delete_tok = {"argtypes": [C.POINTER(Hash_Table), C.c_char_p], "restype": C.c_void_p, "func": self.ht_delete}
        
        self.ht_search = self.loaded_shared_library.ht_search
        ht_search_tok = {"argtypes": [C.POINTER(Hash_Table), C.c_char_p], "restype": C.c_char_p, "func": self.ht_search}
        
        self.free_table = self.loaded_shared_library.free_table
        free_table_tok = {"argtypes": [C.POINTER(Hash_Table)], "restype": C.c_void_p, "func": self.free_table}
        
        self.setup_c_types(**create_table_tok)
        self.setup_c_types(**ht_insert_tok)
        self.setup_c_types(**ht_delete_tok)
        self.setup_c_types(**ht_search_tok)
        self.setup_c_types(**free_table_tok)
        
        # Extensions later on
        ## Ex. fast start, secure boot, sharding
        self.table_size = table_size
        self.table_name = table_name
        
        self.table = self.create_table(self.table_size)
        
    def setup_c_types(self, **kwargs):
        kwargs["func"].argtypes = kwargs["argtypes"]
        kwargs["func"].restype = kwargs["restype"]
        
    def convert_to_bytes(self, item: Union[str, int, float, bytes]):
        if isinstance(item, bytes):
            return item
        elif isinstance(item, int) or isinstance(item, float):
            item = str(item)
        elif isinstance(item, str) != True:
            raise Exception(f"Can't deal with that type for now: {item}!")
            
        return bytes(item, "utf-8")
        
    def insert_item(self, key: Union[str, int, float, bytes], val: Union[str, int, float, bytes]) -> bool:
        try:
            key = self.convert_to_bytes(key)
            val = self.convert_to_bytes(val)
            
            self.ht_insert(self.table, key, val)
        except Exception as e:
            print(e)
            return False
        
        return True
        
    def delete_item(self, key: Union[str, int, float, bytes]) -> bool:
        try:
            key = self.convert_to_bytes(key)
            
            self.ht_delete(self.table, key)
        except Exception as e:
            print(e)
            return False
            
        return True
        
    def get_item(self, key: Union[str, int, float, bytes]) -> Union[str, bool]:
        try:
            key = self.convert_to_bytes(key)
            
            result = self.ht_search(self.table, key)
            
            if result:
                return result.decode("utf-8")
            else:
                return False
                
        except Exception as e:
            print(e)
            return False
            
    def __str__(self) -> str:
        return self.table_name
    
    def __del__(self):
        try:
            self.free_table(self.table)
        except Exception as e:
            print(e)
            
class Cache:
    def __init__(self, table_size: int = 50000, table_name: str = "Cached Key-Value Storage Database", encryption_key: str = "Marlins#1234567890"):
        self.table = Cached_Table(table_size=table_size, table_name=table_name)
        self.crypto = AESCipher(encryption_key)
        
    def convert_to_bytes(self, item: Union[str, int, float, bytes]):
        if isinstance(item, bytes):
            return item
        elif isinstance(item, int) or isinstance(item, float):
            item = str(item)
        elif isinstance(item, str) != True:
            raise Exception(f"Can't deal with that type for now: {item}!")
            
        return bytes(item, "utf-8")
        
    def add(self, key: Union[str, int, float, bytes], val: Union[str, int, float, bytes]) -> bool:
        encrypted_value = self.crypto.encrypt(str(val))
        
        return self.table.insert_item(key, encrypted_value)
        
    def get(self, key: Union[str, int, float, bytes]) -> Union[str, bool]:
        result = self.table.get_item(key)
        
        if result:
            return self.crypto.decrypt(result)
        else:
            return False
            
    def delete(self, key: Union[str, int, float, bytes]) -> bool:
        return self.table.delete_item(key)
        
# Restructure to put it all in one!
class Encrypted_Cache:
    pass
        
if __name__ == "__main__":
    print("Testing low-level cache API")
    cache = Cached_Table()
    
    cache.insert_item("ip", "172.168.1.2")
    cache.insert_item("ip_version", 4)
    cache.insert_item("os_version", 7.1)
    cache.insert_item("trusted_anchor_key", bytes("s3cur3", "utf-8"))
    
    print(cache.get_item("os_version"))
    
    cache.insert_item("os_version", 8.3)
    
    print(cache.get_item("os_version"))
    
    print(f'Deleting os_version from cache: {cache.delete_item("os_version")}')
        
    print(cache.get_item("os_version"))  
    
    print("\n\n\nTesting encrypted cache!")
    encrypted_cache = Cache()
    encrypted_cache.add("ip", "172.168.1.2")
    encrypted_cache.add("ip_version", 4)
    encrypted_cache.add("os_version", 7.1)
    encrypted_cache.add("trusted_anchor_key", bytes("s3cur3", "utf-8"))
    
    print(encrypted_cache.get("os_version")) 
    
    encrypted_cache.add("os_version", 8.3)
    
    print(encrypted_cache.get("os_version"))
    print(f'Deleting os_version from cache: {encrypted_cache.delete("os_version")}')   
    print(encrypted_cache.get("os_version"))
