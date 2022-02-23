# **motion-planning-net**

This work is based on Motion Planning Neural Network presented in:
https://arxiv.org/abs/1806.05767 \
The goal was to create a Neural Planner for 2D maps.

# **Network structure**

<p align="center">
    <img src="images/network_architecture.png" alt="drawing" width="1000"/>
</p>

The network structure consists of two main parts. An encoder that encodes map images into obstacle space $X_{obs}$ and the planning network itself.\
The encoder is part of an autoencoder network that has been trained to return input images. Later on planning network, which is a simple feedfroward network, uses encoded images, start position and goal positon to predict next state of an agent.\
During online planning, the paths provided by the Planning Network are simplified and checked for validity. If two consecutive states cannot be connected without encountering an object, then the A* planning algorithm is used to plan a new path between these points.

# **Data**

To train the Neural Planner, 100 diferent environments were generated. For each of this environment 4000 diferent starting and goal points were randomly choosen. It gives a total of 400000 path planning problems.

This element is necessary to focus network learning on the path.
Each image has a resolution of 120x120px.

A* algorithm was used for path planning. To minimize the number of turns, special heuristics was implemented.

Unsolved samples:
<p align="center">
    <img src="images/map_sample0.png" alt="drawing" width="240"/>
    <img src="images/map_sample1.png" alt="drawing" width="240"/>
    <img src="images/map_sample2.png" alt="drawing" width="240"/>
    <img src="images/map_sample3.png" alt="drawing" width="240"/>
    <img src="images/map_sample4.png" alt="drawing" width="240"/>
</p>

Solved samples:
<p align="center">
    <img src="images/map_solved_sample0.png" alt="drawing" width="240"/>
    <img src="images/map_solved_sample1.png" alt="drawing" width="240"/>
    <img src="images/map_solved_sample2.png" alt="drawing" width="240"/>
    <img src="images/map_solved_sample3.png" alt="drawing" width="240"/>
    <img src="images/map_solved_sample4.png" alt="drawing" width="240"/>
</p>

# **Code**

To generate a dataset, first you need to generate maps. To do this, run the generate_maps.ipnb file. Then you have to plan training paths. The next step is to plan the paths for the generated maps. To do so run A_star_path_planning.ipnb.\
Last step is to train the network, for this use the motion_planning_network.ipnb file.

# **Results**


