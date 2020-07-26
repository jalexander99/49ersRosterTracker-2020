import sys

class Players():
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
    def __repr__(self):
        return self.name + ' | ' + self.position + ' | ' + self.number


#Players by Jersey Number/Jersey Number Grabber

Players.playersFor1 = Players('Shawn Poindexter', 'WR', '#1')
Players.playersFor2 = 'There is currently nobody wearing #2 on the 49ers.'
Players.playersFor3 = Players('CJ Beathard', '3rd String QB', '#3')
Players.playersFor4 = Players('Nick Mullens', 'Backup QB', '#4')
Players.playersFor5 = 'There is currently nobody wearing #5 on the 49ers.'
Players.playersFor6 = Players('Mitch Wishnowsky', 'Punter', '#6')
Players.playersFor7 = Players('Chris Finke', 'Practice Squad WR', '#7')
Players.playersFor8 = 'There is currently nobody wearing #8 on the 49ers.'
Players.playersFor9 = Players('Robbie Gould', 'FG Kicker', '#9')
Players.playersFor10 = Players('Jimmy Garoppolo', 'Starting QB', '#10')
Players.playersFor11 = Players('Brandon Aiyuk', 'WR/PR', '#11')
Players.playersFor12 = 'There is currently nobody wearing #12 on the 49ers.'
Players.playersFor13 = Players('Richie James', 'WR/PR', '#13')
Players.playersFor14 = Players('Chris Thompson', 'Practice Squad WR', '#14')
Players.playersFor15 = Players('Trent Taylor', 'WR', '#15')
Players.playersFor16 = 'There is currently nobody wearing #16 on the 49ers.'
Players.playersFor17 = Players('Jalen Hurd', 'WR', '#17')
Players.playersFor18 = Players('Dante Pettis', 'WR', '#18')
Players.playersFor19 = Players('Deebo Samuel', 'WR', '#19')
Players.playersFor20 = Players('Jimmie Ward', 'FS', '#20')
Players.playersFor21 = 'There is currently nobody wearing #21 on the 49ers.'
Players.playersFor22 = Players('Jason Verrett', 'CB', '#22')
Players.playersFor23 = Players('Ahkello Witherspoon', 'CB', '#23')
Players.playersFor24 = Players("K'Waun Williams", 'Slot/Nickel CB', '#24')
Players.playersFor25 = Players('Richard Sherman', 'CB', '#25')
Players.playersFor26 = Players('Tevin Coleman', 'RB', '#26')
Players.playersFor27 = 'There is currently nobody wearing #27 on the 49ers.'
Players.playersFor28 = Players('Jerrick McKinnon', 'RB', '#28')
Players.playersFor29 = Players('Jaquaski Tartt', 'SS', '#29')
Players.playersFor30 = Players('Jeff Wilson Jr.', 'RB', '#30')
Players.playersFor31 = Players('Raheem Mostert', 'RB', '#31')
Players.playersFor32 = Players('DJ Reed', 'CB', '#32')
Players.playersFor33 = Players('Tarvarius Moore', 'S', '#33')
Players.playersFor34 = 'There is currently nobody wearing #34 on the 49ers.'
Players.playersFor35 = Players('Tim Harris', 'Practice Squad CB', '#35')
Players.playersFor36 = Players('Marcell Harris', 'FS', '#36')
Players.playersFor37 = 'There is currently nobody wearing #37 on the 49ers.'
Players.playersFor38 = Players('Jamycal Hasty', 'Practice Squad RB', '#38')
Players.playersFor39 = 'There is currently nobody wearing #39 on the 49ers.'
Players.playersFor40 = 'There is currently nobody wearing #40 on the 49ers.'
Players.playersFor41 = Players('Emmanuel Moseley', 'CB', '#41')
Players.playersFor42 = 'There is currently nobody wearing #42 on the 49ers.'
Players.playersFor43 = Players('Daniel Helm', 'Practice Squad TE', '#43')
Players.playersFor44 = Players('Kyle Juszczyk', 'FB', '#44')
Players.playersFor45 = 'There is currently nobody wearing #45 on the 49ers.'
Players.playersFor46 = 'There is currently nobody wearing #47 on the 49ers.'
Players.playersFor47 = 'There is currently nobody wearing #47 on the 49ers.'
Players.playersFor48 = 'There is currently nobody wearing #48 on the 49ers.'
Players.playersFor49 = Players('DeMarkus Acy', 'CB', '#49')
Players.playersFor50 = 'There is currently nobody wearing #50 on the 49ers.'
Players.playersFor51 = Players('Azeez Al-Shaair', 'ROLB', '#51')
Players.playersFor52 = 'There is currently nobody wearing #52 on the 49ers.'
Players.playersFor53 = Players('Mark Nzeocha', 'LB', '#53')
Players.playersFor54 = Players('Fred Warner', 'MLB', '#54')
Players.playersFor55 = Players('Dee Ford', 'LE', '#55')
Players.playersFor56 = Players('Kwon Alexander', 'LOLB', '#56')
Players.playersFor57 = Players('Dre Greenlaw', 'ROLB', '#57')
Players.playersFor58 = Players('Weston Richburg', 'C', '#58')
Players.playersFor59 = Players('Joe Walker', 'MLB', '#59')
Players.playersFor60 = Players('Daniel Brunskill', 'OL/RG', '#60')
Players.playersFor61 = 'There is currently nobody wearing #61 on the 49ers.'
Players.playersFor62 = 'There is currently nobody wearing #62 on the 49ers.'
Players.playersFor63 = 'There is currently nobody wearing #63 on the 49ers.'
Players.playersFor64 = 'There is currently nobody wearing #64 on the 49ers.'
Players.playersFor65 = 'There is currently nobody wearing #65 on the 49ers.'
Players.playersFor66 = Players('Tom Compton', 'OL/RG', '#66')
Players.playersFor67 = Players('Justin Skule', 'OL/T', '#67')
Players.playersFor68 = Players('Colton McKivitz', 'OL/RG', '#68')
Players.playersFor69 = Players('Mike McGlinchey', 'RT', '#69')
Players.playersFor70 = 'There is currently nobody wearing #70 on the 49ers.'
Players.playersFor71 = Players('Trent Williams', 'LT', '#71')
Players.playersFor72 = 'There is currently nobody wearing #72 on the 49ers.'
Players.playersFor73 = 'There is currently nobody wearing #73 on the 49ers.'
Players.playersFor74 = 'There is currently nobody wearing #74 on the 49ers.'
Players.playersFor75 = Players('Laken Tomlinson', 'LG', '#75')
Players.playersFor76 = 'There is currently nobody wearing #76 on the 49ers.'
Players.playersFor77 = Players('Julian Taylor', 'DT', '#77')
Players.playersFor78 = Players('Shon Coleman', 'OL/LT', '#78')
Players.playersFor79 = 'There is currently nobody wearing #79 on the 49ers.'
Players.playersFor80 = 'There is currently nobody wearing #80 on the 49ers.'
Players.playersFor81 = Players('Jauan Jennings', 'WR', '#81')
Players.playersFor82 = Players('Ross Dwelley', 'TE', '#82')
Players.playersFor83 = 'There is currently nobody wearing #83 on the 49ers.'
Players.playersFor84 = Players('Kendrick Bourne', 'WR', '#84')
Players.playersFor85 = Players('George Kittle', 'TE', '#85')
Players.playersFor86 = Players('Kyle Nelson', 'LS/TE', '#86')
Players.playersFor87 = 'There is currently nobody wearing #87 on the 49ers.'
Players.playersFor88 = 'There is currently nobody wearing #88 on the 49ers.'
Players.playersFor89 = Players('Charlie Woerner', 'TE', '#89')
Players.playersFor90 = Players('Kevin Givens', 'DT', '#90')
Players.playersFor91 = Players('Arik Armstead', 'DT', '#91')
Players.playersFor92 = Players('Kerry Hyder', 'DE', '#92')
Players.playersFor93 = Players('DJ Jones', 'DT', '#93')
Players.playersFor94 = Players('Solomon Thomas', 'DT', '#94')
Players.playersFor95 = Players('Kentavius Street', 'DT', '#96')
Players.playersFor96 = 'There is currently nobody wearing #96 on the 49ers.'
Players.playersFor97 = Players('Nick Bosa', 'RE', '#97')
Players.playersFor98 = Players('Ronald Blair', 'DE', '#98')
Players.playersFor99 = Players('Javon Kinlaw', 'DT', '#99')




