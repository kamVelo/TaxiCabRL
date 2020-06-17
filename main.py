import gym
import numpy as np
env = gym.make("Taxi-v3").env

env.s = 328

epochs = 0
penalties, rewards = 0, 0

frames = []
done = False

while not done:

    action = env.action_space.sample()
    state,reward,done,info = env.step(action)
    if reward == -10:
        penalties += 1

    frames.append({
        'frame':env.render(mode="ansi"),
        'state': state,
        'action':action,
        'reward': reward
    })
    epochs += 1
print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalties))

from IPython.display import clear_output
from time import sleep
def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        print(f"Timestep: {i+1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)
print_frames(frames)


