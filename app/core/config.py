import os

DATABASE_URL        = os.getenv('DATABASE_URL', 'sqlite:///tokens.db')
INGRESS_DOMAIN      = os.getenv('INGRESS_DOMAIN', 'token-service.local')
