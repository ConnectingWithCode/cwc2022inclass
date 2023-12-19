import play

play.new_image("christmas_background.png")

countdown = play.new_text("3", size=400, y=180, color="blue")
countdown.hide()

p1_score = play.new_text("player 1 score: 0", y=180, x=-230, color="blue")
p1_score.value = 0

p2_score = play.new_text("player 2 score: 0", y=180, x=230, color="blue")
p2_score.value = 0

#                  0               1                 2
p1_images = ["p1_frosty.png", "p1_santa.png", "p1_rudolph.png"]
p2_images = ["p2_frosty.png", "p2_santa.png", "p2_rudolph.png"]

FROSTY = 0
SANTA = 1
RUDOLPH = 2


player1 = play.new_image(p1_images[0], size=50, x=-200, y=-50)
player1.costume = 0

player2 = play.new_image(p2_images[0], size=50, x=200, y=-50)
player2.costume = 0



@play.when_any_key_pressed
async def do(key):
    if key == "space":
        player1.hide()
        player2.hide()
        countdown.show()
        await play.timer(seconds=1.0)
        countdown.words = "2"
        await play.timer(seconds=1.0)
        countdown.words = "1"
        await play.timer(seconds=1.0)
        countdown.hide()

        player1.image = p1_images[player1.costume]
        player2.image = p2_images[player2.costume]

        player1.show()
        player2.show()

        if player1.costume == FROSTY and player2.costume == SANTA:
            p1_score.value += 1
        if player1.costume == SANTA and player2.costume == RUDOLPH:
            p1_score.value += 1
        if player1.costume == RUDOLPH and player2.costume == FROSTY:
            p1_score.value += 1

        if player2.costume == FROSTY and player1.costume == SANTA:
            p2_score.value += 1
        if player2.costume == SANTA and player1.costume == RUDOLPH:
            p2_score.value += 1
        if player2.costume == RUDOLPH and player1.costume == FROSTY:
            p2_score.value += 1

        p1_score.words = f"player 1 score: {p1_score.value}"
        p2_score.words = f"player 2 score: {p2_score.value}"


@play.when_any_key_pressed
def do2(key):
    if key == "left":
        player2.costume = 0
    if key == "up":
        player2.costume = 1
    if key == "right":
        player2.costume = 2


    if key == "a":
        player1.costume = 0
    if key == "w":
        player1.costume = 1
    if key == "d":
        player1.costume = 2




play.start_program()
