from django.test import TestCase

from empresas.models import Empresas
from empresas.views import *


class EmpresasMethodTests(TestCase):

	def test_crea_empresa(self):
		emp = Empresas(nombre='nPrueba',correo='cPrueba')
		emp.save()
		self.assertEqual(emp.nombre, 'nPrueba')
		self.assertEqual(emp.correo, 'cPrueba')
		
	def test_devuelve_empresa(self):
		emp2 = Empresas(nombre="empresa_prueba",correo="correo_prueba")
		emp2.save()
		emp3=Empresas(nombre=" ",correo=" ")
		emp3=emp2.getEmpresa()
		self.assertEquals(emp3.nombre, emp2.nombre)
		
	
