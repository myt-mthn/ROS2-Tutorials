# ROS2 Tutorials – Day 04

This folder contains the material for **Day 04** of the ROS2 Tutorials.

📄 **Read the full Day-04 Manuals (PDFs):**  
- [Manual 1 – Services Fundamentals & Setup](M5-Services_Fundamentals.pdf)  
- [Manual 2 – Step-by-Step Code & Execution](M6-Services_Implementation.pdf)

---

Day 04 focuses on **ROS2 Services** – creating, understanding, and using service servers and clients.  
By the end of this session, you will be able to:

### ✅ Understand ROS2 Services  
- Difference between topics and services  
- Synchronous request/response communication  

### ✅ Create a ROS2 Interface Package (`service_pkg`)  
- Define `.srv` files  
- Understand `CMakeLists.txt` for services  
- Configure `package.xml` for service generation  

### ✅ Create a Python Node Package (`my_py_pkg`)  
- Write a service server node  
- Write a service client node  
- Import `.srv` interfaces from another package  

### ✅ Build and Run the Workspace  
- Correct build order for interface and Python packages  
- Source the workspace and run nodes  

### ✅ Test Services  
- Send requests from client and receive responses  
- Debug common service issues  
- Understand server/client logging  

---

### 💡 Quick Start

To run and test the ROS2 services for Day 04:

1. Clone the repository:

```bash
git clone https://github.com/myt-mthn/ROS2-Tutorials.git
```
2. Navigate to the Day 04 workspace:

```bash
cd ROS2-Tutorials/DAY-04/ros2_ws
```

3. Build the interface package first:

```bash
colcon build --packages-select service_pkg
source install/setup.bash
```

4. Then build the Python node package:

```bash
colcon build --packages-select my_py_pkg
source install/setup.bash
```

5. Open two terminals:

  Terminal 1 – run server:
```bash
ros2 run my_py_pkg srv_server
```

  Terminal 2 – run client:
```bash
ros2 run my_py_pkg srv_client
```
---    

Everything is described in detail inside the **Manual 1** and **Manual 2** PDFs.  
Follow the PDFs step-by-step for a complete beginner-friendly ROS2 service experience.    

---
