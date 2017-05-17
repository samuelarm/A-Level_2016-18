import random

def test_case(n):
    if n == 1:
        return [0, 1, 2] # No win (+0)
    elif n == 2:
        return [2, 1, 2] # 2 matches (+50)
    elif n == 3:
        return [4, 4, 4] # 3 matches (+100)
    elif n == 4:
        return [3, 5, 5] # 2 skulls (-100)
    elif n == 5:
        return [1, 1, 1] # 3 bells (+500)
    elif n == 6:
        return [5, 5, 5] # 3 skulls (=0)

player_credit = 100 # pence
symbol = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

case = 1 # test case counter

game_is_running = True
while game_is_running:

    print("Credit: £%.2f" % float(player_credit / 100))

    if player_credit < 20:
        print("Not enough credit. Game over!")
        game_is_running = False
        break
    else:
        # get player option
        while True:
            option = input("Bet 20p to (S)pin or (C)ash out: ").upper()
            if option == "S":
                cashed_out = False
                break
            elif option == "C":
                cashed_out = True
                break
        
        if not cashed_out:
            # 20p deducted from player's credit
            player_credit = player_credit - 20
            print("Bet placed (Credit: £%.2f)" % float(player_credit / 100))
            # spin the wheels
            symbol_count = [0 for x in range(6)]
            wheel = [random.randint(0, 5) for i in range(3)] # uncomment to play as normal <<<<<<<<
            # wheel = test_case(case) # uncomment to test
            # case += 1               # uncomment to test
            print("%s - %s - %s" % (symbol[wheel[0]], symbol[wheel[1]], symbol[wheel[2]]))
            # count symbols
            for selection in wheel:
                symbol_count[selection] += 1
            # win / lose conditions
            winning_spin = False
            for i in range(len(symbol_count)):
                if symbol_count[i] == 2: # two of the same
                    if symbol[i] == "Skull":
                        # deduct 100 or cap at zero
                        if player_credit >= 100:
                            print("You lose £1.00!")
                            player_credit -= 100
                        else:
                            print("You lose all your credit!")
                            player_credit = 0
                    else:
                        print("You win 50p!")
                        player_credit += 50
                    winning_spin = True
                    break
                elif symbol_count[i] == 3: # three of the same
                    if symbol[i] == "Skull":
                        print("You lose all your credit!")
                        player_credit = 0
                    elif symbol[i] == "Bell":
                        print("You win £5.00!")
                        player_credit += 500
                    else:
                        print("You win £1.00!")
                        player_credit += 100
                    winning_spin = True
                    break

            if not winning_spin:
                print("No win! :(")

        else:
            print("You cashed out £%.2f. Thank you for playing!" % float(player_credit / 100))
            game_is_running = False