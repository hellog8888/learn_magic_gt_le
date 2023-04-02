stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    @property
    def words(self):
        return self.lst_words

    def __gt__(self, other):
        if isinstance(other, StringText):
            return len(self.lst_words) > len(other.lst_words)

    def __ge__(self, other):
        if isinstance(other, StringText):
            return len(self.lst_words) >= len(other.lst_words)

    def __lt__(self, other):
        if isinstance(other, StringText):
            return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):
        if isinstance(other, StringText):
            return len(self.lst_words) <= len(other.lst_words)

lst_text = [StringText(stich[x].strip("–?!,.;").replace('  ', ' ').split(' ')) for x in range(len(stich))]

lst_text_sorted = sorted(lst_text, reverse=True)

lst_text_sorted = [' '.join(x.words) for x in lst_text_sorted]