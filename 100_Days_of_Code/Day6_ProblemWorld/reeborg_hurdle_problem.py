def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif not wall_in_front() and wall_on_right():
        move()
    else:
        turn_right()
        move()