from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Email configuration (you'll need to set these environment variables)
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
EMAIL_USER = os.getenv('EMAIL_USER', 'your-email@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your-app-password')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', 'chaiallu2025@gmail.com')

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_form_data(data):
    """Validate form data"""
    errors = []
    
    if not data.get('name') or len(data['name'].strip()) < 2:
        errors.append("Name must be at least 2 characters long")
    
    if not data.get('email') or not validate_email(data['email']):
        errors.append("Please provide a valid email address")
    
    if not data.get('message') or len(data['message'].strip()) < 10:
        errors.append("Message must be at least 10 characters long")
    
    return errors

def send_email(name, email, subject, message):
    """Send email using SMTP"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"Portfolio Contact: {subject or 'New Message'}"
        
        # Email body
        body = f"""
        New message from your portfolio website:
        
        Name: {name}
        Email: {email}
        Subject: {subject or 'No subject'}
        Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Message:
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_USER, RECIPIENT_EMAIL, text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Email sending error: {e}")
        return False

@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Validate form data
        errors = validate_form_data(data)
        if errors:
            return jsonify({"error": "Validation failed", "details": errors}), 400
        
        # Extract data
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        # Log the contact attempt
        print(f"Contact form submission from {name} ({email})")
        
        # Try to send email
        email_sent = send_email(name, email, subject, message)
        
        if email_sent:
            return jsonify({
                "message": "Thank you for your message! I'll get back to you soon.",
                "status": "success"
            }), 200
        else:
            # If email fails, still acknowledge the message but log it
            print(f"Failed to send email for contact from {name} ({email})")
            return jsonify({
                "message": "Message received! I'll get back to you soon.",
                "status": "success"
            }), 200
            
    except Exception as e:
        print(f"Contact endpoint error: {e}")
        return jsonify({
            "error": "Internal server error",
            "message": "Something went wrong. Please try again later."
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()}), 200

if __name__ == '__main__':
    # Only run in debug mode if explicitly set
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)