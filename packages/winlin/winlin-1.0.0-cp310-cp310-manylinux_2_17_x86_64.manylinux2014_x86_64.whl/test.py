from sys import argv
import winlin


def winlin_test(fname, wid, c1, c2):
    func = getattr(winlin, fname, None)
    if func:
        print(func(wid, c1, c2))
    else:
        print(f'typo? {func=}')
        

if __name__ == '__main__':
    fname = argv[1]
    wid = int(argv[2], 16)
    c1, c2 = int(argv[3]), int(argv[4])
    winlin_test(fname, wid, c1, c2)
    
