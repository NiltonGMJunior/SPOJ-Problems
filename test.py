#   Nilton G. M. Junior
#   04/12/2018
#   Sphere Online Judgment
#   TEST - Life, the Universe and Everything
#   https://www.spoj.com/problems/TEST/

def main():

    while True:
        try:
            num = input()
        except EOFError:
            break
        if num == '42':
            break
        print(num)

if __name__ == '__main__':
    main()
