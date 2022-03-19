class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        # self.arena = [[0 for w in range(width)] for h in range(height)]
        self.state = [[0,0]]
        self.width = width
        self.height = height
        self.length = 0
        self.food = food
    
    
    def move(self, direction):
        """
        :type direction: str
        :rtype: int
        """
        x, y = self.state[-1]
        print(x,y, self.state)
        if direction == "L":
            y -= 1
        elif direction == "R":
            y += 1 
        elif direction == "U":
            x -= 1 
        elif direction == "D":
            x += 1 
        print(x,y, self.state)
        
        #check that snake does not hit boundary
        if y < 0 or y >= self.width or x < 0 or x >= self.height:
            return -1
        # print(head)
        # print(self.state)
        
        #check that snake doesn't eat itself
        if [x,y] in self.state[1:]: 
            return -1
        
        self.state.append([x,y])
        
        #if there is food, elongate the snake
        if self.food and [x,y] == self.food[0]:
            self.length += 1
            self.food = self.food[1:]
        else:
            self.state = self.state[1:]
        
        return self.length
    
    
    
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)