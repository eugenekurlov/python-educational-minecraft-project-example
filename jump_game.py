from mcpi.minecraft import Minecraft
import mcpi.block as block
import random
import keyboard
import time
from datetime import datetime
import database as db


def game():
    isGame = True
    mc = Minecraft.create()
    score = 0

    multiple_game_results = []
    initial_position = mc.player.getTilePos()
    y = initial_position.y - 1

    press_key_number = 0
    x_previous, y_previous, z_previous = 0, 0, 0
    while score < 15:
        position = mc.player.getTilePos()
        if position.y < y:
            finish = datetime.now()
            date = finish.strftime('%Y-%m-%d %H:%M:%S')
            try:
                total_time = finish - start
            except NameError:
                mc.postToChat("You are far away from start height level. Run the game again")
                break
            multiple_game_results.append((date, score, total_time))

            air_block = block.AIR.id
            mc.setBlock(x_previous, y_previous, z_previous, air_block)
            mc.postToChat("You fall. If you want to try again, press 'y', otherwise press 'n'")

            if keyboard.read_key() == 'y':
                mc.postToChat("Nice, you should return to the level place")
                timer = 15
                for _ in range(4):
                    if mc.player.getTilePos().y == initial_position.y:
                        y = mc.player.getTilePos().y - 1
                        press_key_number = 0
                        score = 0
                        break
                    else:
                        mc.postToChat(f"you have {timer} sec till the game end")
                        time.sleep(5)
                        timer -= 5
                else:
                    mc.postToChat("You have ran out of time. Game over.")
                    break
            elif keyboard.read_key() == 'n':
                mc.postToChat("See you next time!")
                break
            else:
                mc.postToChat("Press another key")
                if press_key_number == 4:
                    mc.postToChat("Sorry, you've pressed wrong keys too many times, game over!")
                    break
                else:
                    press_key_number += 1

        z = round(position.z)

        # press 'r' button to create a block
        if keyboard.is_pressed('r'):
            if isGame:
                start = datetime.now()
                isGame = False
            x0 = round(position.x - 2)
            x1 = round(position.x + 2)

            x = random.randint(x0, x1)
            y += 1
            z += random.choice((1, -1))

            my_block = block.GOLD_BLOCK.id
            mc.setBlock(x, y, z, my_block)

            if score > 0:
                time.sleep(2)
                air_block = block.AIR.id
                mc.setBlock(x_previous, y_previous, z_previous, air_block)

            x_previous, y_previous, z_previous = x, y, z
            keyboard.wait('r')
            score += 1
            mc.postToChat("Level up. Current score is %d" % score)

    else:
        mc.postToChat("You win! Your score = " + str(score))
        finish = datetime.now()
        date = finish.strftime('%Y-%m-%d %H:%M:%S')
        total_time = finish - start
        multiple_game_results.append((date, score, total_time))

        air_block = block.AIR.id
        mc.setBlock(x_previous, y_previous, z_previous, air_block)

    return multiple_game_results


if __name__ == '__main__':
    game = game()
    file_name = "records_table.csv"
    path_to_file = db.os.getcwd() + f"\\{file_name}"
    flag = db.check_file(path_to_file)
    if flag:
        df = db.load_table(file_name)
        db.write_to_table(file_name, df, game)
    else:
        db.create_table(file_name)
