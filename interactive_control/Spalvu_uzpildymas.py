from app import db, Spalvynas


zalia = Spalvynas("Žalia", "0", "255", "0")
raudona = Spalvynas("Raudona", "255", "0", "0")
melyna = Spalvynas("Mėlyna", "0", "0", "255")
geltona = Spalvynas("Geltona", "255", "255", "0")
balta = Spalvynas("Balta", "255", "255", "255")
isjungimas = Spalvynas("Išjungimas", "0", "0", "0")


db.session.add_all([zalia, raudona, melyna,  geltona, balta, isjungimas])
db.session.commit()
