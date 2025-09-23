# GEO1000 - Assignment 2 (part 1)
# Authors: Timber Groeneveld
# Studentnumbers: 4213513

"""So we know the starting point, ending point and the number of steps. Now we have to calculate the total amount of possible paths.
In case of the example where start is 1, end is 4 and moves are 5 there are 5 possible paths.
Variables: start, end, moves, paths"""

def move(start, end, moves):
    """This function takes the starting point, end point and the number of required moves and returns the number of possible paths.
    Arguments:
        start: The starting point of the robot.
        end: The end point of the robot.
        moves: The number of moves required, these van be right (+) moves or left (-) moves.
    Returns:
        paths: The total number of possible paths given the arguments."""
    # If the number of moves runs out, check if the location of the robot has reached the endpoint.
    if moves == 0:
        if start==end:
            return 1                                # In case a path succeeds after its moves runs out
        else:
            return 0                                # In case a path fails
    # Try different steps to right and left, use recursion to check for every step and add up successful paths.
    paths = 0                                       # Start path counter at zero
    right_paths = move(start + 1, end, moves - 1)   # Call the function again with one place to the right and one move spent
    paths += right_paths                            # Add the outcome (0 or 1) to the total number of successful paths
    left_paths = move(start - 1, end, moves - 1)    # Call the function again with one place to the left and one move spent
    paths += left_paths                             # Add the outcome (0 or 1) to the total number of successful paths
    # Returns the number of successful paths
    return paths

# Print the function and give starting point, ending point and a number of moves
if __name__ == "__main__":
    print("running robot.py directly")
    print(move(1, 4, 5))  # Expected output: 5
    print(move(4, 1, 5))  # Expected output: 5
    print(move(1, 4, 2))  # Expected output: 0