kalimat = str(input("Masukan Kalimat ="))
vokal = 'aiueoAIUEO'
jumlah_vokal = str(sum(1 for char in kalimat if char in vokal))

print("Jumlah huruf vokal =" +jumlah_vokal)

#penjelasan
#kode ini menjelaskan bagaimana cara mengambil huruf vokal dengan contoh codingan akhir print("Jumlah huruf vokal =" +jumlah_vokal)
