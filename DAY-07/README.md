# Day 07 – ROS 2 Launch Files

## 📌 What Is Day 07 About?

**Day 07 focuses on ROS 2 Launch Files**, which are used to start and manage **multiple ROS 2 nodes using a single command**.

Instead of running each node manually in separate terminals, this day introduces how to:
- Start a complete ROS 2 system at once
- Control node execution centrally
- Prepare robot applications for real-world usage

This is a **critical milestone** because real robots and production systems are *never launched node-by-node manually*.

---

## 📘 Full Manual (Detailed Explanation)

The complete step-by-step explanation for Day 07 is available here:

🔗 **Day 07 – Launch Files Manual**  
[Launch Files - Manual](M13 - Launch Files.pdf)

> Refer to the manual for:
> - Launch file fundamentals  
> - Python launch file structure  
> - Parameter passing  
> - CLI verification  
> - Real robot startup workflows  

This README is intentionally kept **execution-focused**.

---

This directory provides a **ready-made ROS 2 workspace (`ros2_ws`)** for quick testing and learning.

---

## 📌 What We Covered (Day 07)

In this day, we worked with:

- ROS 2 Python launch files (`.launch.py`)
- Launching **multiple nodes with one command**
- Publisher–Subscriber execution via launch files
- Passing **parameters through launch files**
- Verifying running systems using **ROS 2 CLI**
- Understanding how launch files integrate with:
  - `setup.py`
  - `colcon build`

---

## 🚀 Quick Start (Using the Provided `ros2_ws`)

### 1️⃣ Go to the workspace
```bash
cd DAY-07/ros2_ws
```
2️⃣ Build
```bash
colcon build
```
3️⃣ Source the environment
```bash
source install/setup.bash
```
4️⃣ Launch the system
```bash
ros2 launch launch_demo_pkg launch.py
```
🔍 Verification (Optional)
```bash
ros2 node list
ros2 topic list
```
➡️ Next Step
Once this launch setup runs successfully, proceed to Day 08, where the system will be extended further.
