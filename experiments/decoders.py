import cell
from colorama import Fore, Back, Style, init, just_fix_windows_console  # print_with_style func has those guys
import json
# FİXME: decoder too slow gotta thread
just_fix_windows_console()


def json_reader(file_name) -> dict:
    """
    reads the config.json
    :param file_name: file name with .json suffix"""
    return json.load(open(file_name))


def pargf_sample_builder(file: str, natural: tuple = (0, 0, 0), number_of_cells: int = 500000):
    """
    :param file: name of the file you want to write on including the suffix
    :param natural: tuple[tuple[int, int], tuple[int, int, int]]
    builds a sample pargf file with all the cells being the same
    :param number_of_cells: the number of cells you want
    """
    screen_list = []
    temp_list = [natural]
    for _ in range(number_of_cells):  # DO NOT TOUCH, ITS GONNA BREAK
        screen_list += temp_list
    print(screen_list)
    with open(file, "w") as file:
        file.flush()
        file.write(str(screen_list))
    return 1


def print_with_style(message: str | Exception | Warning, type: str = None, pack: list[str, str, str] | tuple[str, str, str] = None) -> None:
    """:param message: the message you want to print
       :param type: the type of the message or more like builtin packs also you must either input type or pack or
       ıll headshot you with an error (ıll thrown an error)
       :param pack: the pack you want to use or simple an iterable that has
       the Fore, Back and Style data that you desire and the order should be (Fore, Back, Style)
        for example ("RED", "BLUE", "DIM")"""
    if type is None and pack is None:
        raise ValueError("as ive said in the docs either input pack or type and you didnt read the docs huh, well have "
                         "fun getting no scope 360'd from God knows where-vile")

    exec(f"print(Fore.{pack[0].upper()} + Back.{pack[1].upper()} + Style.{pack[2].upper()} + {message})")


def progress_finder(whole_task: int, done_task: int, progress_note: str = None) -> tuple:
    return done_task / whole_task, progress_note


def worm_algorithm(file, auto_log, starting_point, end_point):  # aka threadable pargf loader
    if starting_point >= end_point:
        raise IndexError("starting point exceeds end point")
    file_buffer = cell.StringBuffer(file[starting_point:end_point], prelisting=True)  # definitely working on it
    if auto_log: print_with_style("buffer loaded", "process_information")
    p1 = cell.CellPointer(0)
    p1.goto_cell_start(file_buffer.stringling)
    for char in file_buffer.stringling:
        if char == "(":
            while char != ")":
                pass  # FIXME: make it so the stuff between commas get to another tuple and putted away


def argf_decoder(file, p):
    print(file)
    print(p)  # this gotta be a binary decoder
    NotImplementedError("work in progress")


def meta_decoder(file_name: str, auto_log):
    """
    :param auto_log: if set to true will log the activities, useful for debugging and looks cool( I mean who doesn't
    get excited when the terminal pops up and starts doing something, eh)
    :param file_name: name of the file with suffix
    fetches the files from the disk and directs the screen data to the decoders
    """
    # init()  # colorama initializer
    # fetching the data from the disk
    if auto_log:
        print(f"fetching the {file_name} from the disk")
    with open(file_name, "r") as file:
        file = file.read()
    if auto_log:
        print_with_style("fetching successful, primary decoding started", "process_information")
    file_name = file_name.strip(".txt")
    p = cell.CellPointer(0)  # stands for pointer
    if file[p + 8] == "a":  # the letter "a" is the second letter in the word "pargf" btw
        p += 6
        if auto_log:
            print("file type is pargf")
        # "natural" decoder
        natural = ""
        p.slide(False)
        while file[p] != "<":
            natural += file[p]
            p.slide(False)
        exec(f"natural = {natural}")
        if auto_log:
            print(f"natural is {natural}")
        # apr_char_num decoder
        apr_char_num = ""  # stands for approximate_size
        p += 8
        while file[p] != "<":
            apr_char_num += file[p]
            p.slide(True)
        apr_char_num = int(apr_char_num)
        if auto_log:
            print(f"apr_char_num is {apr_char_num}")
        metadata = (file_name, natural, apr_char_num)
        if auto_log:
            print(f"metadata is {metadata}")
        while file[p] != "[":
            p.slide(True)
        file.replace(file[0: p], "")
    elif file[p] == "r":  # the letter "r" is the second letter in the word "argf" btw
        p += 5
        if auto_log:
            print("decoding")
        argf_decoder(file, p)
    else:
        # make the compiler
        p += 5


if __name__ == "__main__":
    meta_decoder("texture.txt", True)
