import re
from prompt_toolkit.document import Document
from prompt_toolkit.completion import FuzzyWordCompleter, Completer, CompleteEvent, Completion
from typing import Callable, Dict, Iterable, List, Optional, Union

class FirstWordFuzzyWordCompleter(Completer):

    def __init__(self, words: Union[List[str], Callable[[], List[str]]],
                 meta_dict: Optional[Dict[str, str]] = None,
                 WORD: bool = False) -> None:

        self.words = words
        self.meta_dict = meta_dict or {}
        self.WORD = WORD

        self.fuzzy_word_completer = FuzzyWordCompleter(words=self.words, WORD=self.WORD)

    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]:
        pattern = re.compile(r"^\w*$")
        if not pattern.match(document.text.strip()):
            return []
        return self.fuzzy_word_completer.get_completions(document, complete_event)
