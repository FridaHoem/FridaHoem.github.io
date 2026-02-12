# Academic Personal Website

A modern, static academic website with automatic publication updates powered by GitHub Actions.

## Features
- **Static & Fast**: Built with pure HTML/CSS/JS.
- **Automated Updates**: Fetches latest publications from Google Scholar weekly via GitHub Actions.
- **Responsive**: Looks good on mobile and desktop.
- **Easy Customization**: Edit HTML for content, CSS for styling.

## customized
### Profile Picture
Replace `assets/profile.jpg` with your own photo.

### Content
Edit `index.html` to update your Bio, Research Interests, and Roles.

### Publications
Publications are fetched automatically. The script `scripts/fetch_scholar.py` runs every Sunday.
To trigger an update manually:
1. Go to the "Actions" tab in your GitHub repository.
2. Select "Update Publications".
3. Click "Run workflow".

## Local Development
1. Clone the repo.
2. Open `index.html` in your browser.
3. To run the publication fetcher locally:
   ```bash
   pip install -r requirements.txt
   python scripts/fetch_scholar.py
   ```

## Requirements
- Python 3.x
- `scholarly` library
