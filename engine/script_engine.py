import random

DESTINATION_KNOWLEDGE = {
    "sumbing": {
        "title": "Gunung Sumbing",
        "elev": "3.371 mdpl",
        "fact": "Gunung tertinggi kedua di Jawa Tengah dengan kawah aktif dan tanjakan engkol-engkolan yang menguji mental.",
        "spots": ["Basecamp Butuh Kaliangkrik (Nepal van Java)", "Kawah Sumbing", "Puncak Rajawali"],
        "hazards": "Angin kawah belerang dan trek pasir curam."
    },
    "merbabu": {
        "title": "Gunung Merbabu",
        "elev": "3.145 mdpl",
        "fact": "Surga sabana terluas di Pulau Jawa dengan panorama magis Gunung Merapi di depannya.",
        "spots": ["Sabana 1 & 2 via Selo", "Pos 3 Watu Tulis", "Puncak Kenteng Songo & Triangulasi"],
        "hazards": "Kabut tebal dan minimnya sumber air di jalur atas."
    },
    "prau": {
        "title": "Gunung Prau (Dieng)",
        "elev": "2.590 mdpl",
        "fact": "Tempat terbaik menikmati golden sunrise terbaik se-Asia Tenggara dengan latar Gunung Sindoro dan Sumbing.",
        "spots": ["Bukit Teletubbies", "Plawangan Patakbanteng", "Taman Bunga Daisy"],
        "hazards": "Suhu dingin ekstrem di musim kemarau (frost/embun upas)."
    },
    "sindoro": {
        "title": "Gunung Sindoro",
        "elev": "3.153 mdpl",
        "fact": "Gunung bertubuh kerucut sempurna dengan sabana bunga edelweiss dan kawah aktif yang menawan.",
        "spots": ["Pos 3 Watu Tatah", "Sunrise Camp Kledung", "Kawah Aktif Sindoro"],
        "hazards": "Bau gas belerang pekat saat angin berhembus ke jalur kawah."
    },
    "slamet": {
        "title": "Gunung Slamet",
        "elev": "3.432 mdpl",
        "fact": "Atap Jawa Tengah, jalur berpasir merah yang panjang dan terkenal dengan sebutan jalur tanpa ampun.",
        "spots": ["Pos 7 Samarantu", "Plawangan Bambangan", "Puncak Surono"],
        "hazards": "Hipotermia dan navigasi rawan tersesat saat kabut hitam turun."
    },
    "lawu": {
        "title": "Gunung Lawu",
        "elev": "3.265 mdpl",
        "fact": "Gunung sakral penuh sejarah, memiliki warung tertinggi di Indonesia (Warung Mbok Yem).",
        "spots": ["Candi Cetho", "Hargo Dumilah", "Warung Mbok Yem"],
        "hazards": "Suhu drop drastis di malam hari dan kabut mistis."
    },
    "semeru": {
        "title": "Gunung Semeru",
        "elev": "3.676 mdpl",
        "fact": "Puncak tertinggi tanah Jawa (Mahameru) dengan danau surga Ranu Kumbolo dan Tanjakan Cinta.",
        "spots": ["Ranu Kumbolo", "Oro-Oro Ombo (Bunga Verbena)", "Puncak Mahameru"],
        "hazards": "Erupsi berkala pasir dan gas beracun Wedhus Gembel."
    },
    "rinjani": {
        "title": "Gunung Rinjani (Lombok)",
        "elev": "3.726 mdpl",
        "fact": "Mahakarya alam vulkanik terindah dengan kaldera megah Segara Anak dan Gunung Baru Jari.",
        "spots": ["Plawangan Sembalun", "Danau Segara Anak", "Puncak Rinjani"],
        "hazards": "Trek pasir 2 langkah maju 1 langkah mundur di letter E."
    },
    "bromo": {
        "title": "Gunung Bromo",
        "elev": "2.329 mdpl",
        "fact": "Lautan pasir bisik dan kawah bergemuruh dengan pemandangan sunrise kelas dunia di Penanjakan.",
        "spots": ["Kawah Bromo", "Pasir Berbisik", "Bukit Kingkong Sunrise"],
        "hazards": "Debu pasir vulkanik dan suhu beku sub-zero."
    }
}

