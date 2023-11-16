import pandas

class Defination:

    def __init__(self, term):
        self.term = term.strip()

    def get(self):
        df = pandas.read_csv("data.csv")
        # tuple since the defination can be more then one
        result = tuple(df.loc[df['word'] == self.term]['definition'])
        return result


if __name__ == "__main__":
    definition = Defination(term='lot')
    print(definition.get())






