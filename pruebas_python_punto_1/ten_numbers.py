def ten_numbers():
    for i in range(0, 101):
        if i % 2 == 0 and i % 5 == 0:
            print(i, ' buzz bazz')
        elif i % 2 == 0:
            print(i, ' buzz')
        elif i % 5 == 0:
            print(i, ' bazz')
        else:
            print(i)


if __name__ == "__main__":
    ten_numbers()
