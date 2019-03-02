from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_nlu.components import Component


from rasa_nlu.tokenizers import Token, Tokenizer


class SpellingCorrect(Component):
    name = "SpellCorrection"
    provides = ["token_spellchecked"]
    requires = ["tokens_slangprocessed"]
    defaults = {}
    language_list = None

    def __init__(self, component_config=None):
        super(SpellingCorrect, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        print("TRAINING SPELLCHECK")
        pass

    def process(self, message, **kwargs):
        from textblob import Word
        token_spellchecked=[]
        T = None
        for token in message.get("tokens_slangprocessed"):
            print(token.text)
            if(len(Word(token.text).spellcheck())):
                token_spellchecked.append(Token(Word(token.text).spellcheck()[0][0],0))
        print(token_spellchecked)
        message.set("token_spellchecked", token_spellchecked)

    def persist(self, model_dir):
        pass

    @classmethod
    def load(cls, model_dir=None, model_metadata=None, cached_component=None,
             **kwargs):

        if cached_component:
            return cached_component
        else:
            component_config = model_metadata.for_component(cls.name)
            return cls(component_config)