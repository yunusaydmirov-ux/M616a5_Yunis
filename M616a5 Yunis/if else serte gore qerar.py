# Adam Asmaca Oyunu (Hangman)

# Təxmin ediləcək gizli söz
gizli_soz = "python"

# Sözün uzunluğu qədər alt xətt yaradırıq (məsələn: _ _ _ _ _ _)
tapilan_herfler = ["_" for _ in gizli_soz]

# Oyunçunun can sayı
can = 6

print("--- Adam Asmaca Oyununa Xoş Gəlmisiniz! ---")
print(" ".join(tapilan_herfler))

while can > 0:
    # İstifadəçidən hərf istəyirik və kiçik hərfə çeviririk
    texmin = input("\nBir hərf daxil edin: ").lower()

    # Girişin düzgünlüyünü yoxlayırıq (yalnız 1 hərf olmalıdır)
    if len(texmin) != 1 or not texmin.isalpha():
        print("Xəta: Zəhmət olmasa yalnız bir hərf daxil edin!")
        continue

    # Hərfin artıq tapılıb-tapılmadığını yoxlayırıq
    if texmin in tapilan_herfler:
        print(f"Bu hərfi artıq tapmısınız: '{texmin}'")
        continue

    # Hərfin gizli sözdə olub-olmamasını yoxlayırıq
    if texmin in gizli_soz:
        print(f"Afərin! '{texmin}' hərfi sözdə var.")
        
        # Hərfin hansı indeksdə olduğunu tapıb yerinə yazırıq
        for i in range(len(gizli_soz)):
            if gizli_soz[i] == texmin:
                tapilan_herfler[i] = texmin
    else:
        can -= 1
        print(f"Təəssüf ki, '{texmin}' hərfi yoxdur.")
        print(f"Qalan canınız: {can}")

    # Sözün cari vəziyyətini ekrana çap edirik
    print(" ".join(tapilan_herfler))

    # Oyunun qazanılıb-qazanılmadığını yoxlayırıq
    if "_" not in tapilan_herfler:
        print("\nTəbriklər! Sözü tamamilə tapdınız və qazandınız! 🎉")
        break

# Əgər canlar qurtarıbsa və söz hələ də tam tapılmayıbsa
if can == 0:
    print(f"\nOyun bitdi! Canlarınız qurtardı. Düzgün söz: '{gizli_soz}' 😢")