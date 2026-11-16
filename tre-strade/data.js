/* Dopo le medie? Tre strade per te! — testi e dati del test (Life School Family) */
var LSF = {};

/* Link e dati da completare: lasciare "" finché non sono pronti */
LSF.config = {
  testUrl: "",
  newsletter: "",
  prenota: "",
  instagram: "",
  blog: "",
  eduki: "",
  amazon: "",
  cercaScuole: "",
  prezzo20: "[prezzo]",
  prezzo45: "[prezzo]",
  codice: "[CODICE]",
  edudoro: "", gratis: "", libro1: "", libro1nome: "", libro2: "", libro2nome: "",
  draft: true
};

LSF.families = { sci: "C", tec: "C", cos: "F", nat: "F", cuc: "F", par: "E", art: "E", mus: "E", lin: "I", per: "I", eco: "I" };

LSF.areaOrder = ["sci", "tec", "cos", "nat", "par", "lin", "art", "mus", "per", "eco", "cuc"];

LSF.areas = {
  sci: {
    name: "Numeri e scienza", color: "#4361EE",
    icon: '<path d="M9 3h6"/><path d="M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M7.5 15h9"/>',
    open: "Vuoi sapere il perché delle cose, e non ti basta la prima risposta.",
    about: "Ti piace ragionare, fare ipotesi, controllare se tornano. Un problema difficile per te è una sfida, non una punizione. Ti trovi bene dove c'è da capire come funziona il mondo.",
    schools: [
      ["L", "Se impari meglio sui libri", "liceo scientifico. Tanta matematica e fisica, insieme a latino e filosofia."],
      ["M", "Se ti piace metà teoria e metà pratica", "liceo scientifico scienze applicate, con più laboratorio e informatica. Oppure liceo tecnologico (ex istituto tecnico) di chimica e biotecnologie."],
      ["F", "Se impari facendo", "liceo professionale (ex istituto professionale) per la gestione delle acque e dell'ambiente. Analisi e controlli sul campo."]
    ],
    tryit: "Scegli una domanda che ti gira in testa e cerca la risposta in tre posti diversi. Dicono tutti la stessa cosa?",
    ask: "Quante ore alla settimana si passano davvero in laboratorio?"
  },
  tec: {
    name: "Tecnologia e informatica", color: "#7C4DDB",
    icon: '<path d="M8 8l-4 4 4 4"/><path d="M16 8l4 4-4 4"/><path d="M13 6l-2 12"/>',
    open: "Non ti basta usare le cose: vuoi sapere cosa c'è dietro lo schermo.",
    about: "Impari in fretta come funziona un'app o un dispositivo, e spesso sei tu a spiegarlo a chi ti sta intorno. Ti piace l'idea di creare qualcosa di digitale, non solo di usarlo.",
    schools: [
      ["L", "Se impari meglio sui libri", "liceo scientifico scienze applicate. Informatica come materia, con una base scientifica forte."],
      ["M", "Se ti piace metà teoria e metà pratica", "liceo tecnologico (ex istituto tecnico) di informatica e telecomunicazioni, oppure di elettronica. Si programma e si costruisce."],
      ["F", "Se impari facendo", "liceo professionale (ex istituto professionale) di manutenzione e assistenza tecnica. Impianti e apparecchi veri, da far funzionare."]
    ],
    tryit: "Prova un corso gratuito di programmazione e crea un gioco piccolo piccolo. Ti viene voglia di continuare?",
    ask: "Quali linguaggi di programmazione si imparano, e da che anno?"
  },
  cos: {
    name: "Costruire e riparare", color: "#C2570C",
    icon: '<path d="M14.5 5.5a4 4 0 0 0 4 5.5l-8.5 8.5a2.1 2.1 0 0 1-3-3L15.5 8a4 4 0 0 0-1-2.5z"/>',
    open: "Hai mani che pensano: capisci le cose mentre le fai.",
    about: "Ti piace vedere un risultato concreto, qualcosa che prima non c'era o non funzionava. Smontare, montare, aggiustare: per te è il modo più naturale di imparare.",
    schools: [
      ["L", "Se impari meglio sui libri", "liceo scientifico, pensando a ingegneria. Oppure liceo artistico a indirizzo architettura."],
      ["M", "Se ti piace metà teoria e metà pratica", "liceo tecnologico (ex istituto tecnico) di meccanica, di costruzioni, oppure di trasporti e logistica."],
      ["F", "Se impari facendo", "liceo professionale (ex istituto professionale) di manutenzione e assistenza tecnica, oppure di industria e artigianato per il Made in Italy."]
    ],
    tryit: "Ripara una cosa rotta che c'è in casa, cercando prima come si fa. Com'è andata?",
    ask: "Posso vedere le officine e i laboratori? Cosa costruiscono le classi terze?"
  },
  nat: {
    name: "Natura e ambiente", color: "#008744",
    icon: '<path d="M5 19c0-8 5-14 14-14 0 9-6 14-14 14z"/><path d="M5 19l8-8"/>',
    open: "Stai bene dove c'è qualcosa di vivo: piante, animali, aria aperta.",
    about: "Noti cose che di solito sfuggono, e ti viene naturale prendertene cura. Ti importa di come sta il pianeta, e vorresti fare qualcosa di concreto.",
    schools: [
      ["L", "Se impari meglio sui libri", "liceo scientifico, pensando a biologia, scienze naturali o veterinaria."],
      ["M", "Se ti piace metà teoria e metà pratica", "liceo tecnologico (ex istituto tecnico) agrario. Coltivazioni, allevamento, ambiente e trasformazione dei prodotti."],
      ["F", "Se impari facendo", "liceo professionale (ex istituto professionale) per l'agricoltura e lo sviluppo rurale. Tanto lavoro in campo e in azienda."]
    ],
    tryit: "Fai crescere una pianta da un seme e tieni un diario di quello che succede. Ti viene voglia di guardarla ogni giorno?",
    ask: "La scuola ha un'azienda agraria o una serra? Quanto tempo ci si passa?"
  },
  par: {
    name: "Parole, storie e idee", color: "#A06600",
    icon: '<path d="M12 7v12"/><path d="M12 7a3 3 0 0 0-3-2H4v12h5a3 3 0 0 1 3 2 3 3 0 0 1 3-2h5V5h-5a3 3 0 0 0-3 2z"/>',
    open: "Per te le parole contano: leggerle, scriverle, discuterle.",
    about: "Ti piacciono le storie, quelle inventate e quelle vere del passato. Fai domande sul perché le persone pensano e agiscono in un certo modo. Sai spiegarti, a voce o per iscritto.",
    schools: [
      ["L", "Se impari meglio sui libri", "liceo classico, con latino, greco, letteratura e filosofia. Oppure liceo delle scienze umane."],
      ["M", "Se ti piace metà teoria e metà pratica", "liceo delle scienze umane economico-sociale. Niente latino, più diritto, economia e due lingue."],
      ["F", "Se impari facendo", "liceo professionale (ex istituto professionale) per i servizi culturali e lo spettacolo. Si raccontano storie con video, audio e immagini."]
    ],
    tryit: "Scrivi una pagina su una cosa che ti è successa questa settimana e falla leggere a qualcuno. Ti è piaciuto scriverla?",
    ask: "Quanto si scrive e si discute in classe, oltre a studiare sul libro?"
  },
  lin: {
    name: "Lingue e mondo", color: "#0E7C9A",
    icon: '<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/>',
    open: "Ti incuriosisce quello che c'è fuori: altri paesi, altre parole, altri modi di vivere.",
    about: "Ti piace capire le persone e farti capire. Le lingue per te non sono una materia: sono un modo per arrivare dappertutto. Ti trovi bene quando c'è da comunicare, viaggiare, mettere in contatto.",
    schools: [
      ["L", "Se impari meglio sui libri", "liceo linguistico. Tre lingue straniere, letteratura e cultura."],
      ["M", "Se ti piace metà teoria e metà pratica", "liceo tecnologico (ex istituto tecnico) a indirizzo turismo, oppure relazioni internazionali per il marketing. Lingue insieme a economia."],
      ["F", "Se impari facendo", "liceo professionale (ex istituto professionale) per l'ospitalità alberghiera, settore accoglienza. Lingue usate ogni giorno con le persone."]
    ],
    tryit: "Guarda un episodio della tua serie preferita in lingua originale, con i sottotitoli. Poi chiediti: mi è piaciuto, o mi ha stancato?",
    ask: "Quante ore di conversazione con insegnanti madrelingua ci sono ogni settimana?"
  },
  art: {
    name: "Arte e immagine", color: "#C433AD",
    icon: '<path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="M14 7l3 3"/>',
    open: "Vedi il mondo per forme e colori, e hai voglia di metterci del tuo.",
    about: "Hai occhio: ti accorgi di quando una cosa è bella, e di quando non funziona. Ti piace creare, con la matita, con la macchina fotografica o con uno schermo.",
    schools: [
      ["L", "Se ti piace anche la teoria", "liceo artistico. Storia dell'arte e molte ore di laboratorio, con indirizzi come arti figurative, design, audiovisivo."],
      ["M", "Se ti piace metà teoria e metà pratica", "liceo tecnologico (ex istituto tecnico) di grafica e comunicazione. Immagini, stampa, video e web."],
      ["F", "Se impari facendo", "liceo professionale (ex istituto professionale) di industria e artigianato per il Made in Italy, per esempio moda. Oppure servizi culturali e spettacolo."]
    ],
    tryit: "Per una settimana fai una foto al giorno alla stessa cosa, in modi diversi. Quale ti piace di più, e perché?",
    ask: "Quali indirizzi si possono scegliere dal terzo anno, e posso vedere i lavori fatti in classe?"
  },
  mus: {
    name: "Musica, danza e sport", color: "#E02424",
    icon: '<path d="M9 18V5l10-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="16" cy="16" r="3"/>',
    open: "Ti esprimi con il corpo, con il ritmo, con l'allenamento.",
    about: "Sai cosa vuol dire ripetere una cosa cento volte finché viene bene. Hai disciplina, anche se magari non la chiami così, e dai il meglio quando ti muovi o suoni.",
    schools: [
      ["", "Se la tua passione è la musica", "liceo musicale. Due strumenti, teoria e musica d'insieme. Si entra con una prova di ammissione."],
      ["", "Se è la danza", "liceo coreutico. Danza classica e contemporanea ogni giorno. Anche qui c'è una prova."],
      ["", "Se è lo sport", "liceo scientifico a indirizzo sportivo. Più discipline sportive, insieme a diritto ed economia dello sport."],
      ["F", "Se impari facendo, dietro le quinte", "liceo professionale (ex istituto professionale) per i servizi culturali e lo spettacolo. Audio, luci e riprese."]
    ],
    tryit: "Chiedi a chi ti insegna o ti allena: \"Secondo te, su cosa devo lavorare di più?\" Ti va di farlo sul serio?",
    ask: "Com'è fatta la prova di ammissione, e quando bisogna iniziare a prepararsi?"
  },
  per: {
    name: "Persone e cura", color: "#CC3D58",
    icon: '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>',
    open: "Ti accorgi di come sta chi hai intorno, e ti viene naturale dare una mano.",
    about: "Sai ascoltare. Ti trovi bene con chi è più piccolo, con le persone anziane, con chi ha bisogno. Un lavoro senza persone intorno ti sembrerebbe vuoto.",
    schools: [
      ["L", "Se impari meglio sui libri", "liceo delle scienze umane. Psicologia, pedagogia e sociologia."],
      ["M", "Se ti piace metà teoria e metà pratica", "liceo tecnologico (ex istituto tecnico) di chimica e biotecnologie, nel percorso sanitario."],
      ["F", "Se impari facendo", "liceo professionale (ex istituto professionale) per la sanità e l'assistenza sociale. Oppure i percorsi per ottico e odontotecnico."]
    ],
    tryit: "Aiuta qualcuno più piccolo a fare i compiti, per mezz'ora. Com'è andata, per voi due?",
    ask: "Dove si fanno i tirocini: in asili, ospedali, case di riposo?"
  },
  eco: {
    name: "Economia e impresa", color: "#5F7F12",
    icon: '<path d="M5 20V10"/><path d="M12 20V4"/><path d="M19 20v-7"/><path d="M3 20h18"/>',
    open: "Ti piace organizzare, far tornare i conti, far funzionare le cose.",
    about: "Hai idee e pensi subito a come realizzarle. Sai convincere, trattare, mettere d'accordo. Ti incuriosisce come nasce un negozio, un marchio, un'azienda.",
    schools: [
      ["L", "Se impari meglio sui libri", "liceo delle scienze umane economico-sociale, oppure liceo del Made in Italy. Diritto ed economia come materie principali."],
      ["M", "Se ti piace metà teoria e metà pratica", "liceo tecnologico (ex istituto tecnico) di amministrazione, finanza e marketing."],
      ["F", "Se impari facendo", "liceo professionale (ex istituto professionale) per i servizi commerciali. Vendita, contabilità e comunicazione."]
    ],
    tryit: "Organizza una piccola vendita, di libri usati o di cose fatte da te. Quanto hai speso, quanto hai guadagnato?",
    ask: "In classe si crea un'impresa simulata, o si fanno periodi in azienda?"
  },
  cuc: {
    name: "Cucina e accoglienza", color: "#8F5A32",
    icon: '<path d="M7 3v8"/><path d="M5 3v5a2 2 0 0 0 4 0V3"/><path d="M7 11v10"/><path d="M17 21V3c-2.500 2-2.500 7 0 9"/>',
    open: "Per te far stare bene qualcuno passa da un piatto o da un benvenuto.",
    about: "Ti piace preparare, assaggiare, servire. Hai cura dei dettagli, e ti dà soddisfazione vedere le persone contente di quello che hai fatto.",
    schools: [
      ["L", "Se ti interessa il cibo come scienza", "liceo tecnologico (ex istituto tecnico) agrario, per la parte agroalimentare."],
      ["M", "Se ti piace metà teoria e metà pratica", "liceo tecnologico (ex istituto tecnico) del turismo. Lingue, territorio e ospitalità."],
      ["F", "Se impari facendo", "liceo professionale (ex istituto professionale) di enogastronomia e ospitalità alberghiera. Cucina, pasticceria, sala e accoglienza. Ci sono anche percorsi regionali di tre anni."]
    ],
    tryit: "Prepara una cena intera per la tua famiglia, dalla spesa al tavolo. Cosa ti è piaciuto di più?",
    ask: "Quante ore di cucina e di sala ci sono già dal primo anno?"
  }
};

