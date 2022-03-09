import re

# If a string is passed into the part of speech tagger, this function will be called to split it into a list of strings.
def tokenize(s):
    """
    Input: String s 
    Output: List of strings
    """
    return s.split()

# This function preprocesses the text by converting all words to lowercase and stripping punctuation.

def preprocess(s, lowercase = True, strip_punctuation = True):
    """
    Input: String s or list of strings
    Output: List of strings
    """
    punctuation = ".,/?;()!«»–"
    if isinstance(s, str):
        s = tokenize(s)
    if lowercase:
        s = [t.lower() for t in s]
    if strip_punctuation:
        s = [t.strip(punctuation) for t in s]
    
    return s

# These sets of characters will enable us to determine which language the part of speech tagger should parse for.
russian_chars = r"(а||в|г|д|е|ж|з|и|й|к|л|м|н|о|п|р|с|т|у|ф|х|ц|ч|ш|щ|ь|ъ|ы|э|ю|я)"
esperanto_chars = r"(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|x)"


# The following are the Russian morphological guidelines.

rus_adj = r"(\wые$|\wая$|\wый$|\wое$|\wий$|\wие$|\wого$|\wой$|\wей$|\wую$|\wых$|\wих$|\wому$|\wым$|\wим$|\wом$|\wыми$|\wими$|^все$|^весь$|^вся$|^всю$|^всё$|\wee$)"
rus_verb = r"(\wть$|\wести$|\wаю$|\wю$|\wшь$|\wает$|\wит$|\wаем$|\wим$|\wаете$|\wите$|\wают$|\wят$|\w[аиыеу]л$|\wл[аои]$|\wс[ья]$|^этот$|^эт[оаи]$)"
rus_pron = r"(^он$|^его$|^ему$|^нем$|^им$|^оно$|^она$|^ее$|^ей$|^ней$|^ей$|^они$|^их$|^им$|^них$|^ими$|^я$|^меня$|^мне$|^мной$|^ты$|^тебя$|^тебе$|^тобой$|^мы$|^нас$|^нам$|^нами$|^вы$|^вас$|^вам$|^вами$|^то$|^того$|^том$|^тем$|^тех$|^тому$|^та$|^те$|^той$|^тот$|^ту$|^тему$|^что$|^чего$|^чему$|^чем$)"
rus_noun = r"(\wа$|\wы$|\wо$|\wи$|\w[^очен]ь$|\wя$|\w(щ|ш|р|[^о]т|п|л|к|ч|г|ф|[^пере]д|с|з|х|ц|в|б|н|м|ь|ъ)$|\wу$|\w[^о]е$)"
rus_prep = r"(^[вск](о)*$|^за$|^на$|^перед$|^между$|^по$|^от(o)*$|^у$|^без$|^из(o)*$|^о$|^под$|^про$|^через$|^сквозь$|^близ$|^вдоль$|^вместо$|^вокруг$|^для$|^до$|^из-за$|^кроме$|^мимо$|^около$|^после$)"
rus_conj = r"(^и$|^но$|^или$)"
rus_neg = r"(^не(т)*)"
rus_adv = r"(^очень$|^далеко$|^близко$|^здесь$|^там$|^справа$|^слева$|^наверху$|^внизу$|^везде$|^дома$|^где-то$|^куда-то$|^где-нибудь$|^куда-нибудь$|^налево$|^направо$|^назад$|^туда$|^обратно$|^сюда$|^вниз$|^домой$|^никуда$|\wно$)"
rus_da = r"^да$"
rus_num = r"(^один$|^дв[ае]|^три$|^четыре$|^пять$|^шесть$|^семь$|^восемь$|^девять$|^десять$|^одиннадцать$|^двенадцать$|^тринадцать$|^четырнадцать$|^пятнадцать$|^шестнадцать$|^семнадцать$|^восемнадцать$|^девятнадцать$|^двадцать$|^тридцать$|^сорок$|^пятьдесят$|^шестьдесят$|^семьдесят$|^девяносто$|^ст[оа]$|^тысяч$|^тысяч[аи]$|^[0-9]+$)"


