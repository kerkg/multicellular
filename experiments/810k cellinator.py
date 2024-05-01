import gc


class SubSet:
    def __init__(self, iterable=None):
        self.items = set()
        if iterable:
            self.items.update(iterable)

    def add(self, item):
        self.items.add(item)

    def remove(self, item):
        self.items.remove(item)

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return str(self.items)


# TODO:  cellworks
# -META-
# pargf
# N>(0,0),(0,0,0)<
# apr_s>4750052<
# -DATA-


def pargf_builder(file: str, natural=((0, 0), (0, 0, 0)), number_of_cells: int = 250000):
    """
    :param file: name of the file you want to write on including the suffix
    :param natural: tuple[tuple[int, int], tuple[int, int, int]]
    builds a sample pargf file with all the cells being the same
    :param number_of_cells: the number of cells you want
    """
    screen_list = []
    cell = natural
    for i in range(number_of_cells):
        screen_list += cell
    with open(file, "w") as file:
        file.flush()
        file.write(str(screen_list))
    return 1

def progress_finder(whole_task: int, done_task: int, progress_note: str = None) -> tuple:
    return whole_task / done_task, progress_note


def pargf_decoder(p, file_name, file) -> set:
    """
    :param file_name: name of the file
    :param file: raw file
    :param p: pointer
    :return: the execution queue( called ex_queue )
    """
    # creating vars for metadata decoding
    file_raw_obj_data = ""
    apr_size = ""  # stands for approximate_size
    # "natural" decoder
    natural = ""
    p += 1
    while file[p] != "<":
        natural += file[p]
        p += 1
    exec(f"natural = {natural}")
    p += 8
    # apr_size decoder
    while file[p] != "<":
        apr_size += file[p]
        p += 1
    apr_size = int(apr_size)
    p += 10
    nsvr = ""  # stands for numerical_SubValue_Register
    cell_register = [(), ()]
    while True:
        while file[p] != ")":
            if file[p] != " ":
                while file[p] != ",":
                    nsvr += file[p]
                if nsvr.isnumeric():
                    nsvr = int(nsvr)
                cell_register[0] = nsvr
            else:
                p += 1
        #         decoder partially works
        if file[p] == "]":
            file_len = p + 1
            break
        p += 1
    # decoding the obj_data

    del file
    gc.collect()
    return {file_name, apr_size, file_len, natural, 1}


def argf_decoder(file, p):
    print(file)
    print(p)
    NotImplementedError("work in progress")


def file_directer(file_name: str) -> None:
    """
    :param file_name: name of the file with suffix
    fetches the files from the disk and directs the screen data to the decoders
    """
    # fetching the data from the disk
    with open(file_name, "r") as file:
        file = file.read()
    file_name = file_name.strip(".txt")
    p = 0  # stands for pointer
    p += 8
    if file[p] == "a":  # the letter "a" is the second letter in the word "pargf" btw
        p += 6
        pargf_decoder(p, file_name, file)
    elif file[p] == "r":  # the letter "r" is the second letter in the word "argf" btw
        p += 5
        argf_decoder(file, p)
    else:
        # make the compiler
        p += 5