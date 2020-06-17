import gym

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