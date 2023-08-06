# Reinforcement Learning Optical Networks Simulator for Open Artificial Inteligent Agents Framework

**RL-ONS-OAIAF** is a Python Framework that you can configurate a Network Enviroment for training Agents.

This framework use the Simulator "Flex Net Sim" [Git-Lab] https://gitlab.com/DaniloBorquez/flex-net-sim


[[_TOC_]]

## Features

- Load Agents with OpenAI
- Create your own Optical Network Enviroment
- Configurate your own reward, done, state and info functions
- Configurate many parameters:
	- Start training
	- Determinate the Step function
	- Determinate the Reset function
- Elastic optical networks support
- Support for different bitrates through a JSON file
- Support for different networks through a JSON file
- Support for multiple routes through a JSON file
- Customize connection arrive/departure ratios
- Support to create your own statistics
- Customize the number of connection arrives that you want to simulate

## Download

Download the latest release from the [release list](https://gitlab.com/IRO-Team/que-dificil). 

If you want to try the actual developed version (a little bit updated, but coul be unstable), you can clone this repository through the git clone command.

```
git clone git@gitlab.com:IRO-Team/que-dificil.git
```

## Pre-Installation

### Nvidia requirements:
+ Max Versión of Nvidia CUDA Toolkit September 2018

### Windows requirements:
+ Install Microsoft Visual Build Tool 2019 or above
+ You must add two environment variables in Windows
+ MPILib C:\Program Files (x86)\Microsoft SDKs\MPI\Lib
+ MPI C:\Program Files (x86)\Microsoft SDKs\MPI
+ Install [MDI Versión 10.0] (https://www.microsoft.com/en-us/download/details.aspx?id=57467)

### Version requirements:
+ Python = [3.7.11] (https://www.python.org/downloads/release/python-3711/)
+ Stable-Baselines = [SB3] (https://stable-baselines.readthedocs.io/en/master/guide/install.html)
	+ pip install stable-baselines3[extra]
+ Tensor-flow = 1.15.0
	+ pip install tensorflow==1.15.0
	+ pip install tensorflow-gpu==1.15
+ Downgrade Protobuf = 3.20.0 
	+ pip install --upgrade protobuf==3.20.0
+ Downgrade Gym = 0.21.0
	+ pip install gym==0.21.0
+ pip install mpi4py (For this step, you need the Windows requirements complete installed)


## Installation

For installation you need download the last release or clone the git code and the pre-installation all completed.

Go to the root folder put in your console "pip install"


## Using  Framework
 
- The Framework load an Optical Network Environment which one can training Agents with Reinforcement Learning. 
- You can use this Framework how a Application or flexible help code for training Agents in Optical Networks.
- You can see the example folder that contains examples files.
- In this examples can you modify the agent, parameters, hiperparameters, network, and more.
- If you want more, can modify one o more functions, how: function reward, function action, function state, function done, function info.

# Simple Example

For use the framework package [pip](https://pip.pypa.io/en/stable/) to install que-dificil.

```bash
pip install que-dificil
```

## Reward Function
For example, the most popular reward function is if that the connection has not allocated, then you get -1, else get 1.
```python
def reward():
    value = env.getSimulator().lastConnectionIsAllocated()
    if (value.name == Controller.Status.Not_Allocated.name):
        value = -1
    else:
        value = 1
    return value
```


## Load Enviroment

```python
import os
import gym
from simNetGymPy import *
import que-dificl

# Get local path's
absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)

#Create the que-dificil Enviroment
env = gym.make("rlonenv-v0")

#Set the reward function
env.setRewardFunc(reward)

#Load the simulator statements and the allocator function 'first_fit_algorithm'
env.initEnviroment(fileDirectory + "/NSFNet.json", fileDirectory + "/NSFNet_routes.json")
env.getSimulator()._goalConnections = 10000
env.getSimulator().setAllocator(first_fit_algorithm)
env.getSimulator().init()

#Start the simulator with goal connections times and without Agent interaction
env.start()
#Load the PPO2 Agent
model = PPO2(MlpPolicy, env, verbose=False)
#Start training in the simulator with 100 interation more, but with Agent interaction
model.learn(total_timesteps=100)
```

## Allocator function

The allocator function is the most important function for use correctly this framework. This function is called every time when one connection want to start the connection.

The function receive from the enviroment seven parameters:
 
- src: The ID from the source node.
- dst: The ID from the destiny node.
- b: The random BitRate assigned by the Simulator.
- c: Connection Object
- n: Network Object
- path: Array list that contain the possible routes of the Connection.
- action: Answer from Agent 

In this example the Agent take the decesion which route (path) must be used for assign the connection in the network.

```python
def first_fit_algorithm(src: int, dst: int, b: BitRate, c: Connection, n: Network, path, action):
    numberOfSlots = b.getNumberofSlots(0)
    actionSpace = len(path[src][dst])

    if action is not None:
        if action == actionSpace:
            action = action - 1
        link_ids = path[src][dst][action]
    else:
        link_ids = path[src][dst][0]
    general_link = []
    for _ in range(n.getLink(0).getSlots()):
        general_link.append(False)
    for link in link_ids:
        link = n.getLink(link._id)
        for slot in range(link.getSlots()):
            general_link[slot] = general_link[slot] or link.getSlot(
                slot)
    currentNumberSlots = 0
    currentSlotIndex = 0
    
    for j in range(len(general_link)):
        if not general_link[j]:
            currentNumberSlots += 1
        else:
            currentNumberSlots = 0
            currentSlotIndex = j + 1
        if currentNumberSlots == numberOfSlots:
            for k in link_ids:
                c.addLink(
                    k, fromSlot=currentSlotIndex, toSlot=currentSlotIndex+currentNumberSlots)
            return Controller.Status.Allocated, c
    return Controller.Status.Not_Allocated, c
```
## Documentation



## Thanks

I really appreciate the help of the following people:
- [Gonzalo España](https://gitlab.com/GonzaloEspana)
- [Erick Viera]
- [Juan Pablo Sanchez]