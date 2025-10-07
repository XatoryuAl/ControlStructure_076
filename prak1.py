percentage = float(input("Masukkan persentase milai siswa:"))

if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
elif percentage >= 50:
    print("Below average performance")
else:
    print("Poor performance")
    