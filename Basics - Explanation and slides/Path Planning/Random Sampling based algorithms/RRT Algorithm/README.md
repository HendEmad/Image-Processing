# Algorithm logic:
- The main idea is based on tree which is a graph where each node has only one parent. 
- It starts with a parent at the start node then it grows till reaching the destination.

# Steps:
1. start_node = tree_parent
2. random sample generation 
3. if generated sample is located in the free space & the direct line of the closest node in the tree doesn't cross any obstacles:
    * Take a step from the tree to the sample using a predefined step size and connect the sample node to the parent of the tree.
4. if not: 
    * choose the next closest node from the tree and repeat the check again.
5. if the sample node == destination node:
    * break(terminate the algorithm)

# Tree simulation
![image](https://user-images.githubusercontent.com/91827137/184045844-0cb82335-619e-4c99-a705-7cd69328cf4b.png)

# Tree representation
![image](https://user-images.githubusercontent.com/91827137/184046711-44c624b5-008f-4c04-9519-ea83b3f8d047.png)
