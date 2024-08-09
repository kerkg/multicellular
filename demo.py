#!/usr/bin/python
# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

# Simple demo of changing foreground, background and brightness.


from colorama import init, Fore, Back, Style, just_fix_windows_console
init()
# print(Fore.GREEN + 'green, '
#     + Fore.RED + 'red, '
#     + Fore.RESET + 'normal, '
#     , end='')
# print(Back.GREEN + 'green, '
#     + Back.RED + 'red, '
#     + Back.RESET + 'normal, '
#     , end='')
# print(Style.DIM + 'dim, '
#     + Style.BRIGHT + 'bright, '
#     + Style.NORMAL + 'normal'
#     , end=' ')
just_fix_windows_console()
pack = []
pack_item = input(":")
pack.append(pack_item)
pack_item = input(":")
pack.append(pack_item)
pack_item = input(":")
pack.append(pack_item)
print([item.upper() for item in pack])
exec(f"print(Fore.{pack[0].upper()} + Back.{pack[1].upper()} + Style.{pack[2].upper()} +"
     "\"id:tetra mesher-3>lmb.rnb(target1=mesh_dist, target2=nt7.get_returns())\", end='')")
