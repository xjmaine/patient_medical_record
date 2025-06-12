from health_app.services.email_service.email_service import EmailService

def get_email_service() -> EmailService:
    """Dependency provider for email service"""
    return EmailService()