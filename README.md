<<<<<<< HEAD
LEAF ME ALONE 🌿🎯

Basic Details

Team Name: THE UNDEAD

Team Members

Team Lead: ARJUN V PILLAI - JAIN UNIVERSITY

Member: MAHIKUMAR H - JAIN UNIVERSITY

Project Description

LEAF ME ALONE is a computer-vision-based web application that analyzes uploaded leaf images and estimates the number of visible vein structures. The result is stored in a database and turned into a fun, game-like experience with rarity levels, a personal dashboard, leaf collection, and leaderboard.

Basically, we made botany competitive for absolutely no reason. 🌿🏆

The Problem (that doesn't exist)

People have leaves.

People have no idea how many veins their leaves have.

And, more importantly, nobody knows which leaf is the most powerful leaf.

This is clearly a crisis.

The Solution (that nobody asked for)

Upload a leaf → let OpenCV stare at it professionally → extract vein-like structures → count them → assign a rarity → save the result → put it on a leaderboard.

Now your leaf has stats, rarity, and a competitive ranking.

You're welcome. 🌿💀

Technical Details

Technologies/Components Used

For Software:

Languages used:

Python

HTML

CSS

SQL

Frameworks used:

Flask

Libraries used:

OpenCV

NumPy

scikit-image

Database:

SQLite

Tools used:

VS Code / Code Editor

Python Virtual Environment

Git & GitHub

Web Browser

For Hardware:

No dedicated hardware is required.

The project runs on a standard computer/laptop with:

CPU

RAM

Storage

Camera or existing leaf images

Internet browser

No fancy sensors.

The leaf does all the suffering. 🌿

Implementation

For Software:

The project uses a classical computer-vision pipeline instead of a trained machine-learning model.

Image Processing Pipeline

Leaf Image
     ↓
Image Upload
     ↓
OpenCV Image Reading
     ↓
Leaf / Background Isolation
     ↓
CLAHE Enhancement
     ↓
Morphological Processing
     ↓
Vein Extraction
     ↓
Thresholding
     ↓
Skeletonization
     ↓
Branch / Vein Analysis
     ↓
Vein Count
     ↓
Visualization

1. Image Upload

The user enters their name and uploads a leaf image through the Flask web interface.

2. Leaf Segmentation

The system attempts to isolate the leaf from its background to reduce false detections.

3. CLAHE Enhancement

CLAHE (Contrast Limited Adaptive Histogram Equalization) improves local contrast and helps make subtle vein-like structures more visible.

4. Vein Extraction

Morphological operations, including black-hat filtering, are used to highlight darker vein-like structures within the leaf.

5. Thresholding

The processed image is converted into a representation where likely vein structures can be separated from the surrounding leaf.

6. Skeletonization

Detected vein regions are skeletonized into thin centerlines for easier structural analysis.

7. Branch Analysis

The skeleton is analyzed for meaningful branches and connected structures, while small fragments are filtered to reduce noise.

8. Result Visualization

The detected structures are highlighted and saved as a separate image. The application displays the original leaf, detected-vein visualization, vein count, and rarity.

Installation

Clone the repository:

git clone https://github.com/MAHIKUMARH/leaf_me_alone.git
cd leaf_me_alone

Create a virtual environment:

python -m venv venv

Activate it on Windows PowerShell:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install flask opencv-python numpy scikit-image

Run

Start the Flask application:

python app.py

Open:



Project Documentation

Project Structure

LEAF_ME_ALONE/
│
├── app.py
├── database.db
│
├── detector/
│   └── vein_counter.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── leaves.html
│   └── dashboard.html
│
└── static/
    ├── style.css
    └── uploads/

app.py

Handles Flask routes, image uploads, computer-vision execution, SQLite operations, dashboard, leaderboard, and leaf deletion.

detector/vein_counter.py

Contains the computer-vision logic for leaf masking, CLAHE enhancement, vein extraction, skeletonization, branch analysis, vein counting, and visualization.

templates/

Contains the Flask/Jinja pages:

index.html → Home/upload page

result.html → Analysis result

leaves.html → Collection and leaderboard

dashboard.html → Personal dashboard

static/

Contains CSS styling, uploaded leaf images, and generated vein visualizations.

Screenshots (Add at least 3)

Replace these paths with your actual screenshot filenames.



Home page where the user enters their name, uploads a leaf, and views the leaderboard.



Analysis result showing the original leaf, detected vein visualization, vein count, and rarity.



Personal dashboard showing collected leaves, total leaves, total veins, best leaf, and highest rarity.



Leaf collection showing analyzed leaves and their rarity classifications.

Diagrams

System Architecture

                    ┌──────────────────┐
                    │      USER        │
                    │  Name + Leaf     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   HTML + CSS     │
                    │    Interface     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      FLASK       │
                    │    app.py        │
                    └────────┬─────────┘
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
        ┌─────────────────┐      ┌─────────────────┐
        │  OpenCV +       │      │     SQLite      │
        │  NumPy          │      │    Database     │
        └────────┬────────┘      └─────────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Vein Detection  │
        │ & Analysis      │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Vein Count +    │
        │ Visualization   │
        └────────┬────────┘
                 │
                 ▼
        ┌────────────────────────────┐
        │ Dashboard / Collection /   │
        │ Leaderboard / Rarity       │
        └────────────────────────────┘

Architecture showing how the interface, Flask backend, computer vision module, and SQLite database interact.

Workflow

START
  │
  ▼
Enter Name
  │
  ▼
Upload Leaf
  │
  ▼
Read Image
  │
  ▼
Isolate Leaf
  │
  ▼
Enhance Image
  │
  ▼
Extract Veins
  │
  ▼
Skeletonize
  │
  ▼
Analyze Branches
  │
  ▼
Calculate Vein Count
  │
  ▼
Assign Rarity
  │
  ▼
Save to SQLite
  │
  ▼
Display Result
  │
  ├──────────────► Dashboard
  ├──────────────► Collection
  └──────────────► Leaderboard

Rarity System

Vein Count

Rarity

1–5

✨ DIVINE

6–499

🌱 BASE

500–1,999

🍃 COMMON

2,000–4,999

💎 RARE

5,000–9,999

⚡ EPIC

10,000–14,999

🔥 LEGENDARY

15,000–20,000

👑 MYTHIC

20,001+

🌌 MYTHIC+

The rarity system is a gamification layer built on top of the computer-vision result.

Database

The project uses SQLite with a leaves table:

leaves
────────────────────────────
id
name
image_path
vein_image_path
vein_count
created_at
────────────────────────────

The database stores user names, uploaded image paths, vein counts, generated visualizations, and analysis timestamps.

Dashboard

The personal dashboard provides:

👤 User name

🌿 Total leaves collected

🕸️ Total veins

🏆 Best leaf

✨ Highest rarity

🌱 Personal leaf collection

The dashboard retrieves leaves associated with the entered name.

Note: This is an MVP identity system based on the user's name, not full authentication.

Leaderboard

The leaderboard sorts users by vein count in descending order.

SELECT name, vein_count
FROM leaves
ORDER BY vein_count DESC
LIMIT 10;

Because apparently leaf veins needed ranked matchmaking. 🏆🌿

Schematic & Circuit

Not applicable.

This project is software-only and does not use electronic circuits or embedded hardware.

Build Photos

Not applicable for hardware.

For the software build, screenshots can be included for:

Project folder structure

Flask application running

Computer-vision output

Database/collection

Dashboard

Project Demo

Video

[Add your demo video link here]

The demo shows the complete workflow: entering a name, uploading a leaf, analyzing the image, viewing the detected veins and rarity, opening the personal dashboard, viewing the collection, and checking the leaderboard.

Additional Demos

You can include:

Live application URL

GitHub repository

Demo screenshots

Computer-vision output examples

Presentation/PPT

Project documentation

Repository:

https://github.com/MAHIKUMARH/leaf_me_alone

Challenges Faced

Background Noise

Background textures can sometimes be interpreted as vein-like structures.

Lighting

Different lighting conditions can affect contrast and vein visibility.

Skeletonization Noise

Small image fragments can create unwanted branches.

Vein Count Accuracy

The system detects visual vein-like structures, so the result should not be interpreted as a scientifically exact biological vein count.

Sensitivity vs Noise

Making the detector more sensitive can detect more structures, but can also increase false detections.

At one point the detector basically looked at a leaf and said:

"3,972 veins."

The leaf was not available for comment. 🌿💀

Why Classical Computer Vision?

The project intentionally uses image-processing techniques instead of a trained machine-learning model.

Advantages for this MVP:

No large labeled dataset required

Easier to develop quickly

Easier to debug

More interpretable processing pipeline

Demonstrates fundamental computer-vision techniques

Simple deployment

Future versions could explore machine learning if a sufficiently large and reliable dataset becomes available.

Future Improvements

More robust leaf segmentation

Better handling of different lighting conditions

Perspective correction

Improved vein detection

Quantitative accuracy evaluation

Larger test dataset

Better biological vein-count approximation

Proper user authentication

Cloud deployment

More advanced rarity mechanics

Additional leaderboard statistics

Optional machine-learning-based vein detection

Team Contributions

ARJUN V PILLAI: Computer-vision pipeline development, vein detection logic, image-processing experimentation, testing and debugging.

MAHIKUMAR H: Flask web application, UI/pages, dashboard, collection, leaderboard, rarity system, project integration and testing.

Final Note 🌿

LEAF ME ALONE started with a simple question:

"Can we count the veins on a leaf?"

And somehow became:

"WHO HAS THE MOST POWERFUL LEAF?"

That's progress. 🌿🏆

Upload a leaf. Get its stats. Become unnecessarily competitive.
=======
<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



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
