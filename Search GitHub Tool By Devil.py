import webbrowser

def signin():
   input('Press Enter To Open Page....')
   webbrowser.open('https://github.com/login')
   i()


def signup():
   input('Press Enter To Open Page....')
   webbrowser.open('https://github.com/join?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home')
   i()
def aco():
    z = input('Enter Your UserName : ')
    webbrowser.open('https://github.com/'+z)
    i()

def ex():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/explore')
    i()

def pull():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/pulls')
    i()

def luss():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/issues')
    i()

def mark():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/marketplace')
    i()

def ser():
    l = input('Search Or Jump To : ')
    webbrowser.open('https://github.com/search?q=' + l)
    i()

def tool():
    x = input("the owner's name : ")
    z = input('Name post : ')
    webbrowser.open('https://github.com/' + x + '/' + z)
    i()

def res():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/new')
    i()

def ora():
    input('Press Enter To open Page....')
    webbrowser.open('https://github.com/organizations/plan')
    i()

def top():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/topics')
    i()

def trend():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/trending')
    i()

def coll():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/collections')
    i()

def ev():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/events')
    i()

def spo():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/sponsors/community')
    i()

def te():
    input('Press Enter To Open Page....')
    webbrowser.open('https://github.com/team')


def i():
    print('''
1 = Search
2 = Sign In
3 = Sign Up
4 = Profile
5 = New Repositoriy
6 = Search Repositoriy
7 = Explore
8 = Pull Requests
9 = Issues
10 = Marketplace
11 = Organization
12 = Topics
13 = Trending
14 = Collections
15 = Events
16 = Git Sponsors
17 = Team''')
    x = int(input('Choose : '))
    if x == 1:
        ser()
    elif x == 2:
        signin()
    elif x == 3:
        signup()
    elif x == 4:
        aco()
    elif x == 5:
        res()
    elif x == 6:
        tool()
    elif x == 7:
        ex()
    elif x == 8:
        pull()
    elif x == 9:
        luss()
    elif x == 10:
        mark()
    elif x == 11:
        ora()
    elif x == 12:
        top()
    elif x == 13:
        trend()
    elif x == 14:
        coll()
    elif x == 15:
        ev()
    elif x == 16:
        spo()
    elif x == 17:
        te()
    else:
        print(' You Did Choose')





print('''
programming by Devil
Snap : pz_a9
IG : qq.hk''')
print('')
print('Search GitHub Tool :)')

i()