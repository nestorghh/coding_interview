class Solution():

    def printSolution(self,board):
        import numpy as np
        print(np.matrix(board))

    def isSafe(self,board,row,col):

        # check the columns to the left of col (range(col))
        for i in range(col):
            if board[row][i]==1:
                return False

        #upper diagonal on left side
        for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
            if board[i][j]==1:
                return False

        # lower diagonal on left side
        for i, j in zip(range(row,N,1), range(col,-1,-1)):
            if board[i][j]==1:
                return False

        return True
        
    def solveNQAux(self,board,col):
        global N
        N=4
        if col>=N:
            return True

        for i in range(N):

            if self.isSafe(board,i,col)==True:
                board[i][col]=1
                
                if self.solveNQAux(board,col+1)==True:
                    return True

                board[i][col]=0
            
        return False

    def solve(self):
        global board
        board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        
        if self.solveNQAux(board,0)==False:
            print("Solution does not exist")
            return False

        self.printSolution(board)
        return True






