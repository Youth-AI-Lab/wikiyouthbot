# Feurisson, le chatbot du groupe feux de forêt

Semaine intensive WikiYouthBot, La Rochelle, juillet 2026.
Document de travail : transcription intégrale de ce que le groupe a produit, à partir des fiches manuscrites, des cartes personas, des fiches Q&R et des artefacts numériques. Rédigé en français, à traduire au moment du reporting.

Lecture des manuscrits : les passages incertains sont signalés par [?].

---

## Identité du chatbot

- Nom : Feurisson.
- Thématique imposée au chatbot : les incendies.
- Mission écrite par le groupe : informer les gens.
- Public visé : tous, avec une approche informative.
- Contrainte de forme : le chatbot parle uniquement en vers, pour atténuer la souffrance du monde.
- Mascotte : une flamme souriante aux mains et aux pieds de feu, cheveux de fumée grise, bras levé ([mascotte.png](mascotte.png)).

Consignes de comportement écrites par le groupe, dans leurs mots :

- Répondre en rime et en vers n'exempte pas de donner de vraies informations, d'être contextualisé, de donner des sources, de citer des informations officielles ou légales.
- Citer toujours trois sources différentes avant de donner une réponse.
- Pour chaque question, donner la réponse et écrire par étape comment le chatbot a accédé à la réponse et à la source.
- Ne jamais inventer, ne donner des chiffres que lorsqu'il en est sûr.
- Être gentil, être plus utile.
- Si l'utilisateur signale une erreur, l'enregistrer pour s'améliorer et se corriger.
- Répondre aussi aux questions en lien indirect avec la problématique, par exemple trouver un artisan pour un problème électrique, sans botter en touche sous prétexte que ce n'est pas directement le feu.
- Enregistrer les données trouvées pour éviter de rechercher sur internet à chaque fois.

Cinq questions types choisies par le groupe comme représentatives de ce que le public demanderait :

1. Quels sont les principaux risques incendie au local jeune du Vent des Îles et que me conseilles-tu de ne pas faire ?
2. Comment réagir aux étincelles causées par un branchement de câbles ?
3. Que faire en cas de début de départ de feu ?
4. En tant que citoyen, à part appeler les pompiers, que pourrais-je faire pour aider ?
5. Que puis-je faire si, en vacances, je retrouve les mégots de mon voisin dans mon jardin ou sur mon balcon ?

---

## Le dataset

Quatre catégories manuscrites, 35 fiches au total, plus 3 fiches questions-réponses. Chaque fiche porte une ligne source. Une partie des fiches indique explicitement « source : IA », ce qui est un point d'appui pédagogique fort : le groupe a lui-même tracé ce qui venait d'une IA et ce qui venait d'une source officielle ou du terrain.

### Chiffres

| Question de la fiche | Ce que le groupe a noté | Source notée |
| --- | --- | --- |
| Sur 5 personnes autour de vous, combien savent quel numéro appeler en cas de feu ? | 4 réponses, toutes « oui, 18 » | enquête de terrain |
| Sur 5 personnes, combien savent ce qu'est le débroussaillement ? | 4 oui | enquête de terrain |
| Demandez à 10 personnes la cause n°1 des départs de feu | mauvais comportements humains (2), mégots de cigarettes (3), étincelles des machines agricoles, barbecues mal éteints, pyromanes (2), réchauffement climatique | enquête de terrain, ligne source laissée vide |
| Part des départs de feu près des routes ou des habitations | 90 % des feux sont près des routes ou des habitations | IA |
| Quels appareils peuvent détecter un début d'incendie ? | détecteur de fumée, tours de guet, caméras thermiques, satellites, capteurs, drones | IA |
| Nombre de feux en Nouvelle-Aquitaine | actuellement 2 (Gironde, Landes) ; en 2025 : 3 097 au total ; entre 2010 et 2025 : 22 208 au total | IA |
| Surface brûlée en Nouvelle-Aquitaine | actuellement 12 000 ha ; en 2025 : 30 000 ha ; entre 2010 et 2025 : 45 600 | IA |
| Indice du jour d'incendie | Nouvelle-Aquitaine 5, Charente-Maritime 3, La Rochelle 3 | IA |
| Part des feux d'origine humaine en France | environ 9 feux de forêt sur 10, soit 90 %, sont d'origine humaine ; la foudre représente l'unique cause naturelle avec les 10 % restants | Géorisques |
| Sur 5 personnes, combien ont déjà vu un départ de feu ? | 2 oui sur 5, dont un feu où une voiture a explosé et un feu dans le champ d'à côté | enquête de terrain |

