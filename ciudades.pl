% Hechos sobre las ciudades
ciudad(ensenada, 'Ciudad costera con hermosas playas y paisajes impresionantes.').
ciudad(tecate, 'Ciudad del pan').
ciudad(tijuana, 'Ciudad del hongkong y de las desapariciones').
ciudad(rosarito, 'Ciudad de langostas').
ciudad(mexicali, 'Ciudad calurosa.').
ciudad(san_quintin, 'Ciudad de las fresas').

% Hechos sobre los logotipos y redes sociales de las ciudades
logo(ensenada, 'https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png').
logo(tecate, 'https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png').
logo(tijuana, 'https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png').
logo(rosarito, 'https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png').
logo(mexicali, 'https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png').
logo(san_quintin, 'https://cdn.freebiesupply.com/logos/large/2x/creative-marketing-logo-png-transparent.png').

redes_sociales(ensenada, 'https://ensenadahoy.com/').
redes_sociales(tecate, 'https://tecatehoy.com/').
redes_sociales(tijuana, 'https://tijuanahoy.com/').
redes_sociales(rosarito, 'https://rosaritohoy.com/').
redes_sociales(mexicali, 'https://mexicalihoy.com/').
redes_sociales(san_quintin, 'https://mexicalihoy.com/').

% Regla para encontrar información completa sobre una ciudad
info_ciudad(Ciudad, Descripcion, Logo, Redes) :-
    ciudad(Ciudad, Descripcion),
    logo(Ciudad, Logo),
    redes_sociales(Ciudad, Redes).
