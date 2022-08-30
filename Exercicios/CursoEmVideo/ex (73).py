#lista com 20  a 5 primeiros b4 ultimos, ordem alfa e posição de um
linuxRank =  ('MX Linux', 'EndeavourOS', 'Manjaro', "Mint", 'Pop!_OS', 'Ubuntu', 'Debian', 'Garuda', 'elementary', 'Fedora', 'Zorin', 'openSUSE', 'KDE' 'neon', 'antiX', 'Solus', 'Slackware', 'Lite', 'PCLinuxOS', 'Arch', 'Artix')
print(f'''
5 primeiros linux do rank: {linuxRank[0:5]}
4 ultimos linux do rank: {linuxRank[-5:-1]}
ordem alfabetica: {sorted(linuxRank)}
o Linux mint está em {linuxRank.index('Mint')+1}º lugar. 
''')
