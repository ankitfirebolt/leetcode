class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse_dict = {}
        for i,key in enumerate("abcdefghijklmnopqrstuvwxyz"):
            morse_dict[key] =  morse[i]
            
        print(morse_dict)
        transformations = set()
        for w in words:
            transformations.add(''.join([morse_dict[c] for c in w]))
        
        return len(transformations)