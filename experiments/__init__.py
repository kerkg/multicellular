# TODO: do the initilazer but first do the other coponents
import default_logger_configuration_for_logging as dlcl
from process_controller import init
from decoders import print_with_style
from os import environ
from platform import freedesktop_os_release, win32_ver, mac_ver


try:
    USER = f"{environ.get('USERNAME')}@{freedesktop_os_release()['PRETTY_NAME']}"
except OSError:
    USER = f"{environ.get('USERNAME')}@{win32_ver()}"
except Exception:
    USER = f"{environ.get('USERNAME')}@{mac_ver()}"
except Exception:  # maybe its nil of those
    USER = f"{environ.get('USERNAME')}@god-knows-os(pronounced god knows so its funny)"


logger = dlcl.default_logger_configuration_for_logging("eyes")  # since it watches the entire goddamn thing
#  also yes this is supposed to be global so don't make it local

try:
    init()
except Exception as e:
    logger.Critical(f"an error have acquired while initializing process_controller,  {e}")
    print_with_style("an error have acquired, please see logs for more details, and feel free to change stuff "
                 "but I dont take any responsibility if you break even more stuff(feel free to ask to our discord tho)")


# TODO: do the rest and the worms
