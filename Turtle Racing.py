import random
import os
from time import sleep
import turtle

clear = lambda: os.system('cls')

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "yellow", "cyan", "orange", "black", "purple", "pink", "brown"]

def get_num_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers you want (2 - 10): ")

        try:
            racers = int(racers)
        except ValueError:
            print("Please enter a number.")
            sleep(2)
            clear()
            continue

        if 2 <= racers <= 10:
            clear()
            return racers
        else:
            print("Please enter a number between 2 and 10.")
            sleep(2)
            clear()

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance) # makes it move by a random number between 1 and 20

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)], turtles

def create_turtles(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors): # enumerate: it gives the index and value. Example: ["red", "green"], the first iteration is going to look like i = 0, color = ["red"] 
        racer = turtle.Turtle() # makes the turtle
        racer.color(color)
        racer.shape("turtle")
        racer.left(90) # makes the look up because they start looking left
        racer.penup() # makes it so they dont draw a line while moving to their position by making them not draw
        racer.setpos(-WIDTH//2 + (i + 1) * spacingX, -HEIGHT//2 + 20) # makes them start from the very left then adding by spacingX each new turlte and making them start 20 pixels off the ground
        racer.pendown()
        turtles.append(racer) # adds the racer to the list

    return turtles

def setup_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

def main():
    racers = get_num_of_racers()
    setup_turtle()

    random.shuffle(COLORS) # shuffles the list
    colors = COLORS[:racers] # [1, 2, 3, 4][:2] -> [1, 2] (gets the first 2 of the list or the number after the ":")

    winner, turtles = race(colors)
    print(f"The color {winner} won the race!")
    sleep(3)
    clear()

    for i in turtles:
        i.clear()
        i.ht()
        del i
    
    again()

def again():
    clear()
    playAgain = input("Would you like to play again (y/n)? ")
    playAgain.lower()

    if playAgain == "y":
        clear()
        main()
    elif playAgain == "n":
        exit()
    else:
        print("The options were y (yes) or n (no)")
        sleep(2)
        clear()
        again()

main()