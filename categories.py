class Categories:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def get_categories(self):
        return self.categories
