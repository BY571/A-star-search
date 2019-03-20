global gridsize
gridsize = 25

w = 25
global grid
grid = [[1]*gridsize for i in range(gridsize)]
# Button constants
wb = 30
xb = 600
yb = 600

def setup():
    size(800,800)
 
    
def draw():
    #print(grid)
    x,y = 0,0
    if (keyPressed == True):
        print("pressed!")
        if key == ENTER:
        # Check if only one start >0< and only one goal >1< state exist
            if count_element(grid, 2) == 1 and count_element(grid, 3) == 1 and count_element(grid,5) == 0:
                print("A* runs!")
                #get_goal, get_start 
                start, goal = search_start_goal_position(grid, 2,3)
                print("starting point: [{},{}], goal point: [{},{}]".format(start[0],start[1],goal[0],goal[1]))
                steps = run_A_star(grid, calc_heuristic_grid(goal),start,goal)
                grid[goal[0]][goal[1]] = 3   #goal state gets lost because of painting blue as final state
            else:
                print("Amount of Start-states or Goal-states is not correct!")
                pass
        if key == "e":
            # erases path taken:
            for i,col in enumerate(grid):
                for j,space in enumerate(col):
                    if space == 5:
                        grid[i][j] = 1

        if key == "n":
            #clears grid
            for i,col in enumerate(grid):
                for j,space in enumerate(col):
                    if space == 2 or space == 3 or space == 5 or space == 4:
                        grid[i][j] = 1
                        
        
            
    for i,row in enumerate(grid):
        for col in row:
            if col == 2:
                #start
                fill(255,0,0)
            elif col == 3:
                #goal
                fill(0,255,0)
                #text("G",col*w,i*w)
            elif col == 4:
                # obstacle
                fill(0,0,0)
            elif col == 5:
                # path
                fill(0,0,255)
            elif col == 1:
                fill(255)
            else:
                fill(255)
            rect(x,y,w,w)
            x = x+w
        y = y+w # starting new line
        x = 0   # setting new line back to 0
            

def make_grid(gridsize, variation=0):
    print("make new grid!")
    if variation == 1:
        gridsize += 1
    elif variation == -1:
        gridsize -= 1
    else:
        pass
    print("gridsize: ",gridsize)
    #global grid
    grid_mask  = [[1]*gridsize for i in range(gridsize)]
    return grid_mask
        
def mousePressed():
    #print(mouseY/w, mouseX/w)
    if mouseButton == LEFT:
        if grid[mouseY/w][mouseX/w] < 4:
            grid[mouseY/w][mouseX/w] += 1
        else:
            grid[mouseY/w][mouseX/w] = 1
    if mouseButton == RIGHT:
        # Deletes Field specifications
        grid[mouseY/w][mouseX/w] = 1


        

