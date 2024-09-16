[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AHFn7Vbn)
# Superjoin Hiring Assignment

### Welcome to Superjoin's hiring assignment! 🚀

### Objective
Build a solution that enables real-time synchronization of data between a Google Sheet and a specified database (e.g., MySQL, PostgreSQL). The solution should detect changes in the Google Sheet and update the database accordingly, and vice versa.

### Problem Statement
Many businesses use Google Sheets for collaborative data management and databases for more robust and scalable data storage. However, keeping the data synchronized between Google Sheets and databases is often a manual and error-prone process. Your task is to develop a solution that automates this synchronization, ensuring that changes in one are reflected in the other in real-time.

### Requirements:
1. Real-time Synchronization
  - Implement a system that detects changes in Google Sheets and updates the database accordingly.
  - Similarly, detect changes in the database and update the Google Sheet.
2. CRUD Operations
  - Ensure the system supports Create, Read, Update, and Delete operations for both Google Sheets and the database.
  - Maintain data consistency across both platforms.
   
### Optional Challenges (This is not mandatory):
1. Conflict Handling
   - Develop a strategy to handle conflicts that may arise when changes are made simultaneously in both Google Sheets and the database.
   - Provide options for conflict resolution (e.g., last write wins, user-defined rules).
2. Scalability: 	
   - Ensure the solution can handle large datasets and high-frequency updates without performance degradation.
   - Optimize for scalability and efficiency.


We have a checklist at the bottom of this README file, which you should update as you progress with your assignment. It will help us evaluate your project.

- [✔️] My code's working just fine! 🥳
- [✔️] I have recorded a video showing it working and embedded it in the README ▶️
- [✔️] I have tested all the normal working cases 😎
- [✔️] I have even solved some edge cases (brownie points) 💪
- [✔️] I added my very planned-out approach to the problem at the end of this README 📜
---
System Design Diagram 
![image](https://github.com/user-attachments/assets/30d0ae77-df4d-4b92-b04b-18ead0b0fb07)
### Tech Stack
- **Backend Framework**: FastAPI
- **Database**: Firebase Firestore
- **Google Sheets Integration**: Google Sheets API, Google Apps Script
- **Programming Language**: Python
- **Authentication**: Firebase Admin SDK for secure access to Firestore
- **Task Scheduling**: Google Apps Script for triggering synchronization
- **Conflict Resolution**: Custom logic within the synchronization process
- **Background Task Queue**: FastAPI BackgroundTasks
- **Caching (Planned)**: Redis for caching Google Sheets data

### Approach

#### Real-time Synchronization
1. **Google Sheets to Firestore**:
   - **Google Apps Script**: Utilized to detect changes in Google Sheets. It triggers on edit (`onEdit`) or structural changes (`onChange`) and sends a webhook to the FastAPI server.
   - **FastAPI Webhook**: Receives the webhook, processes the change, and updates Firestore accordingly. Data is mapped from Google Sheets to a Firestore document structure.

2. **Firestore to Google Sheets**:
   - **Firestore Listener**: Monitors changes in Firestore documents and triggers updates in Google Sheets.
   - **Google Sheets API**: Updates the relevant row in Google Sheets to reflect changes from Firestore, ensuring bidirectional synchronization.
   - **Conflict Resolution**: Employs a "Last Write Wins" strategy using timestamps to handle simultaneous changes.

#### CRUD Operations
- Supports Create, Read, Update, and Delete operations in both Google Sheets and Firestore.
- Automatically synchronizes new entries, updates, and deletions between Google Sheets and Firestore.

#### Conflict Handling
- **Strategy**: Implemented a "Last Write Wins" strategy where each record includes a `last_modified` timestamp. The most recent change based on timestamps is applied.
- **Fallback**: Logs conflicts that can't be automatically resolved for manual intervention.

#### Scalability
- **Efficient API Usage**: Batch operations and optimized API calls are used to handle high-frequency updates.
- **Error Handling**: Robust error handling and retries manage API rate limits and network issues.
- **Background Task Queue**: FastAPI's `BackgroundTasks` is used to queue and process multiple requests efficiently.
- **Caching (Planned)**: A Redis cache layer is planned to temporarily store Google Sheets data, reducing API calls and preventing quota exhaustion.

### Getting Started
1. **Prerequisites**:
   - Google Cloud Project with Sheets API enabled.
   - Firebase Project with Firestore Database.
   - Service Account Key for authentication.
   - Python environment set up with necessary dependencies.

2. **Installation**:
   - Clone the repository.
   - Set up environment variables for Google Sheets and Firebase credentials.
   - Deploy the FastAPI server.

3. **Configuration**:
   - Configure Google Apps Script to point to the FastAPI server webhook.
   - Set up Firestore listener to monitor changes in the database.

4. **.env example**
  ```
# .env
GOOGLE_SHEETS_KEY_PATH=
GOOGLE_SHEETS_ID=
GOOGLE_SHEET_NAME=
FIREBASE_ADMIN_KEY_PATH=
```

6. **Running the Project**:
   - Start the FastAPI server.
   - Make changes in Google Sheets or Firestore to see real-time synchronization in action.

### Video Demo
https://drive.google.com/drive/folders/14DzkV5ppT_sDwri0JO1XgzqZ_u8HoRDu?usp=sharing

### Conclusion
This project offers an automated, real-time synchronization solution between Google Sheets and Firestore. It supports full CRUD operations, conflict resolution through a "Last Write Wins" strategy, and efficient handling of high-frequency updates using FastAPI's background task processing. A Redis cache layer is planned to further optimize performance and avoid API quota exhaustion. 

### Comments
Feel free to add your thoughts or any challenges faced during the project here. We will read and consider your insights!