class PlayersByPosition:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
    def __repr__(self):
        return self.name + ' | ' + self.position + ' | ' + self.number


#Players by Position/Depth Chart

PlayersByPosition.QB = [Players.playersFor10, Players.playersFor4, Players.playersFor3]
PlayersByPosition.RB = [Players.playersFor31, Players.playersFor26, Players.playersFor28, Players.playersFor30, Players.playersFor38]
PlayersByPosition.FB = [Players.playersFor44]
PlayersByPosition.TE = [Players.playersFor85, Players.playersFor82, Players.playersFor89]
PlayersByPosition.WR = [Players.playersFor19, Players.playersFor11, Players.playersFor84, Players.playersFor17, Players.playersFor18, Players.playersFor13, Players.playersFor81, Players.playersFor15, Players.playersFor7, Players.playersFor1]
PlayersByPosition.LT = [Players.playersFor71, Players.playersFor78, Players.playersFor67]
PlayersByPosition.LG = [Players.playersFor75]
PlayersByPosition.C = [Players.playersFor58]
PlayersByPosition.RG = [Players.playersFor60, Players.playersFor66, Players.playersFor68]
PlayersByPosition.RT = [Players.playersFor69, Players.playersFor67]
PlayersByPosition.RE = [Players.playersFor97, Players.playersFor55, Players.playersFor98, Players.playersFor92]
PlayersByPosition.DT = [Players.playersFor91, Players.playersFor99, Players.playersFor94, Players.playersFor93, Players.playersFor90, Players.playersFor77, Players.playersFor95]
PlayersByPosition.LE = [Players.playersFor55, Players.playersFor97, Players.playersFor98]
PlayersByPosition.LB = [Players.playersFor54, Players.playersFor56, Players.playersFor57, Players.playersFor51, Players.playersFor53, Players.playersFor59]
PlayersByPosition.CB = [Players.playersFor25, Players.playersFor24, Players.playersFor41, Players.playersFor23, Players.playersFor32, Players.playersFor22, Players.playersFor49, Players.playersFor35]
PlayersByPosition.FS = [Players.playersFor20, Players.playersFor33]
PlayersByPosition.SS = [Players.playersFor29, Players.playersFor36]
PlayersByPosition.K = [Players.playersFor9]
PlayersByPosition.P = [Players.playersFor6]
PlayersByPosition.LS = [Players.playersFor86]
PlayersByPosition.KR = [Players.playersFor13]
PlayersByPosition.PR = [Players.playersFor13, Players.playersFor11, Players.playersFor18]


