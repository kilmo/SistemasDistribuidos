import web
import bottle
import pymssql  

class ImcAPI(object):
  

	def post_individuo(self, cursor):
		
		form = web.input(name="formulario")
		name = form.name
		idade = form.idade
		sexo = form.sexo
		altura = form.altura
		peso = form.peso
		imc = calcula_IMC(altura, peso)
		cursor.execute('INSERT into Pessoas values (name, idade, sexo, altura, peso, imc)')
		cursor.commit()
		return imc

	def calcula_IMC(self, altura, peso):
		total = peso/(altura * altura)
		return total

	def list_all(self, cursor):
		cursor.execute('SELECT * FROM Pessoa')
		row = cursor.fetchone()  
	    while row:  
	        print (str(row[0]) + " " + str(row[1]) + " " + str(row[2])+ " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
	        row = cursor.fetchone() 



	if __name__ == "__main__":
		app.run()