/* s:1 = domanda sul modo di imparare (una sola risposta). Codici stile: L libri, M metà e metà, F facendo, X nessun punto */
LSF.questions = [
  { q: "Hai un pomeriggio tutto libero. Cosa fai?", o: [["Smonto qualcosa per capire come funziona.", "cos"], ["Disegno, fotografo o monto un video.", "art"], ["Aiuto qualcuno che ha un problema.", "per"], ["Cerco la risposta a una curiosità che mi gira in testa.", "sci"], ["Suono, ballo o faccio sport.", "mus"], ["Preparo qualcosa di buono da mangiare.", "cuc"], ["Leggo o scrivo una storia.", "par"], ["Sto all'aperto, tra piante e animali.", "nat"]] },
  { q: "In un lavoro di gruppo, quale parte prendi tu?", o: [["Scrivo i testi.", "par"], ["Organizzo chi fa cosa e tengo i tempi.", "eco"], ["Preparo la parte al computer.", "tec"], ["Costruisco il modellino.", "cos"], ["Curo disegni e colori.", "art"], ["Faccio i calcoli e i grafici.", "sci"], ["Cerco informazioni anche in inglese.", "lin"], ["Metto pace quando si litiga.", "per"]] },
  { q: "Sei in gita. Cosa ti resta più in mente?", o: [["Gli animali e le piante che ho visto.", "nat"], ["Le parole in un'altra lingua che ho sentito.", "lin"], ["Quello che ho mangiato, e come era preparato.", "cuc"], ["La storia del posto, raccontata dalla guida.", "par"], ["I quadri, i palazzi, i colori.", "art"], ["Come erano costruiti ponti e macchinari.", "cos"], ["I negozi: cosa vendono e quanto costa.", "eco"], ["Le persone che ho incontrato.", "per"]] },
  { q: "Ti regalano un corso gratis per un anno. Quale scegli?", o: [["Una lingua straniera.", "lin"], ["Disegno e fumetto.", "art"], ["Creare videogiochi.", "tec"], ["Musica, danza o uno sport.", "mus"], ["Esperimenti di laboratorio.", "sci"], ["Cucina e pasticceria.", "cuc"], ["Primo soccorso.", "per"], ["Falegnameria e riparazioni.", "cos"]] },
  { q: "Per imparare una cosa nuova, come ti viene meglio?", s: 1, o: [["Leggo e ci ragiono per conto mio.", "L"], ["Faccio prove ed esperimenti finché capisco.", "M"], ["Guardo qualcuno che la fa, poi provo io.", "F"], ["Dipende da cosa devo imparare.", "X"]] },
  { q: "Apri YouTube. Su quali video ti fermi?", o: [["Come si costruisce o si ripara qualcosa.", "cos"], ["Ricette e sfide in cucina.", "cuc"], ["Esperimenti e curiosità di scienza.", "sci"], ["Viaggi in altri paesi.", "lin"], ["Animali e natura.", "nat"], ["Tutorial di disegno o di moda.", "art"], ["Prove di telefoni e videogiochi.", "tec"], ["Chi racconta come ha aperto un'attività.", "eco"]] },
  { q: "A scuola si organizza una festa. Di cosa ti occupi?", o: [["Della musica e dello spettacolo.", "mus"], ["Dei soldi: quanto si spende e come.", "eco"], ["Del buffet.", "cuc"], ["Delle decorazioni.", "art"], ["Delle luci e dell'impianto audio.", "tec"], ["Di accogliere chi arriva.", "per"], ["Degli inviti e del discorso.", "par"], ["Di montare palco e tavoli.", "cos"]] },
  { q: "Quale problema ti piacerebbe risolvere da grande?", o: [["Trovare la cura per una malattia.", "sci"], ["Proteggere boschi, mari e animali.", "nat"], ["Aiutare le persone in difficoltà.", "per"], ["Inventare una tecnologia che ancora non esiste.", "tec"], ["Far capire tra loro persone di paesi diversi.", "lin"], ["Costruire case e città migliori.", "cos"], ["Raccontare storie che fanno pensare.", "par"], ["Creare un'azienda che dà lavoro a tante persone.", "eco"]] },
  { q: "Quale di queste cose ti riesce senza fatica?", o: [["Spiegare bene una cosa a qualcuno.", "per"], ["Fare calcoli a mente.", "sci"], ["Imparare una canzone o un movimento nuovo.", "mus"], ["Ricordare parole in un'altra lingua.", "lin"], ["Capire come funziona un'app nuova.", "tec"], ["Inventare storie.", "par"], ["Far crescere una pianta o accudire un animale.", "nat"], ["Far passare una mia idea.", "eco"]] },
  { q: "Quale tipo di lezione ti piace di più?", s: 1, o: [["Quella in cui si ascolta e si discute.", "L"], ["Quella in cui si fanno esperimenti.", "M"], ["Quella in cui si crea qualcosa con le mani.", "F"], ["Mi piacciono tutte allo stesso modo.", "X"]] },
  { q: "Hai 50 euro da spendere come vuoi. Cosa compri?", o: [["Colori e materiale per creare.", "art"], ["Un gioco o un accessorio per il computer.", "tec"], ["Un libro o un fumetto.", "par"], ["Attrezzi o un kit da montare.", "cos"], ["Ingredienti per una cena speciale.", "cuc"], ["Qualcosa per il mio sport o il mio strumento.", "mus"], ["Un regalo per qualcuno a cui tengo.", "per"], ["Li metto da parte e li faccio fruttare.", "eco"]] },
  { q: "Quale posto vorresti visitare dietro le quinte?", o: [["Un laboratorio di ricerca.", "sci"], ["Una fattoria o un parco naturale.", "nat"], ["La cucina di un grande ristorante.", "cuc"], ["Un ospedale.", "per"], ["Un teatro o uno studio di registrazione.", "mus"], ["Un cantiere o un'officina.", "cos"], ["Un aeroporto internazionale.", "lin"], ["La sede di una grande azienda.", "eco"]] },
  { q: "Chi ti conosce viene da te quando ha bisogno di...", o: [["Un consiglio, o qualcuno che ascolta.", "per"], ["Aiuto con i compiti di matematica.", "sci"], ["Sistemare il telefono o il computer.", "tec"], ["Un'idea per un disegno o un regalo.", "art"], ["Tradurre qualcosa.", "lin"], ["Scrivere un messaggio difficile.", "par"], ["Aggiustare la bici o un oggetto rotto.", "cos"], ["Organizzare un'uscita.", "eco"]] },
  { q: "Guardi un documentario. Quale scegli?", o: [["Lo spazio e i pianeti.", "sci"], ["Gli animali selvatici.", "nat"], ["Popoli e culture lontane.", "lin"], ["La vita di una grande figura dell'arte.", "art"], ["Come nascono robot e intelligenza artificiale.", "tec"], ["Una leggenda dello sport.", "mus"], ["Una civiltà del passato.", "par"], ["Come si prepara il cibo nel mondo.", "cuc"]] },
  { q: "Devi imparare a usare un oggetto nuovo. Cosa fai?", s: 1, o: [["Leggo le istruzioni dall'inizio alla fine.", "L"], ["Cerco di capire come funziona dentro.", "M"], ["Provo subito e imparo sbagliando.", "F"], ["Un po' di tutto, dipende dall'oggetto.", "X"]] },
  { q: "In una storia o in un videogioco, quale personaggio scegli?", o: [["Chi fa scoperte scientifiche.", "sci"], ["Chi inventa e costruisce macchine.", "cos"], ["Chi cura la squadra.", "per"], ["Chi esplora e parla con tutti i popoli.", "lin"], ["Chi fa affari.", "eco"], ["Chi incanta con la musica.", "mus"], ["Chi controlla i sistemi informatici.", "tec"], ["Chi protegge la foresta.", "nat"]] },
  { q: "Devi fare un regalo fatto da te. Cosa prepari?", o: [["Un disegno o un oggetto decorato.", "art"], ["Una torta o dei biscotti.", "cuc"], ["Una lettera o una poesia.", "par"], ["Un piccolo gioco al computer.", "tec"], ["Una canzone suonata o cantata.", "mus"], ["Un oggetto costruito in legno o cartone.", "cos"], ["Una piantina cresciuta da me.", "nat"], ["Un buono: \"ti aiuto quando serve\".", "per"]] },
  { q: "Che cosa ti dicono spesso gli adulti?", o: [["\"Hai sempre una domanda in più.\"", "sci"], ["\"Hai le mani d'oro.\"", "cos"], ["\"Sai parlare bene.\"", "par"], ["\"Hai occhio per i colori e i dettagli.\"", "art"], ["\"Hai ritmo ed energia.\"", "mus"], ["\"Sai stare con chi è più piccolo.\"", "per"], ["\"Hai il senso degli affari.\"", "eco"], ["\"Con te gli animali stanno tranquilli.\"", "nat"]] },
  { q: "Vai a vivere un anno in un posto nuovo. Dove?", o: [["In una città straniera, per imparare la lingua.", "lin"], ["In una casa in mezzo alla natura.", "nat"], ["In una città piena di musei e teatri.", "art"], ["Vicino a un centro di ricerca o a un osservatorio.", "sci"], ["In una città tecnologica, piena di novità.", "tec"], ["In un centro sportivo o in un'accademia di musica.", "mus"], ["In un posto famoso per la sua cucina.", "cuc"], ["In una città di negozi e affari.", "eco"]] },
  { q: "Come ti prepari per una verifica?", s: 1, o: [["Leggo e ripeto a voce.", "L"], ["Faccio schemi ed esercizi.", "M"], ["Mi servono esempi concreti, o provare davvero.", "F"], ["Cambio metodo ogni volta.", "X"]] },
  { q: "Nel tempo libero entri in un gruppo. Quale?", o: [["Una squadra o una banda musicale.", "mus"], ["Un gruppo di volontariato.", "per"], ["Un club di robotica.", "tec"], ["Un gruppo di teatro.", "par"], ["Un gruppo che cura un orto o un parco.", "nat"], ["Un club di scacchi e giochi di logica.", "sci"], ["Un gruppo che organizza un mercatino.", "eco"], ["Uno scambio con coetanee e coetanei di altri paesi.", "lin"]] },
  { q: "Trovi una vecchia scatola in soffitta. Cosa speri che ci sia dentro?", o: [["Un microscopio o un telescopio.", "sci"], ["Lettere e diari di tanti anni fa.", "par"], ["Attrezzi e pezzi di ricambio.", "cos"], ["Colori, pennelli e una macchina fotografica.", "art"], ["Uno strumento musicale.", "mus"], ["Un ricettario di famiglia.", "cuc"], ["Cartoline e mappe di tutto il mondo.", "lin"], ["Un vecchio computer da far ripartire.", "tec"]] },
  { q: "Quale lavoro proveresti per un giorno?", o: [["Curare le persone in ospedale.", "per"], ["Cucinare in un ristorante.", "cuc"], ["Curare gli animali o proteggere un parco.", "nat"], ["Programmare.", "tec"], ["Scrivere per un giornale.", "par"], ["Progettare case o riparare motori.", "cos"], ["Tradurre o accompagnare turisti.", "lin"], ["Gestire un negozio.", "eco"]] },
  { q: "Cosa riesci a fare a lungo senza stancarti?", o: [["Risolvere un problema difficile.", "sci"], ["Allenarmi o provare un pezzo.", "mus"], ["Disegnare o creare.", "art"], ["Leggere o scrivere.", "par"], ["Costruire qualcosa al computer.", "tec"], ["Lavorare con le mani.", "cos"], ["Ascoltare e aiutare chi ha bisogno.", "per"], ["Cucinare.", "cuc"]] },
  { q: "Tra cinque anni, come ti immagini a scuola?", s: 1, o: [["Su libri e idee, per prepararmi all'università.", "L"], ["Metà teoria e metà laboratorio.", "M"], ["A imparare un mestiere, con pratica vera.", "F"], ["Non lo so ancora.", "X"]] },
  { q: "Puoi fare una domanda a una persona esperta. A chi la fai?", o: [["A chi studia gli animali.", "nat"], ["A chi cucina in un grande ristorante.", "cuc"], ["A chi ha fondato un'azienda.", "eco"], ["A chi ha vinto nello sport o vive di musica.", "mus"], ["A chi parla dieci lingue.", "lin"], ["A chi disegna o gira film.", "art"], ["A chi ha viaggiato nello spazio.", "sci"], ["A chi scrive libri.", "par"]] },
  { q: "In che cosa hai fatto più progressi negli ultimi anni?", o: [["Nel prendermi cura di piante o animali.", "nat"], ["In cucina.", "cuc"], ["Nel gestire i miei soldi.", "eco"], ["Nello sport, nella musica o nel ballo.", "mus"], ["Nelle lingue straniere.", "lin"], ["Nel disegno.", "art"], ["Nel capire le persone.", "per"], ["Nel costruire e riparare.", "cos"]] },
  { q: "Dopo le medie, che strada ti attira di più?", s: 1, o: [["Studiare a lungo, anche dopo le superiori.", "L"], ["Un diploma che mi faccia lavorare oppure continuare.", "M"], ["Imparare presto un mestiere e iniziare a lavorare.", "F"], ["Non ci ho ancora pensato.", "X"]] }
];

