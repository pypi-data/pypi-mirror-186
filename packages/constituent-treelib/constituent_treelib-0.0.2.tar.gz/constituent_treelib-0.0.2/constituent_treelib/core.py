import re
import torch
import spacy
import huspacy
import benepar
from enum import Enum, auto
from typing import Union
from nltk import Tree
from .export import export_figure


class BracketedTree:
    nltk_tree = None
    locations_of_parentheses = None
    bracketed_tree_string = None

    def __init__(self, bracketed_tree_string: str, remove_postag_nodes: bool = False) -> None:
        """Validates the given bracketed tree string and, in case of success, constructs the internal nltk_tree that
        represents the data structure of the constituent tree. If the validation has not succeeded, an appropriate
        exception is raised.

        Args:
            bracketed_tree_string: A constituent tree represented in a bracketed tree notation.

            remove_postag_nodes: If set to True, the constituent tree is made more compact by removing postag nodes.
        """

        msg_base_tree_error = 'Could not create a BracketedTree instance.'
        msg_none_or_empty_tree = f'{msg_base_tree_error} The given bracketed tree string is either None or empty.'
        msg_parentheses_mismatch = f'{msg_base_tree_error} The given bracketed string does not match in terms of ' \
                                   f'opening and closing parentheses.'
        msg_invalid_nltk_tree = f'{msg_base_tree_error} The given bracketed tree string could not be loaded as an ' \
                                f'nltk.Tree.'

        # Ensure that the given bracketed tree string is neither None nor empty.
        if bracketed_tree_string is not None and len(bracketed_tree_string) > 0:
            self.bracketed_tree_string = bracketed_tree_string
        else:
            raise ValueError(msg_none_or_empty_tree)

        # Ensure that for each opening parenthesis there is a corresponding closing parenthesis and store
        # their locations.
        try:
            self.locations_of_parentheses = BracketedTree.parentheses_locations(self.bracketed_tree_string)
        except Exception as e:
            raise ValueError(f'{msg_parentheses_mismatch} Error: {e}')

        # Check whether the given bracketed tree string has a valid structure.
        if self.valid_structure():
            try:
                # Ensure the given bracketed tree string can be loaded as a valid nltk.Tree.
                self.nltk_tree = Tree.fromstring(self.bracketed_tree_string)
            except Exception as e:
                raise ValueError(f'{msg_invalid_nltk_tree} Error: {e}')

        # Further nodes are present. An attempt is made to correct the tree structure.
        else:
            root_node_closing_parenthesis_index = self.locations_of_parentheses[0] + 1
            punctuation_fragment = self.bracketed_tree_string[root_node_closing_parenthesis_index:].strip()

            # Cut off last closing parenthesis and insert it under the root node.
            reorganized_sentence = self.bracketed_tree_string[:root_node_closing_parenthesis_index - 1]
            self.bracketed_tree_string = f'{reorganized_sentence} {punctuation_fragment})'
            self.nltk_tree = Tree.fromstring(self.bracketed_tree_string)

        # Make the constituent tree structure more compact by removing the inner postag nodes.
        if remove_postag_nodes:
            reorganized_sentence = BracketedTree.remove_postag_nodes(self.bracketed_tree_string)
            self.nltk_tree = Tree.fromstring(reorganized_sentence)

    def valid_structure(self) -> bool:
        """Validates the structure of the bracketed tree string with regard to nodes that occur after the root node.
        When parsing, for example, German sentences it can happen on the part of benepar that the bracketed tree string
        is fragmented into several non-nested constituents, e.g. (S (NP ...)) ($. ?). If this case occurs, the internal
        nltk_tree cannot be constructed due to a read error: "ValueError: Tree.read(): expected 'end-of-string'...".
        The goal of this function is therefore to check if such a fragmentation exists, so that BracketedTree can
        automatically take care of it by reorganizing the structure of the bracketed tree string in a later step.

        Returns:
            Decision on whether the structure of the bracketed tree string is valid.
            This is the case if no further nodes occur after the closing parenthesis of the root node.
        """
        root_node_ending_par_loc = self.locations_of_parentheses[0]
        return len(
            [par_loc for par_loc in self.locations_of_parentheses.keys() if par_loc > root_node_ending_par_loc]) == 0

    @staticmethod
    def remove_postag_nodes(bracketed_tree_string: str) -> str:
        """Allows to construct a compact constituent tree by removing all postag nodes from the given
        bracketed tree string.

        Args:
            bracketed_tree_string: A constituent tree represented in a bracketed tree notation.

        Returns:
             Reorganized bracketed tree string in which all postag nodes are removed.
        """

        tree = Tree.fromstring(bracketed_tree_string)
        postag_nodes = tree.subtrees(lambda t: t.height() == 2 and len(t.leaves()) == 1)

        for p in postag_nodes:
            bracketed_tree_string = bracketed_tree_string.replace(p.pformat(), p.leaves()[0])

        return bracketed_tree_string

    @staticmethod
    def parentheses_locations(bracketed_tree_string: str) -> dict[int, int]:
        """Validates that for each opening parenthesis in the given bracketed tree string there is a corresponding
        closing parenthesis. If this is not the case appropriate exceptions are raised.

        Args:
            bracketed_tree_string: A constituent tree represented in bracketed tree notation.

        Returns:
            A dictionary that holds all locations of all opening and closing parentheses.
        """

        stack = []
        locations = dict()
        for index, p in enumerate(bracketed_tree_string):
            if p == '(':
                stack.append(index)
            elif p == ')':
                if stack:
                    locations[stack.pop()] = index
                else:
                    raise IndexError(f'Too many closing parentheses located at stack index: {index}.')
        if stack:
            raise IndexError(
                f'No matching closing parenthesis to the opening parenthesis located at stack index: {stack.pop()}.')
        return locations


