import numpy as np

class AbelianSandpile:
    """
    An Abelian sandpile model simulation. The sandpile is initialized with a random
    number of grains at each lattice site. Then, a single grain is dropped at a random
    location. The sandpile is then allowed to evolve until it is stable. This process
    is repeated n_step times.

    A single step of the simulation consists of two stages: a random sand grain is 
    dropped onto the lattice at a random location. Then, a set of avalanches occurs
    causing sandgrains to get redistributed to their neighboring locations.
    
    Parameters:
    n (int): The size of the grid
    grid (np.ndarray): The grid of the sandpile
    history (list): A list of the sandpile grids at each timestep
    """

    def __init__(self, n=100, random_state=None):
        self.n = n
        np.random.seed(random_state) # Set the random seed
        self.grid = np.random.choice([0, 1, 2, 3], size=(n, n))
        self.history =[self.grid.copy()] # Why did we need to copy the grid?


    def step(self):
        """
        Perform a single step of the sandpile model. Step corresponds a single sandgrain 
        addition and the consequent toppling it causes. 

        Returns: None
        """


        highStacks = [] #list of tuples giving  the coordinates of every high stack
        for i in range(self.n):
            for j in range(self.n):
                if self.history[-1][i][j] > 3:
                    highStacks.append((i,j))

                    
        for pos in highStacks:  #remove 4 from every high stack and after making sure it's in the grid, add 1 to every nearest neighbor
            self.grid[pos[0]][pos[1]] -= 4
            if pos[0] - 1 >= 0:
                self.grid[pos[0] - 1][pos[1]] += 1
            if pos[0] + 1 < self.n:
                self.grid[pos[0] + 1][pos[1]] += 1
            if pos[1] - 1 >= 0:
                self.grid[pos[0]][pos[1] - 1] += 1
            if pos[0] + 1 < self.n:
                self.grid[pos[0]][pos[1] + 1] += 1

            self.history = [self.grid.copy()]  # Because of my approach of finding all the sandpiles that will
                                                # topple, I don't really need this
            
        

    # we use this decorator for class methods that don't require any of the attributes 
    # stored in self. Notice how we don't pass self to the method
    @staticmethod
    def check_difference(grid1, grid2):
        """Check the total number of different sites between two grids"""
        return np.sum(grid1 != grid2)

    
    def simulate(self, n_step):
        """
        Simulate the sandpile model for n_step steps.
        """

        for i in range(n_step):
            self.step()

            if self.check_difference(self.grid, self.history[-1]) == 0:
                break

if __name__ == "__main__":
    sandpile = AbelianSandpile(n=100)

    sandpile.simulate(100)
    print("I did it")