LSF.phrases = {
  F: "Sul tuo podio c'è una cosa sola, detta in tre modi: impari e stai bene quando fai. Cerca una scuola dove si lavora davvero, non solo sui banchi.",
  E: "Sul tuo podio c'è una cosa sola, detta in tre modi: hai bisogno di esprimerti. Cerca una scuola che ti lasci spazio per farlo.",
  I: "Sul tuo podio c'è una cosa sola, detta in tre modi: per te contano le persone. Cerca una scuola che ti porti in mezzo alla gente.",
  CF: "Ti piace capire come funzionano le cose, e poi metterci le mani. Le scuole con tanto laboratorio sono fatte per chi è come te.",
  CE: "Hai una testa che ragiona e una che crea. Non devi sceglierne una: cerca una scuola che le tenga insieme.",
  CI: "Ti interessano le idee, e ti interessano le persone. Chi sa spiegare cose difficili in modo semplice ha proprio questo doppio talento.",
  FE: "Crei con le mani, e in quello che fai metti qualcosa di tuo. È il terreno di chi progetta, costruisce e inventa cose belle.",
  FI: "Ti piace il lavoro concreto, e ti piace farlo per qualcuno. Molti mestieri nascono proprio da qui: fare bene una cosa per chi ne ha bisogno.",
  EI: "Hai cose da dire, e ti interessa chi hai davanti. Comunicare, in tutte le sue forme, è il tuo terreno.",
  CFE: "Ragioni, costruisci e crei. Ti mancano solo le occasioni per provare tutto: gli open day servono a questo.",
  CFI: "Capisci, fai, e ti importa delle persone. Sono le tre cose che servono a chi risolve problemi veri.",
  CEI: "Idee, creatività e persone. Hai tante strade davanti, e la buona notizia è che si assomigliano più di quanto sembra.",
  FEI: "Mani, fantasia e voglia di stare con la gente. Cerca una scuola dove si lavora in gruppo e si vede il risultato.",
  CFEI: "Il tuo podio va in tante direzioni, e va bene così. Vuol dire che hai molte porte aperte: visita più scuole che puoi, e ascolta dove ti senti a casa."
};

