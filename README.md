# **motion-planning-net**

This work is based on Motion Planning Neural Network presented in:
https://arxiv.org/abs/1806.05767 \
The goal was to create a Neural Planner for 2D maps.

# **Data**

To train the Neural Planner, 100 diferent environments were generated. For each of this environment 4000 diferent starting and goal points were randomly choosen. It gives a total of 400000 path planning problems.

This element is necessary to focus network learning on the path.
Each image has a resolution of 120x120px.

A star algorithm was used for path planning. To minimize the number of turns, special heuristics was implemented.

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

# **Network structure**

<p align="center">
    <img src="images/network_architecture.png" alt="drawing" width="1000"/>
</p>

The network structure consists of two main parts. An encoder that encodes map images in the obstacle space $X_{obs}$ and the planning network itself.\
The encoder is the part of the autoencoder network that was trained to return input images. Then only part of the encoder was used to encode the images.

# **Results**


