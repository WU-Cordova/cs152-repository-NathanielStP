import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT, VT]]] = \
            Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(number_of_buckets)], data_type=LinkedList)
        self._count: int = 0
        self._load_factor_threshold: float = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function
    
    def _get_bucket_number(self, key: KT):
        return self._default_hash_function(key) % len(self._buckets)

    def __getitem__(self, key: KT) -> VT:
        bucket_index: int = self._get_bucket_number(key)
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]

        for [k, v] in bucket_chain:
            if k == key:
                return v
        raise KeyError

    def __setitem__(self, key: KT, value: VT) -> None:       
        bucket_index: int = self._get_bucket_number(key)
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]

        for (k, v) in bucket_chain:
            if k == key:
                bucket_chain.remove((k, v))
                self._count -= 1
                break
        bucket_chain.append((key, value))
        self._count += 1

    def keys(self) -> Iterator[KT]:
        for bucket_chain in self._buckets:
            for [k, _] in bucket_chain:
                yield k
    
    def values(self) -> Iterator[VT]:
        for bucket_chain in self._buckets:
            for [_, v] in bucket_chain:
                yield v

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for bucket_chain in self._buckets:
            for [k, v] in bucket_chain:
                yield (k, v)
            
    def __delitem__(self, key: KT) -> None:
        bucket_index: int = self._get_bucket_number(key)
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]

        for [k, v] in bucket_chain:
            if k == key:
                bucket_chain.remove((k, v))
                self._count -= 1
                return
        raise KeyError
    
    def __contains__(self, key: KT) -> bool:
        bucket_index: int = self._get_bucket_number(key)
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]

        for [k, _] in bucket_chain:
            if k == key:
                return True
        return False
            
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        for bucket_chain in self._buckets:
            for [k, _] in bucket_chain:
                yield k
    
    def __eq__(self, other: object) -> bool:
        list1 = []
        list2 = []
        for item in self:
            list1.append(item)
        for item in other:
            list2.append(item)
        return list1 == list2

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)