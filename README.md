# Chaitanya Allu - Portfolio Website

A modern, responsive portfolio website showcasing my skills as a Full Stack Developer and UI/UX Designer.

## Features

- **Modern Design**: Clean, professional dark theme with cyan accents
- **Responsive Layout**: Optimized for all devices and screen sizes
- **Interactive Elements**: Smooth animations, typing effects, and hover interactions
- **Contact Form**: Functional contact form with email integration
- **Project Showcase**: Professional project display with GitHub links
- **Skills Visualization**: Animated progress bars and radial charts
- **Smooth Navigation**: Single-page application with smooth scrolling

## Technologies Used

### Frontend

- HTML5
- CSS3 (with animations and responsive design)
- JavaScript (ES6+)
- Typed.js for typing animations
- Boxicons for icons

### Backend

- Python Flask
- SMTP for email functionality
- CORS support for cross-origin requests

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Modern web browser
- Gmail account (for email functionality)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/AlluChaitanya/Portfolio-Website.git
   cd Portfolio-Website
   ```

2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure email settings**

   - Copy `env.example` to `.env`
   - Update the email configuration in `.env`:
     ```env
     EMAIL_USER=your-gmail@gmail.com
     EMAIL_PASSWORD=your-app-password
     RECIPIENT_EMAIL=chaiallu2025@gmail.com
     ```

   **Note**: For Gmail, you'll need to:

   - Enable 2-factor authentication
   - Generate an App Password
   - Use the App Password instead of your regular password

4. **Run the application**

   ```bash
   # Development mode
   python app.py

   # Production mode
   export FLASK_DEBUG=False
   python app.py
   ```

5. **Open in browser**
   - Frontend: Open `index.html` in your browser
   - Backend API: `http://localhost:5000`

## Project Structure

```
Portfolio/
├── index.html          # Main HTML file
├── stylesheet.css      # CSS styles and animations
├── main.js            # JavaScript functionality
├── app.py             # Flask backend server
├── requirements.txt   # Python dependencies
├── env.example        # Environment variables template
├── README.md          # This file
├── home.jpg           # Profile image
├── pro1.png          # Project 1 screenshot
├── pro2.png          # Project 2 screenshot
├── bg.jpg            # Background image
└── Chaitanya_Allu_JavaFullStack.pdf  # Resume
```

## Features Breakdown

### Home Section

- Animated typing effect for job titles
- Professional introduction
- Social media links
- Call-to-action buttons

### About Section

- Personal background and skills
- Professional summary
- Downloadable resume

### Services Section

- UI/UX Design services
- Web Development expertise
- Deployment and hosting solutions

### Skills Section

- Technical skills with animated progress bars
- Professional strengths with radial charts
- Visual representation of expertise levels

### Portfolio Section

- Project showcase with hover effects
- GitHub links for each project
- Project descriptions and technologies used

### Contact Section

- Functional contact form
- Email integration
- Social media links
- Contact information

## Customization

### Personal Information

- Update personal details in `index.html`
- Replace images with your own
- Modify social media links
- Update project information

### Styling

- Modify colors in `stylesheet.css`
- Update animations and transitions
- Adjust responsive breakpoints

### Backend

- Configure email settings in `app.py`
- Add additional API endpoints
- Implement database storage if needed

## Deployment

### Frontend

- Deploy to GitHub Pages, Netlify, or Vercel
- Update API URL in `main.js` for production

### Backend

- Deploy to Heroku, Railway, or similar platforms
- Set environment variables in deployment platform
- Update CORS settings if needed

## Contributing

Feel free to fork this project and customize it for your own portfolio. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

- **Email**: chaiallu2025@gmail.com
- **Phone**: +1 806-730-5847
- **Location**: Lubbock, TX, USA
- **GitHub**: [AlluChaitanya](https://github.com/AlluChaitanya)

---

_Developed with ❤️ by Chaitanya Allu_
