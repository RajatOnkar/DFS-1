'''
// Time Complexity :
# Problem 1 - O(m*n) m - no. of rows, n - no. of columns (both BFS and DFS)
# Problem 2 - O(m*n) + O(m*n) ~= O(m*n) the first m*n is to get all '0's and the next for '1's.
// Space Complexity :
# Problem 1 - O(m*n) m - no. of rows, n - no. of columns (both BFS and DFS)
# Problem 2 - O(m*n) as we parse the entire matrix and update it
// Did this code successfully run on Leetcode :
# Yes the code ran successfully.
// Any problem you faced while coding this :

// Your code here along with comments explaining your approach
'''
## Problem 1 - Flood fill
# Solution: BFS
# Take a boiler plate array for directions, take the original color to check if matches the desired 
# color.
# Initialize a queue and append the initial row and column index, make the initial pixel with color.
# Using the starting pixel row and column check all directions. Append the row and column indexes into
# the stack and pop after the color is changed. 
# Once all direction colors are changed, return the resultant image.

from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image == None: return image
        dirs = [[1,0], [-1,0], [0,-1], [0,1]]
        m = len(image)
        n = len(image[0])
        org_color = image[sr][sc]
        if org_color == color: return image
        queue = deque()
        queue.append(sr)
        queue.append(sc)
        image[sr][sc] = color
        while len(queue) > 0:
            cr = queue.popleft()
            cc = queue.popleft()
            for dir in dirs:
                nr = cr + dir[0]
                nc = cc + dir[1]
                if nr >= 0 and nr < m and nc >= 0 and nc < n and image[nr][nc] == org_color:
                    queue.append(nr)
                    queue.append(nc)
                    image[nr][nc] = color
        return image

# Solution: DFS
# Initialize the boiler plate array for directions and store the orginal color with the 1st pixel.
# We iterate over the matrix calling the dfs function. The function checks for bounds that is all 4 
# corners of the matrix and if there is no pixel with the original color.
# We iterate over the matrix in all directions and change the pixel value to new color. Return the result
# image.

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image == None: return image
        dirs = [[1,0], [-1,0], [0,-1], [0,1]]
        org_color = image[sr][sc]
        if org_color == color: return image
        self.dfs(image, sr, sc, color, org_color, dirs)
        return image
    
    def dfs(self, image, sr, sc, color, org_color, dirs):
        ##base
        if sr < 0 or sr == len(image) or sc < 0 or sc == len(image[0]) or image[sr][sc] != org_color:
            return
        ##logic
        image[sr][sc] = color
        for dir in dirs:
            nr = sr + dir[0]
            nc = sc + dir[1]
            self.dfs(image, nr, nc, color, org_color, dirs)

## Problem 2 - 01 Matrix
# Initialize a queue and get all the independent elements in the matrix i.e all '0's.
# Pop each zero and append the corresponding nodes from all the directions and append the queue.
# Initially when we get the value '1' we will make it '-1' to refer as a visited node. The next time
# when we reach the same element we will increment its distance.
# Return the resultant matrix with the distances.

from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        dirs = [[1,0], [-1,0], [0,-1], [0,1]]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: 
                    queue.append([i,j])
                else:
                    mat[i][j] = -1
        dist = 1
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                for dir in dirs:
                    nr = curr[0] + dir[0]
                    nc = curr[1] + dir[1]
                    if nr >= 0 and nr <m and nc >= 0 and nc < n and mat[nr][nc] == -1:
                        queue.append([nr, nc])
                        mat[nr][nc] = dist
            dist += 1
        return mat