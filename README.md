# Website & App Blocker

The **Website & App Blocker** is a productivity tool designed to help users stay focused by blocking distracting websites and applications during specified time periods. It provides an easy-to-use interface to manage blocked websites, schedule blocking hours, and ensure settings are secure with password protection.

---

## Features

- **Website Blocking:** Blocks access to specific websites by modifying the system's hosts file.
- **App Blocking (Planned):** Monitors and restricts access to selected applications.
- **Password Protection:** Secures critical actions like enabling or disabling blocking with a password.
- **Custom Blocking Schedule:** Automatically blocks websites and apps during specified hours.
- **User-Friendly GUI:** Built using Tkinter for intuitive navigation and configuration.
- **Action Log:** Displays a detailed log of all actions performed for transparency.

---

## Technologies Used

- **Python 3.13**: Core programming language.
- **Tkinter**: For building the graphical user interface (GUI).
- **psutil** (Planned): For managing and terminating application processes.
- **File Handling**: Used to modify the system's `hosts` file for website blocking.

---

## Setup Instructions

### Prerequisites
- Python 3.13 installed on your system.
- Administrator/root access is required to modify the system's `hosts` file.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/website-app-blocker.git
2. Navigate to the project directory:
   ```bash
   cd website-app-blocker

3. Install required Python packages:
   ```bash
   pip install psutil

4. Run the program:
   ```bash
   python blocker.py











