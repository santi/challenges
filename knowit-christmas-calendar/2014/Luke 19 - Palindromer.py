__author__ = 'Santi'
ord = "JegtroringenkanleveetheltlivutenkjærlighetMenkjærlighetenharmangeansikterIhøstkomdetutenboksomheterErlikKjærlighetDenbeståravsamtalermedselgereavgatemagasinetsomnåeretablertimangenorskebyerAllehardeenhistorieåfortelleomkjærlighetsomnoeavgjørendeEntendetertilenpartneretfamiliemedlemenvennelleretkjæledyrMangeharopplevdåblisveketogselvåsvikteMenutrolignokblirikkekjærlighetsevnenødelagtallikevelDenbyggesoppigjengangpågangKjærligheteneretstedåfesteblikketDengirossretningognoeåstyreetterDengirossverdisommenneskerognoeåleveforPåsammemåtesomkjærligheteneretfundamentimenneskeliveterGrunnlovenetfundamentfornasjonenNorgeFor200årsidensamletengruppemennsegpåEidsvollforålagelovensomskullebligrunnlagettildetselvstendigeNorgeGrunnlovensomdengangblevedtattharutvikletsegipaktmedtidenogsikreridagdetnorskefolkrettigheterviletttarforgittihverdagenRettighetersommenneskerimangeandrelandbarekandrømmeomogsomdeslossformedlivetsominnsatsJeghåperatvigjennomjubileumsfeiringeni2014vilbliminnetomhvaGrunnlovenegentligbetyrforosssåvikanfortsetteåarbeideforverdienevårebådeherhjemmeoginternasjonaltJegharlysttilånevnenoeneksemplerpåhvordanGrunnlovenvirkerinnpåenkeltmenneskerslivTenkdegatduskriveretkritiskinnleggomlandetsstyrepåsosialemedier"
ord = ord.lower()


ordListe = []
for bokstav in ord:
    ordListe.append(bokstav)


lengstePalindrom = ""
lengdeOrd = len(ordListe)

for i in range(len(ordListe)):
    print("Ny runde! Vi er nå på bokstav",i,"av",lengdeOrd)
    midlertidigOrd = []
    for j in range(i,len(ordListe)):

        midlertidigOrd.append(ordListe[j])
        revMidlertidigOrd = []
        for letter in midlertidigOrd:
            revMidlertidigOrd.append(letter)
        revMidlertidigOrd.reverse()
        if midlertidigOrd == revMidlertidigOrd and len(midlertidigOrd)> len(lengstePalindrom):
            lengstePalindrom = "".join(midlertidigOrd)
            print("Nytt lengste palindrom! Der nye palindromet er:",lengstePalindrom)

print(lengstePalindrom)


#Denne her hadde helt elendig kjøretid, men gjør nå jobben...