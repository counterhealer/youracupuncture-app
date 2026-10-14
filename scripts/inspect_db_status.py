import sqlite3

conn = sqlite3.connect('data/acupuncture.db')
c = conn.cursor()
tables = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
print("Database Tables and Row Counts:")
for t in tables:
    count = c.execute(f"SELECT count(*) FROM {t}").fetchone()[0]
    print(f"  - {t}: {count} records")

conn.close()
