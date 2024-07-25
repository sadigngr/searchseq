from searchseq.utils.bases import _bases
from searchseq.utils.errors import ChangeError

class Hash:

    def __init__(self,pattern : str):
        self._multiplier = 10
        self._pattern = pattern
        self._hash = 0
        self._prime = 113
        for i in range(len(self._pattern)):
            self._hash += (_bases[self._pattern[i]] * (self.multiplier**(len(self._pattern) - (i+1))))
        self._hash = self._hash%self._prime

    @property
    def prime(self):
        return self._prime
    @prime.setter
    def prime(self,value):
        self._prime = value
        print("Setting the prime value manually is only for debugging and testing and is not advised if you're not sure of what you're doing.")


    @property
    def multiplier(self):
        return self._multiplier

    @multiplier.setter
    def multiplier(self,value):
        self._multiplier = value
        print("Setting the multiplier manually is only for debugging and testing and is not advised if you're not sure of what you're doing.")
    @property
    def hash(self):
        return self._hash

    @hash.setter
    def hash(self,value):

        print("Setting the hash manually is only for debugging and testing and is not advised if you're not sure of what you're doing.")
        self._hash = value
