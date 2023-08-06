import ctypes as C
import cached_table

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
        self.loaded_shared_library = C.CDLL(cached_table)
        
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
            
if __name__ == "__main__":
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
