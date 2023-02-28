def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front() and not wall_on_right():
        turn_right()
        move()
    elif not wall_in_front() and wall_on_right():
        move()
    elif front_is_clear():
        move() 
    elif right_is_clear(): 
        turn_right()
        move()
    else:
        turn_left()