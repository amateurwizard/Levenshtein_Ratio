import Levenshtein


def main():
    file_name = "Big Buck Bunny (2028) [1080p BluRay X265 HEVC 10-bit AAC 7.1]"
    test_string = "BluRay"

    input_data = []
    fruits = ["apple", "banana", "cherry"]
    distorted_data = [' A ', ' Of ', ' And ', ' The ', 'x265', 'I\'m ', 'St. ', 'Web-DL', 'WebRip', 'eztv.re', 'Blu-ray', 'eztv.re', 'A.K.A.', '10bit', 'chery']

    input_data = file_name.split()

    print(input_data)

    for index, item in enumerate(input_data):
        for index2, item2 in enumerate(distorted_data):       # Replace broken metadata
            levenshtein_ratio = Levenshtein.ratio(input_data[index].lower(), distorted_data[index2].lower())

            if levenshtein_ratio > 0.5:
                input_data[index] = distorted_data[index2]
                print("Input", end=": ")
                print(input_data[index])
                print("Levenshtein Ratio", end=": ")
                print(levenshtein_ratio)
    print(input_data)

    print("\n******This is a test******")
    levenshtein_ratio = Levenshtein.ratio(distorted_data[10], test_string)
    print("Levenshtein Ratio (Raw)", end=": ")
    print(levenshtein_ratio)
    levenshtein_distance = Levenshtein.distance(distorted_data[10], test_string)
    print("Levenshtein Distance (Raw)", end=": ")
    print(levenshtein_distance)

    levenshtein_ratio = Levenshtein.ratio(distorted_data[10].lower(), test_string.lower())
    print("Levenshtein Ratio", end=": ")
    print(levenshtein_ratio)
    levenshtein_distance = Levenshtein.distance(distorted_data[10].lower(), test_string.lower()),
    print("Levenshtein Distance", end=": ")
    print(levenshtein_distance)


main()
