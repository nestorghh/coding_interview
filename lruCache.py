class lruCache:
    def __init__(self, capacity):
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn):
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
            self._isbn_price_table[isbn]=price
        else:
            return -1
        
        return price

    def insert(self,isbn,price):
        
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table)==self._capacity:
            self._isbn_price_table.popitem(last=False)    

         self._isbn_price_table[isbn]=price

    def erase(self,isbn):
        if isbn in self._isbn_price_table:
            self._isbn_price.table.pop(isbn)
        else:
            return -1