LSF.styles = {
  L: { name: "Sui libri", row: "sui libri", text: ["Impari bene leggendo, ascoltando e ragionando.", "Ti piace capire un'idea fino in fondo prima di passare alla successiva.", "Per te vanno bene le scuole dove si studia tanta teoria, pensate per chi poi continua all'università."] },
  M: { name: "Metà teoria e metà pratica", row: "metà e metà", text: ["Capisci davvero una cosa quando la vedi funzionare.", "Ti serve la spiegazione, ma anche il laboratorio dove metterla alla prova.", "Per te vanno bene le scuole che uniscono studio ed esperienza, e che lasciano aperte due porte: lavorare o continuare a studiare."] },
  F: { name: "Facendo", row: "facendo", text: ["Impari con le mani, con il corpo, provando e riprovando.", "Stare a lungo su una sedia ti pesa, ma quando c'è da fare dai il meglio.", "Per te vanno bene le scuole con tante ore di pratica vera, dove si impara un mestiere."] },
  X: { name: "Un po' di tutto", row: "", text: ["Non hai un solo modo di imparare: cambi a seconda di quello che hai davanti.", "È una forza, perché ti adatti.", "Nei tuoi profili, leggi tutte e tre le righe e chiediti quale ti incuriosisce di più."] }
};

