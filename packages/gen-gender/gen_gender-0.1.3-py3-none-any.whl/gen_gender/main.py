import pathlib
import pickle
import platform
import re
import string
from collections import Counter
from datetime import datetime

import stanza

pkl_path = str(pathlib.Path(__file__).parent.absolute()) + "/pkl/"
stanza_path = str(pathlib.Path(__file__).parent.absolute()) + "/stanza_resources"

dict_full_name = pkl_path + "dict.opcorpora"
dict_noun_male = pkl_path + "bin_dict_noun_male"
dict_not_correct_name = pkl_path + "not_correct"
dict_masc_name = pkl_path + "masc_name"
dict_femn_name = pkl_path + "fem_name"

emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F99F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F1F2-\U0001F1F4"  # Macau flag
    "\U0001F1E6-\U0001F1FF"  # flags
    "\U0001F600-\U0001F64F"
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001f926-\U0001f937"
    "\U0001F1F2"
    "\U0001F1F4"
    "\U0001F620"
    "\u200d"
    "\u2640-\u2642"
    "]+",
    flags=re.UNICODE,
)


def get_endline_symbol():
    _endline_symbol = ""
    if platform.system() == "Windows":
        _endline_symbol = "\r\n"
    elif platform.system() == "Linux":
        _endline_symbol = "\n"
    return _endline_symbol


