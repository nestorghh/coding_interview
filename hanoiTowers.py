class Solution():
    def move(self,from_,to):
        print("Move disc from {} to {}".format(from_,to))

    def moveVia(self,from_,via,to):
        self.move(from_,via)
        self.move(via,to)

    def hanoi(self,n,from_,via,to):
        if n==0:
            pass
        else:
            self.hanoi(n-1,from_,to,via)
            self.move(from_,to)
            self.hanoi(n-1,via,from_,to)

