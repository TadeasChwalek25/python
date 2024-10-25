class Student:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.znamky = []

    def pridat_znamku(self, znamka):
        self.znamky.append(znamka)
        return f"Známka {znamka} byla přidána."

    def prumer(self):
        if self.znamky:
            return sum(self.znamky) / len(self.znamky)
        return "Student nemá žádné známky."


student = Student("Petr")
print(student.pridat_znamku(3))  
print(student.pridat_znamku(2))  
print(student.pridat_znamku(2))  
print(f"Průměr známek: {student.prumer():.2f}")  