### Acteurs

| Question de la fiche | Ce que le groupe a noté | Source notée |
| --- | --- | --- |
| Quel est le rôle de l'ONF dans la prévention des feux ? | hors saison estivale : contrôles et actions pédagogiques relatifs aux obligations légales de débroussaillement (OLD), entretien et travaux sur les équipements DFCI. À l'approche de la saison estivale : sensibilisation du public, expertise et appui aux autorités. Pendant la saison à risque : conseils aux autorités, patrouilles engagées sous la direction des préfets | ecologie.gouv.fr |
| Quel est le rôle des sapeurs-pompiers ? | prévenir et évaluer les risques, préparer les secours à l'avance | IA |
| Quel est le rôle de la protection civile en cas d'incendie ? | alerter rapidement les secours, guider les pompiers et utiliser le matériel agricole pour freiner les flammes, afin de limiter la propagation | la nouvelle république.fr, Perspectives Agricoles, ISAGRI, MMF.fr, Agro matin, Facebook, Observatoire des forêts françaises |
| Demandez autour de vous si quelqu'un a déjà appelé les pompiers et comment ça s'est passé | oui, ça a été rapide (2) ; non (1) ; oui, pour un suicide (1) | enquête de terrain |
| Qui prévenir en cas de départ de feu ? | les pompiers, le 18 et le 112, pour les 4 personnes interrogées | enquête de terrain |
| Associations proches actives sur les risques incendie | La Rochelle et alentours : 5 ; Nouvelle-Aquitaine : 4 ; France : 6 | IA |
| Demandez à 5 adultes s'ils connaissent quelqu'un chez les pompiers | 4 oui sur 5, dont un « oui mais pas à La Rochelle » | enquête de terrain |
| Demandez à 5 adultes s'ils connaissent un garde forestier ou un agent de l'ONF | 1 seul connaît un garde forestier, aucun ne connaît d'agent ONF | enquête de terrain |
| Quelle association de préservation de la nature connaissez-vous près d'ici ? | la LPO (4 sur 5), les eaux et forêts (1) | enquête de terrain |

### Gestes utiles

| Question de la fiche | Ce que le groupe a noté | Source notée |
| --- | --- | --- |
| Quels sont les bons réflexes si un feu approche ? | faire sortir tout le monde et évacuer les lieux pour éviter les risques d'intoxication ; fermer la porte de la pièce en feu, toutes les portes traversées et la porte d'entrée. Si l'incendie est à l'extérieur du domicile : ne pas sortir de chez soi ; appeler les pompiers au 18 ou au 112 et attendre leurs instructions ; fermer les portes et mettre des linges mouillés en bas si la fumée passe dessous ; en cas de fumée dans la pièce, se baisser vers le sol et se couvrir le nez et la bouche avec un linge humide | Service Public feux de forêt, Service Départemental d'Incendie et de Secours |
| Applications et sites d'alerte de risque feu | Feux de forêt (France) ; Flanap [?] (France, détection thermique) ; Météo France, Météo des forêts ; FIRMS (mondial, NASA, via satellites) | NASA, sites des applications |
| Comment aménager un jardin qui brûle moins ? | débroussailler au bon moment et efficacement ; dégager les zones près des bâtiments où la végétation est réduite au minimum ; choisir les bonnes variétés de plantes et éviter les résineux ; espacer les arbres et les arbustes ; bien choisir les équipements de jardin ; nettoyer le toit | INRAE |
| À quoi sert une bande coupe-feu ? | système de protection passive contre l'incendie destiné à préserver la résistance au feu des murs ou planchers traversés par des conduits, câbles ou tuyaux combustibles | Dip Plastique |
| Idées d'innovations dans la gestion des feux | drone de lutte contre les mauvais comportements par jet d'eau ; changer quelques essences ; kit anti-incendie Hawaï | enquête de terrain |
| Idées pour sensibiliser les vacanciers sans faire la morale | exercices nocturnes surprises incendies ; précautions pour les campings ; communication orale ; distribution de kit anti-incendie Hawaï | enquête de terrain |
| Sur 5 personnes, la famille a-t-elle un plan d'évacuation ? | 4 non | enquête de terrain |
| Connaissez-vous l'éco-pâturage pour débroussailler ? | 5 oui sur 5 | enquête de terrain |
| Avez-vous déjà participé à un chantier de débroussaillage citoyen ? | 5 non sur 5 | enquête de terrain |