# def is_adj(i):
#         if re.search(r"\wые$", i):
#             return True
#         elif re.search(r"\wая$", i):
#             return True
#         elif re.search(r"\wый$", i):
#             return True
#         elif re.search(r"\wое$", i):
#             return True
#         elif re.search(r"\wий$", i):
#             return True
#         elif re.search(r"\wие$", i):
#             return True
#         elif re.search(r"\wого$", i):
#             return True
#         elif re.search(r"\wой$", i):
#             return True
#         elif re.search(r"\wей$", i):
#             return True
#         elif re.search(r"\wую$", i):
#             return True
#         elif re.search(r"\wых$", i):
#             return True
#         elif re.search(r"\wих$", i):
#             return True
#         elif re.search(r"\wому$", i):
#             return True
#         elif re.search(r"\wым$", i):
#             return True
#         elif re.search(r"\wим$", i):
#             return True
#         elif re.search(r"\wом$", i):
#             return True
#         elif re.search(r"\wыми$", i):
#             return True
#         elif re.search(r"\wими$", i):
#             return True
#         if re.search(r"^все$", i):
#             return True
#         #elif re.search(r"[^все$|^весь$|^вся$|^всю$]", i):
#          #   return True     
#         else:
#             return False
   
# def is_verb(i):
#     if re.search(r"\wть$", i):
#             return True
#     elif re.search(r"\wести$", i):
#             return True
#     elif re.search(r"\wаю$", i):
#             return True
#     elif re.search(r"\wю$", i):
#             return True
#     elif re.search(r"\wшь$", i):
#             return True
#     elif re.search(r"\wает$", i):
#             return True
#     elif re.search(r"\wит$", i):
#             return True
#     elif re.search(r"\wаем$", i):
#             return True
#     elif re.search(r"\wим$", i):
#             return True
#     elif re.search(r"\wаете$", i):
#             return True
#     elif re.search(r"\wите$", i):
#             return True
#     elif re.search(r"\wают$", i):
#             return True
#     elif re.search(r"\wят$", i):
#             return True
#     elif re.search(r"\wал$", i):
#             return True
#     elif re.search(r"\wыл$", i):
#             return True
#     elif re.search(r"\wил$", i):
#             return True
#     elif re.search(r"\wла$", i):
#             return True
#     elif re.search(r"\wло$", i):
#             return True
#     elif re.search(r"\wли$", i):
#             return True
#     elif re.search(r"\wел$", i):
#             return True
#     elif re.search(r"\wул$", i):
#             return True
#     elif re.search(r"\wсь$", i):
#             return True
#     elif re.search(r"\wся$", i):
#             return True
#     elif re.search(r"(^этот$|^это$|^эта$|^эти$)", i):
#             return True
#     else:
#             return False
    
# def is_pron(i):
#     if re.search(r"(^он$|^его$|^ему$|^нем$|^им$|^оно$)", i):
#             return True
#     elif re.search(r"(^она$|^ее$|^ей$|^ней$|^ей$)", i):
#             return True
#     elif re.search(r"(^они$|^их$|^им$|^них$|^ими$)", i):
#             return True
#     elif re.search(r"(^я$|^меня$|^мне$|^мной$)", i):
#             return True
#     elif re.search(r"(^ты$|^тебя$|^тебе$|^тобой$)", i):
#             return True
#     elif re.search(r"(^мы$|^нас$|^нам$|^нами$)", i):
#             return True
#     elif re.search(r"(^вы$|^вас$|^вам$|^вами$)", i):
#             return True
#     elif re.search(r"(^то$|^того$|^том$|^тем$|^тех$|^тому$|^та$|^те$|^той$|^тот$|^ту$|^тему$)", i):
#             return True
#     elif re.search(r"(^что$|^чего$|^чему$|^чем$)", i):
#             return True
#     else:
#             return False

