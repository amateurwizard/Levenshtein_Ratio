import Levenshtein


def main():
    test_string = "BluRay"
    file_name = "Big Buck Bunny (2028) [1080p BluRay X265 HEVC 10-bit AAC 7.1]"
    distorted_data = [' A ', ' Of ', ' And ', ' The ', 'x265', 'I\'m ', 'St. ', 'Web-DL', 'WebRip', 'eztv.re',
                      'Blu-ray', 'eztv.re', 'A.K.A.', '10bit', 'chery']

    input_data = file_name.split()      # Putting the file name into a list.

    print("Input Data", end=": ")
    print(input_data)
    print("\n")

    for index, item in enumerate(input_data):
        for index2, item2 in enumerate(distorted_data):     # Nested for loop, to match all indexes between two lists.
            levenshtein_ratio = Levenshtein.ratio(input_data[index].lower(), distorted_data[index2].lower())

            if levenshtein_ratio > 0.5:     # Replace if the code if the match is good.
                print("Input", end=": ")
                print(input_data[index])
                input_data[index] = distorted_data[index2]
                print("Levenshtein Ratio", end=": ")
                print(levenshtein_ratio)
                print("Output", end=": ")
                print(input_data[index])
                print("\n")

    print("Output Data", end=": ")
    print(input_data)

    print("\n******This is a test******")       # Practice test cases for finding Levenshtein ratio & distances.
    levenshtein_ratio = Levenshtein.ratio(distorted_data[10], test_string)
    print("Levenshtein Ratio (Raw)", end=": ")
    print(levenshtein_ratio)
    levenshtein_distance = Levenshtein.distance(distorted_data[10], test_string),
    print("Levenshtein Distance (Raw)", end=": ")
    print(levenshtein_distance)

    levenshtein_ratio = Levenshtein.ratio(distorted_data[10].lower(), test_string.lower())
    print("Levenshtein Ratio", end=": ")
    print(levenshtein_ratio)
    levenshtein_distance = Levenshtein.distance(distorted_data[10].lower(), test_string.lower()),
    print("Levenshtein Distance", end=": ")
    print(levenshtein_distance)


main()