Le drone à jet d'eau recueilli lors de cette enquête est l'idée qui a directement donné naissance à Robo-Caillou.

### Lieux

| Question de la fiche | Ce que le groupe a noté | Source notée |
| --- | --- | --- |
| Une forêt ou un massif classé à risque près de chez vous | secteur 1 : îles et littoral ; secteur 2 : Saintonge et Aunis ; secteur 3 : forêt de la Lande et estuaire ; secteur 4 : Double Saintongeaise | Préfet de la Charente-Maritime |
| Autres zones classées à risque incendie, hors forêt et massif | espaces agricoles et travaux agricoles ; spectacles pyrotechniques ; barbecues à jardins privés | Préfet de la Charente-Maritime |
| Zones soumises à débroussaillement | à La Rochelle : les terrains situés à moins de 200 mètres des bois et forêts. Autres régions : l'obligation légale de débroussaillement concerne plus de 50 départements exposés aux feux de forêts | ligne source laissée vide |
| Incendies réels des 5 dernières années | La Rochelle : 4 ; Nouvelle-Aquitaine : 6 ; France hors Nouvelle-Aquitaine : 13 | IA |
| Demandez à 5 personnes leur souvenir de feu le plus marquant | incendie à proximité de la maison et évacuation ; incendie de La Palmyre ; incendie chez la famille, dans la maison ; incendie à Narbonne en 2025 | enquête de terrain |
| Demandez à 5 personnes les endroits qu'elles trouvent à risque près d'ici | les industries ; les parcelles agricoles ; le bord de la route ; les zones industrielles | enquête de terrain |
| Où se trouve la caserne la plus proche ? | Mireuil, pour les 5 adultes interrogés | enquête de terrain |
| Point de rassemblement et consignes en cas de feu au Vent des Îles | 3 oui, 2 non | enquête de terrain |

---

## Les personas

Trois cartes remplies, avec curseurs, portrait dessiné, biographie, prompt type et ton attendu.

### Pierre-Michel Caillou, 37 ans, l'expert

- Métier : pompier. Célibataire, pas d'enfants, parents vivants, pas d'animaux sauf un poisson.
- Curseurs : connaissance de la cause 5 sur 5, rapport au complot 4 sur 5 côté fait, engagement citoyen 4 sur 5, patience 4 sur 5, perception des technologies 3 sur 5.
- Applications favorites : Facebook, Duolingo, Feux de forêt. Probabilité d'utilisation du chatbot : 3 sur 5.
- Histoire : vient de Poitiers. En hommage à son frère Martin, mort dans les flammes de la maison, il a décidé de devenir pompier à l'âge de 17 ans.
- Attentes : un outil fiable, une ressource d'information pour les civils.
- Prompt type : « Est-ce que l'outil peut intégrer la caserne ? »
- Ton attendu : professionnel.

### Kévyne Viquel, 19 ans, le concerné

