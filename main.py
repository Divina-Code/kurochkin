def test():
    it = 0
    gess_code = True

    if it == 4:
        bot.send_message(id, "You finish the game!")
    else:
        if gess_code == True:
            code = str(rid(100, 999))
            bot.send_message(id, f"Right number: {code}")

        rnum = 0
        rplace = 0
        bot.send_message(id, "Enter secret code")
        inp = message.text

        if len(inp) != 3:
            bot.send_message(id, "This nmber isn`t three letter")
            gess_code = False
        elif not inp.isdigit():
            bot.send_message(id, "This isn`t number")
            gess_code = False

        elif inp == code:
            bot.send_message(id, "You right gess number!")
            gess_code = True
            it += 1
        else:
            for g in inp:
                if g in code:
                    rnum += 1
            for er in range(3):
                if inp[er] == code[er]:
                    rplace += 1
            bot.send_message(id, f"You right gess {rnum} numbers and {rplace} places of numbers!")
            gess_code = False
