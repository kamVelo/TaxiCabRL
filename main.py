import gym
import numpy as np
env = gym.make("Taxi-v3").env

env.s = 328

epochs = 0
penalties, rewards = 0, 0

frames = []
done = False




