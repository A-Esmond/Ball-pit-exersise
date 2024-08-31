def ball_pit_volume(ball_pit_radius, ball_pit_height):
  volume1 = 3.14 * ball_pit_radius * ball_pit_radius * ball_pit_height
  return volume1

def ball_volume(ball_radius):
  volume2 = (4/3) * 3.14 * ball_radius * ball_radius * ball_radius
  return volume2

def balls_needed(volume1, volume2):
  balls_needed = (volume1 / volume2) * 0.75
  return balls_needed

ball_pit_radius = int(input("What is the radius of the ball pit? "))
ball_pit_height = int(input("What is the height of the ball pit? "))
pit_volume = ball_pit_volume(ball_pit_radius, ball_pit_height)

ball_radius = int(input("What is the radius of the ball? "))
ball_volume_value = ball_volume(ball_radius)

number_of_balls = balls_needed(pit_volume, ball_volume_value)

print(f"Number of balls needed: {number_of_balls: .0f}")