#Start of Program

def mainMenu():
    x = input('Type "1" to use the 49ers Depth Chart, "2" for the 49ers Jersey Number Grabber, or "QUIT" to close the program: ').upper()
    if x == 'QUIT':
        sys.exit()

    elif int(x) == 1:
        print('Welcome to the 49ers Depth Chart Tracker! Type "EXIT" to go back to the main menu.')

        while True:
            z = input("Please choose a position group ('QB, RB, FB, TE, WR, LT, LG, C, RG, RT, RE, DT, LE, LB, CB, FS, SS, K, P, KR, PR, LS') to display: ").upper()
            if z == 'QB':
                print(PlayersByPosition.QB)
            elif z == 'RB':
                print(PlayersByPosition.RB)
            elif z == 'FB':
                print(PlayersByPosition.FB)
            elif z == 'TE':
                print(PlayersByPosition.TE)
            elif z == 'WR':
                print(PlayersByPosition.WR)
            elif z == 'LT':
                print(PlayersByPosition.LT)
            elif z == 'LG':
                print(PlayersByPosition.LG)
            elif z == 'C':
                print(PlayersByPosition.C)
            elif z == 'RG':
                print(PlayersByPosition.RG)
            elif z == 'RT':
                print(PlayersByPosition.RT)
            elif z == 'RE':
                print(PlayersByPosition.RE)
            elif z == 'DT':
                print(PlayersByPosition.DT)
            elif z == 'LE':
                print(PlayersByPosition.LE)
            elif z == 'LB':
                print(PlayersByPosition.LB)
            elif z == 'CB':
                print(PlayersByPosition.CB)
            elif z == 'FS':
                print(PlayersByPosition.FS)
            elif z == 'SS':
                print(PlayersByPosition.SS)
            elif z == 'K':
                print(PlayersByPosition.K)
            elif z == 'P':
                print(PlayersByPosition.P)
            elif z == 'KR':
                print(PlayersByPosition.KR)
            elif z == 'PR':
                print(PlayersByPosition.PR)
            elif z == 'LS':
                print(PlayersByPosition.LS)
            elif z == 'EXIT':
                mainMenu()

    elif int(x) == 2:
        print("Welcome to the 49ers Jersey Number Grabber! Type 'EXIT' to go back to the main menu.")
        while True:
            jersNumber = input("Choose a jersey number between 1-99 to see who on the San Francisco 49ers is currently wearing that number: ")
            try:
                if int(jersNumber) < 1:
                    print("Please choose a number higher than 0:")
                elif int(jersNumber) > 99:
                    print("Please choose a number lower than 100:")


                if int(jersNumber) == 1:
                    print(Players.playersFor1)
                elif int(jersNumber) == 2:
                    print(Players.playersFor2)
                elif int(jersNumber) == 3:
                    print(Players.playersFor3)
                elif int(jersNumber) == 4:
                    print(Players.playersFor4)
                elif int(jersNumber) == 5:
                    print(Players.playersFor5)
                elif int(jersNumber) == 6:
                    print(Players.playersFor6)
                elif int(jersNumber) == 7:
                    print(Players.playersFor7)
                elif int(jersNumber) == 8:
                    print(Players.playersFor8)
                elif int(jersNumber) == 9:
                    print(Players.playersFor9)
                elif int(jersNumber) == 10:
                    print(Players.playersFor10)
                elif int(jersNumber) == 11:
                    print(Players.playersFor11)
                elif int(jersNumber) == 12:
                    print(Players.playersFor12)
                elif int(jersNumber) == 13:
                    print(Players.playersFor13)
                elif int(jersNumber) == 14:
                    print(Players.playersFor14)
                elif int(jersNumber) == 15:
                    print(Players.playersFor15)
                elif int(jersNumber) == 16:
                    print(Players.playersFor16)
                elif int(jersNumber) == 17:
                    print(Players.playersFor17)
                elif int(jersNumber) == 18:
                    print(Players.playersFor18)
                elif int(jersNumber) == 19:
                    print(Players.playersFor19)
                elif int(jersNumber) == 20:
                    print(Players.playersFor20)
                elif int(jersNumber) == 21:
                    print(Players.playersFor21)
                elif int(jersNumber) == 22:
                    print(Players.playersFor22)
                elif int(jersNumber) == 23:
                    print(Players.playersFor23)
                elif int(jersNumber) == 24:
                    print(Players.playersFor24)
                elif int(jersNumber) == 25:
                    print(Players.playersFor25)
                elif int(jersNumber) == 26:
                    print(Players.playersFor26)
                elif int(jersNumber) == 27:
                    print(Players.playersFor27)
                elif int(jersNumber) == 28:
                    print(Players.playersFor28)
                elif int(jersNumber) == 29:
                    print(Players.playersFor30)
                elif int(jersNumber) == 30:
                    print(Players.playersFor30)
                elif int(jersNumber) == 31:
                    print(Players.playersFor31)
                elif int(jersNumber) == 32:
                    print(Players.playersFor32)
                elif int(jersNumber) == 33:
                    print(Players.playersFor33)
                elif int(jersNumber) == 34:
                    print(Players.playersFor34)
                elif int(jersNumber) == 35:
                    print(Players.playersFor35)
                elif int(jersNumber) == 36:
                    print(Players.playersFor36)
                elif int(jersNumber) == 37:
                    print(Players.playersFor37)
                elif int(jersNumber) == 38:
                    print(Players.playersFor38)
                elif int(jersNumber) == 39:
                    print(Players.playersFor39)
                elif int(jersNumber) == 40:
                    print(Players.playersFor40)
                elif int(jersNumber) == 41:
                    print(Players.playersFor41)
                elif int(jersNumber) == 42:
                    print(Players.playersFor42)
                elif int(jersNumber) == 43:
                    print(Players.playersFor43)
                elif int(jersNumber) == 44:
                    print(Players.playersFor44)
                elif int(jersNumber) == 45:
                    print(Players.playersFor45)
                elif int(jersNumber) == 46:
                    print(Players.playersFor46)
                elif int(jersNumber) == 47:
                    print(Players.playersFor47)
                elif int(jersNumber) == 48:
                    print(Players.playersFor48)
                elif int(jersNumber) == 49:
                    print(Players.playersFor49)
                elif int(jersNumber) == 50:
                    print(Players.playersFor50)
                elif int(jersNumber) == 51:
                    print(Players.playersFor51)
                elif int(jersNumber) == 52:
                    print(Players.playersFor52)
                elif int(jersNumber) == 53:
                    print(Players.playersFor53)
                elif int(jersNumber) == 54:
                    print(Players.playersFor54)
                elif int(jersNumber) == 55:
                    print(Players.playersFor55)
                elif int(jersNumber) == 56:
                    print(Players.playersFor56)
                elif int(jersNumber) == 57:
                    print(Players.playersFor57)
                elif int(jersNumber) == 58:
                    print(Players.playersFor58)
                elif int(jersNumber) == 59:
                    print(Players.playersFor59)
                elif int(jersNumber) == 60:
                    print(Players.playersFor60)
                elif int(jersNumber) == 61:
                    print(Players.playersFor61)
                elif int(jersNumber) == 62:
                    print(Players.playersFor62)
                elif int(jersNumber) == 63:
                    print(Players.playersFor63)
                elif int(jersNumber) == 64:
                    print(Players.playersFor64)
                elif int(jersNumber) == 65:
                    print(Players.playersFor65)
                elif int(jersNumber) == 66:
                    print(Players.playersFor66)
                elif int(jersNumber) == 67:
                    print(Players.playersFor67)
                elif int(jersNumber) == 68:
                    print(Players.playersFor68)
                elif int(jersNumber) == 69:
                    print(Players.playersFor69)
                elif int(jersNumber) == 70:
                    print(Players.playersFor70)
                elif int(jersNumber) == 71:
                    print(Players.playersFor71)
                elif int(jersNumber) == 72:
                    print(Players.playersFor72)
                elif int(jersNumber) == 73:
                    print(Players.playersFor73)
                elif int(jersNumber) == 74:
                    print(Players.playersFor74)
                elif int(jersNumber) == 75:
                    print(Players.playersFor75)
                elif int(jersNumber) == 76:
                    print(Players.playersFor76)
                elif int(jersNumber) == 77:
                    print(Players.playersFor77)
                elif int(jersNumber) == 78:
                    print(Players.playersFor78)
                elif int(jersNumber) == 79:
                    print(Players.playersFor79)
                elif int(jersNumber) == 80:
                    print(Players.playersFor80)
                elif int(jersNumber) == 81:
                    print(Players.playersFor81)
                elif int(jersNumber) == 82:
                    print(Players.playersFor82)
                elif int(jersNumber) == 83:
                    print(Players.playersFor83)
                elif int(jersNumber) == 84:
                    print(Players.playersFor84)
                elif int(jersNumber) == 85:
                    print(Players.playersFor85)
                elif int(jersNumber) == 86:
                    print(Players.playersFor86)
                elif int(jersNumber) == 87:
                    print(Players.playersFor87)
                elif int(jersNumber) == 88:
                    print(Players.playersFor88)
                elif int(jersNumber) == 89:
                    print(Players.playersFor89)
                elif int(jersNumber) == 90:
                    print(Players.playersFor90)
                elif int(jersNumber) == 91:
                    print(Players.playersFor91)
                elif int(jersNumber) == 92:
                    print(Players.playersFor92)
                elif int(jersNumber) == 93:
                    print(Players.playersFor93)
                elif int(jersNumber) == 94:
                    print(Players.playersFor94)
                elif int(jersNumber) == 95:
                    print(Players.playersFor95)
                elif int(jersNumber) == 96:
                    print(Players.playersFor96)
                elif int(jersNumber) == 97:
                    print(Players.playersFor97)
                elif int(jersNumber) == 98:
                    print(Players.playersFor98)
                elif int(jersNumber) == 99:
                    print(Players.playersFor99)

            except ValueError:
                if jersNumber == 'EXIT':
                    mainMenu()


print("Welcome to the 2020 San Francisco 49ers Roster Tracker!")
print("Here you can keep up-to-date with the 49ers by accessing the real-time updated roster of the 49ers as well as use the integrated 49ers Jersey Number Grabber.")
mainMenu()












