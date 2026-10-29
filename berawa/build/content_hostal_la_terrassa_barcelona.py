# Contenido de la demo Hostal La Terrassa (Barcelona) (es/ca/en/fr). Hechos de laterrassa-barcelona.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Básica Exterior','Básica Interior','Chapelle'],'ca':['Bàsica Exterior','Bàsica Interior','Chapelle'],'en':['Basic Exterior','Basic Interior','Chapelle'],'fr':['Basica Exterior','Basica Interior','Chapelle']}
RD={
'es':['Cama doble (135 x 190 cm), baño privado con ducha y un pequeño balcón al exterior o a la terraza; 10,50 m².','Cama doble (135 x 190 cm) y baño privado con ducha; da a un pequeño espacio interior; 11 m².','Cama doble (150 x 200 cm), ventana al exterior y baño privado con ducha; admite cama supletoria; 18 m².'],
'ca':['Llit doble (135 x 190 cm), bany privat amb dutxa i un petit balcó a l\'exterior o a la terrassa; 10,50 m².','Llit doble (135 x 190 cm) i bany privat amb dutxa; dona a un petit espai interior; 11 m².','Llit doble (150 x 200 cm), finestra a l\'exterior i bany privat amb dutxa; admet llit supletori; 18 m².'],
'en':['Double bed (135 x 190 cm), private bathroom with shower and a small balcony facing outside or the terrace; 10,50 m².','Double bed (135 x 190 cm) and private bathroom with shower; facing a small inner space; 11 m².','Double bed (150 x 200 cm), window to the exterior and private bathroom with shower; an extra bed is possible; 18 m².'],
'fr':['Lit double (135 x 190 cm), salle de bains privée avec douche et petit balcon sur l\'extérieur ou la terrasse ; 10,50 m².','Lit double (135 x 190 cm) et salle de bains privée avec douche ; donne sur un petit espace intérieur ; 11 m².','Lit double (150 x 200 cm), fenêtre sur l\'extérieur et salle de bains privée avec douche ; lit d\'appoint possible ; 18 m².']}
ART={
'hero':('arches',3301,['#f3e7dc','#e2bfa0','#b4805a','#7a3b2e','#4a2019']),
'intro':('columns',3302,['#f2e8df','#f8f1ea','#b8893e','#7a3b2e','#4a2019']),
'r1':('arches',3311,['#f1e5da','#ddb898','#ad7a55','#7a3b2e','#4a2019']),
'r2':('columns',3312,['#efe5dc','#f6efe8','#c08c40','#80412f','#4d231a']),
'r3':('skyline',3313,['#4a2a2a','#e48a5f','#f9d19b','#482828','#381f1f','#241414']),
'g1':('hills',3321,['#e6ecd9','#f1e6c4','#f6cf8a','#a9c19e','#80a085','#587767']),
'g2':('arches',3322,['#f2e6db','#dfbb9b','#b07d57','#7a3b2e','#4a2019']),
'g3':('columns',3323,['#f1e7de','#f7f0e9','#b8893e','#7a3b2e','#4a2019']),
'g4':('skyline',3324,['#44282a','#e2a160','#f6d59e','#42262a','#33201f','#211414']),
'g5':('hills',3325,['#e3ead6','#f0e5c2','#f4cf8c','#9fbf96','#6f9a72','#4d7550']),
'g6':('arches',3326,['#f0e4d9','#dbb695','#a97752','#7a3b2e','#4a2019'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal La Terrassa · Hostal en Ciutat Vella, a 3 minutos de La Boqueria y las Ramblas',see_rooms='Ver habitaciones',hero_k='Barcelona · Ciutat Vella',hero_t='En el centro, con terraza jardín',hero_s='En Junta de Comerç, 11: a 3 minutos de La Boqueria y las Ramblas y a 300 metros del metro Liceu (L3).',
 intro_t='Un hostal céntrico y sencillo',intro_p1='Hostal La Terrassa está en Ciutat Vella, a unos 25 minutos a pie de la playa de La Barceloneta y a 15 de plaça de Catalunya.',
 intro_p2='Todas las habitaciones tienen baño privado, aire acondicionado o calefacción según la estación, artículos de aseo y wifi gratis. Recepción abierta 24/7 y terraza jardín hasta las 23:00.',
 stats=['Ciutat Vella','Terraza jardín','Recepción 24/7','Metro Liceu a 300 m'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Los tres tipos de habitación del hostal.',
 svcs=['Baño privado en todas las habitaciones','Aire acondicionado o calefacción','Wifi gratis','Recepción 24/7','Terraza jardín hasta las 23:00','Desayuno continental opcional','Consigna de equipaje gratis','Ordenador para clientes'],
 loc_p='Carrer Junta de Comerç, 11 · 08001 Barcelona, en Ciutat Vella, a 300 metros del metro Liceu (L3).',
 chips=['¿Qué habitaciones tiene?','¿Hay desayuno?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Hostal La Terrassa · Hostal a Ciutat Vella, a 3 minuts de La Boqueria i les Rambles',see_rooms='Veure habitacions',hero_k='Barcelona · Ciutat Vella',hero_t='Al centre, amb terrassa jardí',hero_s='A Junta de Comerç, 11: a 3 minuts de La Boqueria i les Rambles i a 300 metres del metro Liceu (L3).',
 intro_t='Un hostal cèntric i senzill',intro_p1='L\'Hostal La Terrassa és a Ciutat Vella, a uns 25 minuts a peu de la platja de La Barceloneta i a 15 de la plaça de Catalunya.',
 intro_p2='Totes les habitacions tenen bany privat, aire condicionat o calefacció segons l\'estació, articles de tocador i wifi gratis. Recepció oberta 24/7 i terrassa jardí fins a les 23:00.',
 stats=['Ciutat Vella','Terrassa jardí','Recepció 24/7','Metro Liceu a 300 m'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Els tres tipus d\'habitació de l\'hostal.',
 svcs=['Bany privat a totes les habitacions','Aire condicionat o calefacció','Wifi gratis','Recepció 24/7','Terrassa jardí fins a les 23:00','Esmorzar continental opcional','Consigna d\'equipatge gratis','Ordinador per a clients'],
 loc_p='Carrer Junta de Comerç, 11 · 08001 Barcelona, a Ciutat Vella, a 300 metres del metro Liceu (L3).',
 chips=['Quines habitacions té?','Hi ha esmorzar?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Hostal La Terrassa · Hostel in Ciutat Vella, 3 minutes from La Boqueria and Las Ramblas',see_rooms='See the rooms',hero_k='Barcelona · Ciutat Vella',hero_t='In the centre, with a garden terrace',hero_s='At Junta de Comerç, 11: 3 minutes from La Boqueria and Las Ramblas and 300 metres from Liceu metro (L3).',
 intro_t='A central, simple hostel',intro_p1='Hostal La Terrassa is in Ciutat Vella, about a 25-minute walk from La Barceloneta beach and 15 from Plaça de Catalunya.',
 intro_p2='Every room has a private bathroom, air conditioning or heating depending on the season, toiletries and free wifi. Reception open 24/7 and a garden terrace until 23:00.',
 stats=['Ciutat Vella','Garden terrace','Reception 24/7','Liceu metro 300 m'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='The hostel\'s three room types.',
 svcs=['Private bathroom in every room','Air conditioning or heating','Free wifi','Reception 24/7','Garden terrace until 23:00','Optional continental breakfast','Free luggage storage','Computer for guests'],
 loc_p='Carrer Junta de Comerç, 11 · 08001 Barcelona, in Ciutat Vella, 300 metres from Liceu metro (L3).',
 chips=['What rooms does it have?','Is there breakfast?','Is there parking?','How do I book?']),
'fr':dict(title='Hostal La Terrassa · Hostal dans la Ciutat Vella, à 3 minutes de La Boqueria et des Ramblas',see_rooms='Voir les chambres',hero_k='Barcelone · Ciutat Vella',hero_t='En plein centre, avec terrasse jardin',hero_s='Junta de Comerç, 11 : à 3 minutes de La Boqueria et des Ramblas et à 300 mètres du métro Liceu (L3).',
 intro_t='Un hostal central et simple',intro_p1='L\'Hostal La Terrassa se trouve dans la Ciutat Vella, à environ 25 minutes à pied de la plage de La Barceloneta et à 15 de la plaça de Catalunya.',
 intro_p2='Toutes les chambres ont salle de bains privée, climatisation ou chauffage selon la saison, articles de toilette et wifi gratuit. Réception ouverte 24/7 et terrasse jardin jusqu\'à 23:00.',
 stats=['Ciutat Vella','Terrasse jardin','Réception 24/7','Métro Liceu à 300 m'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Les trois types de chambre de l\'hostal.',
 svcs=['Salle de bains privée dans chaque chambre','Climatisation ou chauffage','Wifi gratuit','Réception 24/7','Terrasse jardin jusqu\'à 23:00','Petit-déjeuner continental en option','Consigne à bagages gratuite','Ordinateur pour les clients'],
 loc_p='Carrer Junta de Comerç, 11 · 08001 Barcelone, dans la Ciutat Vella, à 300 mètres du métro Liceu (L3).',
 chips=['Quelles chambres a-t-il ?','Y a-t-il un petit-déjeuner ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
W='https://laterrassa-barcelona.com/'
BOOK=dict(mode='engine',url={'es':W+'reserva/?lang=es','ca':W+'reserva/?lang=ca','en':W+'book/','fr':W+'reservation/?lang=fr'})
D=dict(name='Hostal La Terrassa',ac='#7a3b2e',ac2='#b8893e',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='Carrer Junta de Comerç, 11 · 08001 Barcelona',phones=['+34 93 302 51 74'],emails=['reservations@laterrassa-barcelona.com'],maps='Hostal La Terrassa, Carrer Junta de Comerç 11, Barcelona',t=T)
META=dict(repo='demo-hostal-la-terrassa-barcelona',name='Hostal La Terrassa',legal_name='S3G 111, S.A.',registry_ids=['NIF A58741547'],
 url='https://laterrassa-barcelona.com/',domain='laterrassa-barcelona.com',municipality='Barcelona',province='Barcelona',sector='hostal en Ciutat Vella',
 read_at='2026-10-29T08:05:00+01:00',created_at='2026-10-29T08:35:00+01:00',built_at='2026-10-29T08:35:00+01:00',audit_date='2026-10-29T07:52:00+01:00',
 rating=dict(value=4.3,coincide=['telefono','web'],date='2026-10-29T06:55:06+01:00',url='https://www.google.com/maps/place/Hostal+La+Terrassa/@41.3800431,2.171395,17z/data=!4m9!3m8!1s0x12a4a258902514db:0xe67c5b02e6f68779!5m2!4m1!1i2!8m2!3d41.3800431!4d2.171395!16s%2Fg%2F1vgn4wr8?hl=es&entry=ttu&g_ep=EgoyMDI2MTAyNy4wIKXMDSoASAFQAw%3D%3D'),
 book=dict(mode='engine',url=BOOK['url'],note='Los botones Reservar van a la pagina de reserva de su propia web en cada idioma (reserva/book/reservation, con el buscador de disponibilidad de su web). La demo no construye ningun motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Hay desayuno?','K03'),('¿Hay parking?','K04'),('¿Es accesible para silla de ruedas?','K05'),('¿Admiten mascotas?','K06'),('¿Dónde está?','K07'),('¿Cómo llegar desde el aeropuerto?','K08'),('¿A qué hora es el check-in?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el correo?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Tienen gimnasio?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Què tenen les habitacions?','K02'),('Hi ha esmorzar?','K03'),('Hi ha pàrquing?','K04'),('És accessible amb cadira de rodes?','K05'),('Admeteu mascotes?','K06'),('On és?','K07'),('Com arribar des de l\'aeroport?','K08'),('A quina hora és el check-in?','K09'),('Com reservo?','K10'),('Quin és el correu?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Teniu gimnàs?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What do the rooms have?','K02'),('Is there breakfast?','K03'),('Is there parking?','K04'),('Is it wheelchair accessible?','K05'),('Are pets allowed?','K06'),('Where is it?','K07'),('How to get there from the airport?','K08'),('What time is check-in?','K09'),('How do I book?','K10'),('What is the email?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Do you have a gym?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Qu\'ont les chambres ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Y a-t-il un parking ?','K04'),('Est-il accessible en fauteuil roulant ?','K05'),('Les animaux sont-ils admis ?','K06'),('Où est-ce ?','K07'),('Comment venir depuis l\'aéroport ?','K08'),('À quelle heure est le check-in ?','K09'),('Comment réserver ?','K10'),('Quel est l\'e-mail ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None)]}
