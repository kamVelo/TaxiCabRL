import gym
import numpy as np
env = gym.make("Taxi-v3").env

env.s = 328

epochs = 0
penalties, rewards = 0, 0

frames = []
done = False

q_table = np.zeros([env.observation_space.n, env.action_space.n])
from IPython.display import clear_output
import random
from time import sleep


"""training the agent"""
#hyperparamaters:
alpha, gamma, epsilon = 0.1, 0.6, 0.1
all_epochs = []
all_penalties = []
for i in range(1,100001):
    state = env.reset()

    epochs, penalties, reward = 0,0,0
    done = False
    while not done:
        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])
        next_state, reward, done, info = env.step(action)
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])
        new_value = (1-alpha)*old_value + alpha*(reward + gamma * next_max)
        if reward == -10:
            penalties += 1
        state = next_state
        epochs += 1

    if i % 100 == 0:
        clear_output(wait=True)
        print(f"Episode: {i}")

print("Training Finished. \n")

"""evaluate agent's performance after Q-Learning"""
total_epochs, total_penalties = 0, 0
episodes = 100
for _ in range(episodes):
    state=env.reset()
    epochs, penalties, rewards = 0, 0, 0

    done = False
    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

        if reward == -10:
            penalties += 1

        epochs += 1

    total_penalties += penalties
    total_epochs += epochs

print(f"Results after {episodes} episodes")
print(f"Average timesteps per episode: {total_epochs / episodes}")
print(f"Average penalties per episode: {total_penalties / episodes}")

