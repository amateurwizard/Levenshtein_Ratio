import numpy as np


def levenshtein_ratio_and_distance(string1, string2, ratio_calc=False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of string1 and the
        first j characters of string2
    """
    # Initialize matrix of zeros
    rows = len(string1) + 1
    columns = len(string2) + 1
    distance = np.zeros((rows, columns), dtype=int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for a in range(1, rows):
        for b in range(1, columns):
            distance[a][0] = a
            distance[0][b] = b

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for column in range(1, columns):
        for row in range(1, rows):
            if string1[row - 1] == string2[column - 1]:
                cost = 0  # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc:
                    cost = 2
                else:
                    cost = 1
            distance[row][column] = min(distance[row - 1][column] + 1,  # Cost of deletions
                                        distance[row][column - 1] + 1,  # Cost of insertions
                                        distance[row - 1][column - 1] + cost)  # Cost of substitutions
    if ratio_calc:
        # Computation of the Levenshtein Distance Ratio
        ratio = ((len(string1) + len(string2)) - distance[row][column]) / (len(string1) + len(string2))
        return ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][column])


def main():
    string1 = "Apple Inc."
    string2 = "apple Inc"

    distance = levenshtein_ratio_and_distance(string1.lower(), string2.lower())
    print(distance)
    ratio = levenshtein_ratio_and_distance(string1, string2, ratio_calc=True)
    print(ratio)


main()
