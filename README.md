# HR Recruitment Submission Portal

A professional web application that allows candidates to submit job applications and upload resumes. The system generates a unique Application ID for each candidate and allows HR teams to track submissions through an intuitive dashboard.

## 📋 Features

- ✅ **Job Application Submission** - Clean, professional form for candidates
- ✅ **Resume Upload** - Secure file upload functionality
- ✅ **Automatic Application ID Generation** - Unique 8-character ID for each submission
- ✅ **HR Recruitment Dashboard** - Track all candidate submissions in real-time
- ✅ **Candidate Tracking** - View all submission details (Name, Email, Phone, Position, Resume)
- ✅ **Responsive Design** - Works on desktop, tablet, and mobile devices
- ✅ **Professional UI** - Bootstrap-based modern interface

## 📸 Screenshots

### 1. Home Page
Shows the landing page with the application form, features section, and navigation navbar.

![Home Page](/home_page.png.png)

### 2. Success Page
Displays the unique Application ID after successful submission.

![Success Page](/result_page.png.png)

### 3. HR Dashboard
Shows all submitted applications in a professional table format with:
- Application ID
- Candidate Name
- Email
- Phone Number
- Position Applied
- Resume File

![HR Dashboard](/hr_dashboard.png.png)

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Storage:** CSV
- **Design:** Bootstrap 5, Custom CSS

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Flask
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/nethranekar-dev/hr-recruitment-portal.git
cd hr-recruitment-portal
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install flask
```

4. Run the application
```bash
python app.py
```

5. Open your browser and go to:
```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
hr-recruitment-portal/
├── app.py                 # Main Flask application
├── README.md              # Project documentation
├── submissions.csv        # Candidate submissions data
├── uploads/               # Folder for uploaded resumes
└── templates/
    ├── index.html         # Home page
    ├── success.html       # Success page
    └── dashboard.html     # HR Dashboard
```

## 💡 How It Works

1. **Candidate Submission**
   - Candidate fills out the application form
   - Uploads their resume
   - Clicks "Submit Application"

2. **Application Processing**
   - System generates unique Application ID
   - Resume file is stored in `/uploads` folder
   - Submission data is saved to CSV

3. **HR Dashboard**
   - HR team can access `/dashboard` route
   - View all candidate submissions
   - Track applications in real-time

## 🎯 Use Cases

- **Recruitment Teams** - Manage and track job applications
- **HR Departments** - Centralized candidate management
- **Job Portals** - Simple application submission system
- **Educational Institutions** - Admissions management

## 📝 CSV Data Format

Each submission is stored as:
```
ApplicationID, Name, Email, Phone, Position, ResumeFile
a1b2c3d4, John Doe, john@example.com, 9876543210, Flutter Developer, a1b2c3d4_resume.pdf
```

## 🔒 Security Notes

- Store uploaded files in a secure directory
- Validate file types before upload
- Implement authentication for HR dashboard (future enhancement)

## 🚧 Future Enhancements

- Email confirmation after submission
- PDF export of submissions
- Search and filter in dashboard
- Admin authentication
- Database integration (replace CSV)
- Application status tracking

## 👨‍💻 Author

## 📞 Support

Report issues on GitHub: https://github.com/nethranekar88-tech/hr-recruitment-portal/issues

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Flutter, Firebase & Flask**

*Last Updated: March 2026*