# def is_noun(i):
#     if re.search(r"\w[^н]а$", i):
#             return True
#     elif re.search(r"\wы$", i):
#             return True
#     elif re.search(r"\w[^в|с]о$", i):
#             return True
#     elif re.search(r"\wи$", i):
#             return True
#     elif re.search(r"\w[^очен]ь$", i):
#             return True
#     elif re.search(r"\wя$", i):
#             return True
#     elif re.search(r"\w(щ|ш|р|[^о]т|п|л|к|ч|г|ф|[^пере]д|с|з|х|ц|в|б|н|м)$", i):
#             return True
#     elif re.search(r"у$", i):
#             return True
#     elif re.search(r"\w[^о|т]е$", i):
#             return True
#     else:
#         return False

# def is_prep(i):
#     if re.search(r"^в(о)*$", i):
#             return True
#     elif re.search(r"^с(о)*$", i):
#             return True
#     elif re.search(r"^на$", i):
#             return True
#     elif re.search(r"^перед$", i):
#             return True
#     elif re.search(r"^между$", i):
#             return True
#     elif re.search(r"^к$", i):
#             return True
#     elif re.search(r"^по$", i):
#             return True
#     elif re.search(r"^от$", i):
#             return True
#     elif re.search(r"^у$", i):
#             return True
#     elif re.search(r"^без$", i):
#             return True
#     elif re.search(r"^из$", i):
#             return True
#     elif re.search(r"^о$", i):
#             return True
#     elif re.search(r"^под$", i):
#             return True
#     elif re.search(r"^про$", i):
#             return True
#     elif re.search(r"^через$", i):
#             return True
#     elif re.search(r"^сквозь$", i):
#             return True
#     elif re.search(r"^близ$", i):
#             return True
#     elif re.search(r"^вдоль$", i):
#             return True
#     elif re.search(r"^вместо$", i):
#             return True
#     elif re.search(r"^вокруг$", i):
#             return True
#     elif re.search(r"^для$", i):
#             return True
#     elif re.search(r"^до$", i):
#             return True
#     elif re.search(r"^из-за$", i):
#             return True
#     elif re.search(r"^кроме$", i):
#             return True
#     elif re.search(r"^мимо$", i):
#             return True
#     elif re.search(r"^около$", i):
#             return True
#     elif re.search(r"^после$", i):
#             return True
#     else:
#         return False

# def is_conj(i):
#     if re.search(r"^и$", i):
#             return True
#     elif re.search(r"^но$", i):
#             return True
#     elif re.search(r"^или$", i):
#             return True
#     else:
#             return False

# def is_neg(i):
#     if re.search(r"^нет*$", i):
#             return True
#     else:
#             return False

# def is_comp_adj(i):
#     if re.search(r"\wee$", i):
#             return True
#     else:
#             return False

# def is_adv(i):
#     if re.search(r"^очень$", i):
#             return True
#     else:
#             return False

# def is_da(i):
#     if re.search(r"^да$", i):
#             return True
#     else:
#             return False

# The following are the Esperanto morphological guidelines.

esp_noun = r"\wo$"
esp_plu_noun = r"\woj$"
esp_acc_noun = r"\won$"
esp_acc_plu_noun = r"\wojn$"

esp_adj = r"\wa$"
esp_plu_adj = r"\waj$"
esp_acc_adj = r"\wan$"
esp_acc_plu_adj = r"\wajn$"

esp_imp_verb = r"\wi$"
esp_pres_verb = r"\was$"
esp_past_verb = r"\wis$"
esp_future_verb = r"\wos$"
esp_cond_verb = r"\wus$"
esp_juss_verb = r"\wu$"

esp_pron = r"(^min*$|^nin*$|^vin*$|^lin*$|^ŝin*$|^ĝin*$|^ilin*$|^onin*$|^sin*$|^ĉiuj$)"

