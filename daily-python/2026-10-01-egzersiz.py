class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c # abc değer tanıma 

    @staticmethod
    def is_valid(a, b, c):
        """Üçgen oluşturulup oluşturulmayacağını kontrol et"""
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# Statik metot çağırma (nesne olmadan)
if Triangle.is_valid(3, 4, 5):
    t = Triangle(3, 4, 5)
    print(f'Çevre: {t.perimeter()}')  # 12
    print(f'Alan: {t.area()}')        # 6.0