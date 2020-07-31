indic_char_map = ['0', 'N', '0', '0', 'A', 'A', 'B', 'B', 'C', 'C', 'P', 'Q', '0', 'D', 'D',
                  'D', 'E', 'E', 'E', 'E', 'F', 'F', 'F', 'F', 'G', 'H', 'H', 'H', 'H', 'G',
                  'I', 'I', 'I', 'I', 'J', 'K', 'K', 'K', 'K', 'L', 'L', 'M', 'M', 'M', 'M',
                  'N', 'A', 'P', 'P', 'Q', 'Q', 'Q', 'R', 'S', 'S', 'S', 'T', '0', '0', '0',
                  '0', 'A', 'B', 'B', 'C', 'C', 'P', 'P', 'E', 'D', 'D', 'D', 'D', 'E', 'E',
                  'E', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'E', 'F', 'F', 'F',
                  'H', 'I', 'I', 'M', 'A', 'P', 'Q', 'Q', 'Q', '0', '0', '0', '1', '2', '3',
                  '4', '5', '6', '7', '8', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                  '0', 'J', 'J', 'Q', 'P', 'P', 'F']

indic_language_chars = {
    "hi": ["ँ", "ं", "ः", "ऄ", "अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ऌ", "ऍ", "ऎ",
           "ए", "ऐ", "ऑ", "ऒ", "ओ", "औ", "क", "ख", "ग", "घ", "ङ", "च", "छ", "ज",
           "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न", "ऩ", "प", "फ",
           "ब", "भ", "म", "य", "र", "ऱ", "ल", "ळ", "ऴ", "व", "श", "ष", "स", "ह", "ऺ",
           "ऻ", "़", "ऽ", "ा", "ि", "ी", "ु", "ू", "ृ", "ॄ", "ॅ", "ॆ", "े", "ै", "ॉ",
           "ॊ", "ो", "ौ", "्", "ॎ", "ॏ", "ॐ", "॑", "॒", "॓", "॔", "ॕ", "ॖ", "ॗ", "क़",
           "ख़", "ग़", "ज़", "ड़", "ढ़", "फ़", "य़", "ॠ", "ॡ", "ॢ", "ॣ", "।", "॥", "०", "१",
           "२", "३", "४", "५", "६", "७", "८", "९", "॰", "ॱ", "ॲ", "ॳ", "ॴ", "ॵ", "ॶ", "ॷ",
           "ॸ", "ॹ", "ॺ", "ॻ", "ॼ", "ॽ", "ॾ", "ॿ"],

    "mr": ["ँ", "ं", "ः", "ऄ", "अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ऌ", "ऍ", "ऎ",
           "ए", "ऐ", "ऑ", "ऒ", "ओ", "औ", "क", "ख", "ग", "घ", "ङ", "च", "छ", "ज",
           "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न", "ऩ", "प", "फ",
           "ब", "भ", "म", "य", "र", "ऱ", "ल", "ळ", "ऴ", "व", "श", "ष", "स", "ह", "ऺ",
           "ऻ", "़", "ऽ", "ा", "ि", "ी", "ु", "ू", "ृ", "ॄ", "ॅ", "ॆ", "े", "ै", "ॉ",
           "ॊ", "ो", "ौ", "्", "ॎ", "ॏ", "ॐ", "॑", "॒", "॓", "॔", "ॕ", "ॖ", "ॗ", "क़",
           "ख़", "ग़", "ज़", "ड़", "ढ़", "फ़", "य़", "ॠ", "ॡ", "ॢ", "ॣ", "।", "॥", "०", "१",
           "२", "३", "४", "५", "६", "७", "८", "९", "॰", "ॱ", "ॲ", "ॳ", "ॴ", "ॵ", "ॶ", "ॷ",
           "ॸ", "ॹ", "ॺ", "ॻ", "ॼ", "ॽ", "ॾ", "ॿ"],

    "bn": [u"ঁ", u"ং", u"ঃ", u"঄", u"অ", u"আ", u"ই", u"ঈ", u"উ", u"ঊ", u"ঋ",
           u"ঌ", u"঍", u"঎", u"এ", u"ঐ", u"঑", u"঒", u"ও", u"ঔ", u"ক", u"খ",
           u"গ", u"ঘ", u"ঙ", u"চ", u"ছ", u"জ", u"ঝ", u"ঞ", u"ট", u"ঠ", u"ড",
           u"ঢ", u"ণ", u"ত", u"থ", u"দ", u"ধ", u"ন", u"঩", u"প", u"ফ", u"ব",
           u"ভ", u"ম", u"য", u"র", u"঱", u"ল", u"঳", u"঴", u"঵", u"শ", u"ষ",
           u"স", u"হ", u"঺", u"঻", u"়", u"ঽ", u"া", u"ি", u"ী", u"ু", u"ূ",
           u"ৃ", u"ৄ", u"৅", u"৆", u"ে", u"ৈ", u"৉", u"৊", u"ো", u"ৌ",
           u"্", u"ৎ", u"৏", u"৐", u"৑", u"৒", u"৓", u"৔", u"৕", u"৖", u"ৗ",
           u"৘", u"৙", u"৚", u"৛", u"ড়", u"ঢ়", u"৞", u"য়", u"ৠ", u"ৡ", u"ৢ",
           u"ৣ", u"৤", u"৥", u"০", u"১", u"২", u"৩", u"৪", u"৫", u"৬", u"৭",
           u"৮", u"৯", u"ৰ", u"ৱ", u"৲", u"৳", u"৴", u"৵", u"৶", u"৷", u"৸",
           u"৹", u"৺", u"৻", u"ৼ", u"৽", u"৾", u"৿"],

    "pa": [u"ਁ", u"ਂ", u"ਃ", u"਄", u"ਅ", u"ਆ", u"ਇ", u"ਈ", u"ਉ", u"ਊ", u"਋",
           u"਌", u"਍", u"਎", u"ਏ", u"ਐ", u"਑", u"਒", u"ਓ", u"ਔ", u"ਕ", u"ਖ",
           u"ਗ", u"ਘ", u"ਙ", u"ਚ", u"ਛ", u"ਜ", u"ਝ", u"ਞ", u"ਟ", u"ਠ", u"ਡ",
           u"ਢ", u"ਣ", u"ਤ", u"ਥ", u"ਦ", u"ਧ", u"ਨ", u"਩", u"ਪ", u"ਫ", u"ਬ",
           u"ਭ", u"ਮ", u"ਯ", u"ਰ", u"਱", u"ਲ", u"ਲ਼", u"਴", u"ਵ", u"ਸ਼", u"਷",
           u"ਸ", u"ਹ", u"਺", u"਻", u"਼", u"਽", u"ਾ", u"ਿ", u"ੀ", u"ੁ", u"ੂ",
           u"੃", u"੄", u"੅", u"੆", u"ੇ", u"ੈ", u"੉", u"੊", u"ੋ", u"ੌ", u"੍",
           u"੎", u"੏", u"੐", u"ੑ", u"੒", u"੓", u"੔", u"੕", u"੖", u"੗", u"੘",
           u"ਖ਼", u"ਗ਼", u"ਜ਼", u"ੜ", u"੝", u"ਫ਼", u"੟", u"੠", u"੡", u"੢", u"੣",
           u"੤", u"੥", u"੦", u"੧", u"੨", u"੩", u"੪", u"੫", u"੬", u"੭", u"੮",
           u"੯", u"ੰ", u"ੱ", u"ੲ", u"ੳ", u"ੴ", u"ੵ", u"੶", u"੷", u"੸", u"੹",
           u"੺", u"੻", u"੼", u"੽", u"੾", u"੿"],

    "gu": [u"ઁ", u"ં", u"ઃ", u"઄", u"અ", u"આ", u"ઇ", u"ઈ", u"ઉ", u"ઊ", u"ઋ",
           u"ઌ", u"ઍ", u"઎", u"એ", u"ઐ", u"ઑ", u"઒", u"ઓ", u"ઔ", u"ક", u"ખ",
           u"ગ", u"ઘ", u"ઙ", u"ચ", u"છ", u"જ", u"ઝ", u"ઞ", u"ટ", u"ઠ", u"ડ",
           u"ઢ", u"ણ", u"ત", u"થ", u"દ", u"ધ", u"ન", u"઩", u"પ", u"ફ", u"બ",
           u"ભ", u"મ", u"ય", u"ર", u"઱", u"લ", u"ળ", u"઴", u"વ", u"શ", u"ષ",
           u"સ", u"હ", u"઺", u"઻", u"઼", u"ઽ", u"ા", u"િ", u"ી", u"ુ", u"ૂ",
           u"ૃ", u"ૄ", u"ૅ", u"૆", u"ે", u"ૈ", u"ૉ", u"૊", u"ો", u"ૌ", u"્",
           u"૎", u"૏", u"ૐ", u"૑", u"૒", u"૓", u"૔", u"૕", u"૖", u"૗", u"૘",
           u"૙", u"૚", u"૛", u"૜", u"૝", u"૞", u"૟", u"ૠ", u"ૡ", u"ૢ", u"ૣ",
           u"૤", u"૥", u"૦", u"૧", u"૨", u"૩", u"૪", u"૫", u"૬", u"૭", u"૮",
           u"૯", u"૰", u"૱", u"૲", u"૳", u"૴", u"૵", u"૶", u"૷", u"૸", u"ૹ",
           u"ૺ", u"ૻ", u"ૼ", u"૽", u"૾", u"૿"],

    "or": [u"ଁ", u"ଂ", u"ଃ", u"଄", u"ଅ", u"ଆ", u"ଇ", u"ଈ", u"ଉ", u"ଊ", u"ଋ",
           u"ଌ", u"଍", u"଎", u"ଏ", u"ଐ", u"଑", u"଒", u"ଓ", u"ଔ", u"କ", u"ଖ",
           u"ଗ", u"ଘ", u"ଙ", u"ଚ", u"ଛ", u"ଜ", u"ଝ", u"ଞ", u"ଟ", u"ଠ", u"ଡ",
           u"ଢ", u"ଣ", u"ତ", u"ଥ", u"ଦ", u"ଧ", u"ନ", u"଩", u"ପ", u"ଫ", u"ବ",
           u"ଭ", u"ମ", u"ଯ", u"ର", u"଱", u"ଲ", u"ଳ", u"଴", u"ଵ", u"ଶ", u"ଷ",
           u"ସ", u"ହ", u"଺", u"଻", u"଼", u"ଽ", u"ା", u"ି", u"ୀ", u"ୁ", u"ୂ",
           u"ୃ", u"ୄ", u"୅", u"୆", u"େ", u"ୈ", u"୉", u"୊", u"ୋ", u"ୌ", u"୍",
           u"୎", u"୏", u"୐", u"୑", u"୒", u"୓", u"୔", u"୕", u"ୖ", u"ୗ", u"୘",
           u"୙", u"୚", u"୛", u"ଡ଼", u"ଢ଼", u"୞", u"ୟ", u"ୠ", u"ୡ", u"ୢ", u"ୣ",
           u"୤", u"୥", u"୦", u"୧", u"୨", u"୩", u"୪", u"୫", u"୬", u"୭", u"୮",
           u"୯", u"୰", u"ୱ", u"୲", u"୳", u"୴", u"୵", u"୶", u"୷", u"୸", u"୹",
           u"୺", u"୻", u"୼", u"୽", u"୾", u"୿"],

    "ta": [u"஁", u"ஂ", u"ஃ", u"஄", u"அ", u"ஆ", u"இ", u"ஈ", u"உ", u"ஊ", u"஋",
           u"஌", u"஍", u"எ", u"ஏ", u"ஐ", u"஑", u"ஒ", u"ஓ", u"ஔ", u"க", u"஖",
           u"஗", u"஘", u"ங", u"ச", u"஛", u"ஜ", u"஝", u"ஞ", u"ட", u"஠", u"஡",
           u"஢", u"ண", u"த", u"஥", u"஦", u"஧", u"ந", u"ன", u"ப", u"஫", u"஬",
           u"஭", u"ம", u"ய", u"ர", u"ற", u"ல", u"ள", u"ழ", u"வ", u"ஶ", u"ஷ",
           u"ஸ", u"ஹ", u"஺", u"஻", u"஼", u"஽", u"ா", u"ி", u"ீ", u"ு", u"ூ",
           u"௃", u"௄", u"௅", u"ெ", u"ே", u"ை", u"௉", u"ொ", u"ோ", u"ௌ", u"்",
           u"௎", u"௏", u"ௐ", u"௑", u"௒", u"௓", u"௔", u"௕", u"௖", u"ௗ", u"௘",
           u"௙", u"௚", u"௛", u"௜", u"௝", u"௞", u"௟", u"௠", u"௡", u"௢", u"௣",
           u"௤", u"௥", u"௦", u"௧", u"௨", u"௩", u"௪", u"௫", u"௬", u"௭", u"௮",
           u"௯", u"௰", u"௱", u"௲", u"௳", u"௴", u"௵", u"௶", u"௷", u"௸", u"௹",
           u"௺", u"௻", u"௼", u"௽", u"௾", u"௿"],

    "te": [u"ఁ", u"ం", u"ః", u"ఄ", u"అ", u"ఆ", u"ఇ", u"ఈ", u"ఉ", u"ఊ", u"ఋ",
           u"ఌ", u"఍", u"ఎ", u"ఏ", u"ఐ", u"఑", u"ఒ", u"ఓ", u"ఔ", u"క", u"ఖ",
           u"గ", u"ఘ", u"ఙ", u"చ", u"ఛ", u"జ", u"ఝ", u"ఞ", u"ట", u"ఠ", u"డ",
           u"ఢ", u"ణ", u"త", u"థ", u"ద", u"ధ", u"న", u"఩", u"ప", u"ఫ", u"బ",
           u"భ", u"మ", u"య", u"ర", u"ఱ", u"ల", u"ళ", u"ఴ", u"వ", u"శ", u"ష",
           u"స", u"హ", u"఺", u"఻", u"఼", u"ఽ", u"ా", u"ి", u"ీ", u"ు", u"ూ",
           u"ృ", u"ౄ", u"౅", u"ె", u"ే", u"ై", u"౉", u"ొ", u"ో", u"ౌ", u"్",
           u"౎", u"౏", u"౐", u"౑", u"౒", u"౓", u"౔", u"ౕ", u"ౖ", u"౗", u"ౘ",
           u"ౙ", u"ౚ", u"౛", u"౜", u"ౝ", u"౞", u"౟", u"ౠ", u"ౡ", u"ౢ", u"ౣ",
           u"౤", u"౥", u"౦", u"౧", u"౨", u"౩", u"౪", u"౫", u"౬", u"౭", u"౮",
           u"౯", u"౰", u"౱", u"౲", u"౳", u"౴", u"౵", u"౶", u"౷", u"౸", u"౹",
           u"౺", u"౻", u"౼", u"౽", u"౾", u"౿"],

    "kn": [u"ಁ", u"ಂ", u"ಃ", u"಄", u"ಅ", u"ಆ", u"ಇ", u"ಈ", u"ಉ", u"ಊ", u"ಋ",
           u"ಌ", u"಍", u"ಎ", u"ಏ", u"ಐ", u"಑", u"ಒ", u"ಓ", u"ಔ", u"ಕ", u"ಖ",
           u"ಗ", u"ಘ", u"ಙ", u"ಚ", u"ಛ", u"ಜ", u"ಝ", u"ಞ", u"ಟ", u"ಠ", u"ಡ",
           u"ಢ", u"ಣ", u"ತ", u"ಥ", u"ದ", u"ಧ", u"ನ", u"಩", u"ಪ", u"ಫ", u"ಬ",
           u"ಭ", u"ಮ", u"ಯ", u"ರ", u"ಱ", u"ಲ", u"ಳ", u"಴", u"ವ", u"ಶ", u"ಷ",
           u"ಸ", u"ಹ", u"಺", u"಻", u"಼", u"ಽ", u"ಾ", u"ಿ", u"ೀ", u"ು", u"ೂ",
           u"ೃ", u"ೄ", u"೅", u"ೆ", u"ೇ", u"ೈ", u"೉", u"ೊ", u"ೋ", u"ೌ", u"್",
           u"೎", u"೏", u"೐", u"೑", u"೒", u"೓", u"೔", u"ೕ", u"ೖ", u"೗", u"೘",
           u"೙", u"೚", u"೛", u"೜", u"ೝ", u"ೞ", u"೟", u"ೠ", u"ೡ", u"ೢ", u"ೣ",
           u"೤", u"೥", u"೦", u"೧", u"೨", u"೩", u"೪", u"೫", u"೬", u"೭", u"೮",
           u"೯", u"೰", u"ೱ", u"ೲ", u"ೳ", u"೴", u"೵", u"೶", u"೷", u"೸", u"೹",
           u"೺", u"೻", u"೼", u"೽", u"೾", u"೿"],

    "ml": [u"ഁ", u"ം", u"ഃ", u"ഄ", u"അ", u"ആ", u"ഇ", u"ഈ", u"ഉ", u"ഊ", u"ഋ",
           u"ഌ", u"഍", u"എ", u"ഏ", u"ഐ", u"഑", u"ഒ", u"ഓ", u"ഔ", u"ക", u"ഖ",
           u"ഗ", u"ഘ", u"ങ", u"ച", u"ഛ", u"ജ", u"ഝ", u"ഞ", u"ട", u"ഠ", u"ഡ",
           u"ഢ", u"ണ", u"ത", u"ഥ", u"ദ", u"ധ", u"ന", u"ഩ", u"പ", u"ഫ", u"ബ",
           u"ഭ", u"മ", u"യ", u"ര", u"റ", u"ല", u"ള", u"ഴ", u"വ", u"ശ", u"ഷ",
           u"സ", u"ഹ", u"ഺ", u"഻", u"഼", u"ഽ", u"ാ", u"ി", u"ീ", u"ു", u"ൂ",
           u"ൃ", u"ൄ", u"൅", u"െ", u"േ", u"ൈ", u"൉", u"ൊ", u"ോ", u"ൌ", u"്",
           u"ൎ", u"൏", u"൐", u"൑", u"൒", u"൓", u"ൔ", u"ൕ", u"ൖ", u"ൗ", u"൘",
           u"൙", u"൚", u"൛", u"൜", u"൝", u"൞", u"ൟ", u"ൠ", u"ൡ", u"ൢ", u"ൣ",
           u"൤", u"൥", u"൦", u"൧", u"൨", u"൩", u"൪", u"൫", u"൬", u"൭", u"൮",
           u"൯", u"൰", u"൱", u"൲", u"൳", u"൴", u"൵", u"൶", u"൷", u"൸", u"൹",
           u"ൺ", u"ൻ", u"ർ", u"ൽ", u"ൾ", u"ൿ"],

}
