# Email templates for different notifications

def load_template(template_name):
    """Load an email template from a file."""
    try:
        with open(f'templates/{template_name}.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        logger = logging.getLogger('EmailTemplateLogger')
        logger.error(f"Template {template_name} not found.")
        return ""


ACCOUNT_CREATION_TEMPLATE = load_template('account_creation')
Subject: Welcome to Our Service

Hello {name},

Thank you for creating an account with us. We're excited to have you on board!

Best regards,
The Team
'''

PASSWORD_RESET_TEMPLATE = '''
Subject: Password Reset Request

Hello {name},

We received a request to reset your password. Click the link below to reset it:
{reset_link}

If you did not request a password reset, please ignore this email.

Best regards,
The Team
'''

# Add more templates as needed
