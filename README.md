#DSAI3202
#work environment for the Parallel and Distributed Computing course where labs and future work will be submitted.

### Question 1: How the Automated Maze Explorer Works

The automated explorer in this project follows a simple but effective algorithm called the **right-hand rule**. Basically, it acts like someone walking through a maze with their right hand always touching the wall. At every step, it checks if it can turn right, go straight, turn left, or backtrack — in that order. This helps it find the exit without getting lost.

To avoid going in circles, it keeps track of its last three moves. If it notices it’s doing the same move over and over (like turning right three times), it assumes it's stuck in a loop and starts backtracking.

Backtracking is done using a path history. It remembers all the cells it visited, so if it gets stuck, it can go backwards until it finds a new path to try.

At the end of the run, it prints out some useful stats like:
- how long it took,
- how many moves it made,
- how many times it had to backtrack,
- and how fast it was moving (on average).

For example, in one of my runs, the explorer solved the static maze in 1279 moves, didn’t need to backtrack at all, and did it so fast that the timer couldn’t even register the time properly.

Overall, it’s a pretty straightforward algorithm, but it works well for this kind of maze setup.

### Question 2: Running Multiple Explorers in Parallel

To solve this, I created a function that runs one maze explorer on the static maze and returns the results (moves, time, backtracks). Then I used Python’s `multiprocessing` module to run 4 explorers in parallel.

Each explorer solved the same static maze independently, and all of them found the solution in 1279 moves with **no backtracking**. Even though their time values are extremely small (a few milliseconds), this shows that the algorithm is consistent and efficient.

Here’s a table of results:

| Explorer | Moves | Backtracks | Time (s) |
|----------|-------|------------|----------|
| 1        | 1279  | 0          | 0.0025   |
| 2        | 1279  | 0          | 0.0023   |
| 3        | 1279  | 0          | 0.0049   |
| 4        | 1279  | 0          | 0.0022   |

Even though the maze and algorithm are the same, slight timing differences appear due to how multiprocessing schedules each task. All explorers performed equally well in terms of pathfinding.

### Question 3: Comparing Explorer Performance

I ran four explorers in parallel on the same static maze and collected data on how many moves they made, how long they took, and how many times they had to backtrack.

All four explorers performed the same in terms of moves — each of them solved the maze in exactly **1279 moves**, which makes sense since they’re using the same algorithm on the same maze. Interestingly, none of them had to backtrack at all, which shows that the right-hand rule was enough to get them to the end without needing to reverse.

The only small difference I noticed was in the **time taken**. Although they were all super fast (just a few milliseconds), the values weren’t identical. This is probably due to how multiprocessing works — each process gets scheduled differently by the operating system, so timing can vary a little even if everything else is the same.

To better visualize the comparison, I created a set of bar charts showing the number of moves, backtracks, and time for each explorer. Since all the backtracks were zero, I added little "0" labels above the bars to make it clear they completed the maze without reversing.

![image](https://github.com/user-attachments/assets/3ac37621-c542-4149-926d-ea9b61f69ac5)

Overall, the results show that the explorer is consistent and performs really well on the static maze, but there’s still room to test it further — maybe on more complex or random mazes — to see where its limits are.
### Summary Table – Explorer Performance (Static Maze)

| Explorer | Moves | Backtracks | Time (s) |
|----------|-------|------------|----------|
| 1        | 1279  | 0          | 0.0025   |
| 2        | 1279  | 0          | 0.0023   |
| 3        | 1279  | 0          | 0.0049   |
| 4        | 1279  | 0          | 0.0022   |

*All explorers completed the maze with identical path lengths and zero backtracking. Slight time differences are due to parallel processing overhead.*


### Question 4: Enhancing the Maze Explorer

The original maze explorer was using the **right-hand rule**, which is simple and works most of the time, but it’s not very smart. It doesn’t know where the goal is, so it just hugs the wall and keeps moving. That means it can take a really long route, even if the goal is nearby. It also doesn’t have any concept of what an optimal path looks like.

To improve this, I added a new method to the `Explorer` class called `bfs_solve()` that uses **Breadth-First Search (BFS)**. BFS is an algorithm that explores all possible paths level by level and always finds the shortest path in a grid-like maze like ours.

With this enhancement:
- The explorer is now **goal-aware**, meaning it knows where the finish is.
- It doesn’t take any unnecessary turns or loops.
- It finds the **shortest path** with no backtracking.
- It’s much faster and more efficient compared to the original method.

I tested this on the static maze and saw a huge difference. The BFS explorer solved the maze in just **128 moves**, while the original one needed **1279 moves** to reach the goal.

Overall, this change made the explorer much smarter, and it’s a big upgrade over the basic wall-following approach



### Question 5: Comparing the Enhanced Explorer (BFS) to the Original

To compare performance, I ran both the original right-hand rule explorer and the new BFS-based explorer on the same static maze.

Here’s the result:

| Algorithm       | Moves | Backtracks | Time (s) |
|----------------|-------|------------|----------|
| Right-Hand Rule| 1279  | 0          | ~0.00    |
| BFS            | 128   | 0          | 0.0013   |

The difference is clear — BFS found a much shorter path (128 vs 1279 moves). Even though both completed with no backtracking, BFS was more efficient because it actually calculates the shortest path rather than blindly exploring.

#### 🧠 Trade-offs
- The right-hand rule is simple and doesn’t require knowledge of the goal, which can be useful in unknown environments.
- BFS, on the other hand, is goal-aware and optimal, but it needs access to the entire maze structure ahead of time.

In our case, BFS is the clear winner because it’s faster, smarter, and produces a shorter, more direct route to the goal.
