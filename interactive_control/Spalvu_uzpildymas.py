from app import db, Spalvynas


zalia = Spalvynas("Žalia", "0, 255, 0")
raudona = Spalvynas("Raudona", "255, 0, 0")
melyna = Spalvynas("Mėlyna", "0, 0, 255")
violetine = Spalvynas("Violetinė", "125, 0, 125")
geltona = Spalvynas("Geltona", "255, 255, 0")


db.session.add_all([zalia, raudona, melyna, violetine, geltona])
db.session.commit()
