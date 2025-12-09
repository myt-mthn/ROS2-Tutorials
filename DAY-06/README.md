# ROS2 Tutorials – Day 06

#### ROS2 Parameters – Runtime Configuration for Nodes

This folder contains the complete material for **Day 06** of the ROS2 Tutorials.

**PDF Manuals:**  
- [**M9 – ROS2 Parameters Fundamentals**](M9-Parameters_Fundamentals.pdf)  
- [**M10 – Parameters Implementation**](M10-Parameters_Implementation.pdf)

---

## 📌 What You Will Learn Today

### ✅ Understand ROS2 Parameters
- What ROS2 parameters are  
- Why parameters are used instead of normal variables  
- How parameters enable runtime configurability  
- Parameter workflow: **Declare → Read → Update → Load (YAML)**  

### ✅ Create a Python Parameter Node (`my_py_pkg`)
- Declare parameters inside a node  
- Read parameter values  
- Update parameters dynamically  
- Apply CLI overrides  
- Load parameters from YAML files

### ✅ Create and Use YAML Parameter Files
- Correct ROS2 YAML syntax  
- How to attach a YAML config to a running node  
- Merging: YAML + CLI overrides  

### ✅ Build a Parameter Client Node
- Use service-based parameter APIs  
- Explore parameter backend services:
  - `get_parameters`
  - `set_parameters`
  - `list_parameters`

---

## 🚀 Quick Start

> **Note:** clone the repo root — the day workspaces are inside the repo under `DAY-06/ros2_ws`.

---

### **1. Clone the Repository**
```bash
git clone https://github.com/myt-mthn/ROS2-Tutorials.git
```

---

### **2. Enter the Day-06 Workspace**
```bash
cd ROS2-Tutorials/DAY-06/ros2_ws
```

---

### **3. Build the Package**
```bash
colcon build --packages-select my_py_pkg
source install/setup.bash
```

---

### **4. Run the Parameter Node (default parameters)**
```bash
ros2 run my_py_pkg param_node
```

You will see:
- Declared parameters  
- Printed values in the terminal  

---

### **5. Override Parameter Values from CLI**
```bash
ros2 run my_py_pkg param_node --ros-args -p robot_name:=turtlebot -p speed:=3.5
```

---

### **6. Use a YAML Parameter File**

Example YAML (in `src/my_py_pkg/config/params.yaml`):

```yaml
my_py_pkg:
  ros__parameters:
    speed: 10.0
    robot_name: "my_robot"
    debug: true
```

Run with YAML:
```bash
ros2 run my_py_pkg param_node --ros-args --params-file src/my_py_pkg/config/params.yaml
```

---

### **7. Run the Parameter Node**

Terminal:
```bash
ros2 run my_py_pkg param_node
```

---

Everything is described in detail inside the **Manual 1** and **Manual 2** PDFs.  
Follow them step-by-step for a complete beginner-friendly ROS2 parameter experience.
