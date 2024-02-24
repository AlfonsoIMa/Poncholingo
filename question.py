import sqlite3, logging, sys

def ask_nouns(CURSOR: sqlite3.Cursor, min_roles_level: int = 100, amount_questions: int = 30) -> int:
    # GET AMOUNT OF NOUNS
    # SCROLL THROUGH THEM AND PROMPT FOR OPTION
    # IF OPTION_CHOSEN IS RIGHT, ROLES + 3; IF NOT (AND ROLES - 2 >= 0), ROLES - 2
    # GRADE
    return 0