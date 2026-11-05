# Student Result Management System (SRMS)

A desktop-based Student Result Management System built with **Python, Tkinter, SQLite, and Pillow**. The application provides a graphical interface for staff to manage academic information, including courses, students, examination results, and reports.

## Features

- **Staff registration and login** for accessing the management interface.
- **Dashboard** with database-driven counts of courses, students, and results.
- **Course management** for maintaining course records.
- **Student management** for maintaining student records.
- **Result management** for recording and managing examination results.
- **Result reporting** through a dedicated report module.
- **Input validation** and user-facing error and confirmation messages.
- **SQLite storage** in a local database file (`rms.db`).
- **Analog clock** on the staff dashboard, generated using Pillow.

> The exact fields and available search, export, or print options depend on the implementation in the individual modules.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Tkinter | Desktop graphical user interface |
| SQLite | Local relational database |
| `sqlite3` | Python interface for SQLite |
| Pillow | Image loading, resizing, and clock rendering |

## Project Structure

The project is organized into modules based on the application's major responsibilities. A typical layout is:

```text
Student-Result-Management-System/
│
├── images/                 # Logo, backgrounds, and clock assets
├── course.py               # Course management
├── student.py              # Student management
├── result.py               # Result management
├── report.py               # Student result reporting
├── login_staff.py          # Staff login window (if used as a separate module)
├── dashboard_main.py       # Application/login navigation entry point
├── rms.db                  # SQLite database
└── README.md
```

Your local project may contain additional files for registration, database initialization, or other windows. Keep those files in the project when running the application.

## Requirements

- Python 3.9 or later recommended
- Tkinter (usually included with standard Python installations; on some Linux distributions it must be installed separately)
- Pillow

## Installation and Setup

1. **Clone or download the repository.**

   ```bash
   git clone <YOUR_GITHUB_REPOSITORY_URL>
   cd Student-Result-Management-System
   ```

2. **Create and activate a virtual environment (recommended).**

   Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   macOS / Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required Python package.**

   ```bash
   pip install Pillow
   ```

   The `sqlite3` and `tkinter` modules are part of Python's standard library in many installations. If Tkinter is unavailable, install the Tkinter package appropriate for your operating system.

4. **Check the database and image assets.**

   Make sure `rms.db` is available in the location expected by the application, or run the project's database/table initialization script if one is provided. Also ensure the required files are present inside the `images/` directory. The application uses relative paths, so run it from the project root directory.

5. **Run the application.**

   If `dashboard_main.py` is your main entry-point file, run:

   ```bash
   python dashboard_main.py
   ```

   If your project uses a different launcher, replace the filename with that entry-point script.

## Database

The application uses SQLite and stores its data locally in `rms.db`. The database contains tables for the main entities, including:

- `staff` — staff registration and account details
- `course` — course information
- `student` — student information
- `result` — examination result information

The application performs database operations through Python's `sqlite3` module. Parameterized SQL queries are used for operations that include user-provided values.

## Application Architecture

The project follows a **modular, layered desktop-application approach**:

1. **Presentation layer:** Tkinter windows, forms, buttons, labels, and dashboard components.
2. **Application logic:** Python classes and functions for validation, navigation, and record-management operations.
3. **Data layer:** SQLite database access through `sqlite3` and SQL queries.

The modules separate major application responsibilities, making the code easier to navigate and maintain.

## Security Note

This is an academic desktop project. The current registration implementation stores passwords as plain text. It should **not** be used as-is for real users or sensitive data. A production implementation should store salted password hashes using a suitable password-hashing algorithm, enforce database constraints such as unique staff emails, and apply appropriate access controls.

## Future Improvements

- Hash passwords and strengthen authentication and authorization.
- Add database constraints and relationships, including foreign keys.
- Improve validation for email addresses, contact numbers, and marks.
- Add automated tests and structured application logging.
- Separate database access and business logic more clearly from Tkinter UI code.
- Consider a centralized database and client-server architecture for multi-user access.

## Author

**Avneel Singh**

---

*Update the repository URL, entry-point filename, and project structure above to match the exact files in your GitHub repository before publishing this README.*