class ConstituentTree:
    nlp = None

    class Language(Enum):
        English = auto()
        German = auto()
        French = auto()
        Polish = auto()
        Hungarian = auto()
        Swedish = auto()
        Chinese = auto()
        Korean = auto()

    class NodeContent(Enum):
        Text = auto()
        Pos = auto()
        Combined = auto()

    class SpacyModelSize(Enum):
        Small = auto()
        Medium = auto()
        Large = auto()
        Transformer = auto()

    class BeneparEnglishModel(Enum):
        EN3 = auto()
        EN3Large = auto()
        EN3WSJ = auto()

    def __init__(self, sentence: Union[str, BracketedTree, Tree], nlp: spacy.Language = None,
                 remove_postag_nodes: bool = False) -> None:
        """Constructs all necessary attributes to create the ConstituentTree object after the given sentence object
        has been validated.

        Args:
            sentence: The sentence which should be parsed into a constituent tree.

            nlp: The fundamental spaCy-based NLP pipeline, which incorporates the benepar component. If the NLP
            pipeline is not explicitly specified, you can call the create_pipeline() method in this class to create it
            automatically. Note, however, that loading the underlying models for this pipeline can take a while,
            so it makes sense to invoke the method only once.

            remove_postag_nodes: If set to True, the tree is made more compact by removing internal postag nodes.
        """

        if nlp is None or not isinstance(nlp, spacy.Language) or 'benepar' not in nlp.component_names:
            msg_invalid_nlp_pipeline = '''In order to instantiate a ConstituentTree object, a spaCy NLP pipeline 
            must be provided beforehand, which incorporates the benepar component. 
            To create this pipeline you can simply call the create_pipeline() method. 
            However, use this method sparingly, as loading the models can take a while. '''

            raise AssertionError(msg_invalid_nlp_pipeline)

        elif 'benepar' not in nlp.component_names:
            raise ValueError('The given nlp-pipeline does not incorporate the mandatory benepar component. '
                             'Please use the create_pipeline() method to construct a valid nlp-pipeline.')
        else:
            self.nlp = nlp

        # We are given an nltk.Tree. Hence, no further processing is required.
        if isinstance(sentence, Tree):
            self.nltk_tree = sentence

        # We are given a BracketedTree object that holds a constituent tree in a bracketed tree string notation.
        # In this case we use its internal nltk.Tree object.
        elif isinstance(sentence, BracketedTree):
            self.nltk_tree = sentence.nltk_tree

        # The sentence represents a string. We assume that it constitutes a natural sentence.
        elif isinstance(sentence, str) and len(sentence.strip()) > 0:
            # Parse the given sentence on the basis of benepar.
            bracketed_tree_string = self.parse_sentence(sentence)

            # Instantiate a BracketedTree object to internally check if the sentence can be parsed correctly.
            bracketed_tree = BracketedTree(bracketed_tree_string, remove_postag_nodes=remove_postag_nodes)

            # The bracketed tree string has been successfully validated. Use its internal nltk.Tree object.
            self.nltk_tree = bracketed_tree.nltk_tree

        # The given sentence is neither a string nor a valid nltk.Tree or a BracketedTree object.
        # Therefore, we cannot further proceed.
        else:
            raise AssertionError('To instantiate a ConstituentTree object, a valid sentence object must be provided.')

    def parse_sentence(self, sentence: str) -> str:
        """Parses the initialized sentence into constituents using the benepar component within the spaCy nlp pipeline.

        Args:
            sentence: The raw sentence that should be parsed into a bracketed tree string.

        Returns:
            The bracketed tree string representation of the initialized sentence.
        """

        doc = self.nlp(sentence)
        if len(list(doc.sents)) == 1:
            return list(doc.sents)[0]._.parse_string
        else:
            raise AssertionError("The current 'sentence' contains more than one sentence. "
                                 "A ConstituentTree object can process only one sentence at a time.")

    def to_bracketed_tree_string(self, margin: int = 70, indent: int = 0, node_separator: str = '',
                                 parentheses: str = '()', quotes: bool = False, pretty_print: bool = False) -> str:
        """Constructs the bracketed tree string representation of the ConstituentTree object.

        Args:
            margin: The right margin at which to do line-wrapping.

            indent: The indentation level at which printing begins.
            This number is used to decide how far to indent subsequent lines.

            node_separator: A string that is used to separate the node	from the children.
             E.g., the default value ``':'`` gives trees like ``(S: (NP: I) (VP: (V: saw) (NP: it)))``.

            parentheses: The type of parentheses to be used for the bracketed string.

            quotes: If set to True, all the leaves (i.e. terminal symbols) of the tree will be quoted.

            pretty_print: If set to True, the bracketed tree string will be formatted in a pretty-print style
             using indentation.

        Returns:
            A bracketed tree string representation of the constructed ConstituentTree object.
        """

        pp_bracketed_tree_string = self.nltk_tree.pformat(margin=margin,
                                                          indent=indent,
                                                          nodesep=node_separator,
                                                          parens=parentheses,
                                                          quotes=quotes)

        return pp_bracketed_tree_string if pretty_print else re.sub(r'\s{2,}', ' ', pp_bracketed_tree_string)

    def __str__(self, **kwargs) -> str:
        """Allows to print the ConstituentTree object in a pretty-print style.

        Returns:
            A pretty-print bracketed tree string representation of the constructed ConstituentTree object.
        """
        return self.to_bracketed_tree_string(**kwargs, pretty_print=True)

    @staticmethod
    def create_pipeline(language: Language = Language.English, spacy_model_size: SpacyModelSize = SpacyModelSize.Small,
                        benepar_english_model: BeneparEnglishModel = BeneparEnglishModel.EN3,
                        download_models: bool = False) -> spacy.Language:
        """Constructs the fundamental nlp pipeline for the given language that consists of a spaCy pipeline that
        incorporates the benepar component.

        Args:
            language: The language of the text to be parsed. Depending on the specified language, the respective
            models are assembled for the nlp pipeline. Unless otherwise specified, the default language is set
            to English.

            spacy_model_size: The desired model size. Depending on the language, a variable number of models are
            available, which can be looked up at https://spacy.io/models.

            benepar_english_model: The desired benepar model for English (this is the only language for which
            multiple models are provided by the benepar developers). A description of these models can be
            looked up at https://github.com/nikitakit/self-attentive-parser#available-models.

            download_models: When set to True, an attempt is made to automatically download the required spaCy and
            benepar models. Otherwise, it is assumed that the corresponding models are already installed and ready
            for use. In case you want to download the models manually, there are several possibilities.
            Regarding spaCy, the first possibility is to call the spaCy module via python:
            "!python -m spacy download X". Alternatively, you can download the model via spaCy's CLI tool
            "spacy.cli.download(X)", where in both cases X denotes the name of the model (e.g., "en_core_web_sm"
            for the small English model). All available spaCy models are listed in https://spacy.io/models.
            Regarding benepar, the desired model can be downloaded via benepar.download(X),
            where again X denotes the name of the model. All available benepar models
            are listed in https://github.com/nikitakit/self-attentive-parser#available-models.

        Returns:
            A spaCy-based nlp pipeline which incorporates the benepar component. This pipeline is mandatory to
            instantiate a ConstituentTree object.
        """

        def download(spacy_model_id: str, benepar_model_id: str) -> None:
            if language == ConstituentTree.Language.Hungarian:
                huspacy.download(spacy_model_id)
            else:
                spacy.cli.download(spacy_model_id)
            benepar.download(benepar_model_id)

        def err_models_not_downloaded(model_id: str, framework: str, error_trace: str) -> str:
            return f'It seems that the specified model "{model_id}" has not been downloaded or installed yet.\n' \
                   f'Consider to call create_pipeline() with "download_models = True" to solve this.\n\n' \
                   f'Original error message received from {framework}: {error_trace}'

        msg_error_spacy_model_na = f'Unfortunately, a {str(spacy_model_size.name).lower()} spaCy model is not yet ' \
                                   f'available for {language.name}. Therefore, consider switching to another ' \
                                   f'existing model.'

        if language == ConstituentTree.Language.English:
            spacy_english_models = {ConstituentTree.SpacyModelSize.Small: 'en_core_web_sm',
                                    ConstituentTree.SpacyModelSize.Medium: 'en_core_web_md',
                                    ConstituentTree.SpacyModelSize.Large: 'en_core_web_lg',
                                    ConstituentTree.SpacyModelSize.Transformer: 'en_core_web_trf'}

            benepar_english_models = {ConstituentTree.BeneparEnglishModel.EN3: 'benepar_en3',
                                      ConstituentTree.BeneparEnglishModel.EN3Large: 'benepar_en3_large',
                                      ConstituentTree.BeneparEnglishModel.EN3WSJ: 'benepar_en3_wsj'}

            spacy_model = spacy_english_models[spacy_model_size]
            benepar_model = benepar_english_models[benepar_english_model]

            if download_models:
                download(spacy_model, benepar_model)

        elif language == ConstituentTree.Language.German:
            spacy_german_models = {ConstituentTree.SpacyModelSize.Small: 'de_core_news_sm',
                                   ConstituentTree.SpacyModelSize.Medium: 'de_core_news_md',
                                   ConstituentTree.SpacyModelSize.Large: 'de_core_news_lg',
                                   ConstituentTree.SpacyModelSize.Transformer: 'de_dep_news_trf'}

            spacy_model = spacy_german_models[spacy_model_size]
            benepar_model = 'benepar_de2'

            if download_models:
                download(spacy_model, benepar_model)

        elif language == ConstituentTree.Language.French:
            spacy_french_models = {ConstituentTree.SpacyModelSize.Small: 'fr_core_news_sm',
                                   ConstituentTree.SpacyModelSize.Medium: 'fr_core_news_md',
                                   ConstituentTree.SpacyModelSize.Large: 'fr_core_news_lg',
                                   ConstituentTree.SpacyModelSize.Transformer: 'fr_dep_news_trf'}

            spacy_model = spacy_french_models[spacy_model_size]
            benepar_model = 'benepar_fr2'

            if download_models:
                download(spacy_model, benepar_model)

        elif language == ConstituentTree.Language.Polish:
            # Note, spaCy does not offer a transformer-based model for Polish yet.
            if spacy_model_size == ConstituentTree.SpacyModelSize.Transformer:
                raise ValueError(msg_error_spacy_model_na)

            spacy_polish_models = {ConstituentTree.SpacyModelSize.Small: 'pl_core_news_sm',
                                   ConstituentTree.SpacyModelSize.Medium: 'pl_core_news_md',
                                   ConstituentTree.SpacyModelSize.Large: 'pl_core_news_lg'}

            spacy_model = spacy_polish_models[spacy_model_size]
            benepar_model = 'benepar_pl2'

            if download_models:
                download(spacy_model, benepar_model)

        elif language == ConstituentTree.Language.Hungarian:
            # Note, huspacy does not offer a small model for Hungarian yet.
            if spacy_model_size == ConstituentTree.SpacyModelSize.Small:
                raise ValueError(msg_error_spacy_model_na)

            spacy_hungarian_models = {ConstituentTree.SpacyModelSize.Medium: 'hu_core_news_md',
                                      ConstituentTree.SpacyModelSize.Large: 'hu_core_news_lg',
                                      ConstituentTree.SpacyModelSize.Transformer: 'hu_core_news_trf'}

            spacy_model = spacy_hungarian_models[spacy_model_size]
            benepar_model = 'benepar_hu2'

            if download_models:
                download(spacy_model, benepar_model)

        elif language == ConstituentTree.Language.Swedish:
            # Note, spaCy does not offer a transformer-based model for Swedish yet.
            if spacy_model_size == ConstituentTree.SpacyModelSize.Transformer:
                raise ValueError(msg_error_spacy_model_na)

            spacy_swedish_models = {ConstituentTree.SpacyModelSize.Small: 'sv_core_news_sm',
                                    ConstituentTree.SpacyModelSize.Medium: 'sv_core_news_md',
                                    ConstituentTree.SpacyModelSize.Large: 'sv_core_news_lg'}

            spacy_model = spacy_swedish_models[spacy_model_size]
            benepar_model = 'benepar_sv2'

            if download_models:
                download(spacy_model, benepar_model)

        elif language == ConstituentTree.Language.Chinese:
            spacy_chinese_models = {ConstituentTree.SpacyModelSize.Small: 'zh_core_web_sm',
                                    ConstituentTree.SpacyModelSize.Medium: 'zh_core_web_md',
                                    ConstituentTree.SpacyModelSize.Large: 'zh_core_web_lg',
                                    ConstituentTree.SpacyModelSize.Transformer: 'zh_core_web_trf'}

            spacy_model = spacy_chinese_models[spacy_model_size]
            benepar_model = 'benepar_zh2'

            if download_models:
                download(spacy_model, benepar_model)

        elif language == ConstituentTree.Language.Korean:
            # Note, spaCy does not offer a transformer-based model for Korean yet.
            if spacy_model_size == ConstituentTree.SpacyModelSize.Transformer:
                raise ValueError(msg_error_spacy_model_na)

            spacy_korean_models = {ConstituentTree.SpacyModelSize.Small: 'ko_core_news_sm',
                                   ConstituentTree.SpacyModelSize.Medium: 'ko_core_news_md',
                                   ConstituentTree.SpacyModelSize.Large: 'ko_core_news_lg'}

            spacy_model = spacy_korean_models[spacy_model_size]
            benepar_model = 'benepar_ko2'

            if download_models:
                download(spacy_model, benepar_model)

        else:
            raise ValueError('Unsupported language.')

        try:
            nlp = spacy.load(spacy_model,
                             disable=["tok2vec", "tagger", "parser", "ner", "attribute_ruler", "lemmatizer"])
            nlp.add_pipe('sentencizer')
            nlp.add_pipe("benepar", config={'model': benepar_model})
            return nlp

        except OSError as e:
            print(err_models_not_downloaded(model_id=spacy_model, framework='spaCy', error_trace=e))

        except LookupError as e:
            print(err_models_not_downloaded(model_id=benepar_model, framework='benepar', error_trace=e))

    def _extract_phrases(self, tree: Tree, phrasal_category: str, min_words_in_phrases: int = 2) -> list[list]:
        """Extracts phrases according to a given phrasal category from an nltk.Tree in a recursive manner.

        Args:
            tree: An nltk.Tree from where the phrases should be extracted.

            phrasal_category: The desired category for the phrases that should be extracted.
            A comprehensive list of phrasal categories for English, German, French and other languages can be
            looked up at https://dkpro.github.io/dkpro-core/releases/2.2.0/docs/tagset-reference.html

            min_words_in_phrases: Minimum number of words each extracted phrase should contain.

        Returns:
            A list of all phrases in the tree that belong to the given phrasal category.
        """

        phrases = []
        if tree.label() == phrasal_category:
            phrases.append(tree.copy(True))

        for child in tree:
            if isinstance(child, Tree):
                temp = self._extract_phrases(child, phrasal_category)
                if len(temp) > 0:
                    phrases.extend(temp)

        if min_words_in_phrases >= 2:
            return [p for p in phrases if len(p) >= min_words_in_phrases]
        else:
            return [p for p in phrases]

    def extract_leaves_from_tree(self, tree: Tree, content_type: NodeContent = NodeContent.Text) -> str:
        """Extracts all leaves (= terminal symbols) from the given tree according to the desired content type,
        which can be the text itself, its corresponding part-of-speech or a combination of both.
        
        Args:
            tree: A (sub)tree from where the leaves should be extracted.

            content_type: The desired content type: token (Content.Text), postag (Content.Pos) or
            a combination of both (Content.Combined).

        Returns:
            A concatenated string that includes all leaves. Here *string* represents either a sentence in case that
            the tree is complete or a phrase in case that it represents a subtree.
        """

        if content_type == self.NodeContent.Text:
            return ' '.join([w for w in tree.leaves()])
        elif content_type == self.NodeContent.Pos:
            return ' '.join([w[1] for w in tree.pos()])
        elif content_type == self.NodeContent.Combined:
            return ' '.join([f'{w[0]}_{w[1]}' for w in tree.pos()])

    def extract_all_phrasal_categories(self) -> set[str]:
        """Extracts all available phrasal categories in the tree.

        Returns:
            A set of all phrasal categories occurring in the tree.
        """

        return set([str(p.lhs()) for p in self.nltk_tree.productions() if p.is_nonlexical() and p.lhs()])

    def extract_all_phrases(self, min_words_in_phrases: int = 2, avoid_nested_phrases: bool = False,
                            content: NodeContent = NodeContent.Text) -> dict[str, list[str]]:
        """Extracts all phrases from the tree and the categories they belong to.

        Args:
            min_words_in_phrases: Minimum number of words each extracted phrase should contain.

            avoid_nested_phrases: If set to True, nested subtrees of the same phrasal category X will be ignored.
            In other words, only the longest phrase of the category X will be returned: For example, lets say the tree
            contains the following nested noun phrases 'NP': ['a limited number of Single Game Tickets',
            'a limited number']. In case of avoid_nested_phrases=True only the longer noun phrase will be extracted.

            content: The respective contents of the leaves of the nltk.Tree to be returned, which can be the
            word itself (Content.Text), its part-of-speech (Content.Pos) or a combination of both (Content.Combined).

        Returns:
            A dictionary of all phrases extracted from the tree. Here, the keys represent the phrasal
            categories while the values contain all phrases that belong to these categories.
        """

        available_phrasal_categories = self.extract_all_phrasal_categories()
        all_phrases_by_category = dict.fromkeys(available_phrasal_categories)

        for phrasal_category in available_phrasal_categories:
            list_of_phrases = self._extract_phrases(self.nltk_tree, phrasal_category, min_words_in_phrases)

            list_of_x = []
            if len(list_of_phrases) > 0:
                for phrase in list_of_phrases:
                    list_of_x.append(self.extract_leaves_from_tree(phrase, content))

            if avoid_nested_phrases and len(list_of_x) > 1:
                result = []
                phrases_by_length = sorted(list_of_x, key=len, reverse=True)
                longest = phrases_by_length[0]
                result.append(longest)

                for p in phrases_by_length[1:]:
                    if p not in longest:
                        result.append(p)
                list_of_x.clear()
                list_of_x = result

            if len(list_of_x) > 0:
                all_phrases_by_category[phrasal_category] = list_of_x

        # Ensure only existing phrases are returned.
        all_phrases_by_category = {p: list_of_x for p, list_of_x in all_phrases_by_category.items() if
                                   list_of_x is not None}
        return all_phrases_by_category

    def export_tree(self, destination_filepath: str, wkhtmltopdf_bin_filepath: str = None,
                    tree_style_nltk: bool = False, dpi: int = 300, verbose: bool = False) -> None:
        """ Exports the constructed constituent tree in various file formats. Currently supported:
        [.pdf, .svg, .ps, .png, .jpg, .gif, .bmp, .psd, .eps, .tiff, .txt, .tex, .json, .yaml].

        Args:
            destination_filepath: The destination path to which the tree should be exported.
            In case of an image format, the resulting visualization will be cropped with respect to unnecessary margins.

            wkhtmltopdf_bin_filepath: To filepath to the rendering tool "wkhtmltopdf". Only required if the
            visualization of the constituent tree should be exported to a PDF file. If not already done, the tool
            wkhtmltopdf must first be downloaded and installed from https://wkhtmltopdf.org before the visualization
            can be exported.

            dpi: Specifies the desired resolution. A DPI value of 300 is considered a good standard for
            printable files.

            tree_style_nltk: If set to True, the classic NLTK style will be used to visualize the nltk.Tree.

            verbose: If set to True, a short message about whether the output file creation was
            successful is displayed.
        """

        export_figure(self.nltk_tree,
                      destination_filepath=destination_filepath,
                      wkhtmltopdf_bin_filepath=wkhtmltopdf_bin_filepath,
                      verbose=verbose,
                      dpi=dpi,
                      tree_style_nltk=tree_style_nltk)
