import play

play.new_image("background.png")

player1 = play.new_image("enterprise.png", x=-320, y=-250, size=20)
player1.speed = 11
player1.score = 0

player2 = play.new_image("klingon.png", x=350, y=-250, size=20)
player2.speed = 7
player2.score = 0

target = play.new_image("earth.png", y=150, size=20)
target.is_game_over = False

message = play.new_text("P1 = 0   P2 = 0", y=-250, font_size=60, color='yellow')


def move_target():
    target.go_to(play.random_position())
    message.words = f"P1 = {player1.score}  P2 = {player2.score}"
    if player1.score == 10:
        message.words = "Player 1 wins!"
        target.is_game_over = True
    if player2.score == 10:
        message.words = "Player 2 wins!"
        target.is_game_over = True


@play.repeat_forever
def do():
    if target.is_game_over:
        return

    if play.key_is_pressed("up"):
        player2.y = player2.y + player2.speed
    if play.key_is_pressed("down"):
        player2.y = player2.y - player2.speed
    if play.key_is_pressed("left"):
        player2.x = player2.x - player2.speed
    if play.key_is_pressed("right"):
        player2.x = player2.x + player2.speed

    if play.key_is_pressed("w"):
        player1.y = player1.y + player1.speed
    if play.key_is_pressed("s"):
        player1.y = player1.y - player1.speed
    if play.key_is_pressed("a"):
        player1.x = player1.x - player1.speed
    if play.key_is_pressed("d"):
        player1.x = player1.x + player1.speed

    if player1.is_touching(target):
        player1.score = player1.score + 1
        move_target()

    if player2.is_touching(target):
        player2.score = player2.score + 1
        move_target()




play.start_program()
