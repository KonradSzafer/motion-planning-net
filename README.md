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
During online path planning paths delivered by the path planning network are simplified and checked for being valid. If you can't connect two consecutive states without hittting an object then A* replanning algorithm is used for planning a new path between those points.

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

To generate dataset first thing you have to do is to generate maps and paths. In order to do this you have to run generate_maps.ipnb file. There you have to specify proper paths for saving data and number of maps and paths you want to genreate for each map. Then you have to plan training paths. For doing so run A_star_path_planning.ipnb. One again you have to set proper paths for reading maps and writing .json files with saved paths./
Last step is to train the network. Evrything you have to know is contained within motion_planning_network.ipnb file.

# **Results**


