#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 17:21
# @Author  : yangmingming
# @Site    : 
# @File    : gym_learn.py
# @Software: PyCharm

import gym

# env = gym.make("CartPole-v1")

env = gym.make("CartPole-v0")
observation = env.reset()
for _ in range(10000):
    env.render()
    action = env.action_space.sample()  # your agent here (this takes random actions)
    observation, reward, done, info = env.step(action)

    if done:
        observation = env.reset()
env.close()
