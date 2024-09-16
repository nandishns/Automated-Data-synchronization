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
### Code Architecture and Design
---
#### 1. **Code Architecture**

- **Modular Design**: The code is divided into different modules based on their functionality, such as services, models, and routers. This separation of concerns helps in organizing the code logically and makes it easier to maintain.

- **Layered Structure**:
  - **Models**: Handle interactions with Firebase Firestore, encapsulating the logic for CRUD operations on the database.
  - **Services**: Contain the business logic for synchronizing data between Google Sheets and Firestore, as well as managing background tasks.
  - **Routers**: Define the API endpoints for handling synchronization, providing a clear entry point for various operations.

#### 2. **OOP Concepts Used**

- **Classes and Objects**: 
  - Classes such as `FirebaseModel`, `GoogleSheetsService`, and `FirebaseListener` encapsulate data and behavior related to specific components (Firestore, Google Sheets, and synchronization logic).
  - Objects of these classes are instantiated to manage interactions with the database and Google Sheets.

- **Encapsulation**:
  - Each class is responsible for a specific part of the system, encapsulating the relevant data and methods. For example, the `FirebaseModel` class handles Firestore operations, while the `GoogleSheetsService` class manages interactions with Google Sheets.
  - This encapsulation ensures that changes in one part of the system do not affect others, promoting modularity.

- **Error Handling**:
  - Classes and methods include error handling mechanisms to catch exceptions and handle them gracefully. This is implemented using `try` and `except` blocks, ensuring the system remains robust and reliable even in the face of unexpected issues.

- **Background Task Handling**:
  - The system utilizes FastAPI's `BackgroundTasks` to handle synchronization tasks asynchronously. This allows the server to queue and process multiple requests efficiently, enhancing performance and responsiveness.

#### 3. **Routers Created**

- **`sync` Router**:
  - **Endpoint**: `/sync`
  - **Functionality**: Handles the synchronization of data from Google Sheets to Firestore. It processes the webhook requests triggered by changes in Google Sheets, retrieves the changed data, and updates Firestore accordingly.

- **`delete_row` Router**:
  - **Endpoint**: `/delete_row`
  - **Functionality**: Handles deletion requests from Google Sheets. When a row is removed in Google Sheets, this router receives the request, identifies the corresponding document in Firestore, and deletes it.

- **Routing with FastAPI**:
  - Each router is defined using FastAPI's `APIRouter` to group related endpoints together. This modular approach makes the code easier to understand and extend.
  - Routers are registered with the FastAPI application, providing a clear and organized way to define and manage the API endpoints.

#### 4. **Flow of Data and Interaction**

- **Data Synchronization**:
  - Changes in Google Sheets trigger webhooks, which are processed by the `sync` router. The router invokes the `GoogleSheetsService` to fetch the latest data and `FirebaseModel` to update Firestore.
  - Changes in Firestore are captured by `FirebaseListener`, which updates Google Sheets using the `GoogleSheetsService`.

- **Conflict Resolution**:
  - The synchronization logic includes conflict resolution based on the "Last Write Wins" strategy, using timestamps to determine the most recent change.

- **Background Processing**:
  - Background tasks are utilized to handle synchronization requests without blocking the main thread, ensuring efficient processing of multiple requests.

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

5. **Running the Project**:
   - Start the FastAPI server.
   - Make changes in Google Sheets or Firestore to see real-time synchronization in action.

### Video Demo
https://drive.google.com/drive/folders/14DzkV5ppT_sDwri0JO1XgzqZ_u8HoRDu?usp=sharing

### Conclusion
This project offers an automated, real-time synchronization solution between Google Sheets and Firestore. It supports full CRUD operations, conflict resolution through a "Last Write Wins" strategy, and efficient handling of high-frequency updates using FastAPI's background task processing. A Redis cache layer is planned to further optimize performance and avoid API quota exhaustion. 

### Comments
- **Integrating Google Sheets API**: Setting up the Google Sheets API and ensuring proper permissions was a bit challenging initially. There were multiple steps to get the API credentials and service account in place, but once configured, it worked seamlessly.

- **Real-time Synchronization**: Implementing real-time synchronization was tricky, especially when handling updates from both Google Sheets and Firestore. Ensuring data consistency while minimizing the number of API calls required careful planning.

- **Conflict Resolution**: Handling simultaneous edits in both Google Sheets and Firestore was a major challenge. Implementing a "Last Write Wins" strategy helped simplify this, but it required adding timestamps and making sure they were used effectively to resolve conflicts.

- **API Rate Limits**: We encountered API rate limits while interacting with Google Sheets frequently. To address this, we planned to integrate Redis as a caching layer to reduce the number of direct API calls, but this is still a pending implementation.

- **Concurrency Handling**: Using FastAPI's background tasks helped manage multiple incoming requests, ensuring that the server wasn't overwhelmed. This was particularly useful for maintaining the responsiveness of the synchronization process.

- **Testing**: Testing the system with various scenarios, including network failures and simultaneous edits, was time-consuming but essential. It helped identify edge cases and refine the conflict resolution strategy.

- **Overall Learning Experience**: This project was a great learning experience in dealing with real-time data synchronization, handling APIs, and implementing conflict resolution strategies. It was challenging but rewarding to see everything come together.
