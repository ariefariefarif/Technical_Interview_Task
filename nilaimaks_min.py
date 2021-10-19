#find the largest number in array list

number=[2,3,12,3,4,6,3,8] #list angka yang akan dicari mana angka terbesar

maksimum=number[0] #variabel penentuan nilai maksimum
minimum=number[0] #variabel penentuan nilai minimum

n=len(number) #variabel yang menentukan banyaknya jumlah angka dalam array

#pencarian nilai maksimum
for i in range(1,n):
	if number[i]>maksimum:
		maksimum=number[i]

#dalam penentuan angka terbesar digunaka looping dimana setiap array[i] akan dibandingkan dengan variabel maksimun (kondisi awal = number[0] yaitu angka pertama dalam array yaitu 2)
#akan terjadi perulangan dimana akan membandingkan sebanyak n kali(8 kali sesuai dengan jumlah len)
#nilai yang memenuhi pengkondisian number[i]>maksimum, akan mengisi variabel maksimum tersebut


#pencarian nilai minimum
for i in range(1,n):
	if number[i]<minimum:
		minimum=number[i]
#sama dengan logic yang digunakan dalam pencarian nilai maksimum, yang berbeda ialah penggunaan < jika ingin mencari nilai terkecil


print("Nilai value: ",number)
print("Nilai paling tinggi: ",maksimum)
print("Nilai paling rendah: ",minimum)