def generate_storyboard(destination: str, duration_sec: int = 30, tone: str = "cinematic"):
    q = destination.lower().strip()
    matched = None
    for k, v in DESTINATION_KNOWLEDGE.items():
        if k in q or q in v["title"].lower():
            matched = v
            break
            
    if not matched:
        matched = {
            "title": destination.title(),
            "elev": "Jalur Eksotis",
            "fact": f"Destinasi petualangan menakjubkan di {destination.title()} yang menyajikan pemandangan spektakuler.",
            "spots": ["Pintu Masuk / Basecamp", "Spot Ikonik Jalur", "Titik View Utama"],
            "hazards": "Medan alam terbuka dan perubahan cuaca mendadak."
        }

    title = matched["title"]
    elev = matched["elev"]
    fact = matched["fact"]
    spots = matched["spots"]

    if duration_sec == 30:
        if tone == "cinematic":
            hook = f"Ada alasan kenapa {title} selalu memanggil kita untuk kembali."
            scenes = [
                {
                    "time": "00:00 - 00:04",
                    "visual": "Extreme close-up sol sepatu trekking menginjak tanah berdebu, dilanjutkan slow-mo carrier dinaikkan ke punggung.",
                    "voiceover": hook,
                    "sfx": "Suara hembusan angin gunung + petikan gitar akustik hangat."
                },
                {
                    "time": "00:04 - 00:12",
                    "visual": "Wide shot langkah kaki melintasi jalur menanjak, diselingi kabut tipis menyelimuti pepohonan.",
                    "voiceover": f"Berdiri di ketinggian {elev}, setiap langkah di sini bukan hanya tentang menaklukkan tanjakan, tapi tentang belajar merendahkan ego.",
                    "sfx": "Suara nafas perlahan + ambience hutan yang tenang."
                },
                {
                    "time": "00:12 - 00:22",
                    "visual": "Golden hour panning shot: siluet tenda di camp area saat matahari mulai menyingsing di ufuk timur.",
                    "voiceover": f"Dan ketika cahaya pertama membelah cakrawala di {spots[1] if len(spots)>1 else 'puncak'}, semua rasa lelah itu seketika sirna tanpa sisa.",
                    "sfx": "Musik orchestral crescendo naik perlahan menyentuh emosi."
                },
                {
                    "time": "00:22 - 00:30",
                    "visual": "Wide drone view 360 derajat lanskap samudera awan, diakhiri senyum pendaki menatap horizon.",
                    "voiceover": f"Tag teman mendakimu yang harus kamu ajak ke {title} musim ini!",
                    "sfx": "Musik fade out halus dengan hembusan angin puncak."
                }
            ]
        elif tone == "viral_genz":
            hook = f"Jangan pernah ngaku anak gunung kalau belum pernah ngerasain treknya {title}!"
            scenes = [
                {
                    "time": "00:00 - 00:04",
                    "visual": "Fast transition: ekspresi syok melihat tanjakan curam di depan mata, zoom cepat ke plang pos.",
                    "voiceover": hook,
                    "sfx": "Whoosh sound effect + bass beat modern beat drop."
                },
                {
                    "time": "00:04 - 00:12",
                    "visual": "Dynamic gimbal shot: jalan nanjak ngebut, keringat menetes, diselingi canda tawa teman se-tim.",
                    "voiceover": f"Trek {elev} ini bener-bener gak ngasih napas. Napas udah di tenggorokan, tapi pemandangan sekitarnya emang gokil parah!",
                    "sfx": "Energetic lofi/synth beat upbeat."
                },
                {
                    "time": "00:12 - 00:22",
                    "visual": "Speed ramp shot: dari jalan kaki langsung masuk ke lautan awan epik dan view sunrise menyala.",
                    "voiceover": f"Pas sampe di {spots[1] if len(spots)>1 else 'puncak'}, fix semua rasa pegel kaki langsung lunas dibayar pemandangan seindah ini.",
                    "sfx": "Audio trend viral hype."
                },
                {
                    "time": "00:22 - 00:30",
                    "visual": "Toss cangkir kopi / tos tangan antar pendaki di depan tenda dengan latar awan.",
                    "voiceover": f"Kira-kira berani ga kamu tektok ke sini? Tulis di komen ya!",
                    "sfx": "Upbeat closing sting."
                }
            ]
        elif tone == "survival":
            hook = f"Pernahkah kamu membayangkan apa yang terjadi jika cuaca ekstrem tiba-tiba menghantam di {title}?"
            scenes = [
                {
                    "time": "00:00 - 00:04",
                    "visual": "Dramatis slow-motion: kabut tebal hitam bergerak cepat menutupi lereng, petir samar di kejauhan.",
                    "voiceover": hook,
                    "sfx": "Deep cinematic sub-bass rumble + suara gemuruh angin kencang."
                },
                {
                    "time": "00:04 - 00:12",
                    "visual": "Close up termometer menunjukkan suhu drop drastis, pendaki merapatkan jaket windbreaker dan kupluk.",
                    "voiceover": f"Di ketinggian {elev}, suhu bisa anjlok hingga mendekati titik beku dalam hitungan menit. Hipotermia adalah musuh nyata.",
                    "sfx": "Suara detak jantung berdegup tegang."
                },
                {
                    "time": "00:12 - 00:22",
                    "visual": "Penanganan darurat: memasang flysheet cepat, memakaikan thermal emergency blanket ke rekan tim.",
                    "voiceover": f"Ingat prinsip STOP: Sit, Think, Observe, Plan. Puncak itu bonus, tapi pulang ke rumah dengan selamat adalah kewajiban mutlak.",
                    "sfx": "Nada instrumen piano dramatis menguat."
                },
                {
                    "time": "00:22 - 00:30",
                    "visual": "Pendaki saling merangkul di basecamp saat pagi tiba dengan senyum kelegaan.",
                    "voiceover": f"Bagikan video ini agar semakin banyak pendaki yang paham arti penting keselamatan di alam bebas.",
                    "sfx": "Angin tenang + outro inspiratif."
                }
            ]
        else: # chill storytelling
            hook = f"Kadang, kita hanya butuh melarikan diri sejenak dari bisingnya kota."
            scenes = [
                {
                    "time": "00:00 - 00:04",
                    "visual": "Pemandangan embun menetes dari daun pinus di pagi hari, uap air hangat dari ceret kopi.",
                    "voiceover": hook,
                    "sfx": "Petikan gitar akustik lembut + kicauan burung pagi."
                },
                {
                    "time": "00:04 - 00:12",
                    "visual": "Duduk santai di depan tenda sambil memegang cangkir, menatap kabut melintas pelan di lembah.",
                    "voiceover": f"Dan {title} selalu punya cara untuk menenangkan jiwa yang lelah. Sunyi di ketinggian {elev} mengajarkan kita arti bersyukur.",
                    "sfx": "Ambient lo-fi hangat menenangkan."
                },
                {
                    "time": "00:12 - 00:22",
                    "visual": "Kamera merekam langkah santai menyusuri sabana hijau yang luas bermandikan cahaya matahari.",
                    "voiceover": f"Tidak perlu terburu-buru mengejar puncak. Nikmati saja setiap jengkal perjalanannya bersama sahabat terbaikmu.",
                    "sfx": "Musik mengalun syahdu."
                },
                {
                    "time": "00:22 - 00:30",
                    "visual": "Senja merah jingga menyinari tenda-tenda berwarna-warni.",
                    "voiceover": f"Kapan terakhir kali kamu menikmati kopi di atas awan seperti ini?",
                    "sfx": "Fade out tenang."
                }
            ]
    else: # 60 seconds
        hook = f"Banyak yang bilang, mendaki {title} adalah tentang menguji batas kemampuan diri."
        scenes = [
            {
                "time": "00:00 - 00:08",
                "visual": "Opening cinematic: Panning view Gunung dari kejauhan saat kabut fajar terangkat, disusul persiapan packing gear di basecamp.",
                "voiceover": f"{hook} Menjulang setinggi {elev}, gunung ini menyimpan sejuta cerita bagi setiap pendaki yang berani melangkah.",
                "sfx": "Suara hembusan angin gunung + petikan dawai akustik lembut."
            },
            {
                "time": "00:08 - 00:20",
                "visual": "Montage jalur: Langkah kaki menapaki akar pohon, bebatuan curam, dan nafas berat pendaki sambil saling memberi semangat.",
                "voiceover": f"Dari pos ke pos, medan {title} tak pernah gagal menguras stamina. Tapi di balik setiap tetes keringat, ada pemandangan hutan lumut dan sabana yang memanjakan mata.",
                "sfx": "Suara langkah kaki di tanah + hembusan nafas + ambience alam."
            },
            {
                "time": "00:20 - 00:35",
                "visual": "Camp area saat malam: Bintang bertaburan (milky way timelaps), diselingi suasana masak bersama di dalam tenda.",
                "voiceover": f"Malam di ketinggian selalu terasa magis. Dinginnya udara dan hangatnya secangkir kopi di sekitar {spots[0]} membuat obrolan sederhana terasa begitu berharga.",
                "sfx": "Suara gemerisik api kompor + gesekan sleeping bag + musik ambient syahdu."
            },
            {
                "time": "00:35 - 00:50",
                "visual": "Summit attack: Cahaya headlamp membelah kegelapan dini hari, tiba-tiba langit berubah menjadi jingga keemasan di bibir puncak.",
                "voiceover": f"Dan ketika fajar menyingsing di {spots[1] if len(spots)>1 else 'puncak'}, seluruh pulau seolah berada di bawah kakimu. Lautan awan membentang sejauh mata memandang.",
                "sfx": "Orchestral crescendo epic dan menyentuh."
            },
            {
                "time": "00:50 - 01:00",
                "visual": "Drone shot menjauh dari puncak memperlihatkan kemegahan alam, diakhiri tulisan quotes keselamatan di layar.",
                "voiceover": f"Karena pada akhirnya, bukan gunung yang kita taklukkan, melainkan diri kita sendiri. Bagikan video ini dan rencanakan tripmu ke {title}!",
                "sfx": "Ending music fade out dengan suara angin damai."
            }
        ]

    full_voiceover = " ".join([s["voiceover"] for s in scenes])
    
    # Generate Caption & Hashtags
    caption = (
        f"Kapan terakhir kali kamu merasa sehidup ini di alam bebas? 🏔️✨\n\n"
        f"Mendaki {title} ({elev}) selalu memberikan pengalaman magis yang sulit dilupakan. "
        f"{fact}\n\n"
        f"📌 Simpan video ini untuk referensi pendakianmu berikutnya!\n"
        f"Tag teman muncakmu di kolom komentar! 👇\n\n"
        f"#{title.lower().replace(' ', '')} #{destination.lower().replace(' ', '')} #pendakiindonesia #mountnesia #id_pendaki #instapendaki #jejakpendaki #camerapendaki #urbanhikers #jelajahgunung #reelsindonesia #fypoutdoor"
    )

    return {
        "destination": title,
        "elevation": elev,
        "duration": duration_sec,
        "tone": tone,
        "hook": hook,
        "scenes": scenes,
        "full_voiceover": full_voiceover,
        "caption": caption
    }
