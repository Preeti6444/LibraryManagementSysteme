# LibraryManagementSysteme
A web-based library management system using Flask and Python.
A simple web application built with Flask to manage book records, including issuing, returning, and tracking availability. The book data is stored and managed in an Excel file.

## Features
- **Dashboard:** Provides an overview of the total, available, and issued books.
- **Book List:** Displays a comprehensive list of all books with their current status (Available/Issued).
- **Issue Book:** Allows librarians to mark a book as 'Issued' by entering its Book ID.
- **Return Book:** Allows librarians to mark an 'Issued' book as 'Available' again by entering its Book ID.
- **Excel Integration:** Uses pandas to read from and write to an Excel file (`data.xlsx`) as the backend database.
- **Responsive Design:** Utilizes Bootstrap for a modern and responsive user interface.

## Technologies Used
- **Flask:** A micro web framework for Python, used for building the web application.
- **HTML, CSS, Bootstrap:** For structuring, styling, and providing a responsive design to the user interface. Bootstrap 5 is used for quick and consistent styling.
- **pandas:** A powerful data manipulation library in Python, used for seamless reading and writing of data to and from the Excel file.
- **openpyxl:** A Python library used by pandas for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd Library-Management-System
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Flask application:**
    ```bash
    python app.py
    ```
5.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Project File Structure
Library_Management_System/
├── Library.xlsx

├── app.py

├── templates/

│   └── add.html

    └── display.html
    
    └── edit.html

├── static/

│   └── style.css

├── README.md

├── requirements.txt


![1](https://github.com/user-attachments/assets/1cfe40bd-5684-4afe-bb6f-600a61866447)
![2](https://github.com/user-attachments/assets/d3432f03-0a91-4c7e-9aa8-b90d52708d20)