class RunGenderSwap:
    lines_processed = 0
    list_result = []

    def __init__(
        self,
        _stanza_module,
    ):

        # ,'det' - Ну каждому свое - bad
        # advcl - Я в этом не разбираюсь, ведь я всего лишь рыбак - good
        # advcl - тогда таксистом идите, как все актеры - bad
        self.list_good_deprel = [
            "root",
            "cop",
            "amod",
            "acl:relcl",
            "ccomp",
            "mark",
            "aux",
            "orphan",
            "conj",
            "csubj",
            "obl",
            "nummod",
            "xcomp",
            "nummod:gov",
            "advcl",
            "nmod",
            "ccomp",
        ]
        self.list_good_noun = ["Я", "СЕБЯ", "ИХ", "ИМ", "МЕНЯ"]
        self.list_good_adj = ["САМ", "САМЫЙ"]
        self.list_bad_noun = [
            "ТЫ",
            "МЫ",
            "ТЕБЯ",
            "ВАС",
            "КТО",
            "КТО-ТО",
            "ВСЕ",
            "МОЙ",
            "ОН",
            "ОНО",
            "ВЫ",
            "ВСЕ",
        ]
        self.list_good_det = [
            "ЭТОТ",
            "ТОТ",
            "ТАКОЙ",
            "ТАКОВ",
            "ЭКИЙ",
            "ЭТАКИЙ",
            "СЕЙ",
            "ОНЫЙ",
        ]
        self.list_entities = []
        self.list_bad_relationships = ["ЖЕНАТ", "ЖЕНАТЫЙ", "ЖЕНИТЬСЯ"]
        self.list_wife_word = ["жена", "девушка"]
        self.nlp = _stanza_module

        self.punctuations_to_ignore = ["!", "?", "...", "?!"]

        self.is_first_sentence_processed = False
        self.unprocessed_dict_size = None
        self.is_now_sentence_separated = True
        self.previous_sentence_separated = True

        with open(dict_noun_male + ".pkl", "rb") as file:
            self.dict_replacing = pickle.load(file)
        with open(dict_full_name + ".pkl", "rb") as handler:
            self.dict_all_words_alternatives = pickle.load(handler)
        with open(dict_not_correct_name + ".pkl", "rb") as handler:
            self.dict_not_correct_words_alternatives = pickle.load(handler)
        with open(dict_not_correct_name + "_lemma.pkl", "rb") as handler:
            self.dict_not_correct_lemma = pickle.load(handler)

        self.list_timestamps_stanza_time = []
        self.list_timestamps_sent_processing = []
        self.list_timestamps_iterate = []
        self.list_timestamps_write_to_file = []

        self.dict_result = {}
        self.dict_headers = {}
        self.dict_lines = {}
        self.count_blocks = 1
        self.stop_script = False

    def write_dict_result_to_file(
        self, out_file_func, dict_result_func, dict_headers_func
    ):
        # print(process.memory_info().rss / (1024 * 1024))
        timestamp_1 = datetime.now()
        for sentence_index in dict_result_func:
            if sentence_index in dict_headers_func:
                for header in dict_headers_func[sentence_index]:
                    out_file_func.write(header)
            out_file_func.write("A:")
            for sent in dict_result_func[sentence_index]:
                out_file_func.write(sent)
            out_file_func.write(get_endline_symbol())
        self.list_timestamps_write_to_file.append(
            (datetime.now() - timestamp_1).total_seconds() * 1000
        )
        return timestamp_1

    def get_conjs_dep_list(self, list_depend_ids, dict_features):
        list_conjs_dep = []
        for dep_id in list_depend_ids:
            id = int(dep_id)
            if dict_features[id]["DEPREL"] == "conj":
                list_conjs_dep.append(id)
        return list_conjs_dep

    def is_have_good_dep_nouns(self, list_depend_ids, dict_lemma, dict_features):
        for dep_id in list_depend_ids:
            id = int(dep_id)
            if (
                dict_lemma[dict_features[id]["TEXT"].lower()].upper()
                in self.list_good_noun
            ):
                return True
        return False

    def get_nsubj_dep_count(self, list_depend_ids, dict_features):
        count = 0
        for dep_id in list_depend_ids:
            id = int(dep_id)
            if dict_features[id]["DEPREL"] == "nsubj":
                count += 1
        return count

    def is_conj_correct(self, head_id, dep_id, dict_features):
        # Я пенсионер, а до этого 40 лет работал учителем.
        if dict_features[int(head_id)]["TYPE"] == dict_features[int(dep_id)]["TYPE"]:
            for feat in dict_features[int(dep_id)]:
                # В своей молодости меня очень возмущало что старшее поколение перестает воспринимать что-то новое, и я пообещал себе что никогда не постарею душой. - gender, aspect bad
                # Сейчас кстати тоже живу в перми, недавно переехал, занимаюсь строительством - aspect
                if (
                    feat == "HEAD"
                    or feat == "TEXT"
                    or feat == "ASPECT"
                    or feat == "VOICE"
                    or feat == "DEPREL"
                    or feat == "GENDER"
                ):
                    continue
                if feat in dict_features[int(head_id)]:
                    if (
                        dict_features[int(dep_id)][feat]
                        != dict_features[int(head_id)][feat]
                    ):
                        return False
        return True

    def have_dep_adp(self, list_depend_ids, dict_features):
        for dep_id in list_depend_ids:
            id = int(dep_id)
            if dict_features[id]["TYPE"] == "ADP":
                return True
        return False

    def have_dep_case(self, list_depend_ids, dict_features):
        for dep_id in list_depend_ids:
            id = int(dep_id)
            if dict_features[id]["DEPREL"] == "case":
                return True
        return False

    def check_for_unchangeable_dependencies(
        self,
        id_head,
        dict_features,
        dict_dependencies,
        dict_lemma,
        list_divided_sentence,
        gender,
    ):
        list_depend_ids = dict_dependencies[id_head].split(",")
        list_unchangeable_ids = []
        list_changeable_ids = []
        for dep_id in list_depend_ids:
            id = int(dep_id)
            if (
                dict_features[id]["TEXT"].upper() in self.list_good_noun
                or dict_features[id]["DEPREL"].upper() in self.list_good_deprel
            ):
                return True, list_divided_sentence
            # Ну из джаза рождался рок. Ты случайно не принц на белом коне - закоментить
            if (
                dict_features[id]["TYPE"] != "UNFEATS"
                or dict_features[id]["TEXT"].upper() in self.list_bad_noun
                or dict_lemma[dict_features[id]["TEXT"].lower()].upper()
                in self.list_bad_noun
            ):
                if dict_features[id]["TEXT"] in self.list_entities and (
                    id != 1 or dict_features[id]["TYPE"].upper() == "PROPN"
                ):
                    if id in dict_dependencies:
                        if self.have_dep_adp(
                            dict_dependencies[id].split(","), dict_features
                        ):
                            continue
                    list_unchangeable_ids.append(id)
                    continue

                word_type = dict_features[id]["TYPE"]
                if "GENDER" in dict_features[id]:
                    if dict_features[id]["GENDER"] != "masc":
                        continue
                # Да на черном был, а вы
                # У меня уже есть 4 детей, соответственно на них много времени трачу, сам ассистентом работаю, кроме того кошек очень люблю - bad conj uncorrect
                if dict_features[id]["DEPREL"] == "conj" and not self.is_conj_correct(
                    dict_features[id]["HEAD"], dep_id, dict_features
                ):
                    continue
                # Всегда рад пообщаться с интересными людьми вы откуда?
                # Привет, меня зовут промобот, всегда рад пообщаться с интересными людьми вы откуда?
                if (
                    dict_lemma[dict_features[id]["TEXT"].lower()].upper() == "ВЫ"
                    and dict_features[id]["TYPE"] != "VERB"
                ):
                    continue
                # Тогда таксистом идите, как все актеры (есть "все", некорректно)
                if (
                    dict_lemma[dict_features[id]["TEXT"].lower()].upper()
                    in self.list_bad_noun
                    or dict_features[id]["TEXT"].upper() in self.list_bad_noun
                ):
                    list_unchangeable_ids.append(id)
                    continue
                elif word_type == "PRON" or word_type == "NOUN":
                    found_alternative = False
                    (
                        found_alternative,
                        list_divided_sentence,
                    ) = self.search_for_alternative(
                        id,
                        dict_features[id]["TYPE"],
                        dict_features,
                        dict_lemma,
                        list_divided_sentence,
                        gender,
                        False,
                    )
                    if not found_alternative:
                        # Ну из джаза рождался рок. (не нужно изменять root глагол)
                        # Пока сдвиги в худшую сторону, посадил зрение ношу очки (сдвиги зависят от посадил - не даст изменить)
                        # вот пару лет назад вернулся в россию(завиисмое россия - не даст сменить)
                        if id in dict_dependencies:
                            # вот пару лет назад вернулся в россию(проверка на наличие предлога перед проверкой)
                            # У меня сынок маленький - тоже тот ещё мечтатель(ограничение на noun из-за "меня")
                            # Сейчас с танцев пришел, а у вас как?
                            if word_type == "NOUN" and self.have_dep_case(
                                dict_dependencies[id].split(","), dict_features
                            ):
                                continue
                        list_unchangeable_ids.append(id)
                        continue
                    elif dict_features[id]["DEPREL"] == "obl":
                        list_changeable_ids.append(id)
        return (
            len(list_unchangeable_ids) == 0 or len(list_changeable_ids) != 0,
            list_divided_sentence,
        )

    def is_have_jena_dep(self, list_depend_ids, dict_lemma, dict_features):
        for dep_id in list_depend_ids:
            id = int(dep_id)
            if (
                dict_features[id]["DEPREL"] == "nsubj"
                and dict_lemma[dict_features[id]["TEXT"].lower()] in self.list_wife_word
            ):
                return True
        return False

    def is_correct_nsubj_deps(self, list_depend_ids, dict_features):
        list_nsubj = []
        for dep_id in list_depend_ids:
            id = int(dep_id)
            if dict_features[id]["TYPE"] == "UNFEATS":
                continue
            if dict_features[id]["DEPREL"] == "nsubj":
                list_nsubj.append(dict_features[id]["TYPE"])
            if dict_features[id]["DEPREL"] in self.list_good_deprel:
                list_nsubj.append(dict_features[id]["DEPREL"])
        dict_nsubj = dict(Counter(list_nsubj))
        if "NOUN" in dict_nsubj and len(dict_nsubj) == 1:
            return False
        else:
            return True

    def is_deprel_need_to_replace(self, id_to_check, dict_features):
        return (
            dict_features[id_to_check]["TYPE"] == "DET"
            and dict_features[id_to_check]["TEXT"].upper() in self.list_good_det
            and dict_features[id_to_check]["DEPREL"] == "det"
        )

    def is_det_head_is_good_noun(self, id_to_check, dict_features):
        id_head = dict_features[id_to_check]["HEAD"]
        return (
            dict_features[id_head]["TYPE"] == "PRON"
            and dict_features[id_head]["TEXT"].upper() in self.list_good_noun
        )

    def is_det_dependencies_adj_and_have_good_noun_dep(
        self, id_to_check, dict_features
    ):
        id_head = dict_features[id_to_check]["HEAD"]
        is_close_dep_is_head = dict_features[id_head]["HEAD"] == 0
        return (
            not is_close_dep_is_head
            and dict_features[id_head]["TYPE"] == "ADJ"
            and dict_features[dict_features[id_head]["HEAD"]]["TYPE"] == "PRON"
            and dict_features[dict_features[id_head]["HEAD"]]["TEXT"].upper()
            in self.list_good_noun
        )

    def is_det_have_dependencies_with_good_noun(
        self, id_to_check, dict_features, dict_dependencies, dict_lemma
    ):
        id_head = dict_features[id_to_check]["HEAD"]
        is_close_dep_is_head = dict_features[id_head]["HEAD"] == 0
        return is_close_dep_is_head and self.is_have_good_dep_nouns(
            dict_dependencies[id_head].split(","),
            dict_lemma,
            dict_features,
        )

    def handle_det_if_need(
        self,
        id_to_check,
        dict_features,
        dict_lemma,
        dict_dependencies,
        list_divided_sentence,
        gender,
    ):
        if self.is_deprel_need_to_replace(id_to_check, dict_features):
            if (
                self.is_det_head_is_good_noun(id_to_check, dict_features)
                or self.is_det_dependencies_adj_and_have_good_noun_dep(
                    id_to_check, dict_features
                )
                or self.is_det_have_dependencies_with_good_noun(
                    id_to_check, dict_features, dict_dependencies, dict_lemma
                )
            ):
                (found_alter, list_divided_sentence,) = self.search_for_alternative(
                    id_to_check,
                    dict_features[id_to_check]["TYPE"],
                    dict_features,
                    dict_lemma,
                    list_divided_sentence,
                    gender,
                )
                return False
        return False

    def search_for_alternative(
        self,
        id_to_search,
        type,
        dict_features,
        dict_lemma,
        list_divided_sentence,
        gender,
        replace=True,
    ):
        word_to_search = dict_features[id_to_search]["TEXT"].lower()
        if type == "NOUN" or type == "PRON":
            lemma = dict_lemma[word_to_search]
            if lemma.upper() in self.list_bad_relationships:
                lemma = "ЗАМУЖНИЙ"
            if lemma in self.dict_replacing:
                replace_word = self.dict_replacing[lemma]
                fem_lemma = replace_word.upper()
                if len(replace_word) != 0:
                    if lemma == word_to_search:
                        if not replace:
                            return True, list_divided_sentence
                        word_sentence_number = id_to_search - 1
                        list_divided_sentence[word_sentence_number] = replace_word
                        return True, list_divided_sentence
                    elif fem_lemma in self.dict_all_words_alternatives:
                        for alternative in self.dict_all_words_alternatives[fem_lemma]:
                            for (
                                alternative_features
                            ) in self.dict_all_words_alternatives[fem_lemma][
                                alternative
                            ]:
                                alternative_features_str = "".join(alternative_features)
                                case_aspect = dict_features[id_to_search]["CASE"]
                                case_matches = (
                                    alternative_features_str.find(case_aspect) != -1
                                )

                                if "NUMBER" in dict_features[id_to_search]:
                                    word_number = dict_features[id_to_search]["NUMBER"]
                                    number_matches = (
                                        alternative_features_str.find(word_number) != -1
                                    )
                                else:
                                    number_matches = True

                                skipping_words_with_bad_tag = (
                                    alternative_features_str.find("V-") != -1
                                )
                                gender_matches = (
                                    alternative_features_str.find(gender) != -1
                                )
                                if (
                                    case_matches
                                    and number_matches
                                    and gender_matches
                                    and not skipping_words_with_bad_tag
                                ):
                                    if not replace:
                                        return True, list_divided_sentence
                                    word_sentence_number = id_to_search - 1
                                    list_divided_sentence[
                                        word_sentence_number
                                    ] = alternative.lower()
                                    return True, list_divided_sentence
                    else:
                        return False, list_divided_sentence
                else:
                    return False, list_divided_sentence
            lemma_upper = lemma.upper()
            if lemma_upper in self.dict_all_words_alternatives:
                for alternative in self.dict_all_words_alternatives[lemma_upper]:
                    for alternative_features in self.dict_all_words_alternatives[
                        lemma_upper
                    ][alternative]:
                        alternative_features_str = "".join(alternative_features)
                        case_aspect = dict_features[id_to_search]["CASE"]
                        case_matches = (
                            alternative_features_str.find(case_aspect) != -1
                            or alternative_features_str.find("ADJS") != -1
                        )

                        if "NUMBER" in dict_features[id_to_search]:
                            word_number = dict_features[id_to_search]["NUMBER"]
                            number_matches = (
                                alternative_features_str.find(word_number) != -1
                            )
                        else:
                            number_matches = True

                        skipping_words_with_bad_tag = (
                            alternative_features_str.find("V-") != -1
                        )
                        gender_matches = alternative_features_str.find(gender) != -1
                        if (
                            case_matches
                            and number_matches
                            and gender_matches
                            and not skipping_words_with_bad_tag
                        ):
                            if not replace:
                                return True, list_divided_sentence
                            word_sentence_number = id_to_search - 1
                            list_divided_sentence[
                                word_sentence_number
                            ] = alternative.lower()
                            return True, list_divided_sentence
            return False, list_divided_sentence
        if type == "DET":
            lemma = dict_lemma[word_to_search]
            lemma_upper = lemma.upper()
            if lemma_upper in self.dict_all_words_alternatives:
                for alternative in self.dict_all_words_alternatives[lemma_upper]:
                    for alternative_features in self.dict_all_words_alternatives[
                        lemma_upper
                    ][alternative]:
                        alternative_features_str = "".join(alternative_features)
                        case_aspect = dict_features[id_to_search]["CASE"]
                        case_matches = (
                            alternative_features_str.find(case_aspect) != -1
                            or alternative_features_str.find("ADJS") != -1
                        )

                        if "NUMBER" in dict_features[id_to_search]:
                            word_number = dict_features[id_to_search]["NUMBER"]
                            number_matches = (
                                alternative_features_str.find(word_number) != -1
                            )
                        else:
                            number_matches = True

                        skipping_words_with_bad_tag = (
                            alternative_features_str.find("V-") != -1
                        )
                        gender_matches = alternative_features_str.find(gender) != -1
                        if (
                            case_matches
                            and number_matches
                            and gender_matches
                            and not skipping_words_with_bad_tag
                        ):
                            if not replace:
                                return True, list_divided_sentence
                            word_sentence_number = id_to_search - 1
                            list_divided_sentence[
                                word_sentence_number
                            ] = alternative.lower()
                            return True, list_divided_sentence
            return False, list_divided_sentence
        if type == "VERB":
            get_bad_relationships = False
            lemma = dict_lemma[word_to_search].upper()
            if lemma.upper() in self.list_bad_relationships:
                lemma = "ВЫЙТИ"
                get_bad_relationships = True
            if lemma == "ОБЗАВЕТЬСЯ":
                lemma = "ОБЗАВЕСТИСЬ"
            if "VARIANT" in dict_features[id_to_search]:
                if dict_features[id_to_search]["VARIANT"] == "short":
                    lemma = dict_features[id_to_search]["TEXT"].upper()
            wrong_aspect = False
            # Я был готов жениться
            if (
                get_bad_relationships
                and dict_features[id_to_search]["VERBFORM"] == "inf"
            ):
                word_sentence_number = id_to_search - 1
                list_divided_sentence[word_sentence_number] = lemma.lower() + " замуж"
                return True, list_divided_sentence
            if lemma in self.dict_all_words_alternatives:
                for alternative in self.dict_all_words_alternatives[lemma]:
                    for alternative_features in self.dict_all_words_alternatives[lemma][
                        alternative
                    ]:
                        alternative_features_str = "".join(alternative_features)
                        if (
                            alternative_features_str.find("VERB") != -1
                            or alternative_features_str.find("INFN") != -1
                            or alternative_features_str.find("PRTS") != -1
                        ):
                            if "ASPECT" in dict_features[id_to_search]:
                                word_aspect = dict_features[id_to_search]["ASPECT"]
                            else:
                                word_aspect = ""

                            if "TENSE" in dict_features[id_to_search]:
                                tense_aspect = dict_features[id_to_search]["TENSE"]
                            else:
                                tense_aspect = ""

                            aspect_matches = (
                                alternative_features_str.find(word_aspect) != -1
                                or alternative_features_str.find(tense_aspect) != -1
                            )

                            # для случаев когда совершенному глаголу в лемме выдает несовершенный
                            if (
                                not aspect_matches
                                and dict_features[id_to_search]["ASPECT"] == "perf"
                            ):
                                wrong_aspect = True

                            if "NUMBER" in dict_features[id_to_search]:
                                word_number = dict_features[id_to_search]["NUMBER"]
                            else:
                                word_number = ""
                            number_matches = (
                                alternative_features_str.find(word_number) != -1
                            )

                            word_tense = tense_aspect
                            tense_matches = (
                                alternative_features_str.find(word_tense) != -1
                            )
                            gender_matches = alternative_features_str.find(gender) != -1
                            if (
                                aspect_matches
                                and number_matches
                                and tense_matches
                                and gender_matches
                            ):
                                if not replace:
                                    return True, list_divided_sentence
                                word_sentence_number = id_to_search - 1
                                if get_bad_relationships:
                                    list_divided_sentence[word_sentence_number] = (
                                        alternative.lower() + " замуж"
                                    )
                                else:
                                    list_divided_sentence[
                                        word_sentence_number
                                    ] = alternative.lower()
                                wrong_aspect = False
                                return True, list_divided_sentence
                        else:
                            break
            if (
                wrong_aspect
            ):  # для случаев когда совершенному глаголу в лемме выдает несовершенный. Добавляем лемме "С" или "НА" в начало
                if word_to_search[0] == "с":
                    lemma = "С" + lemma
                elif word_to_search[0] == "н":
                    lemma = "НА" + lemma
                if lemma in self.dict_all_words_alternatives:
                    for alternative in self.dict_all_words_alternatives[lemma]:
                        for alternative_features in self.dict_all_words_alternatives[
                            lemma
                        ][alternative]:
                            alternative_features_str = "".join(alternative_features)
                            word_aspect = dict_features[id_to_search]["ASPECT"]
                            aspect_matches = (
                                alternative_features_str.find(word_aspect) != -1
                            )
                            word_number = dict_features[id_to_search]["NUMBER"]
                            number_matches = (
                                alternative_features_str.find(word_number) != -1
                            )
                            word_tense = dict_features[id_to_search]["TENSE"]
                            tense_matches = (
                                alternative_features_str.find(word_tense) != -1
                            )
                            gender_matches = alternative_features_str.find(gender) != -1
                            if (
                                aspect_matches
                                and number_matches
                                and tense_matches
                                and gender_matches
                            ):
                                if not replace:
                                    return True, list_divided_sentence
                                word_sentence_number = id_to_search - 1
                                if get_bad_relationships:
                                    list_divided_sentence[word_sentence_number] = (
                                        alternative.lower() + " замуж"
                                    )
                                else:
                                    list_divided_sentence[
                                        word_sentence_number
                                    ] = alternative.lower()
                                return True, list_divided_sentence
        elif type == "UNCORRECT":
            lemma_with_features = []
            # проверка на наличие слова в словаре некорректных слов
            for key in self.dict_not_correct_words_alternatives:
                if word_to_search.upper() == key[0]:
                    lemma_with_features = key
            if (
                len(lemma_with_features) != 0
            ):  # в предложение лемма из словаря некорректных
                for key in self.dict_not_correct_words_alternatives[
                    lemma_with_features
                ]:
                    str_alternative_features = "".join(
                        [
                            "".join(element)
                            for element in self.dict_not_correct_words_alternatives[
                                lemma_with_features
                            ][key]
                        ]
                    )
                    numb = dict_features[id_to_search]["NUMBER"]
                    numb_match = str_alternative_features.find(numb) != -1
                    case = dict_features[id_to_search]["CASE"]
                    case_match = str_alternative_features.find(case) != -1

                    if "TENSE" in dict_features[id_to_search]:
                        tense = dict_features[id_to_search]["TENSE"]
                        tense_match = str_alternative_features.find(tense) != -1
                    else:
                        tense_match = True

                    gen_match = str_alternative_features.find(gender) != -1
                    if numb_match and case_match and gen_match and tense_match:
                        if not replace:
                            return True, list_divided_sentence
                        word_sentence_number = id_to_search - 1
                        list_divided_sentence[word_sentence_number] = key.lower()
                        return True, list_divided_sentence
            elif (
                word_to_search.upper() in self.dict_not_correct_lemma
            ):  # в предложение некорректное слово
                lemma = tuple(self.dict_not_correct_lemma[word_to_search.upper()])
                for key in self.dict_not_correct_words_alternatives[lemma]:
                    str_alternative_features = "".join(
                        [
                            "".join(element)
                            for element in self.dict_not_correct_words_alternatives[
                                lemma
                            ][key]
                        ]
                    )
                    numb = dict_features[id_to_search]["NUMBER"]
                    numb_match = str_alternative_features.find(numb) != -1
                    case = dict_features[id_to_search]["CASE"]
                    case_match = str_alternative_features.find(case) != -1

                    if "TENSE" in dict_features[id_to_search]:
                        tense = dict_features[id_to_search]["TENSE"]
                        tense_match = str_alternative_features.find(tense) != -1
                    else:
                        tense_match = True

                    gen_match = str_alternative_features.find(gender) != -1
                    if numb_match and case_match and gen_match and tense_match:
                        if not replace:
                            return True, list_divided_sentence
                        word_sentence_number = id_to_search - 1
                        list_divided_sentence[word_sentence_number] = key.lower()
                        return True, list_divided_sentence
        elif type == "OTHER":
            lemma = dict_lemma[word_to_search].upper()
            if "VARIANT" in dict_features[id_to_search]:
                if dict_features[id_to_search]["VARIANT"] == "short":
                    lemma = dict_features[id_to_search]["TEXT"].upper()
            if lemma.upper() in self.list_bad_relationships:
                if not replace:
                    return True, list_divided_sentence
                word_sentence_number = id_to_search - 1
                list_divided_sentence[word_sentence_number] = "ЗАМУЖЕМ".lower()
                return True, list_divided_sentence
            if lemma in self.dict_all_words_alternatives:
                for alternative in self.dict_all_words_alternatives[lemma]:
                    for alternative_features in self.dict_all_words_alternatives[lemma][
                        alternative
                    ]:
                        alternative_features_str = "".join(alternative_features)
                        if "CASE" in dict_features[id_to_search]:
                            word_case = dict_features[id_to_search]["CASE"]
                            case_matches = (
                                alternative_features_str.find(word_case) != -1
                            )
                        else:
                            case_matches = True
                        if "NUMBER" in dict_features[id_to_search]:
                            word_number = dict_features[id_to_search]["NUMBER"]
                            number_matches = (
                                alternative_features_str.find(word_number) != -1
                            )
                        else:
                            number_matches = True
                        # формы с "V-" в фичах пересекаются с обычными падежами, но хз когда применяются - скипаем их
                        skipping_words_with_bad_tag = (
                            alternative_features_str.find("V-") != -1
                        )
                        gender_matches = alternative_features_str.find(gender) != -1
                        if (
                            case_matches
                            and number_matches
                            and gender_matches
                            and not skipping_words_with_bad_tag
                        ):
                            if not replace:
                                return True, list_divided_sentence
                            word_sentence_number = id_to_search - 1
                            list_divided_sentence[
                                word_sentence_number
                            ] = alternative.lower()
                            return True, list_divided_sentence
            return False, list_divided_sentence
        return False, list_divided_sentence

    def iterate_through_list(
        self,
        list_depend_ids,
        dict_features,
        dict_dependencies,
        dict_lemma,
        list_divided_sentence,
        gender,
    ):
        list_unchangeable_ids = []
        list_conj_deps = []
        is_changing = True
        for dep_id in list_depend_ids:
            found_uncorrect_obl_depend = False
            id = int(dep_id)
            dict_features[id]["TEXT"].lower()
            if (
                (
                    dict_features[id]["TYPE"] == "DET"
                    or dict_features[id]["TYPE"] == "ADJ"
                )
                and dict_features[len(dict_features)]["TEXT"] in string.punctuation
                and len(dict_features) == 2
            ):
                continue
            if dict_features[id]["TYPE"] != "UNFEATS":
                if dict_features[id]["TEXT"] not in self.list_entities or id == 1:
                    deprel = dict_features[id]["DEPREL"]
                    if self.handle_det_if_need(
                        id,
                        dict_features,
                        dict_lemma,
                        dict_dependencies,
                        list_divided_sentence,
                        gender,
                    ):
                        continue
                    if (
                        deprel == "nsubj"
                        or deprel == "root"
                        or deprel == "conj"
                        or deprel == "conj"
                        or deprel == "obj"
                    ) and dict_lemma[
                        dict_features[id]["TEXT"].lower()
                    ] in self.list_wife_word:
                        if (
                            deprel != "root"
                            and dict_features[dict_features[id]["HEAD"]]["TYPE"]
                            == "VERB"
                        ):
                            head_id = dict_features[id]["HEAD"]
                            head_type = dict_features[dict_features[id]["HEAD"]]["TYPE"]
                            (_, list_divided_sentence,) = self.search_for_alternative(
                                head_id,
                                head_type,
                                dict_features,
                                dict_lemma,
                                list_divided_sentence,
                                "masc",
                            )
                        (
                            found_alter,
                            list_divided_sentence,
                        ) = self.search_for_alternative(
                            id,
                            dict_features[id]["TYPE"],
                            dict_features,
                            dict_lemma,
                            list_divided_sentence,
                            "masc",
                        )
                        if id in dict_dependencies:
                            list_divided_sentence = self.iterate_through_list(
                                dict_dependencies[id].split(","),
                                dict_features,
                                dict_dependencies,
                                dict_lemma,
                                list_divided_sentence,
                                "masc",
                            )
                        continue
                    # а я стараюсь ограничивать сладким своего сына - good
                    # Почувствовал себя красивым - bad
                    if (
                        deprel == "obl"
                        and dict_features[id]["TYPE"] == "ADJ"
                        and dict_lemma[dict_features[id]["TEXT"].lower()].upper()
                        not in self.list_good_adj
                        and not self.is_have_good_dep_nouns(
                            dict_dependencies[dict_features[id]["HEAD"]].split(","),
                            dict_lemma,
                            dict_features,
                        )
                    ):
                        continue
                    # Тоже вернулся с улицы - ходил за детьми, забирал с сада и школы что за собака
                    if deprel == "parataxis":
                        if self.is_conj_correct(
                            dict_features[id]["HEAD"], dep_id, dict_features
                        ):
                            deprel = "conj"
                    # Я один сын у родителей, очень их люблю
                    if id in dict_dependencies:
                        if deprel == "nmod" and self.have_dep_case(
                            dict_dependencies[id].split(","), dict_features
                        ):
                            continue
                    # это прекрасное время, друг мой(conj - неправильно определен, если не совпадают фичи)
                    # я живу в небольшом городке у меня есть брат, он гитарист, а у тебя есть кто-то?
                    # Честно говоря, это редкость, когда старшие начинают разбираться в современности и идут в ногу со временем не подумайте чего плохой, я наоборот восхищен - bad check correctness
                    # if deprel == 'conj' \
                    #         and not is_conj_correct(dict_features[id]['HEAD'], dep_id, dict_features):
                    #     if __debug__:
                    #         print('Conj correctness - false. HEAD ID: ' + str(dict_features[id]['HEAD']) + ' DEP ID: ' + str(dep_id))
                    #     # continue
                    if deprel == "obl" or deprel == "conj":
                        for key in dict_features:
                            if (
                                dict_features[key]["HEAD"] == id
                                and dict_features[key]["TYPE"] == "ADP"
                            ):
                                found_uncorrect_obl_depend = True
                                break
                    # Япония интересная страна, но сам никогда там не был
                    if not (
                        dict_lemma[dict_features[id]["TEXT"].lower()].upper()
                        in self.list_good_adj
                        and dict_features[id]["DEPREL"] == "nsubj"
                        and self.get_nsubj_dep_count(
                            dict_dependencies[dict_features[id]["HEAD"]].split(","),
                            dict_features,
                        )
                        < 2
                    ):
                        # and dict_features[id]['TYPE'] != 'ADJ': #Это я к предыдущему
                        if (
                            deprel not in self.list_good_deprel
                            or found_uncorrect_obl_depend
                        ) and (
                            dict_features[id]["TEXT"].upper() not in self.list_good_noun
                            and gender != "masc"
                        ):
                            if id in dict_dependencies:
                                list_divided_sentence = self.iterate_through_list(
                                    dict_dependencies[id].split(","),
                                    dict_features,
                                    dict_dependencies,
                                    dict_lemma,
                                    list_divided_sentence,
                                    gender,
                                )
                            continue

                    # Сын родился сегодня - не изменяем, если есть только nsubj зависимость, без корректных из list_good_deprel
                    if id in dict_dependencies:
                        if not self.is_correct_nsubj_deps(
                            dict_dependencies[id].split(","), dict_features
                        ) and not self.is_have_jena_dep(
                            dict_dependencies[id].split(","), dict_lemma, dict_features
                        ):
                            continue
                        (
                            changeable,
                            list_divided_sentence,
                        ) = self.check_for_unchangeable_dependencies(
                            id,
                            dict_features,
                            dict_dependencies,
                            dict_lemma,
                            list_divided_sentence,
                            gender,
                        )
                        is_changing = changeable

                    if "GENDER" in dict_features[id]:
                        word_type = dict_features[id]["TYPE"]
                        word_gender = dict_features[id]["GENDER"]
                        have_wife_dep = False
                        if id in dict_dependencies:
                            have_wife_dep = self.is_have_jena_dep(
                                dict_dependencies[id].split(","),
                                dict_lemma,
                                dict_features,
                            )
                        # существительное или местоимение
                        if (
                            word_type == "NOUN" or word_type == "PRON"
                        ) and word_gender == "masc":  # Да, я еще отец 2 детей. Ты случайно не принц на белом коне?
                            # если у слова нет женского рода - не изменяем зависимые
                            if is_changing:
                                #     list_unchangeable_ids = check_for_unchangeable_dependencies(dict_dependencies[id].split(','),dict_features,dict_dependencies, dict_lemma)
                                # if len(list_unchangeable_ids) == 0:  # проверяем на наличие неизменяемых зависимостей
                                # if not search_for_alternative(id,dict_features[id]['TYPE']) and dict_features[id]['TEXT'].upper() not in list_good_noun:
                                # Я сам из казахстана, пока учусь на третьем курсе в агау, буду ветврачом, подрабатываю после учебы курьером в грильнице(dict_features[id]['DEPREL'] != 'root') - good
                                # Добрый день(dict_features[id]['DEPREL'] != 'root') - bad
                                found_alter = False
                                (
                                    found_alter,
                                    list_divided_sentence,
                                ) = self.search_for_alternative(
                                    id,
                                    dict_features[id]["TYPE"],
                                    dict_features,
                                    dict_lemma,
                                    list_divided_sentence,
                                    gender,
                                )
                                if (
                                    not found_alter
                                    and dict_features[id]["TEXT"].upper()
                                    not in self.list_good_noun
                                ):
                                    # проверяем conj-зависимости, за ними могут быть изменяемые слова
                                    if id in dict_dependencies:
                                        list_conj_deps = self.get_conjs_dep_list(
                                            dict_dependencies[id].split(","),
                                            dict_features,
                                        )
                                    if len(list_conj_deps) == 0:
                                        continue
                            else:
                                continue
                        # глагол
                        elif word_type == "VERB" and word_gender == "masc":
                            if is_changing:
                                #     list_unchangeable_ids = check_for_unchangeable_dependencies(dict_dependencies[id].split(','),dict_features,dict_dependencies)
                                # if len(list_unchangeable_ids) == 0: #если есть неизменяемое существительное или местоимение - не изменяем
                                found_alter = False
                                (
                                    found_alter,
                                    list_divided_sentence,
                                ) = self.search_for_alternative(
                                    id,
                                    dict_features[id]["TYPE"],
                                    dict_features,
                                    dict_lemma,
                                    list_divided_sentence,
                                    gender,
                                )
                                if (
                                    not found_alter
                                    and dict_features[id]["TEXT"].upper()
                                    not in self.list_good_noun
                                ):
                                    # проверяем conj-зависимости, за ними могут быть изменяемые слова
                                    if id in dict_dependencies:
                                        list_conj_deps = self.get_conjs_dep_list(
                                            dict_dependencies[id].split(","),
                                            dict_features,
                                        )
                                    if len(list_conj_deps) == 0:
                                        continue
                            else:
                                continue
                        # из словаря некорректных
                        elif word_type == "UNCORRECT" and word_gender == "masc":
                            if is_changing:
                                #     list_unchangeable_ids = check_for_unchangeable_dependencies(dict_dependencies[id].split(','),dict_features,dict_dependencies)
                                # if len(list_unchangeable_ids) == 0:  # если есть неизменяемое существительное или местоимение - не изменяем
                                found_alter = False
                                (
                                    found_alter,
                                    list_divided_sentence,
                                ) = self.search_for_alternative(
                                    id,
                                    dict_features[id]["TYPE"],
                                    dict_features,
                                    dict_lemma,
                                    list_divided_sentence,
                                    gender,
                                )
                            else:
                                continue
                        # остальное
                        # Какой у вас бизнес?(проверка изменяемых зависимостей)
                        elif (word_gender == "masc" and gender == "femn") or (
                            word_gender == "fem" and gender == "masc"
                        ):
                            if is_changing:
                                #     list_unchangeable_ids = check_for_unchangeable_dependencies(dict_dependencies[id].split(','),dict_features,dict_dependencies)
                                # if len(list_unchangeable_ids) == 0:  # если есть неизменяемое существительное или местоимение - не изменяем
                                found_alter = False
                                (
                                    found_alter,
                                    list_divided_sentence,
                                ) = self.search_for_alternative(
                                    id,
                                    "OTHER",
                                    dict_features,
                                    dict_lemma,
                                    list_divided_sentence,
                                    gender,
                                )
                            else:
                                continue
                        elif (word_gender == "neut" and deprel != "root") or (
                            word_gender == "fem" and not have_wife_dep
                        ):
                            continue
                    # Да ничего сложного нет главное желание(continue)
                    # Мне тоже, я люблю быть дома один, мне эио часто удаётся, мы с мамой работаем в разное время, а в каком городе ты живёшь?(ignore)
                    # Я вот хочу стать гонщиком(стать без рода - не скипаем глаголы)
                    elif (
                        deprel != "root"
                        and dict_features[id]["TYPE"] != "VERB"
                        and dict_features[id]["TEXT"].upper() not in self.list_good_noun
                    ):
                        continue
                    elif (
                        dict_lemma[dict_features[id]["TEXT"].lower()].upper()
                        in self.list_bad_relationships
                    ):
                        (
                            found_alter,
                            list_divided_sentence,
                        ) = self.search_for_alternative(
                            id,
                            dict_features[id]["TYPE"],
                            dict_features,
                            dict_lemma,
                            list_divided_sentence,
                            gender,
                        )

            # итерировать только через изменяемые
            if len(list_conj_deps) != 0:
                list_divided_sentence = self.iterate_through_list(
                    list_conj_deps,
                    dict_features,
                    dict_dependencies,
                    dict_lemma,
                    list_divided_sentence,
                    gender,
                )
            elif id in dict_dependencies:
                list_dependencies = dict_dependencies[id].split(",")
                [x for x in list_dependencies if x not in list_unchangeable_ids]
                list_divided_sentence = self.iterate_through_list(
                    dict_dependencies[id].split(","),
                    dict_features,
                    dict_dependencies,
                    dict_lemma,
                    list_divided_sentence,
                    gender,
                )
        return list_divided_sentence

    def make_divided_feature_from_ucorrect(self, list_features_uncorrect):
        dict_features_divided = {}
        list_features_cur_word = list_features_uncorrect.split(",")
        if len(list_features_cur_word) == 4:
            dict_features_divided["GENDER"] = list_features_cur_word[0]
            dict_features_divided["NUMBER"] = list_features_cur_word[1]
            dict_features_divided["TENSE"] = list_features_cur_word[2]
            dict_features_divided["CASE"] = list_features_cur_word[3]
        elif len(list_features_cur_word) == 3:
            dict_features_divided["GENDER"] = list_features_cur_word[0]
            dict_features_divided["NUMBER"] = list_features_cur_word[1]
            dict_features_divided["CASE"] = list_features_cur_word[2]
        else:
            dict_features_divided["NUMBER"] = list_features_cur_word[0]
            dict_features_divided["CASE"] = list_features_cur_word[1]
        dict_features_divided["TYPE"] = "UNCORRECT"
        return dict_features_divided

    def divide_sentences_bulk(self, dict_to_divide):
        list_sentences_func = []
        regex_sentence = r"[\s\S]+?[\.\?\!]."
        regex_sentence_end = "([a-zа-яё0-9])$"
        for sent_index in dict_to_divide:
            # list_orig_sent_tmp = sent_index
            # for sentence in list_orig_sent_tmp:
            for sent in dict_to_divide[sent_index]:
                orig_sent_tmp = re.search(regex_sentence, sent)
                if orig_sent_tmp:
                    # next_string = re.sub(regex_sentence, '', sentence, 1)
                    cur_string = orig_sent_tmp.group()
                    cur_string = cur_string.replace("...", ".")
                    cur_string = cur_string.replace("..", ".")
                    regex_combine_spaces = re.compile(r"\s+")
                    cur_string = regex_combine_spaces.sub(" ", cur_string).strip()
                    orig_sent_end_of_sent = re.search(regex_sentence_end, cur_string)
                    if orig_sent_end_of_sent:
                        cur_string = cur_string + " ."
                    list_sentences_func.append(cur_string)
                elif len(sent) != 0:
                    sentence = sent
                    orig_sent_end_of_sent = re.search(regex_sentence_end, sentence)
                    if orig_sent_end_of_sent:
                        sentence = sentence + " ."
                    list_sentences_func.append(sentence)
        return list_sentences_func

    def process_sent(self, sentences_tmp, dict_result):
        result_sent = ""
        str_sentence = ""
        head_id = 0
        start_time = datetime.now()

        doc = self.nlp(sentences_tmp)

        timestamp_1 = datetime.now()
        self.list_timestamps_stanza_time.append(
            (timestamp_1 - start_time).total_seconds() * 1000
        )

        for sent in doc.sentences:
            for ent in sent.ents:
                self.list_entities.append(ent.text)

        for sent in doc.sentences:
            # ключ - слово от которого зависят слова, которые записаны в значения
            dict_dependencies = {}
            dict_features = {}  # слово и морфологические признаки
            dict_lemma = {}  # слово и его лемма

            remove_sent_text = False
            skip_to_next_sent = False
            # sentence_index = dict_lines[sent.text]
            for sent_index in self.dict_lines:
                if sent.text in self.dict_lines[sent_index]:
                    sentence_index = sent_index
                    remove_sent_text = True
                    break
                elif len(self.dict_lines[sent_index][0]) == 0:
                    continue
                else:
                    skip_to_next_sent = True

            if skip_to_next_sent:
                continue
            elif remove_sent_text:
                if isinstance(self.dict_lines[sentence_index], list):
                    self.dict_lines[sentence_index].pop(
                        self.dict_lines[sentence_index].index(sent.text)
                    )
                if len(self.dict_lines[sentence_index]) == 0:
                    del self.dict_lines[sentence_index]

            list_divided_sentence = []
            for word in sent.words:
                list_divided_sentence.append(word.text)

            for word in sent.words:
                if word.head <= 0:
                    head_id = word.id
                    dict_dependencies["root"] = [head_id]

                dict_dependencies[word.head] = (
                    dict_dependencies[word.head] + ","
                    if word.head in dict_dependencies
                    else ""
                ) + str(word.id)
                dict_features_divided = {}
                lemma_with_features = []

                # проверка на наличие слова в словаре некорректных слов
                for key in self.dict_not_correct_words_alternatives:
                    if word.text.upper() == key[0]:
                        lemma_with_features = key

                if (
                    len(lemma_with_features) != 0
                ):  # в предложение лемма из словаря некорректных
                    list_features_cur_word = lemma_with_features[1].split()
                    if len(list_features_cur_word) == 2:
                        dict_features_divided = self.make_divided_feature_from_ucorrect(
                            list_features_cur_word[1]
                        )
                    else:
                        dict_features_divided = self.make_divided_feature_from_ucorrect(
                            "".join(list_features_cur_word)
                        )
                    del lemma_with_features
                elif (
                    word.text.upper() in self.dict_not_correct_lemma
                ):  # в предложение некорректное слово
                    lemma = tuple(self.dict_not_correct_lemma[word.text.upper()])
                    str_alternative_features = "".join(
                        [
                            "".join(element)
                            for element in self.dict_not_correct_words_alternatives[
                                lemma
                            ][word.text.upper()]
                        ]
                    )
                    list_features_cur_word = str_alternative_features.split()[1]
                    dict_features_divided = self.make_divided_feature_from_ucorrect(
                        list_features_cur_word
                    )
                    del lemma
                else:
                    if word.feats:
                        list_features = word.feats.split("|")
                        if len(list_features) == 1:
                            dict_features_divided["TYPE"] = "UNFEATS"
                        else:
                            for feature in list_features:
                                list_divided_feature = feature.split("=")
                                feature_name = list_divided_feature[0].upper()
                                dict_features_divided[
                                    feature_name
                                ] = list_divided_feature[1].lower()
                            if word.upos == "AUX":
                                dict_features_divided["TYPE"] = "VERB"
                            else:
                                dict_features_divided["TYPE"] = word.upos
                            for key in dict_features_divided:
                                if key == "ASPECT":
                                    # в словаре dict.opcorpora.txt иначе названы падежи, по сравнению со stanza
                                    if dict_features_divided[key] == "imp":
                                        dict_features_divided[key] = "impf"
                                if key == "CASE":
                                    # в словаре dict.opcorpora.txt иначе названы падежи, по сравнению со stanza
                                    if dict_features_divided[key] == "ins":
                                        dict_features_divided[key] = "ablt"
                    # понадобиться для определения переводимости obl-зависимости
                    elif word.upos == "ADP" and word.text != "на":
                        dict_features_divided["TYPE"] = "ADP"
                    else:
                        dict_features_divided["TYPE"] = "UNFEATS"

                dict_features_divided["HEAD"] = word.head
                dict_features_divided["DEPREL"] = word.deprel
                dict_features_divided["TEXT"] = word.text

                dict_features[word.id] = dict_features_divided.copy()
                del dict_features_divided
                dict_lemma[word.text.lower()] = word.lemma

            timestamp_2 = datetime.now()
            self.list_timestamps_sent_processing.append(
                (timestamp_2 - timestamp_1).total_seconds() * 1000
            )

            list_divided_sentence = self.iterate_through_list(
                dict_dependencies["root"],
                dict_features,
                dict_dependencies,
                dict_lemma,
                list_divided_sentence,
                "femn",
            )

            # print(list_divided_sentence)

            list_divided_sentence[0] = list_divided_sentence[0].capitalize()

            for word in list_divided_sentence:
                if word not in string.punctuation or word == "-":
                    str_sentence += " "
                str_sentence += word

            timestamp_3 = datetime.now()
            self.list_timestamps_iterate.append(
                (timestamp_3 - timestamp_2).total_seconds() * 1000
            )

            str_sentence = str_sentence[1:]
            result_sent += str_sentence + " "
            if sentence_index in dict_result:
                dict_result[sentence_index] = dict_result[sentence_index] + [
                    result_sent
                ]
            else:
                dict_result[sentence_index] = [result_sent]
            # print(result_sent)
            str_sentence = ""
            result_sent = ""

    def process_bulk(self, out_file=None):
        list_sentences = self.divide_sentences_bulk(self.dict_lines)

        str_to_process = ""
        for item in list_sentences:
            self.process_sent(str_to_process, self.dict_result)
            str_to_process = "" + item + "\n\n"
        if len(str_to_process) != 0:
            self.process_sent(str_to_process, self.dict_result)
        list_sentences.clear()

        if out_file is not None:
            timestamp_1 = self.write_dict_result_to_file(
                out_file, self.dict_result, self.dict_headers
            )
            self.list_timestamps_write_to_file.append(
                (datetime.now() - timestamp_1).total_seconds() * 1000
            )

        self.list_result.append(self.dict_result.copy())
        self.dict_result.clear()
        self.dict_lines.clear()
        self.dict_headers.clear()

    def divide_sentences(self, string_to_divide):
        list_sentences_func = []
        # разделение предложений
        # regex_sentence = r'[A-Za-zА-Яа-яЁёé\d\?!, \–\-\—\'\"\:\/\ \+\`‍\% ́«»#$^&*@№;()，=*₽€]+?[\.\?\!].'
        regex_sentence = r"[\s\S]+?[\.\?\!]."
        # символ окончания предложения
        regex_sentence_end = "([A-Za-zА-Яа-яЁё0-9])$"
        # для определния некорректного начала предложения
        regex_sentence_uncorrect_dot = (
            r"[\.\?\!]+[A-Za-zА-Яа-яЁё0-9\–\-\—\'\"\\/\+\`‍+\%]"
        )
        # для вставки пробела между точкой и символом для корректной обработки
        regex_group = r"([\.\?\!])([A-Za-zА-Яа-яЁё0-9\–\-\—\'\"\\/\+\`‍+\%])"

        string_to_divide = string_to_divide.replace(",", ".")

        # для вставки пробела между символом и точкой для корректной обработки
        regex_group_with_dot = r"([\s\S])([\.\?\!])"
        uncorrect_dot = re.search(regex_sentence_uncorrect_dot, string_to_divide)
        string_to_divide = string_to_divide.replace("...", ".")
        string_to_divide = string_to_divide.replace("..", ".")
        string_to_divide = string_to_divide.replace("/", "")

        if len(string_to_divide) == 0:
            return list_sentences_func

        regex_combine_spaces = re.compile(r"\s+")
        string_to_divide = regex_combine_spaces.sub(" ", string_to_divide).strip()

        string_to_divide = emoji_pattern.sub(r"", string_to_divide)
        if string_to_divide[0] == ".":
            string_to_divide = string_to_divide[2:]
        # print(string_to_divide)
        if uncorrect_dot:
            string_to_divide = re.sub(regex_group, r"\1 \2", string_to_divide)

        orig_sent_tmp = re.search(regex_sentence, string_to_divide)
        if orig_sent_tmp:
            next_string = re.sub(regex_sentence, "", string_to_divide, 1)
            cur_string = orig_sent_tmp.group()

            while (
                cur_string.startswith("!")
                or cur_string.startswith("?")
                or cur_string.startswith(".")
                or cur_string.startswith(" ")
            ):
                cur_string = cur_string[1:]

            orig_sent_end_of_sent = re.search(regex_sentence_end, cur_string)
            if orig_sent_end_of_sent:
                cur_string = cur_string + " ."
            cur_string = re.sub(regex_group_with_dot, r"\1 \2", cur_string)
            cur_string = ". ".join(i.capitalize() for i in cur_string.split(". "))

            list_sentences_func.append(cur_string)
            list_sentences_func = list_sentences_func + self.divide_sentences(
                next_string
            )
        elif len(string_to_divide) != 0:
            cur_string = string_to_divide

            while (
                cur_string.startswith("!")
                or cur_string.startswith("?")
                or cur_string.startswith(".")
                or cur_string.startswith(" ")
            ):
                cur_string = cur_string[1:]

            orig_sent_end_of_sent = re.search(regex_sentence_end, cur_string)
            if orig_sent_end_of_sent:
                cur_string = cur_string + " ."
            cur_string = re.sub(regex_group_with_dot, r"\1 \2", cur_string)
            cur_string = ". ".join(i.capitalize() for i in cur_string.split(". "))

            list_sentences_func.append(cur_string)
        return list_sentences_func

    def is_sentence_separated(self, sentence):
        for punctuation_to_ignore in self.punctuations_to_ignore:
            if sentence.find(punctuation_to_ignore) == -1:
                continue

            return True
            break

        return False

    def is_only_single_sentence_in_result(self):
        return not self.is_first_sentence_processed and self.unprocessed_dict_size == 0

    def is_sentence_first_and_sequential(self):
        return (
            not self.is_first_sentence_processed and not self.is_now_sentence_separated
        )

    def is_sentence_not_last_and_sequential(self):
        return self.unprocessed_dict_size != 0 and not self.is_now_sentence_separated

    def get_next_sentence_to_concatinate(self, sentence):
        if self.is_only_single_sentence_in_result():
            return sentence.capitalize()

        if self.is_sentence_first_and_sequential():
            self.is_first_sentence_processed = True
            return sentence.translate(str.maketrans(",.", ".,"))

        if self.is_sentence_not_last_and_sequential():
            return sentence.lower().translate(str.maketrans(",.", ".,"))

        if self.previous_sentence_separated:
            return sentence.capitalize()
        else:
            return sentence.lower()

    def make_single_str_from_result_sentences(self, sentences_dict, result):
        self.unprocessed_dict_size = len(sentences_dict)
        for _, sentences in sentences_dict.items():
            self.unprocessed_dict_size -= 1
            self.previous_sentence_separated = self.is_now_sentence_separated
            self.is_now_sentence_separated = self.is_sentence_separated(sentences[0])

            result += self.get_next_sentence_to_concatinate(sentences[0])

        return result

    def process_result_sentences_into_one(self):
        result = ""
        self.is_first_sentence_processed = False
        self.is_now_sentence_separated = True
        for sentences_dict in self.list_result:
            result = self.make_single_str_from_result_sentences(sentences_dict, result)
        return result

    def start(self, text="") -> str:
        self.list_result.clear()
        for item in self.divide_sentences(text):
            self.dict_lines[self.count_blocks] = [item.rstrip()]
            self.count_blocks += 1
        self.process_bulk()

        return self.process_result_sentences_into_one()


stanza_module = stanza.Pipeline(
    lang="ru",
    processors="tokenize,pos,lemma,depparse,ner",
    use_gpu=False,
    logging_level="error",
    pos_batch_size=3000,
)
script = RunGenderSwap(stanza_module)


def swap(text: str) -> str:
    """Основная функция. Изменение рода с мужского на женский"""
    gen = script.start(text).strip()
    return gen
