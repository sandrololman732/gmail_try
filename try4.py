from flask import Flask, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        message = data['message']

        # Replace the following with your email sending code
        # Ensure that you set up a secure way to store email credentials
        # Using a configuration file or environment variables is recommended
        sender_email = 'your_email@gmail.com'
        sender_password = 'your_email_password'
        receiver_email = 'ivanstrk685@gmail.com'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        subject = 'New Message from Your Website'
        body = f'Message: {message}'

        email_message = f'Subject: {subject}\n\n{body}'
        server.sendmail(sender_email, receiver_email, email_message)

        server.quit()
        return 'Message sent successfully!'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
