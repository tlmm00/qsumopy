import gym
from gym import spaces
from qsimpy import QTask, QNode, Broker, Dataset
import numpy as np
import random

class QuantumEnv(gym.Env):
    def __init__(self):
        super(QuantumEnv, self).__init__()
        self.action_space = spaces.Discrete(2)  # Example: 0 = Node 1, 1 = Node 2
        self.observation_space = spaces.Box(low=0, high=1, shape=(2,), dtype=np.float32)
        self.broker = Broker(env=self)
        self.nodes = [QNode(self, name='Quantum Node 1'), QNode(self, name='Quantum Node 2')]
        for node in self.nodes:
            self.broker.add_node(node)
        self.current_task = None

    def reset(self):
        self.current_task = self.generate_task()
        return self.get_observation()

    def generate_task(self):
        return QTask(name='Task', arrival_time=random.randint(1, 3))

    def get_observation(self):
        # Example observation: node utilization
        return np.array([self.nodes[0].utilization, self.nodes[1].utilization])

    def step(self, action):
        if action == 0:
            self.broker.allocate_task(self.current_task, self.nodes[0])
        else:
            self.broker.allocate_task(self.current_task, self.nodes[1])
        
        reward = self.calculate_reward()
        done = True  # End after one task for simplicity
        return self.get_observation(), reward, done, {}

    def calculate_reward(self):
        # Simple reward function based on task completion
        return 1  # Reward for completing a task

# Set up the Gymnasium environment
env = QuantumEnv()

# Example of running the environment
obs = env.reset()
for _ in range(5):  # Run for 5 steps
    action = env.action_space.sample()  # Random action
    obs, reward, done, _ = env.step(action)
    print(f"Observation: {obs}, Reward: {reward}")
