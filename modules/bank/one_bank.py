class Bank:
    def __init__(self, title, link, programs):
        self.title = title
        self.link = link
        self.programs = programs

    def __repr__(self):
        return 'Bank < {}, {}, {} >'.format(self.title,
                                            self.link,
                                            self.programs)
