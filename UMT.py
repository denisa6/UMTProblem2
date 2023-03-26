"""
Any 2 points can form a rectangle.
I am determining the remaining 2 points and checking if we have them in our set of given coordinates.
"""
# function to find number of possible rectangles
def countRectangles(coord):
    aux_coord = coord;
    # number of rectangles
    ans = 0;
    for i in range(len(coord)):
        for j in range(len(coord)):
            if (coord[i][0] != coord[j][0] and coord[i][1] != coord[j][1]):
                if([coord[i][0], coord[j][1]] in aux_coord and [coord[j][0], coord[i][1]] in aux_coord):
                    ans += 1
 
    # return the final answer
    # /4 because we find the same rectangle when we check for each combination of 2 points (AB, BC, CD, AD)
    return int(ans / 4);


# first sample
n1 = 6;
coord1 = [0] * n1
coord1[0] = [1, 1];
coord1[1] = [1, 3];
coord1[2] = [2, 1];
coord1[3] = [2, 3];
coord1[4] = [3, 1];
coord1[5] = [3, 3];
print("first sample\nexpected result: 3\nactual result: " + str(countRectangles(coord1)) + "\n");

# second sample
n2 = 5;
coord2 = [0] * n2
coord2[0] = [1, 1];
coord2[1] = [1, 3];
coord2[2] = [2, 1];
coord2[3] = [3, 1];
coord2[4] = [3, 3];
print("second sample\nexpected result: 1\nactual result: " + str(countRectangles(coord2)) + "\n");
