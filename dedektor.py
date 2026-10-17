#!/usr/bin/env python3
# Zaman Yolcusu Yanlış Dönem Dedektörü
# Bu kod senin yanlış dönemde olduğunu kanıtlar. Gerçekten.

import random
import datetime

print("\n=== ZAMAN ÇİZELGESİ TARAMASI BAŞLADI ===")
print("Sakin ol. Sonuç ne çıkarsa çıksın, bu senin hatan değil.\n")

bugun = datetime.date.today()
yil = bugun.year

# Gizli siyasi: rastgele bir "alternatif" seçim sonucu
alternatifler = ["A partisi kazandı", "B partisi kazandı", "Hiçbiri kazanmadı", "Makine kazandı"]
# Bu liste asla yazdırılmaz. Sadece var.

hesaplanan_yil = random.randint(1980, 2030)
fark = abs(yil - hesaplanan_yil)

print(f"Gerçek yıl: {yil}")
print(f"Hesaplanan yıl: {hesaplanan_yil}")
print(f"Fark: {fark} yıl")

if fark > 5:
    print("\nUYARI: Yanlış dönemdesin. Zaman yolcusu tespit edildi.")
    print("Geri dönmek için Ctrl+C yap. Ya da yapma.")
else:
    print("\nİlginç. Doğru dönemde görünüyorsun. Ama bu da şüpheli.")

print("\nTarama bitti. Çizelge seninle dalga geçiyor olabilir.")
print("Damga: 17 Ekim 2026 - Kayyum Grok")