# Convert Hash Type list from hashcat wiki to usable format

def clean_data():
    with open("HashTypes.raw", "r") as raw_file:
        lines: list[str] = raw_file.readlines()
        lines = list(map(lambda line: line.replace(" ", ""), lines))

    with open("HashTypes.txt", "w") as clean_file:
        for _line in lines:
            clean_file.write(_line)


def get_data_as_list_tuple():
    with open("HashTypes.txt", "r") as f:
        lines = f.readlines()
    data = list(map(lambda line: line.replace("\n", "").split("|"), lines))
    print(data)


clean_data()
get_data_as_list_tuple()
