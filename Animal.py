class Animal:
    def __init__(self, nume, varsta, culoare, specie, greutate):
        self.nume = nume
        self.varsta = varsta
        self.culoare = culoare
        self.specie = specie
        self.greutate = greutate

    def __str__(self):
        return f"{self.nume} ({self.specie}), {self.varsta} ani, culoare: {self.culoare}, greutate: {self.greutate} kg"

    @property
    def detalii_suplimentare(self):
        return f"Detalii specifice despre {self.nume}"

    @property
    def actiune_specifica(self):
        return f"O acțiune specifică pentru {self.nume}"

class Pasare(Animal):
    def __init__(self, nume, varsta, culoare, specie, greutate, aripi_span, sunet):
        super().__init__(nume, varsta, culoare, specie, greutate)
        self.aripi_span = aripi_span
        self.sunet = sunet

    def __str__(self):
        return f"{super().__str__()}, aripi span: {self.aripi_span} m, sunet: {self.sunet}"

    @property
    def detalii_suplimentare(self):
        return f"{super().detalii_suplimentare}, aripi span: {self.aripi_span} m"

    def actiune_noua(self):
        return f"{super().actiune_specifica}: zboara"

class Reptila(Animal):
    def __init__(self, nume, varsta, culoare, specie, greutate, lungime_coada, venin):
        super().__init__(nume, varsta, culoare, specie, greutate)
        self.lungime_coada = lungime_coada
        self.venin = venin

    def __str__(self):
        return f"{super().__str__()}, lungime coada: {self.lungime_coada} m, venin: {self.venin}"

    @property
    def actiune_specifica(self):
        return f"O acțiune specifică pentru {self.nume}: folosește veninul"

    def actiune_noua(self):
        return f"{super().actiune_specifica}: se taraste"


if __name__ == "__main__":
    animal_generic = Animal("Rex", 3, "maro", "caine", 10)
    print(animal_generic)
    print(animal_generic.detalii_suplimentare)
    print(animal_generic.actiune_specifica)

    pasare = Pasare("Pinguin", 2, "alb-negru", "pinguin", 5, 1.2, "chirp")
    reptila = Reptila("Viper", 4, "verde", "sarpe", 2, 0.8, "toxic")

    print(pasare)
    print(pasare.detalii_suplimentare)
    print(pasare.actiune_specifica)
    print(pasare.actiune_noua())

    print(reptila)
    print(reptila.detalii_suplimentare)
    print(reptila.actiune_specifica)
    print(reptila.actiune_noua())
