# from turtle import Turtle, Screen, color
# timmy = Turtle()
# my_screen = Screen()
# color("dodger blue")
# timmy.forward(100)
# my_screen.exitonclick()


from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align["Pokemon Name"] = "l"
table.align["Type"] = "l"
print(table)
