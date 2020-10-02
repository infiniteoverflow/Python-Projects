import time
class Solver():
    
    #Enter sudoku you want to get solved
    sudoku = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    for i in range(9):
            no=i+1
            nums = input("Enter the "+str(no)+" row:")
            for j in range(9):
                sudoku[i][j]=int(nums[j])
    start = time.perf_counter()

    
    


    def __init__(self):
        self.solve(self.sudoku)
        print("Solved sudoku")
        self.display(self.sudoku)

    # Find_empty function will check for cells with zero and return its position
    def find_empty(self,sudoku):  
        for i in range (len(sudoku)):
            for j in range (len(sudoku[0])):
                if sudoku[i][j]== 0:
                    return (i,j)   #(row,col)

    # Valid funtion will check row,col and 3x3 box for valid input
    def valid(self,sudoku,num,pos): 
        # Check row 
        for i in range (len(sudoku[0])):
            if num==sudoku[pos[0]][i] and pos[1]!=i:
                return False
        # Check column
        for i in range (len(sudoku)):
            if num == sudoku[i][pos[1]] and pos[0]!=i:
                return False

        # Check 3x3 box
        box_x = pos[1]//3
        box_y = pos[0]//3

        for i in range(box_y*3,box_y*3+3):
            for j in range(box_x*3,box_x*3+3):
                if num == sudoku[i][j] and pos!=(i,j):
                    return False

        return True

    # Solve fuction will solve sudoko using Backtrack algorithm
    def solve(self,sudoku): 

        self.display(sudoku)
        print()
        
        find = self.find_empty(sudoku)
        if not find:
            return True
        else:
            row,col = find

        for i in range (1,10):
            if self.valid(sudoku,i,(row,col)):
                sudoku[row][col]=i
              
                if self.solve(sudoku):
                    return True
                
                sudoku[row][col] = 0

        self.display(sudoku)
        return False



    # Display funtion to display sudoko in terminal
    def display(self,sudoku): 
        for i in range (len(sudoku)):
            if i%3==0 and i!=0:
                print("- - - - - - - - - - -")
            for j in range (len(sudoku[0])):
                if j%3==0 and j!=0:
                    print('|',end=' ')
                if j == 8:
                    print(sudoku[i][j])
                else:
                    print(sudoku[i][j],end=' ')
        timer= time.perf_counter()-self.start
        print("Elapsed time: ",timer)
    
Solver()
