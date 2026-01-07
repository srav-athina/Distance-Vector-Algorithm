# Distance Vector Routing Algorithm 📡

![Status](https://img.shields.io/badge/Status-Archived-red)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Course](https://img.shields.io/badge/Course-Computer_Networks-green)

> **Note:** This project is archived and serves as a reference implementation of the Bellman-Ford routing algorithm for distributed network systems.

## 📖 Overview
This project implements the **Distance Vector Routing Algorithm** (based on the **Bellman-Ford** equation). It simulates how routers in a network dynamically discover the shortest paths to all other nodes by exchanging routing tables with their immediate neighbors.

The simulation handles:
* **Route Discovery:** Nodes initialize with direct neighbor costs and iteratively update paths.
* **Dynamic Updates:** Convergence to optimal paths through iterative vector exchange.
* **Infinity Handling:** Logic to handle unreachable nodes or broken links (simulated).

## 🧠 Algorithm Details
The core logic relies on the Bellman-Ford equation:
$$D_x(y) = \min_v \{ c(x,v) + D_v(y) \}$$
Where:
* $D_x(y)$ is the cost of the least-cost path from node $x$ to $y$.
* $c(x,v)$ is the link cost from $x$ to neighbor $v$.
* $D_v(y)$ is the cost from neighbor $v$ to $y$.

## 📂 Project Structure
* `dv.py`: Contains the core `Node` and `Router` classes that implement the routing logic and table updates.
* `dv_test.py`: A test suite that sets up various network topologies to verify convergence and correctness.

## 🚀 Usage

### Prerequisites
* Python 3.x

### Running the Simulation
You can run the test suite to see the algorithm in action across different network topologies:

```bash
# Clone the repository
git clone [https://github.com/srav-athina/Distance-Vector-Algorithm.git](https://github.com/srav-athina/Distance-Vector-Algorithm.git)

# Navigate to directory
cd Distance-Vector-Algorithm

# Run the test suite
python dv_test.py
