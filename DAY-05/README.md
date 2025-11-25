# ROS2 Tutorials – Day 05

#### ROS2 Actions – Long-Running Tasks with Feedback

This folder contains the complete material for **Day 05** of the ROS2 Tutorials.

**PDF Manuals:**  
- [**M7 – ROS2 Actions Fundamentals**](M7-Actions_Fundamentals.pdf)
- [**M8 – Action Server & Client Implementation**](M8-Actions_Implementation.pdf)
---

## 📌 What You Will Learn Today

### ✅ Understand ROS2 Actions
- Why actions are used instead of services  
- Difference between **topics**, **services**, and **actions**  
- Action communication workflow: **Goal → Feedback → Result**

### ✅ Create a ROS2 Action Interface Package (`action_pkg`)
- Create `.action` files  
- Structure of **Goal / Result / Feedback**  
- Configure `package.xml` for action generation  
- Configure `CMakeLists.txt` with `rosidl_default_generators`

### ✅ Implement a Python Action Server & Client (`my_py_pkg`)
- Initialize an action server  
- Accept and process goals  
- Publish continuous feedback  
- Send final results  
- Write a Python action client to send goals and print feedback

### ✅ Build and Run the Workspace
- Correct build order for interface + Python packages  
- Use `colcon` with package selection  
- How to `source` the workspace  
- How to run both server and client

---

## 🚀 Quick Start    

> **Note:** clone the repo root — the day workspaces are inside the repo under `DAY-05/ros2_ws`.

1. Clone the repository:

```bash
git clone https://github.com/myt-mthn/ROS2-Tutorials.git
```

2. Change into the Day-05 workspace:
```bash
cd ROS2-Tutorials/DAY-05/ros2_ws
```

3. Build the action interface package first:
```bash
colcon build --packages-select action_pkg
source install/setup.bash
```

4. Then build the Python action nodes:
```bash
colcon build --packages-select my_py_pkg
source install/setup.bash
```
5. Run the Action Nodes

Terminal 1 – start the Action Server
```bash
ros2 run my_py_pkg action_server
```

Terminal 2 – start the Action Client
```bash
ros2 run my_py_pkg action_client
```

You should see:

- The client sends a goal
- The server publishes periodic feedback
- The server returns the final result

Everything is described in detail inside the Manual 1 and Manual 2 PDFs.  
Follow the PDFs step-by-step for a complete beginner-friendly ROS2 service experience.
