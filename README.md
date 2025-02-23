# DFS-1

## Problem1 (https://leetcode.com/problems/flood-fill/)

# Solution: BFS
# Take a boiler plate array for directions, take the original color to check if matches the desired 
# color.
# Initialize a queue and append the initial row and column index, make the initial pixel with color.
# Using the starting pixel row and column check all directions. Append the row and column indexes into
# the stack and pop after the color is changed. 
# Once all direction colors are changed, return the resultant image.

# Solution: DFS
# Initialize the boiler plate array for directions and store the orginal color with the 1st pixel.
# We iterate over the matrix calling the dfs function. The function checks for bounds that is all 4 
# corners of the matrix and if there is no pixel with the original color.
# We iterate over the matrix in all directions and change the pixel value to new color. Return the result
# image.

## Problem2 (https://leetcode.com/problems/01-matrix/)

# Initialize a queue and get all the independent elements in the matrix i.e all '0's.
# Pop each zero and append the corresponding nodes from all the directions and append the queue.
# Initially when we get the value '1' we will make it '-1' to refer as a visited node. The next time
# when we reach the same element we will increment its distance.
# Return the resultant matrix with the distances.