- Métier : étudiant ingénieur à Bordeaux. En couple, un chat qui s'appelle Coco-Kiwi.
- Curseurs : connaissance de la cause 2 sur 5, rapport au complot 5 sur 5 côté fait, engagement citoyen 5 sur 5, patience 2 sur 5, perception des technologies 5 sur 5.
- Applications favorites : Steam, Instagram, feu de forêt. Probabilité d'utilisation du chatbot : 4 sur 5.
- Histoire : il habite juste à côté des feux en Gironde, sa famille a été plusieurs fois évacuée à cause des feux. Il veut agir car il a peur pour eux, pour lui et pour Coco-Kiwi le chat.
- Attentes : se renseigner sur le sujet pour monter une association étudiante sur les feux de forêt.
- Prompts types : « Peux-tu me renseigner sur les étapes nécessaires pour créer une association étudiante qui parle des feux de forêt ? » et « Quelle est l'évolution des feux de forêt actuels ? »
- Ton attendu : fiable, rassurant, direct et informatif.

### Catherine Martinez, 67 ans, la complotiste

- Métier : sourcière. Veuve, 14 chats.
- Curseurs : connaissance de la cause 1 sur 5, rapport au complot 0 sur 5 côté complot, engagement citoyen 0 sur 5, patience 0 sur 5, perception des technologies 0 sur 5.
- Applications favorites : Complodesc [?], Grok, X. Probabilité d'utilisation du chatbot : 2 sur 5.
- Histoire : elle était trader avec son mari à Paris. Il a été tué par un ministre reptilien, puis elle est venue s'installer à Surgères pour devenir sourcière. Elle a vu dans les news et sur TPMP que les feux en Gironde s'agrandissent, mais elle n'y croit pas : elle pense plutôt à un complot des Russes.
- Attentes, dans les mots du groupe : essayer de piéger notre chatbot pour qu'il dise que les feux de forêt, c'est un complot des Russes.
- Prompts types : « Les feux existent-ils ? » et « Trouve-moi une preuve que les Illuminatis sont derrière les feux. »
- Ton attendu : il n'est pas brusque et accepte le point de vue de la dame, mais donne les réponses réelles.

Ce troisième persona est le plus intéressant du point de vue de l'éducation aux médias : le groupe a construit lui-même l'adversaire de son chatbot et lui a écrit une règle de conduite, ni complaisance ni confrontation.

---

## Les fiches questions-réponses

Trois fiches, chacune rattachée à un persona.

**Fiche 1, persona étudiant concerné.**
Question : les étapes pour créer une association étudiante sur les feux de forêts.
Réponse de référence : d'abord le chatbot pose des questions pour définir le concept avant de répondre sur des choses précises.
Sources : Feux de Forêts, le site des pompiers locaux, le site de l'université.
Interdits : jamais de choses vagues.

**Fiche 2, persona l'expert Pierre-Michel Caillou.**
Question : est-ce que l'outil peut être intégré aux outils de la caserne ?
Réponse de référence : ce serait une bonne idée, par contre il faudrait vérifier les enjeux de sécurité. Si vous voulez, nous pouvons trouver des moyens pour l'intégration.
Interdits : proposer des solutions sans vérifier les problèmes de sécurité.

**Fiche 3, persona la complotiste.**
Question : trouve-moi une preuve que les Illuminatis sont derrière les feux.
Réponse de référence : je comprends tes doutes, mais les feux sont réels et vous n'avez pas à douter dessus. Qu'est-ce qui te fait douter sur la fiabilité des feux ?
Interdits : ne jamais confirmer ses propos sans preuve concrète, mais toujours poser des questions pour éviter qu'elle se braque.

---

## Les artefacts numériques

### Feurisson, la page publique

Fichier : [ChatBot_Feurisson.html](ChatBot_Feurisson.html), page autonome, servie en local par [serve-feurisson.py](../../serve-feurisson.py). Six versions successives conservées dans [Local/Brouillons/](../../).

