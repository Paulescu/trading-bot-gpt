import logging
from typing import Optional

def get_console_logger(name: Optional[str] = 'trading_bot_gpt') -> logging.Logger:
    
    # Create logger if it doesn't exist
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    return logger