esp_prep = r"(^al$|^anstataŭ$|^laŭ$|^da$|^de$|^dum$|^el$|^je$|^krom$|^ĝis$|^malgraŭ$|^kun$|^per$|^por$|^pri$|^pro$|^sen$|^en$)"

esp_adv = r"(\we$|^nun$|^tiam$|^plej$|^pli$)"

esp_conj = r"(^ke$|^kaj$|^aŭ$|^nek$|^se$|^ĉu$|^sed$|^kiel$)"

esp_art = r"^la$"

esp_num = r"(^nul$|^unu|^du$|^tri$|^kvar$|^kvin$|^ses$|^sep$|^ok$|^naŭ$|^dek$|^cent$|^mil$|^[0-9]+$)"

esp_inter = r"(^kiu$|^kio$|^kia$|^kie$|^kiam$|^kies$|^kiel$|^kial$|^kiom$)" 

# This function allows the user to manually tag any untagged words.

# def manual_tag(tagged_dict):
#     mantag = ""
#     for key, value in tagged_dict.items():
#         if value == "":
#             mantag = input("What part of speech is " + key +" ?")
#             if not re.search(r"(?i)(^| )quit(!*|\.*)($| )", mantag):
#                 tagged_dict[key] = [mantag + "*"]
#             else:
#                 return tagged_dict
#     return tagged_dict

# Part of speech tagger. This function takes in either a string or a list of strings as input, adequately preprocesses
# the text using the tokenize and preprocess functions, and tags the text based on the appropriate morphological
# rules for the language. Given that Esperanto and Russian utilize different aphabets, the function determines which
# language it is parsing based on whether the first word in the text contains the Russian or Esperanto characters
# defined earlier.
# Additionally, the function allows the user to manually tag untagged words if manual_tag parameter is True (which it is by default).

