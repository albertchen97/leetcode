from collections import defaultdict

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        num_of_total_rabbits = 0
        num_of_colors = defaultdict(int)
        remaining_rabbits_of_color = defaultdict(int)
        seen_answer_color = defaultdict(int)
        color = -1
        
        for answer in answers:
            # Whoever answered 0 is always the only rabbit of this color in the forest
            if answer == 0:
                color += 1
                num_of_colors[color] = 1
            
            # Otherwise, it could be a rabbit of a new color or a rabbit of the same color with a previously answered rabbit
            else:
                # If this is the first time this number is answered, it means it's a new color
                if answer not in seen_answer_color.keys():
                    color += 1
                    # The total number of rabbits of the color `color` is 1 (the answered rabbit itself) plus the number of other rabbits of the same color in the forest which is given by the rabbit's answer
                    num_of_colors[color] = 1 + answer

                    # Assign this new color to this sepcific answer
                    seen_answer_color[answer] = color

                    # Record the remaining number of rabbits of color `color`
                    remaining_rabbits_of_color[color] = answer

                # If we have seen this number answered before, it could mean either the current rabbit is of the same color as a previously answered rabbit OR the current rabbit is of a new color. It depends on the number of remaining rabbits of this color.
                else:
                    # If we know there are remaining rabbits of the same color as a previously answered rabbit AND the current rabbit answered the same number as a previously answered rabbit, to get the minimum possible number of rabbits in the forest, we can assume that the rabbit is of the same color as the previously answered rabbit who answered the same number.
                    color_of_this_answer = seen_answer_color[answer]
                    if remaining_rabbits_of_color[color_of_this_answer] > 0:
                        # Decrease the number of remaining rabbits of this color
                        remaining_rabbits_of_color[color_of_this_answer] -= 1
                    # No more possible remaining rabbits of this color left. Therefore, the current rabbit must be of a new color.
                    else:
                        color += 1

                        num_of_colors[color] = 1 + answer

                        # Assign this new color to this answer
                        seen_answer_color[answer] = color

                        # Record the remaining number of rabbits of color `color`
                        remaining_rabbits_of_color[color] = answer

        return sum(num_of_colors.values())  
        # Time: O(n) because one-pass
        # Space: O(n) because worst case would create dictionaries of the same length as the input list
                    
    