LSF.text = {
  welcome: ["Ciao, sono Mary.", "Faccio l'educatrice da più di vent'anni, e ho tre figli.", "Ho creato Life School Family, dove preparo materiali per imparare in modo diverso.", "Ho accompagnato tante persone della tua età in questa scelta. E ho capito una cosa: la scelta viene meglio quando parti da te, non dai consigli che ricevi.", "Per questo ho preparato questo test.", "Ti faccio delle domande, e tu rispondi pensando a te.", "Alla fine troverai un podio con le tre strade che ti somigliano di più.", "Ci vogliono circa dieci minuti."],
  howto: ["Le domande sono ventotto.", "Non ci sono risposte giuste o sbagliate: vale quello che piace a te, non quello che ci si aspetta da te.", "Di solito puoi scegliere fino a tre risposte.","In alcune domande puoi sceglierne una sola: te lo dico io quando succede.", "Se vuoi ascoltare invece di leggere, tocca l'altoparlante.", "E rispondi d'istinto: la prima idea è quasi sempre quella vera."],
  mary: ["Mary, Maria Silvia Santi, è educatrice diplomata e lavora con bambini, ragazzi e famiglie da oltre vent'anni.", "A Bologna ha fondato e guidato per quindici anni progetti di cura condivisa e sostegno alle famiglie.", "Oggi è l'anima di Life School Family, un progetto educativo dedicato all'istruzione parentale, alla pedagogia della relazione e alla neurodiversità.", "È mamma di tre figli, che segue in prima persona nel loro percorso di studio, ed è autrice di materiali didattici e di romanzi.", "Questo test nasce dalla sua esperienza: aiutare a scegliere partendo da chi si è, non da cosa ci si aspetta."]
};
