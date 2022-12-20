#======HAPUS TANDA (#) UNTUK MENJALANKAN SYNTAX=====

#def KelvinToFahrenheit(Temperature):
#   assert (Temperature >= 0),"Colder than absolute zero!"
#   return ((Temperature-273)*1.8)+32

#print(KelvinToFahrenheit(273))
#print(int(KelvinToFahrenheit(505.78)))
#print(KelvinToFahrenheit(-5))



#try:
#   fh = open("testfile", "w")
#   fh.write("Ini adalah file test untuk menguji exception handling.")
#except IOError:
#   print("Error: tidak bisa menemukan file atau membaca data")
#else:
#   print("Penulisan isi didalam file berhasil dilakukan")
#   fh.close()



#try:
#   fh = open("testfile", "r")
#   fh.write("Ini adalah file test untuk menguji exception handling.")
#except IOError:
#   print("Error: tidak bisa menemukan file atau membaca data")
#else:
#   print("Penulisan isi didalam file berhasil dilakukan")


   
#try:
#   fh = open("testfile", "w")
#   fh.write("Ini adalah file test untuk menguji exception handling.")
#finally:
#   print("Error: tidak dapat menemukan data atau membaca data")

# Jika kita tidak memiliki ijin untuk membuka file di mode tulis, maka
# hasil yang akan kita dapatkan adalah =

#try:
#   fh = open("testfile", "w")
#   try:
#      fh.write("Ini adalah file test untuk menguji exception handling.")
#   finally:
#      print("Akan menutup file")
#      fh.close()
#except IOError:
#   print("Error: tidak dapat menemukan data atau membaca data")



# Definisikan sebuah fungsi disini.
#def temp_convert(var):
#   try:
#      return int(var)
#   except ValueError as Argument :
#      print("Argumen tidak berisi nomor-nomor\n", Argument)

# Memanggil lagi fungsi disini.
#temp_convert("xyz");



#def functionName( level ):
#   if level < 1:
#      raise ("Invalid level!", level)
#   print(raise)
      # The code below to this would not be executed
      # if we raise the exception



#class Networkerror(RuntimeError):
#   def __init__(self, arg):
#      self.args = arg

#try:
#   raise Networkerror("Bad hostname")
#except Networkerror,e:
#   print (e.args)
