# uurchlugdduggui temdegt muruud
s = "hello"
print(s)
#s[0] = "H" typeError uusne

# orond ni shine temdegt mur uusgene
s = "H" + s[1:]
print(s)

#temdegt murin uildlig oilgoh
s1 = "hello"
s2 = s1.upper()  #shine temdegt mur uusgenge s1 iig uurluhgui
print(s1) #hello uurclugduhgui
print(s2) #"HELLO"

#sanah on nuluulul
id_before = id(s1)
s1 = s1 + "world" # shine murin object uusne
id_after = id(s1)
print(id_before == id_after)  #false, uur objects


