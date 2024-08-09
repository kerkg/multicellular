
def index_error_overrider(actual_lenght: int, index: int) -> int:
    """wraps around when index is too big"""
    if index < actual_lenght: return index
    else: return (actual_lenght % index)-1  # -1 because indexes start at 0
    # for example if you want to grab the 11. index from a string that has a length of 10, youd have to grab the 0.index
