def calculate_pph(db: Session, income: float):
    rules = db.execute(
        "SELECT * FROM tax_rules WHERE :income BETWEEN min_income AND max_income",
        {"income": income}
    ).fetchone()

    if not rules:
        return 0

    return income * rules.rate