# Flask User Management System

A modern, full-stack CRUD (Create, Read, Update, Delete) web application built with Flask and Firebase Firestore for managing user information.

## 🚀 Features

- ✅ **User Management**: Add, view, edit, and delete users
- ✅ **Real-time Database**: Powered by Google Firebase Firestore
- ✅ **Modern UI**: Clean and responsive design with Bootstrap and custom CSS
- ✅ **Form Validation**: Client-side and server-side validation
- ✅ **Duplicate Check**: Prevents duplicate email and contact numbers
- ✅ **Auto ID Management**: Automatic user ID assignment and reordering
- ✅ **Formatted Timestamps**: Human-readable date and time format (e.g., "2nd Jan 6:20 PM")
- ✅ **Responsive Design**: Works seamlessly on desktop and mobile devices

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- Google Firebase account
- Firebase project with Firestore enabled

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Flask-Task3
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask firebase-admin
```

### 4. Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project or select an existing one
3. Enable Firestore Database
4. Go to Project Settings → Service Accounts
5. Click "Generate New Private Key" to download your service account key
6. Rename the downloaded file to `serviceAccountKey.json`
7. Place it in the root directory of the project

**⚠️ Important**: Never commit `serviceAccountKey.json` to version control. It's already included in `.gitignore`.

### 5. Configure Firebase

The `firebase.py` file is already configured to use `serviceAccountKey.json`. Make sure the file is in the root directory:

```
Flask-Task3/
├── app.py
├── firebase.py
├── serviceAccountKey.json  ← Place your Firebase credentials here
├── templates/
└── static/
```

## 🎯 Usage

### Running the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:8000`

### Accessing the Application

Open your web browser and navigate to:
```
http://localhost:8000
```

## 📁 Project Structure

```
Flask-Task3/
│
├── app.py                      # Main Flask application
├── firebase.py                 # Firebase configuration
├── serviceAccountKey.json      # Firebase credentials (not in git)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
│
├── templates/                  # HTML templates
│   ├── index.html             # User list page
│   ├── add_user.html          # Add user form
│   └── edit_user.html         # Edit user form
│
└── static/                     # Static files
    ├── style.css              # Custom styles
    └── app.js                 # JavaScript functionality
```

## 🔧 Configuration

### Firebase Firestore Structure

The application uses a collection named `users` with the following structure:

```json
{
  "user_id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "contact": "1234567890",
  "created_at": "2nd Jan 6:20 PM",
  "updated_at": "2nd Jan 6:20 PM"
}
```

### Firestore Security Rules

Make sure your Firestore security rules allow read/write access (for development):

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{document=**} {
      allow read, write: if true; // Change this for production!
    }
  }
}
```

**⚠️ Warning**: The above rules allow public access. For production, implement proper authentication and authorization.

## 🎨 Features in Detail

### User Operations

- **Create**: Add new users with name, email, and contact number
- **Read**: View all users in a table format
- **Update**: Edit existing user information
- **Delete**: Remove users (automatically reorders IDs)

### Auto ID Management

When a user is deleted, the system automatically reorders all user IDs to maintain sequential numbering (1, 2, 3, ...).

### Duplicate Prevention

The application checks for duplicate emails and contact numbers before adding new users.

### Timestamp Formatting

Timestamps are displayed in a human-readable format:
- Format: "2nd Jan 6:20 PM"
- Automatically updates when users are created or modified

## 📦 Dependencies

- **Flask**: Web framework
- **firebase-admin**: Firebase Admin SDK for Python
- **Bootstrap**: CSS framework (via CDN)
- **Font Awesome**: Icons (via CDN)

## 🔒 Security Notes

1. **Service Account Key**: Never commit `serviceAccountKey.json` to version control
2. **Firestore Rules**: Implement proper security rules for production
3. **Environment Variables**: Consider using environment variables for sensitive data
4. **Input Validation**: Always validate and sanitize user inputs

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Your Name

## 🙏 Acknowledgments

- Flask documentation
- Firebase documentation
- Bootstrap team

## 📸 Screenshots

Screenshots are available in the `screenshots/` directory.

---

**Note**: This is a development version. Make sure to implement proper security measures before deploying to production.

