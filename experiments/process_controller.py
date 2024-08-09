from sys import thread_info
import multiprocessing



def process_pre_init_setter(offset: int):  # ppis
    """ initializes the Process control unit"""
    process_group = {}
    # thread initialization
    for i in range(multiprocessing.cpu_count() - offset):
        process_group.update({f"{thread_info.name}{i}": "spawned"})
    return process_group

# TODO: şu yukardakş funcu aşağıda alıtır pro cess grupu herkeşle paylaş init yerine bu aşağıdki initi kullan bide json kullan
    
class ProcessControlUnit:
    def __init__(self):
        process_group = process_pre_init_setter()  # still working on it
