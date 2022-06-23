class edad2:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print(self, mensaje)

julian = edad2(19)


print ('mi nombre es julian y tengo',julian.edad)



