class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_water, curr_water, curr_max = 0, 0, height[0]
        
        # left->right pass
        index = 0
        for i,h in enumerate(height):
            if h>=curr_max:
                curr_max = h
                total_water += curr_water
                curr_water = 0
                index = i
            else:
                curr_water+= (curr_max-h)
        
        #right->left pass upto index
        curr_water, curr_max = 0, height[-1]
        for h in height[index:][::-1]:
            if h>=curr_max:
                curr_max = h
                total_water += curr_water
                curr_water = 0
            else:
                curr_water+= (curr_max-h)
                
        
        return total_water
            
                        