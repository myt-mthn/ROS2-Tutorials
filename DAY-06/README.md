# ROS2 Tutorials – Day 06

#### ROS2 Parameters – Runtime Configuration for Nodes

This folder contains the complete material for **Day 06** of the ROS2 Tutorials.

**PDF Manuals:**  
- [**M9 – ROS2 Parameters Fundamentals**](M9-Parameters_Fundamentals.pdf)  
- [**M10 – Parameters Implementation**](M10-Parameters_Implementation.pdf)
- [**M11 – Parameters Implementation with Callback**](M11-Parameters_Implementation-withCallback.pdf)

---

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
colcon build --packages-select param_pkg
source install/setup.bash
```

---

### **4. Run the Parameter Node (default parameters)**
```bash
ros2 run param_pkg param_node
```

You will see:
- Declared parameters  
- Printed values in the terminal  

---

### **5. Override Parameter Values from CLI**
```bash
ros2 run param_pkg param_node --ros-args -p number_paaram:=45
```

---

### **6. Use a YAML Parameter File**

Example YAML (in `src/param_pkg/config/params.yaml`):

```yaml
param_pkg:
  ros__parameters:
    number_param:54
```

Run with YAML:
```bash
ros2 run param_pkg param_node --ros-args --params-file src/param_pkg/config/params.yaml
```

---

### **7. Run the Parameter Node**

Terminal:
```bash
ros2 run param_pkg param_node
```

---

Everything is described in detail inside the **Manual 1**, **Manual 2** and **Manual 3** PDFs.  
Follow them step-by-step for a complete beginner-friendly ROS2 parameter experience.
