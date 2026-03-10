# Screenshots Guide

## How to Add Screenshots

Follow these steps to capture and add screenshots to your GitHub repository:

### Step 1: Capture Screenshots

The app is running at: http://127.0.0.1:5000

Capture these 4 key pages:

#### 1. Home Page (index.html)
- Show the navbar, hero section, application form, and features section
- File: `home-page.png`

#### 2. Application Form Close-up
- Show the form with all fields: Name, Email, Phone, Position dropdown, Resume upload
- File: `application-form.png`

#### 3. Success Page (success.html)
- Show the success message and Application ID
- File: `success-page.png`

#### 4. HR Dashboard (dashboard.html)
- Show the table with submissions and submission count
- File: `dashboard.png`

### Step 2: Save Screenshots

Save each screenshot with these names in the `screenshots/` folder:
- `home-page.png`
- `application-form.png`
- `success-page.png`
- `dashboard.png`

### Step 3: Update README

The main README.md already has sections for screenshots. 

To add images, in each screenshot section, add:
```markdown
![Home Page](/screenshots/home-page.png)
```

### How to Take Screenshots

**On Windows:**
- Press `Windows + Shift + S` - Use Snip & Sketch
- Or use Print Screen key
- Paste into Paint and save as PNG

**Using Browser:**
- Right-click → Inspect → Device Toolbar
- Take screenshot of the page
- Save as PNG

### Files Already Created

- ✅ Created `screenshots/` folder
- ✅ Updated README.md with screenshot sections

### Next Steps

1. Take 4 screenshots of your app pages
2. Save them to: `C:\Users\hp\Flutter_Projects\ai-dataset-upload-portal\screenshots\`
3. Run these commands to push to GitHub:

```powershell
cd c:\Users\hp\Flutter_Projects\ai-dataset-upload-portal
git add .
git commit -m "Add screenshots and improved README"
git push origin main
```

### Your GitHub Repo
https://github.com/nethranekar-dev/hr-recruitment-portal
