def calculate_pph(db: Session, income: float):
    rules = db.execute(
        "SELECT * FROM tax_rules WHERE :income BETWEEN min_income AND max_income",
        {"income": income}
    ).fetchone()

    if not rules:
        return 0

    return income * rules.rate

def get_tax_rules(db: Session):
    return db.execute("SELECT * FROM tax_rules").fetchall()

def calculate_pph(db, income):
    if income <= 0:
        return 0
    # logic existing

def cek_status_gaji(income):
    if income <= 0 :
        return "Error: Gaji tidak valid"  # Low income
    elif income <= 10000000:
        return "Kategori: Menengah" # Middle income
    else:
        return "Kategori: Tinggi"  # High income
    