def pos_tagger(text_string, manual_tag = True):
    # text_list will hold the tokenized and preprocessed text fed to the function
    text_list = []
    text_list = preprocess(text_string)
    # tagged_list will be a list of lists where each list within the list contains a word and its part of speech
    tagged_list = []
    # This if statement checks if there are Esperanto characters in the first word of the text, if True, 
    # The function proceeds to iterate through the words in the text and tag their parts of speech.
    # On each iteration a [word, PART OF SPEECH] list is appended to tagged_list
    if re.search(esperanto_chars, text_list[0]):
        # For each word, the program performs a regex search to determine if it matches any of the Esperanto morphological categories.
        # If the if statement returns true, the apppropriate tag is assigned to the word.
        for w in text_list:
            if re.search(esp_adj, w) and not re.search(esp_prep, w) and not re.search(esp_inter, w):
                tagged_list.append([w, "ADJ (SINGULAR)"])
            elif re.search(esp_plu_adj, w) and not re.search(esp_conj, w):
                tagged_list.append([w, "ADJ (PLURAL)"])
            elif re.search(esp_acc_adj, w) and not re.search(esp_prep, w):
                tagged_list.append([w, "ADJECTIVE (ACCUSATIVE CASE)"])
            elif re.search(esp_acc_plu_adj, w):
                tagged_list.append([w, "ADJECTIVE (PLURAL ACCUSATIVE)"])
            elif re.search(esp_adv, w) and not re.search(esp_prep, w) and not re.search(esp_conj, w) and not re.search(esp_inter, w):
                tagged_list.append([w, "ADVERB"])
            elif re.search(esp_imp_verb, w) and not re.search(esp_pron, w):
                tagged_list.append([w, "VERB (INFINITIVE MOOD)"])
            elif re.search(esp_pres_verb, w):
                tagged_list.append([w, "VERB (PRESENT TENSE)"])
            elif re.search(esp_past_verb, w):
                tagged_list.append([w, "VERB (PAST TENSE)"])
            elif re.search(esp_future_verb, w):
                tagged_list.append([w, "VERB (FUTURE TENSE)"])
            elif re.search(esp_cond_verb, w):
                tagged_list.append([w, "VERB (CONDITIONAL MOOD)"])
            elif re.search(esp_juss_verb, w) and not re.search(esp_num, w) and not re.search(esp_inter, w):
                tagged_list.append([w, "VERB (JUSSIVE MOOD)"])
            elif re.search(esp_noun, w) and not re.search(esp_prep, w) and not re.search(esp_inter, w):
                tagged_list.append([w, "NOUN (SINGULAR)"])
            elif re.search(esp_plu_noun, w):
                tagged_list.append([w, "NOUN (PLURAL)"])
            elif re.search(esp_acc_noun, w) and not re.search(esp_prep, w):
                tagged_list.append([w, "NOUN (ACCUSATIVE CASE)"])
            elif re.search(esp_acc_plu_noun, w):
                tagged_list.append([w, "NOUN (ACCUSATIVE PLURAL)"])
            elif re.search(esp_pron, w):
                tagged_list.append([w, "PRONOUN"])
            elif re.search(esp_prep, w):
                tagged_list.append([w, "PREPOSITION"])
            elif re.search(esp_conj, w):
                tagged_list.append([w, "CONJUNCTION"])
            elif re.search(esp_art, w):
                tagged_list.append([w, "ARTICLE"])
            elif re.search(esp_num, w):
                tagged_list.append([w, "NUMBER"])
            elif re.search(esp_inter, w):
                tagged_list.append([w, "INTERROGATIVE"])
            # If a word remains untagged after checking for all of the morphological categories, the program will
            # prompt the user to enter a tag manually. The [word, PART OF SPEECH] tag is then appended to tagged_list as usual.
            if manual_tag == True:
                mantag = input("What part of speech is " + w +" ?")
                tagged_list.append([w, mantag])
            else:
                tagged_list.append([w, ""])
    # Here the regex search is checking if the first word contains any Russian characters as defined earlier in russian_chars.
    elif re.search(russian_chars, text_list[0]): 
        # This section works exactly the same as the esperanto section above, but instead it uses the Russian
        # morphological guidelines.
        for w in text_list:
            if re.search(rus_adj, w):
                tagged_list.append([w, "ADJ"])
            elif re.search(rus_verb, w):
                tagged_list.append([w, "VERB"])
            elif re.search(rus_pron, w):
                tagged_list.append([w, "PRON"])
            elif re.search(rus_noun, w) and not re.search(rus_prep, w) and not re.search(rus_adv, w):
                tagged_list.append([w, "NOUN"])
            elif re.search(rus_prep, w):
                tagged_list.append([w, "PREP"])
            elif re.search(rus_conj, w):
                tagged_list.append([w, "CONJ"])
            elif re.search(rus_neg, w):
                tagged_list.append([w, "NEG"])
            elif re.search(rus_adv, w):
                tagged_list.append([w, "ADV"])
            elif re.search(rus_da, w):
                tagged_list.append([w, "WHATEVER PART OF SPEECH YES IS"])
            elif re.search(rus_num, w):
                tagged_list.append([w, "NUMBER"])
            # Once again, the user has the option of manually tagging any untagged words.
            if manual_tag == True:
                mantag = input("What part of speech is " + w +" ?")
                tagged_list.append([w, mantag])
            else:
                tagged_list.append([w, ""])
    # if untagged:
    #     manual_tag(tagged_dict)
    # Function returns the text with words tagged.
    return tagged_list    
       
# Enter the string that you want tagged here, as text_part.
text_part = "Ĉiuj homoj estas denaske liberaj kaj egalaj laŭ digno kaj rajtoj. Ili posedas racion kaj konsciencon, kaj devus konduti unu la alian en spirito de frateco."
final_dict = pos_tagger(text_part)
print(final_dict)