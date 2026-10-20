# 🧠 Cognitive & Circadian Digital Twin (Proof-of-Concept)

> **Happiest Health Hackathon Submission**  
> A dynamic, predictive "What-If" physiological simulator modeling the impact of sleep debt, caffeine timing, chronotypes, and screen exposure on afternoon cognitive clarity.

---

## 👤 Participant Details
- **Student Name:** Ayush Chandra
- **Institution:** Graphic Era Hill University
- **Use Case Domain:** Healthcare & Personal Preventative Wellness

---

## 📌 Problem Statement & Strategic Vision
Most health tools act as static logs—they summarize past events without predicting future physiological impacts. 

This **Digital Twin Proof-of-Concept** bridges tracking and actionability by creating a dynamic behavioral feedback loop. Users execute **"What-If" scenario simulations** to optimize caffeine intake, sleep windows, and focus curves in real time, projecting how behavioral adjustments alter 24-hour cognitive energy curves.

---

## ✨ Key Technical Features
- **Dynamic "What-If" Simulator:** Real-time sliders alter caffeine timing, sleep quality, chronotypes, and screen habits to preview energy curves.
- **Side-by-Side Twin Comparison:** Overlays current behavioral predictions against an idealized benchmark twin curve.
- **24-Hour Energy Curve:** Visualizes circadian alertness, sleep debt penalties, and caffeine half-life decay.
- **Deep Sleep Inhibition Index:** Calculates projected sleep disruption caused by late-day stimulant intake.
- **Actionable Optimization Engine:** Automatically generates recommendations based on modeled state shifts.

---

## 🛠️ Technical Stack & AI/ML Architecture

### Core Technologies
- **Language:** Python 3.9+
- **Frontend/UI:** Streamlit (Web Dashboard Framework)
- **Data & Analytics:** NumPy, Pandas
- **Visualization:** Plotly Graph Objects

### Algorithmic Modeling & Mathematical Framework
The Digital Twin engine uses a deterministic heuristic simulation model incorporating:
1. **Circadian Phase Functions:** Modified sinusoidal wave function modeling natural 24-hour body temperature and cortisol fluctuations:
   $$f(t) = 50 + 35 \cdot \sin\left(\frac{(t - 2)\pi}{8}\right) - 10 \cdot \cos\left(\frac{(t - 2)\pi}{4}\right)$$
2. **Pharmacokinetic Decay Model:** First-order exponential decay function simulating caffeine concentration and peak metabolic absorption ($t_{max} \approx 1.5\text{ hrs}$):
   $$C(t) = \left(\frac{\text{Dose}}{2}\right) \cdot \left(\frac{\Delta t}{1.5}\right) \cdot e^{\left(1 - \frac{\Delta t}{1.5}\right)}$$
3. **Adenosine Blockade & Sleep Debt Penalty:** Linear-exponential penalties mapping adenosine accumulation against cumulative sleep deficit ($8.0\text{ hrs} - [\text{Sleep} \times \text{Quality Factor}]$).

---

## 🏗️ System Architecture & Presentation Artifacts

### 1. System Architecture Diagram
- **PDF Version:** [`docs/System_Architecture.pdf`](./docs/System_Architecture.pdf)
- **PPTX Version:** [`docs/System_Architecture.pptx`](./docs/System_Architecture.pptx)

### 2. Project Presentation & Outcomes Deck
- **PDF Version:** [`docs/Project_Presentation.pdf`](./docs/Project_Presentation.pdf)
- **PPTX Version:** [`docs/Project_Presentation.pptx`](./docs/Project_Presentation.pptx)

*(Note: All linked documentation files are configured for open access without requiring additional permissions).*

---

## 📽️ Project Demonstration Video
Watch the demonstration video showcasing real-time parameter tuning and scenario simulations:

[![Watch Demonstration Video](https://img.youtube.com/vi/YOUR_YOUTUBE_VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID)

> **YouTube Video Link:** [https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID](https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID)  
> *(Replace `YOUR_YOUTUBE_VIDEO_ID` with your actual video link ID once uploaded)*

---

## 🚀 Quickstart Guide

### 1. Clone & Setup
```bash
git clone [https://github.com/YOUR_USERNAME/digital-twin-wellness.git](https://github.com/YOUR_USERNAME/digital-twin-wellness.git)
cd digital-twin-wellness