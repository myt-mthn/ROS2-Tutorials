# ROS2 Tutorials – Day 05
## ROS2 Actions – Long-Running Tasks with Feedback

This folder contains the complete material for **Day 05** of the ROS2 Tutorials.

**PDF Manuals:**  
- **M7 – ROS2 Actions Fundamentals** (`M7-Actions_Fundamentals.pdf`)  
- **M8 – Action Server & Client Implementation** (`M8-Actions_Implementation.pdf`)

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

## 📂 Project Structure Provided

The repository already contains a `ros2_ws` folder including the action interface and python nodes:

