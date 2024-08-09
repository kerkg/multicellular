import gc
# from colorama import Fore, Back, Style, init, deinit
# FİXME: decoder too slow gotta thread


def pargf_builder(file: str, natural: tuple = ((0, 0), (0, 0, 0)), number_of_cells: int = 250000):
    """
    :param file: name of the file you want to write on including the suffix
    :param natural: tuple[tuple[int, int], tuple[int, int, int]]
    builds a sample pargf file with all the cells being the same
    :param number_of_cells: the number of cells you want
    """
    screen_list = []
    cell: tuple = natural
    for i in range(number_of_cells):
        screen_list += cell
    with open(file, "w") as file:
        file.flush()
        file.write(str(screen_list))
    return 1


def progress_finder(whole_task: int, done_task: int, progress_note: str = None) -> tuple:
    return done_task/whole_task, progress_note


def pargf_decoder(p: int, file_name: str, file: str, auto_log: bool, p_mov_direction: bool, start_point: int,
                  apr_char_num: int, natural: set) -> set:
    """
    :param file_name: name of the file
    :param file: raw file
    :param p: pointer
    :param auto_log: activates the loggers helps debugging and looks cool
    :param p_mov_direction: pointer moving direction if set to true pointer will start at top-left if set to false
    pointer will start at bottom right
    :param start_point: starting point of the p
    :param apr_char_num: approximate character number
    :param natural: natural value of the cells
    :return: the pargf object
    """
    if auto_log: print("pre-declaring the vars")
    # decoding raw file data to the raw_page_obj
    p += start_point
    raw_page_obj = []
    cell_cache = ""
    subcell_value_end_counter = 0
    num_of_cells = 0
    if auto_log: print("pre-declared the vars")
    while 1:
        cell_cache += file[p]
        if file[p] == ")":
            subcell_value_end_counter += 1
            if subcell_value_end_counter == 2:
                exec(f"cell_cache=({cell_cache})")
                raw_page_obj.append(cell_cache)
                subcell_value_end_counter = 0
                num_of_cells += 1
                if num_of_cells % 1000 == 0 and auto_log:
                    print(f"100 cells has processed,approximately {apr_char_num-num_of_cells} cells left ,p is:{p}")
        if file[p] == "]":
            file_len = p + 1
            break
        p += 1
    del file, subcell_value_end_counter, p, cell_cache
    gc.collect()
    return {file_name, file_len, num_of_cells, raw_page_obj, natural}


def argf_decoder(file, p):
    print(file)
    print(p)
    NotImplementedError("work in progress")


def file_directer(file_name: str, auto_log):
    """
    :param auto_log: if set to true will log the activities, useful for debugging and looks cool( I mean who doesn't
    get excited when the terminal pops up and starts doing something, eh)
    :param file_name: name of the file with suffix
    fetches the files from the disk and directs the screen data to the decoders
    """
    # init()  # colorama initializer
    # fetching the data from the disk
    if auto_log: print(f"fetching the {file_name} from the disk")
    with open(file_name, "r") as file:
        file = file.read()
    if auto_log: print("fetching successful, invoking the decoding")
    file_name = file_name.strip(".txt")
    p = 0  # stands for pointer
    p += 8
    if file[p] == "a":  # the letter "a" is the second letter in the word "pargf" btw
        p += 6
        if auto_log: print("decoding started( oh boi, here it comes")
        # "natural" decoder
        natural = ""
        p += 1
        while file[p] != "<":
            natural += file[p]
            p += 1
        exec(f"natural = {natural}")
        if auto_log: print("natural decoded")
        # apr_char_num decoder
        p += 8
        apr_char_num = ""  # stands for approximate_size
        while file[p] != "<":
            apr_char_num += file[p]
            p += 1
        apr_char_num = int(apr_char_num)
        if auto_log: print("apr_char_num decoded, invoking the decoder")
        res = pargf_decoder(p, file_name, file.replace(file[0,p], ""), auto_log, False, 1,
                            apr_char_num, natural)  # re means return
    elif file[p] == "r":  # the letter "r" is the second letter in the word "argf" btw
        p += 5
        if auto_log: print("decoding")
        argf_decoder(file, p)
    else:
        # make the compiler
        p += 5
    return res


file_directer("texture.txt", True)
