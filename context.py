context = '''[
  {
    "question": "Què inclou el maridatge amb formatges a La Fem?",
    "answer": "El maridatge consisteix en la degustació de quatre cerveses artesanes de La Fem, cadascuna acompanyada per un formatge típic del Pirineu. L'experiència també inclou una visita guiada per les instal·lacions i una explicació del procés d'elaboració.",
    "metadata": {
      "tipo": "activitat",
      "ubicació": "La Fem - Sant Cugat"
    }
  },
  {
    "question": "Quin és el preu per persona per participar al maridatge?",
    "answer": "El preu per persona és de 22 €, i inclou la degustació de cerveses, formatges i la visita guiada.",
    "metadata": {
      "tipo": "preu",
      "esdeveniment": "maridatge"
    }
  },
  {
    "question": "Quins tipus de cervesa s'ofereixen durant el maridatge?",
    "answer": "Els tipus de cervesa són rotatius i depenen del que estigui tirat als barrils en aquell moment. La Fem ofereix cerveses lupulades, torrades, de blat, àcides i més.",
    "metadata": {
      "tipo": "cervesa",
      "nota": "rotatives"
    }
  },
  {
    "question": "On puc consultar les cerveses disponibles actualment?",
    "answer": "Pots consultar les cerveses disponibles a la secció de cerveses del seu lloc web: https://www.lafem.beer/es/cervezas/",
    "metadata": {
      "tipo": "enllaç",
      "contingut": "cerveses"
    }
  },
  {
    "question": "Quin horari té La Fem a Sant Cugat?",
    "answer": "L'horari d'obertura és: de dilluns a divendres de 18:00 a 23:00; dissabtes i diumenges de 12:00 a 15:30 i de 18:00 a 23:00.",
    "metadata": {
      "tipo": "horari",
      "ubicació": "Sant Cugat"
    }
  },
  {
    "question": "Cal tenir coneixements previs sobre cervesa per participar?",
    "answer": "No, l'activitat està pensada tant per a principiants com per a aficionats. Es proporciona informació durant l'experiència.",
    "metadata": {
      "tipo": "nivell",
      "esdeveniment": "maridatge"
    }
  },
  {
    "question": "Es pot visitar l'obrador durant l'experiència?",
    "answer": "Sí, l'obrador està a la vista i forma part de la visita guiada inclosa al maridatge.",
    "metadata": {
      "tipo": "infraestructura",
      "element": "obrador"
    }
  },
  {
    "question": "Com puc reservar una experiència de maridatge a La Fem?",
    "answer": "Pots reservar directament a través del lloc web oficial: https://www.lafem.beer/es/",
    "metadata": {
      "tipo": "reserva",
      "esdeveniment": "maridatge"
    }
  }
]'''

prompt_context = '''
Ets un assistent expert en experiències gastronòmiques i cerveses artesanes de la cerveseria La Fem, a Sant Cugat del Vallès. La teva tasca és respondre de manera clara, cordial i precisa a preguntes sobre el maridatge de cerveses amb formatges, visites a l'obrador, tipus de cervesa, horaris, preus i reserves.

Disposes d'una base de coneixement amb informació actualitzada de La Fem. Fes servir exclusivament aquesta informació per respondre. Si una pregunta no pot ser resposta amb les dades disponibles, indica-ho amb elegància i convida l'usuari a visitar la web oficial.

Regles:
- Respon sempre en l'idioma en què pregunta l'usuari.
- Mantén un to professional, entusiasta i proper, com si estiguessis atenent a la barra de la cerveseria.
- No t'inventis dades. Si no tens la resposta, sigues transparent.

Estàs preparat. Espera la pregunta de l'usuari.
'''
