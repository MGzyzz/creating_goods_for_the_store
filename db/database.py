from utils import id_gen, random_colors


class Database:
    product = [
        {'category': 'Food', 'description': 'Hamburgers', 'amount': 200},
        {'category': 'Entertainment', 'description': 'Hamburgers', 'amount': 1000},
        {'category': 'Car', 'description': 'Hamburgers', 'amount': 250},
    ]

    colors = [
        {'id': 'Food', 'color': next(random_colors)},
        {'id': 'Entertainment', 'color': next(random_colors)},
        {'id': 'Car', 'color': next(random_colors)},
    ]

    @classmethod
    def all(cls):
        return cls.product

    @classmethod
    def total_sum(cls):
        total = sum([i['amount'] for i in cls.product])
        return total

    @classmethod
    def sum_category(cls):
        category_totals = []
        unique_categories = set(item['category'] for item in cls.product)

        for category in unique_categories:
            total_amount = sum(item['amount'] for item in cls.product if item['category'] == category)
            category_totals.append({'category': category, 'amount': total_amount})
        return category_totals


    @classmethod
    def add(cls, post: dict[str, str]):
        post['amount'] = int(post['amount'])
        cls.product.append(post)
        print(f"Вывод: {post}")