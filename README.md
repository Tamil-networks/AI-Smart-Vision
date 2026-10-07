👁️ AI Smart Vision

AI Smart Vision is a wearable assistive system designed to help visually impaired users understand their surroundings through AI-based visual processing, distance sensing, voice interaction, and audio feedback.

The system uses an NVIDIA Jetson Orin Nano (8GB) as the central processing unit. A 120-degree wide-angle camera and HC-SR04 distance sensor provide environmental information, while a MEMS microphone enables audio input. The processed information is delivered to the user through Bluetooth earbuds.

🎯 Objective

The objective of AI Smart Vision is to develop a wearable AI-assisted system that can process information from the user's surroundings and communicate useful information through audio.

The system combines:

Computer vision
Object detection
Text recognition
Distance sensing
Voice processing
AI-based decision making
Audio feedback
✨ Key Features
👁️ Object Detection

The system uses YOLOv8 for object detection.

The camera captures the surrounding environment and sends the visual information to the Jetson Orin Nano for AI processing.

🔤 Text Recognition

PaddleOCR is used for text recognition from the camera input.

This allows the system to process visible text and convert it into information that can be communicated to the user.

📏 Distance Detection

An HC-SR04 distance sensor provides distance information about nearby objects.

🎙️ Voice Input

A MEMS microphone provides audio input to the system for voice processing.

🧠 AI Decision Engine

The Jetson Orin Nano contains an AI decision engine that combines information from the different input systems and determines the appropriate response.

🔊 Voice Output

Processed information is communicated to the user through Bluetooth earbuds.

🏗️ System Architecture

The core system architecture is:

             120° Wide-Angle Camera
                       │
                       ▼
                ┌───────────────┐
                │               │
                │ NVIDIA Jetson │
                │ Orin Nano 8GB │
                │               │
                │ • YOLOv8      │
                │ • PaddleOCR   │
                │ • Voice       │
                │   Processing  │
                │ • AI Decision │
                │   Engine      │
                │               │
                └───────┬───────┘
                        │
                        ▼
                 Bluetooth Earbuds
                     Audio Out


       HC-SR04 ────────────┐
                            │
       MEMS Microphone ─────┤
                            ▼
                     Jetson Orin Nano

The uploaded block diagram shows the camera and HC-SR04 distance sensor connected to the Jetson Orin Nano, with the MEMS microphone providing AudioIn and Bluetooth earbuds providing AudioOut.

🔋 Power Management System

The wearable system includes a dedicated power management section.

The block diagram specifies:

Rechargeable Li-Ion battery pack
Battery Management System
DC-DC buck converter
Power switch

The power path is:

Rechargeable Li-Ion Battery Pack
              │
              ▼
    Battery Management System
              │
              ▼
       DC-DC Buck Converter
          (12V → 5V)
              │
              ▼
         Power Switch
              │
              ▼
     NVIDIA Jetson Orin Nano

The block diagram specifies the DC-DC buck converter as providing a stable 12V-to-5V output.

🔧 Hardware Components
Component	Purpose
NVIDIA Jetson Orin Nano 8GB	Main AI processing unit
120° Wide-Angle Camera	Captures the surrounding visual environment
HC-SR04 Distance Sensor	Provides distance information
MEMS Microphone	Audio input
Bluetooth Earbuds	Audio output
Rechargeable Li-Ion Battery Pack	Portable power source
Battery Management System	Battery/power management
DC-DC Buck Converter	Provides regulated power
Power Switch	Controls system power

These components and their relationships are represented in the uploaded system block diagram.

🧠 AI Processing

The Jetson Orin Nano acts as the central processing platform.

The block diagram identifies four main processing functions:

YOLOv8

Used for object detection from camera input.

PaddleOCR

Used for text recognition from visual input.

Voice Processing

Processes audio input from the MEMS microphone.

AI Decision Engine

Combines the processed information to determine the system's response.

🔄 System Workflow
Environment
     │
     ▼
120° Wide-Angle Camera
     │
     ▼
YOLOv8 Object Detection
     │
     ├──────────────┐
     │              │
     ▼              ▼
PaddleOCR       AI Processing
     │              │
     └──────┬───────┘
            │
            ▼
      AI Decision Engine
            │
            ▼
      Voice Processing
            │
            ▼
      Bluetooth Earbuds
            │
            ▼
          User

Distance information from the HC-SR04 and voice input from the MEMS microphone are also provided to the Jetson Orin Nano.

🖼️ Block Diagram

The complete hardware and processing architecture is shown below.

🛠️ Technology Stack
AI / Machine Learning
YOLOv8
PaddleOCR
AI Decision Engine
Hardware Computing
NVIDIA Jetson Orin Nano 8GB
Sensors & Input
120° Wide-Angle Camera
HC-SR04 Distance Sensor
MEMS Microphone
Output
Bluetooth Earbuds
Power
Rechargeable Li-Ion Battery Pack
Battery Management System
DC-DC Buck Converter
Power Switch
📂 Suggested Repository Structure
ai-smart-vision/
│
├── README.md
│
├── hardware/
│   ├── block_diagram.png
│   └── hardware_details.md
│
├── ai/
│   ├── yolo/
│   ├── paddleocr/
│   └── decision_engine/
│
├── audio/
│   ├── input/
│   └── output/
│
├── sensors/
│   └── hc_sr04/
│
├── power/
│   └── power_management.md
│
├── software/
│   └── ...
│
├── screenshots/
│   └── ...
│
└── LICENSE

Adjust this structure to match your actual project files before publishing.

🚀 Getting Started

The exact installation procedure depends on the software implementation running on the Jetson Orin Nano.

A typical development workflow is:

1. Set up NVIDIA Jetson Orin Nano
              ↓
2. Connect camera and sensors
              ↓
3. Configure AI environment
              ↓
4. Install YOLOv8
              ↓
5. Install PaddleOCR
              ↓
6. Configure voice processing
              ↓
7. Configure AI decision engine
              ↓
8. Connect Bluetooth audio output
              ↓
9. Test the complete system
📸 Project Images

Add actual project photographs and demonstrations to the repository.

Recommended structure:

screenshots/
├── prototype.jpg
├── camera.jpg
├── jetson.jpg
├── wearable.jpg
├── object-detection.jpg
└── text-recognition.jpg

Then display them in the README:

![AI Smart Vision Prototype](screenshots/prototype.jpg)
🔮 Future Development

Possible future development areas include:

Custom YOLOv8 model training
Improved object recognition
Improved text recognition
Better distance awareness
Natural voice interaction
More intelligent AI decision making
Improved wearable hardware design
Lower power consumption
Smaller hardware enclosure
Additional environmental understanding
📊 Project Status

Status: Completed / Prototype Development

AI Smart Vision combines AI, computer vision, embedded computing, sensors, audio processing, and wearable hardware into a single assistive technology platform.

👨‍💻 Developer

Tamilselvan

Software Developer

⭐ Project

If you find AI Smart Vision interesting, consider giving the repository a ⭐ on GitHub.
