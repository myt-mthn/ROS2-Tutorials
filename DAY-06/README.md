# ROS2 Tutorials – Day 06: Parameters

This repository contains materials for **Day 06 – Parameters** of the ROS2 Tutorials series.  
Here you will find **four manuals** covering parameters in ROS 2, and a **workspace for quick testing** of the implementation examples.

The manuals guide you from basic understanding to practical implementation using Python nodes.

---

> Note: The `ros2_ws` workspace included under `DAY-06/` corresponds to **Manual 2**, enabling quick build and run of the example

---

## 📄 Manuals

| Manual | Description |
|--------|-------------|
| **Manual 1** | Parameter Fundamentals |
| **Manual 2** | Parameter Implementation (Publishing a Number) |
| **Manual 3** | Parameter Callback (Dynamic Updates) |
| **Manual 4** | Parameters Using YAML |
> All manuals are in PDF format. Download and follow them in sequence for best understanding. :contentReference[oaicite:2]{index=2}

---

## 🚀 Quick Start – Run the Example Workspace (Manual 2)

### 1. Open a new terminal  
Navigate into the example workspace:

```bash
cd DAY-06/ros2_ws
```
2. Build the workspace
```bash
colcon build
```
3. Source the workspace
```bash
source install/setup.bash
```
▶ Manual 2 Example – Publish a Number Parameter
Run the basic parameter node

```bash
ros2 run param_pkg param_node
```
The node should log the current value of the parameter and publish it continuously.

View the published topic
In a separate terminal (source the workspace first):

```bash
ros2 topic echo /number
```
Change the parameter dynamically
Open another terminal and run:

```bash
ros2 param set /number_param_node number_param 99
```
The running node from the first terminal should show the updated value immediately.  


## 🧠 Notes  

Manuals 1, 3, and 4 contain step-by-step explanations and code walkthroughs — refer them for detailed instructions.

Manual 2 includes a ready workspace so you can build and test immediately without creating a package from scratch.

Launch file usage will be covered in later days; here we focus on command-line and YAML parameter usage.