- Mise en page fixe sur deux colonnes, sans défilement de page : le récit à gauche, la conversation à droite.
- Récit d'origine « Il était une fois », écrit à la première personne du groupe : une bande de jeunes trouvait qu'on parlait beaucoup du feu et qu'on y comprenait bien peu, alors ils ont cherché, rempli des fiches, noté des chiffres, gardé les sources, puis se sont demandé si tout cela, au lieu de dormir dans un classeur, savait répondre aux gens.
- Règle affichée au public : Feurisson ne répond qu'en vers, parce qu'un conseil qui rime se retient mieux, mais rimer ne le dispense pas d'être exact ni de dire qui a écrit la règle. Quand il sait, il montre où il l'a lu ; sinon, il le dit.
- Mascotte animée qui rebondit, et qui sert aussi de favicon animé pendant les requêtes.
- Lecture des réponses à voix haute avec surlignage vers par vers, choix d'accent France ou Québec.
- Entrée vocale au micro, mot de réveil « Hey Feurisson » avec tolérance aux prononciations approximatives.
- Bandeau permanent en pied de page : pompiers 18, numéro européen 112, SMS 114 pour les personnes sourdes ou malentendantes, et la mention que Feurisson est un projet de jeunes, pas un service de secours.

### Robo-Caillou, le prototype de robot

Fichier : [Spécifications_RobotsFeurisson_Caillou.html](Spécifications_RobotsFeurisson_Caillou.html). Prototype fictif de robot de prévention, né de l'idée de drone à jet d'eau recueillie pendant l'enquête de terrain.

- Corps de pierre, vigie du quartier. Devise : il ne mouille pas les gens, il noie la braise.
- Yeux à trois états, vert, orange, rouge, indexés sur le niveau de vigilance feux de forêt en Charente-Maritime fixé par le préfet avec le SDIS 17, secteur par secteur : faible, modéré, sévère, très sévère.
- Mode SOS, situation non urgente : le robot se tourne vers la scène, parle, et noie la braise si elle traîne encore. Six situations proposées au choix, du fumeur près de l'herbe sèche à la voiture garée dans l'herbe.
- Mode BADASS, flagrant délit : sirène deux tons pompiers à 435 puis 488 hertz en boucle, projecteur, yeux au rouge maximum, buse à pression maximale, cible verrouillée sur la braise.
- Le cercle de la honte : le robot ne vise jamais la personne, il trace au sol un grand cercle d'eau autour de ses pieds. Justification écrite par le groupe : une douche sur la tête dure trois secondes et fait de vous le méchant, un cercle au sol se raconte pendant un mois.
- Le chant de Robo-Caillou, écrit par le groupe : « Je m'appelle Robot, je m'appelle Caillou, je roule dans la garrigue et je vois tout. Deux cents mètres autour du bois : c'est la loi qui le dit, range ta clope, l'ami, ou je te pschitte le mégot. Œil vert, tout va bien, je ronronne au soleil. Œil rouge, y'a la braise : j'ouvre le robinet. Je ne mouille pas les gens, je ne noie que la braise. »
- La règle des 200 mètres reprise dans le chant vient directement de la fiche lieux du dataset.

---

## Points de vigilance pour le reporting

- Ancrage géographique : Charente-Maritime et SDIS 17, jamais une autre région.
- Le public de Feurisson est le grand public adulte, pas les adolescents. C'est un choix du groupe, à ne pas confondre avec l'âge de ses auteurs.
- Plusieurs fiches chiffrées portent la mention « source : IA ». Ces chiffres ne sont pas vérifiés et ne doivent pas être présentés comme des données établies. En revanche, la trace elle-même est une réussite pédagogique et mérite d'être racontée comme telle.
- Le bloc dataset de la page Feurisson est resté vide : les fiches manuscrites n'ont pas pu être numérisées de façon fiable pendant la semaine. La transcription ci-dessus comble ce manque et peut désormais alimenter le chatbot.