def run_A_star(grid, heuristic_grid, start, goal):
    # fill the grid cells which are used as the way with blue
    step = 0
    open_list = []
    state = start
    path = []
    #global_min_g_value = len(grid)**2
    while state != goal:
        
        print("current state: {}".format(state))
        
        step +=1
        #delay(1000)
        min_g_value = len(grid)**2
        if (state[0] != 0 and grid[state[0]-1][state[1]] != 4 and grid[state[0]-1][state[1]] != 5 and grid[state[0]-1][state[1]] != 2):
            # check if up is possible to expand and not blocked by obstacle
            print("up is possible")
            new_possible_state = (state[0]-1, state[1])
            movement = "move up"
            g_value = step + heuristic_grid[new_possible_state[0]][new_possible_state[1]]
            open_list.append([movement, new_possible_state, step, g_value])

        if (state[0] != gridsize-1 and grid[state[0]+1][state[1]] != 4 and grid[state[0]+1][state[1]] != 5 and grid[state[0]+1][state[1]] != 2):
        # check if down is possible and not blocked by obstacle
            print("down is possible")
            new_possible_state = (state[0]+1, state[1])
            movement = "move down"
            g_value = step + heuristic_grid[new_possible_state[0]][new_possible_state[1]]
            open_list.append([movement, new_possible_state, step, g_value])
  
        if (state[1] != 0 and grid[state[0]][state[1]-1] != 4 and grid[state[0]][state[1]-1] != 5 and grid[state[0]][state[1]-1] != 2):
            #check if left is possible and not blocked by obstacle
            print("left is possible")
            new_possible_state = (state[0], state[1]-1)
            movement = "move left"
            g_value = step + heuristic_grid[new_possible_state[0]][new_possible_state[1]]
            open_list.append([movement, new_possible_state, step, g_value]) 

        if (state[1] != gridsize-1  and grid[state[0]][state[1]+1] != 4 and grid[state[0]][state[1]+1] != 5  and grid[state[0]][state[1]+1] != 2):
            # check if right is possible and not blocked by obstacle
            print("right is possible")
            new_possible_state = (state[0], state[1]+1)
            movement = "move right"
            g_value = step + heuristic_grid[new_possible_state[0]][new_possible_state[1]]
            open_list.append([movement, new_possible_state, step, g_value])

        # improvement of more possible ways to expand
        if (state[1] != gridsize-1 and state[1] != 0 and state[0] != gridsize -1 and state[0] != 0 and grid[state[0]-1][state[1]+1] != 4 and grid[state[0]-1][state[1]+1] != 5  and grid[state[0]-1][state[1]+1] != 2):
            # check if right is possible and not blocked by obstacle
            print("upright is possible")
            new_possible_state = (state[0]-1, state[1]+1)
            movement = "move upright"
            g_value = step + heuristic_grid[new_possible_state[0]][new_possible_state[1]]
            open_list.append([movement, new_possible_state, step, g_value])

        if (state[1] != gridsize-1 and state[1] != 0 and state[0] != gridsize -1 and state[0] != 0 and grid[state[0]-1][state[1]-1] != 4 and grid[state[0]-1][state[1]-1] != 5  and grid[state[0]-1][state[1]-1] != 2):
            # check if right is possible and not blocked by obstacle
            print("upleft is possible")
            new_possible_state = (state[0]-1, state[1]-1)
            movement = "move upleft"
            g_value = step + heuristic_grid[new_possible_state[0]][new_possible_state[1]]
            open_list.append([movement, new_possible_state, step, g_value])

        if (state[1] != gridsize-1 and state[1] != 0 and state[0] != gridsize -1 and state[0] != 0 and grid[state[0]+1][state[1]+1] != 4 and grid[state[0]+1][state[1]+1] != 5  and grid[state[0]+1][state[1]+1] != 2):
            # check if right is possible and not blocked by obstacle
            print("downright is possible")
            new_possible_state = (state[0]+1, state[1]+1)
            movement = "move downright"
            g_value = step + heuristic_grid[new_possible_state[0]][new_possible_state[1]]
            open_list.append([movement, new_possible_state, step, g_value])

        if (state[1] != gridsize-1 and state[1] != 0 and state[0] != gridsize -1 and state[0] != 0 and grid[state[0]+1][state[1]-1] != 4 and grid[state[0]+1][state[1]-1] != 5  and grid[state[0]+1][state[1]-1] != 2):
            # check if right is possible and not blocked by obstacle
            print("downleft is possible")
            new_possible_state = (state[0]+1, state[1]-1)
            movement = "move downleft"
            g_value = step + heuristic_grid[new_possible_state[0]][new_possible_state[1]]
            open_list.append([movement, new_possible_state, step, g_value])
        
        
        
        # checking for the lowest g_value -> delete all the other possible states -> remaining element of open_list is new state
        
        #print(grid)    
        print(open_list)
        min_g_value = open_list[0][3]
        lowest_opener_idx = 0
        for idx, opener in enumerate(open_list):
                       
            if opener[3] < min_g_value:
                min_g_value = opener[3]
                lowest_opener_idx = idx
                
            
                
        lowest_opener = open_list[lowest_opener_idx]
        state = lowest_opener[1]
        print(lowest_opener[0])
        #paint new state blue as the taken path:
        grid[state[0]][state[1]] = 5

        # delete all member of opening list
        del(open_list[:])
        
    print("Found goal in {} steps!".format(step))
    return step


def search_start_goal_position(list_, start_value, goal_value):
    """
    Searches for the starting and goal position in a 2dim list
    Input: 2dim list, starting value, goal value
    Returns: starting position tupel, goal position tupel
    """
    for x in range(len(list_)):
        for y in range(len(list_)):
            if list_[x][y] == start_value:
                start = (x,y)
            elif list_[x][y] == goal_value:
                goal = (x,y)
    return start, goal


def count_element(list_, element):
    """
    Counts the appearance of a element in a 2dim list
    Input: 2dim list, int element
    Return: int appearance
    """
    overall = 0
    for i in list_:
        overall += i.count(element)
    return overall

def calc_heuristic_grid(goal):
    """
    Calculates the heuristic function to a given grid and goal as the as the euclidean distance.
    Input: 2dim list, goal-tupel
    Return: 2dim list 
    """
    global heuristic_grid
    heuristic_grid = make_grid(gridsize)
    for i in range(len(heuristic_grid)):
            for j in range(len(heuristic_grid)):
                dist_x = abs(goal[0]-i)
                dist_y = abs(goal[1]-j)
                if dist_x > dist_y:
                    heuristic_grid[i][j] = dist_x
                else:
                    heuristic_grid[i][j] = dist_y
    print("HEURIST",heuristic_grid)
    return heuristic_grid
