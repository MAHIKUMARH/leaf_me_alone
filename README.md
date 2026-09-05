<img width="1342" height="882" alt="image" src="https://github.com/user-attachments/assets/45c8e3a6-6259-4f9c-8374-4c678ddff97f" /># LEAF ME ALONE 🌿🎯

## Basic Details

### Team Name: THE UNDEAD


### Team Members

* Team Lead: **ARJUN V PILLAI** - JAIN UNIVERSITY
* Member 2: **MAHIKUMAR H** - JAIN UNIVERSITY

### Project Description

**LEAF ME ALONE** is a fun web application that analyzes uploaded leaf images and counts their visible veins using classical computer vision. Users can collect leaves, track their best vein count, compete on a leaderboard, and unlock rarity levels based on their leaf's vein count.

### The Problem (that doesn't exist)

Nobody knows **which leaf is the most veiny**.

People have been picking up random leaves for centuries without asking the most important question:

> **"Bro... how many veins does this thing have?"** 🌿

### The Solution (that nobody asked for)

We built **LEAF ME ALONE**, because apparently counting leaf veins manually wasn't useless enough.

Upload a leaf → OpenCV processes it → veins are detected → the system counts them → you get a rarity level → your score goes onto the leaderboard.

Because every leaf deserves to know how unnecessarily special it is. 🌿🔥

---

## Technical Details

### Technologies/Components Used

### For Software:

* **Python**
* **Flask**
* **OpenCV**
* **NumPy**
* **scikit-image**
* **SQLite**
* **HTML/CSS**
* **Gunicorn**
* **Git & GitHub**
* **Render** for deployment
* **VS Code** for development

### For Hardware:

* **Not applicable**
* This project is completely software-based.

---

## Implementation

### For Software:

### Installation

Clone the repository:

```bash
git clone https://github.com/MAHIKUMARH/leaf_me_alone.git
cd leaf_me_alone
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Run

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

### Live Demo

[LEAF ME ALONE — Live Website]((https://leaf-me-alone.onrender.com/login))

---

# Project Documentation

## Software

### Screenshots

<img width="1913" height="896" alt="image" src="https://github.com/user-attachments/assets/081a317c-8985-4c9d-9606-a1665dff51f7" />


*Homepage where users enter their name, upload a leaf image, and access the leaderboard and dashboard.*

[![Uploading image.png…]
](Add result page screenshot here)

*Result page showing the uploaded leaf, detected veins, vein count, and rarity classification.*

![<img width="1472" height="975" alt="image" src="https://github.com/user-attachments/assets/85ed1828-5800-4b41-a647-bdf222bd66ab" />
](Add dashboard screenshot here)

*Personal dashboard showing the user's collected leaves, total veins, best leaf, and highest rarity.*

---

# Diagrams

![Workflow](Add workflow/architecture diagram here)

*Workflow of LEAF ME ALONE: leaf image upload → image preprocessing → leaf segmentation → vein enhancement → skeletonization and branch detection → vein count → rarity classification → database → dashboard and leaderboard.*

### Processing Pipeline

```text
Leaf Image
     ↓
Image Upload
     ↓
OpenCV Processing
     ↓
Leaf Segmentation
     ↓
CLAHE Enhancement
     ↓
Black-Hat Vein Extraction
     ↓
Thresholding
     ↓
Skeletonization
     ↓
Branch Detection
     ↓
Vein Count
     ↓
Rarity Classification
     ↓
SQLite Database
     ↓
Dashboard + Leaderboard
```

---

## For Hardware

### Schematic & Circuit

**Not applicable — LEAF ME ALONE is a software-only project.**

### Build Photos

**Not applicable — no physical hardware or circuit was used.**

---

# Project Demo

## Video

[Add your demo video link here]

*The demo shows the complete workflow of LEAF ME ALONE: uploading a leaf, detecting its veins, displaying the vein count and rarity, saving the leaf to the collection, and viewing the dashboard and leaderboard.*

## Additional Demos

**Live website:**
[LEAF ME ALONE](https://leaf-me-alone.onrender.com/login)

**GitHub Repository:**
[LEAF ME ALONE — GitHub Repository](https://github.com/MAHIKUMARH/leaf_me_alone?utm_source=chatgpt.com)

---

# Team Contributions

* **ARJUN V PILLAI:** Classical computer vision pipeline, leaf segmentation, vein detection, image-processing experimentation, testing, and debugging.
* **MAHIKUMAR H:** Flask web application, SQLite database, frontend UI, dashboard, leaf collection, leaderboard, rarity system, deployment, and project integration.

---

## Rarity System 🌿

|    Vein Count | Rarity       |
| ------------: | ------------ |
|           0–5 | ✨ DIVINE     |
|         6–499 | 🌱 BASE      |
|     500–1,999 | 🍃 COMMON    |
|   2,000–4,999 | 💎 RARE      |
|   5,000–9,999 | ⚡ EPIC       |
| 10,000–14,999 | 🔥 LEGENDARY |
|       15,000+ | 👑 MYTHIC    |

---

## Why Classical Computer Vision?

Instead of using a trained AI model, LEAF ME ALONE uses **traditional image-processing techniques**. This keeps the project lightweight, explainable, and suitable for running without a large training dataset.

The main techniques include:

* Leaf segmentation
* CLAHE contrast enhancement
* Morphological black-hat transformation
* Thresholding
* Skeletonization
* Branch/node detection
* Connected-component analysis

---

Made with ❤️ at **TinkerHub Useless Projects**

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000\&link=https%3A%2F%2Fwww.tinkerhub.org%2F)

![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)


# [Project Name] 🎯


## Basic Details
### Team Name: [Name]


### Team Members
- Team Lead: [Name] - [College]
- Member 2: [Name] - [College]
- Member 3: [Name] - [College]

### Project Description
[2-3 lines about what your project does]

### The Problem (that doesn't exist)
[What ridiculous problem are you solving?]

### The Solution (that nobody asked for)
[How are you solving it? Keep it fun!]

## Technical Details
### Technologies/Components Used
For Software:
- [Languages used]
- [Frameworks used]
- [Libraries used]
- [Tools used]

For Hardware:
- [List main components]
- [List specifications]
- [List tools required]

### Implementation
For Software:
# Installation
[commands]

# Run
[commands]

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Name 1]: [Specific contributions]
- [Name 2]: [Specific contributions]
- [Name 3]: [Specific contributions]

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



>>>>>>> 69311fd79051eb09e3b7ab1c8ad147682aabe197
