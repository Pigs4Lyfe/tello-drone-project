from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()


tello.move_up(180)
tello.move_forward(305)
tello.move_left(305)
tello.move_back(305)
tello.move_right(305)

tello.land()