#definisi fungsi
def print_info(arg1, *vartuple):
    print("Outpunya adalah : ")
    print(arg1)
    for var in vartuple:
        print(var)

# Pemanggilan fungsi
# Satu argumen
print_info(10)

# Empat argumen
print_info(10, 20, 30, 40)