import play

print("Hello Button")

play.new_image("background.png")
inc_button = play.new_image("incrementButton.png", size=30, x=240, y=-140)
dec_button = play.new_image("decrementButton.png", size=30, x=-240, y=-140)
reset_button = play.new_image("resetButton.png", size=30, x=0, y=-140)
message = play.new_text("0", y=100, font_size=300, color="purple")
message.counter = 0

@inc_button.when_clicked
def inc_clicked():
  print("You clicked increment")
  message.counter = message.counter + 1
  message.words = message.counter


@dec_button.when_clicked
def dec_clicked():
  print("You clicked decrement")
  message.counter = message.counter - 1
  message.words = message.counter


@reset_button.when_clicked
def reset_clicked():
  print("You clicked reset")
  message.counter = 0
  message.words = message.counter



play.start_program()