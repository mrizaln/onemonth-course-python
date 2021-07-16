import random

waifu = ["Mashiro",
         "Elaina",
         "Victorique",
         "Siesta",
         "Ayame",
         "Pekora",
         "Okayu",
         "Rushia",
         "Fubuki",
         "Frostleaf",
         "Vigna"]

kegiatan = ["makan",
            "tidur",
            "main game",
            "ngoding",
            "belajar"]

tempat = ["rumah",
          "perpustakaan",
          "taman",
          "sekolah",
          "kafe"]

random_tempat   = random.choice(tempat)
random_kegiatan = random.choice(kegiatan)
random_waifu    = random.choice(waifu)

print(f"Apakah kau mau {random_kegiatan} dengan {random_waifu} di {random_tempat}?")
