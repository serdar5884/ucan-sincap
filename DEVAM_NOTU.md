# Uçan Sincap: Kapadokya — 2D sürüm (Devam Notu)

> For Claude: reply in Turkish. Do NOT use subagents (user: they burn limits). Work directly on index.html.

- Bu, kullanıcının 24 Ekim 2026'da geri dönülmesini istediği sürüm: Three.js/ajan çalışmasından ÖNCEKİ hâl.
- Tek dosya: `index.html` (HTML + CSS + JS, 2D canvas, piksel art, 180x320 düşük çözünürlük, nearest upscale).
- İçerik: Flappy tarzı balon + sincap; peri bacaları (şapkalı/sivri/kale) ve sarkıtlar; fındık (+1) ve altın palamut (+5);
  gündüz→gün batımı→gece döngüsü; her 10 skorda hava (Açık, Rüzgârlı, Yağmurlu, Sisli, Karlı, Fırtınalı);
  Garaj: 7 karakter (Sincap, Gri Sincap, Kar Sincabı, Kirpi, Tilki, Baykuş, Van Kedisi) + 7 balon (Klasik, Gökkuşağı,
  Nazar Boncuğu, Lale, Kilim, Gece Yıldızı, Altın Balon); madalyalar; "İzle ve Devam Et" (örnek reklam); Web Audio sesleri.
- Kayıt anahtarları (localStorage): pbu_best, pbu_nuts, pbu_mute, pbu_own_ch, pbu_own_bl, pbu_sel_ch, pbu_sel_bl.
- Font: Pixelify Sans (Google Fonts linki).
- Not: Ayrıca bir Three.js sürümü (us3d) yapılmıştı; kullanıcı onu istemedi ve bu sürüme dönüldü.

## 24 Ekim akşamı — eleştirmen turu 1 (uygulandı)
- Peri bacaları kalın/tombik (fatBody, geniş kubbeli şapka CAPF), sarkan kayalar tombik + düz pürüzlü taban, aynı tüf paleti, düzensiz katman çizgileri.
- Arka plan bacaları tombik; fındık 9x11 + parlayan halka + mıknatıs (18 px).
- Pixelify Sans dosyaya gömülü (internetsiz çalışır). Skor arkasında koyu zemin.
- Zorluk yumuşatıldı: hız 72+0.6*skor (max 100), boşluk ilk 3 kapı 115 sonra max(86,108-0.5*skor), aralık max(104,124-0.4*skor), yükseklik farkı ≤ 30+1.5*skor.
- Çarpışma daha affedici; canlandırma koruması sadece oyunda azalır; ölümde 80 ms donma; balon hafif eğilir.
- Oyun bitti: "Tekrar Dene" üstte, 0.7 sn tıklama kilidi, skor<3 ise reklam butonu gizli, skor bonusu (+skor/2 fındık), sıradaki ürüne kalan fındık.
- Fiyatlar düşürüldü (karakter 15/35/70/120/200/320, balon 20/45/80/130/220/350); madalyalar 5/12/25/40.
- Fırtına flaşı .2, sis örtüsü .2; flap sesi kısıldı; skor sesi yükseliyor; sabit 1/120 alt adım.
- "İzle ve Devam Et" hakkı oyun başına 5 (revLeft), butonda kalan hak gösterilir (sayı monospace, çünkü Pixelify'da 5 'S' gibi görünüyor).
- Kalkan güçlendirmesi: 5. kapıdan sonra her kapıda %10 şansla boşluğun ortasında çıkar (aynı anda tek kalkan). Alınca SHIELD_T=6 sn peri bacalarına/yere çarpınca ölünmez (yerden sekilir); oyuncunun etrafında mavi halka ve süre çubuğu, son 1.5 sn yanıp söner.

## İstanbul bölümleri (24 Ekim 2026)
- Her 8 kapıda bir bölge değişir (`SEC`): Kapadokya ↔ İstanbul Boğazı; geçişte banner + arka plan yumuşak geçişi (`curReg`, `regB`).
- İstanbul engelleri (`makeIstTower`): Galata Kulesi, Kız Kulesi, Dolmabahçe Saat Kulesi; üstte koyu yağmur bulutları (`makeIstCloud`). Çarpışma yine `hw(y)` profilinden.
- Arka plan (`drawIstanbul`): Anadolu tepeleri, Boğaz köprüsü (gece ışıklı), cami/minare silueti, Galata, Boğaz suyu, vapur, martılar; zemin rıhtım (`GPI`).

## Zorluk düşürüldü (24 Ekim 2026)
- Hız 66+skor*.45 (en fazla 90), aralık max(114,132-skor*.3), boşluk ilk 3 kapıda 122 sonra max(96,116-skor*.4), yükseklik farkı en fazla 56, yerçekimi 560, zıplama -165.

## Şehir yolları (1 Kasım 2026)
- `REG` dizisi: Kapadokya → İstanbul → Sivas → Bursa → Konya, her `SEC`=8 kapıda bir sonraki şehir; sonra "Tur 2" ile başa döner. Girişte "…'dasın!" banner'ı + şehir ipucu.
- İlk kez gidilen şehir: +10 fındık (`pbu_reg` = ulaşılan en uzak şehir). Menüde "Gezilen şehir x/5", oyun sonunda "Ulaştığın yer".
- Tarihi yapı bilgileri: engel ekrana girince altta 📍 etiketi (`LMK`), şehre girişte rastgele bilgi (`RFACT`), `#lmTag`.
- Şehir özellikleri: İstanbul simit (+3), Sivas Balıklı Kaplıca buharı yukarı iter (`vents`), Bursa sallanan teleferik kabinleri (sadece üst engel hareketli, boşluk +8), Konya altın palamut bereketi. Hava şehre bağlı (Sivas kar, Konya rüzgâr; 2. turda Kapadokya rüzgâr).
- Engeller: Sivas Selçuklu minareli medrese/kümbet + kar bulutu; Bursa Yeşil Türbe, Tophane Saat Kulesi, teleferik; Konya Mevlâna Türbesi, İnce Minareli Medrese + toz bulutu.
- Arka planlar: `drawKap/drawIstanbul/drawSivas/drawBursa/drawKonya`, geçişte çapraz geçiş (`regFrom`, `regT`). Zeminler GP/GPI/GPE/GPK/GPW.
- Yeni güç: Mıknatıs (`MAG_T`=8 sn) fındıkları uzaktan çeker.
- Kullanılmayan kalıntı: `ruzgar` özelliği (Erciyes fikri) update içinde duruyor, hiçbir şehir kullanmıyor; TRAV/PINE/NEMS vb. paletler de öyle.

## Kolaydan zora (1 Kasım 2026)
- Hız 58+skor*.55 (en fazla 125), boşluk ilk 3 kapı 124 sonra max(90,120-skor*.3), aralık max(108,130-skor*.2), yükseklik farkı min(22+skor*.9,64). 2. turda banner "Daha hızlı!".

## 6 hata düzeltildi (1 Kasım 2026, ajan incelemesi sonrası)
1. Yarıda bırakılan turun fındıkları artık kaydediliyor (`bankNuts()` startGame/toMenu'da; sayfa kapanırken `pagehide`).
2. Skor bonusu tur başına bir kez (`bonusPaid`), devam edip tekrar ölünce tekrar eklenmiyor.
3. Rakamlar: Pixelify'da 5≈S sorunu için gömülü piksel rakam fontu (aynı aile adı, `unicode-range: U+0030-0039`, fontTools ile üretildi).
4. Şehir başlığı/ipucu satırları artık sarılıyor; "Yeni şehir +10" balonun yanında uçan yazı; 📍 yerine ◆.
5. Sivas: kar/sis katmanı hafifletildi (WXC snow .08, fog .12), kar bulutları koyulaştırıldı.
6. Dokunmatik cihazda hazır ekranı ipucu "Dokundukça balon yükselir".
- Ajanların özellik önerileri (sırada): günlük görevler, günlük ödül (7 gün), şehir pasaportu/kartpostal albümü, şehirden başlama bileti, karakter yetenekleri, kalkan/mıknatıs yükseltmeleri, şehir sonu özel kapılar, şehir müzikleri, juice (Maşallah!/titreşim/kombo), görsel öğretici. Ekonomi notu: garaj toplam 1605 fındık.

## Yeni özellikler (1 Kasım 2026 akşam)
- **Günlük hediye** (`#daily`, `pbu_daily {d,s}`): 7 günlük seri 10/15/20/25/30/40 fındık, 7. gün özel **Lokum balonu** (`BALLOONS` id 'lokum', `gift:true`, satılmaz; zaten varsa 60 fındık). Seri bozulursa 1. güne döner. Menüye her girişte açılır.
- **Günün görevleri** (`#missions`, `pbu_mis`): tarihten tohumlu 3 görev (`MPOOL`): kapı, fındık, oyun sayısı, kalkan, mıknatıs, palamut, tarihi yapı, şehre ulaş, simit (İstanbul görüldüyse), buhar (Sivas görüldüyse). `mEvent(k,v)` ile ilerler; bitince oyunda ★ bildirimi, menüde kırmızı rozet; ödül panelden alınır.
- **Pasaport** (`#passport`, `pbu_lm`, `pbu_stamp`): 13 tarihi yapı (`CITY_LM`, `LM_NAME`; Kapadokya'ya 'peri' ve 'kale' eklendi). Şehrin tüm yapıları görülünce pul + 20 fındık. Gezilen şehirlerin bilgileri (RFACT) gösterilir.
- **Şehirden başla** (`#cityPick`): gezilmiş şehirlerden başlanabilir, ücret `START_COST` [0,15,30,45,60]; parası yetmezse Kapadokya'dan başlar. Menü arka planı seçili şehre geçer. `reset()` gateN = startCity*SEC.
- Titreşim: toplamada 8 ms, ölümde 40 ms.
- `shot.py` artık günlük hediye penceresini kapatıp devam ediyor.

## 2. ajan turu düzeltmeleri (6 Kasım 2026)
- Şehirden başlama ücreti: kapı geçmeden yeniden başlar/menüye dönersen iade (`feePaid`, `refundFee`). Para yetmezse BAŞLA "FINDIK YETMEZ" olur, sessizce Kapadokya'ya düşmez.
- `pagehide` listesine 'ad' eklendi. Ölünce şehir başlığı kapanıyor. `showBanner(txt, sub, pri)`: şehir başlığı (pri 2) açıkken güç yazıları alt bilgi kutusuna gider.
- Tarihi yapı algılama engel başına (`o.seen`, `o.reg === curReg`); bilgi kutusu yalnızca ilk keşifte ("Yeni: … · pasaporta eklendi"); şehir bilgisi tur başına bir kez; şehir değişince kuyruk temizlenir.
- GÖREVLER butonu alınmamış günlük hediye varsa önce onu açar. 7. gün Lokum zaten varsa "+60" yazar. "Oyna" görevi ilk dokunuşta sayılır.
- Font: B, G ve ! için de özel piksel harfler (B "8" gibi görünüyordu).
- HUD: skor kutusu sabit en; sincap tepeye çıkınca HUD ve başlık soluklaşır. Başlık koyu zeminli, dar. Bilgi kutusu daha büyük ve opak. Menü butonları ~44 px. Garaj ızgarasında alt solma. Hazır ekranında dokunma halkası.
- **Güçler sekmesi (garaj):** Kalkan 6→11 sn, Mıknatıs 8→15.5 sn, 5 kademe, fiyat `UP_COST` [40,80,140,220,320], kayıt `pbu_up`.
- Denge: zorluk `dScore() = score + startCity*6` (Konya'dan başlayıp kolay fındık açığı kapandı); şehirden başlarken de ilk 3 kapı kolay.
- Devam hakkı 5 kaldı (kullanıcı isteği). Ajan önerileri sırada: şehir sonu patron kapıları, karakter yetenekleri, kartpostal koleksiyonu, haftalık şehir etkinliği, beceri görevleri + "Maşallah!" serisi, müzik.

## 6 yeni özellik (6 Kasım 2026 gece)
1. **Büyük Kapı** (`makeBoss`, `BOSS`, `bossPassed`): her şehrin 8. kapısı altın parıltılı simge yapı (Kaya Kale, Galata, Çifte Minareli, Yeşil Türbe, Mevlâna), boşluk +6, yaklaşınca "★ Büyük Kapı!" başlığı, geçince +15 fındık + konfeti. **Pasaport pulu artık sadece Büyük Kapı geçilince** (+20).
2. **Karakter yetenekleri** (`PERK`, `perk`): Gri Sincap geniş çekim, Kar Sincabı kalkan +2 sn, Kirpi 1 çarpmayı affeder (`spineOK`), Tilki %25 çift fındık, Baykuş 2x palamut, Van Kedisi 6 sn mıknatısla başlar. Garajda `#gPerk` satırı; eski talimat metni kaldırıldı.
3. **Kartpostallar** (`CARDS` 5×6=30, `pbu_cards`, `POSTCARD` sprite): kapıların %6'sında çıkar, yeni kart başlık+bilgi gösterir, tekrar gelirse +5 fındık. Pasaportta "Kartpostallar x/30" bölümü.
4. **Haftalık şehir etkinliği** (`pbu_week`, `weekNo`, `evNuts`): her hafta bir şehir; orada fındıklar çift, 80 fındık toplayınca o şehrin etkinlik balonu (ev0..ev4: Kapadokya Şafağı, Boğaz, Çini, Yeşil Bursa, Sema; `gift:'Etkinlik'`), zaten varsa +50. Menüde `#evLine`.
5. **Seri ve övgü** (`combo`, `comboUp`, `praise`, `#praise`): her 5 ardışık fındıkta "Süper!/Maşallah!/Helal!/Bravo!/Efsane! xN" +2 fındık; fındık kaçınca seri biter; her 10 kapıda "Aferin!" vb. Yeni görevler: combo, boss, card.
6. **Müzik** (`MUS`, `MEL`, `musicTick`): şehir başına makam/ölçek ve tempo (Kapadokya Hicaz, İstanbul Uşşak, Sivas Hüseyni, Bursa pentatonik, Konya yavaş ney havası), bas + darbuka benzeri ritim; oyunda hızla biraz hızlanır. Ses düğmesi 3 durum: Ses Açık → Müzik Kapalı → Ses Kapalı (`pbu_music`).

## Kullanıcı düzeltmeleri (7 Kasım 2026)
- "+" görünen her şey kaldırıldı: Mevlâna tepeliği artık düz alem, Büyük Kapı yıldızı baklava şeklinde, palamut ışıltısı 2x2 nokta, Konya arka plan minaresi yeniden çizildi, semazenler artı gibi görünmesin diye yeniden çizildi (bir kol yukarı, bir kol aşağı, geniş etek).
- 10 kapı övgüsünde "Aferin!" yerine "Ooo".
- Sivas buhar sütunları (dikey ip gibi görünen şey) tamamen kaldırıldı; Sivas ipucu "Kar yağıyor, Kangal köpeğine el salla!". Buhar görevi yerine "Sivas'ta N fındık topla" görevi; eski kayıtlı görev listesi geçersiz anahtar içerirse yeniden üretilir.

## 4 yeni şehir (7 Kasım 2026) — toplam 9 şehir
Sıra: Kapadokya(0) → İstanbul(1) → Sivas(2) → Bursa(3) → Konya(4) → **Ankara(5) → Erzurum(6) → Adıyaman(7) → Antalya(8)**, sonra Tur 2.
- Ankara: Anıtkabir (`makeAnit`), Atakule (`makeAtakule`), Ankara Kalesi (`makeAnKale`); arka plan kale tepesi + Anıtkabir + Atakule + apartmanlar; Büyük Kapı Anıtkabir; marş havası.
- Erzurum: Üç Kümbetler (`makeKumbet(...,'uckumbet')`), Yakutiye minaresi; üstte buz sarkıtları (`makeIcicle`); yoğun kar + Palandöken rüzgârı (`feat:'ruzgar'`, ±110 itme); arka plan Palandöken + telesiyej; Büyük Kapı Yakutiye; bar oyunu temposu.
- Adıyaman: Nemrut taş başları (`makeNemrut`), Cendere Köprüsü sütunu (`makeCendere`); arka plan tümülüs + taş başlar + köprü; altın palamut sık (`feat:'palamut'`); Büyük Kapı Nemrut.
- Antalya: Yivli Minare (`makeMinaret(...,'yivli')`, dilimli), Hadrian Kapısı (`makeHadrian`), palmiye (`makePalm`); Akdeniz, Düden Şelalesi, yelkenli, yunus; kum zemin `GPS`; **portakal** (+3, `ORANGE` sprite, görev 'orange'); Büyük Kapı Yivli Minare.
- Her yeni şehre: 3 bilgi (`RFACT`), 6 kartpostal (toplam 54), pasaport yapıları, başlama ücreti (75/90/105/120), etkinlik balonu (ev5 Ay Yıldız, ev6 Oltu Taşı, ev7 Nemrut Günbatımı, ev8 Portakal), müzik (`MUS`).
- Haftalık etkinlik artık `w % REG.length` (9 şehir döner).

## Daha uzun yollar + kutlama (7 Kasım 2026)
- `SEC` 8 → **12** (her şehir 12 kapı; 12. kapı Büyük Kapı).
- Büyük Kapı geçilince `startCeleb()`: "Tebrikler! Yeni yolun açıldı: <şehir>" başlığı (pri 3), 12 renkli kutlama balonu aşağıdan yükselir (`celebB`, `drawCeleb`), 3.2 sn boyunca konfeti patlamaları (`confettiBurst`, patlama sesi) ve yağan konfeti (parçacık `s:2`, `g` artık çarpan), fanfar + titreşim.
- Büyük Kapı'dan sonra 210 px boş kutlama alanı (`lastBoss`), içinde 7 fındıklık yay (ortada palamut); sonra yeni şehir yolu başlar.

## Ay sönükleştirildi (7 Kasım 2026)
- Gece ayı: en fazla %42 opaklık, yarıçap 6→4, parıltı halkası kaldırıldı.

## Şehir adı daha uzun, kutlamada ölümsüzlük (7 Kasım 2026)
- `showBanner` süresi önceliğe göre: şehir adı (pri 2) 4.8 sn, kutlama (pri 3) 3.6 sn; CSS animasyon süresi satır içi ayarlanıyor.
- Kutlama sırasında (`celebT > 0`) engel ve yere çarpma öldürmez (yerde zıplar); kutlama bitince 0.8 sn ek koruma (`invT`).

## (7 Kasım 2026)
- `SEC` 12 → 16 (her şehir 16 kapı).
- Kutlama balonları %55 opaklıkla (saydam) çiziliyor.

## Fon müziği kaldırıldı (7 Kasım 2026)
- `startMusic()` hemen dönüyor (müzik kodu duruyor ama çalmıyor; geri açmak için baştaki `return;` silinir ve ses düğmesi 3 duruma döndürülür). Ses düğmesi yine Açık/Kapalı; efektler aynen.

## BÖLÜM SİSTEMİ + müzik geri (7 Kasım 2026 akşam) — oyun artık sonsuz değil
- **18 bölüm** (`LV_N`): Bölüm 1–9 "Gezgin" = şehirler sırayla (`lvCity(L) = (L-1)%9`), Bölüm 10–18 "Usta" = aynı şehirler gece başlar (`phase0 = .5`), daha hızlı. Bölüm uzunluğu `lvLen(L) = 15 + floor((L-1)/3)` kapı (15–20); son kapı Büyük Kapı, sonra kapı üretimi durur.
- Zorluk: `dScore() = (L-1)*6 + score*.6` → hız, boşluk, aralık, yükseklik farkı bölümle artar. Eski şehir döngüsü/`SEC`/Tur 2 ve şehirden başlama ücreti devre dışı (`#cityPick` gizli, `START_COST` kullanılmıyor).
- Büyük Kapı → kutlama ("Tebrikler! Bölüm N tamamlandı!") → 3.6 sn sonra `showWin()`: yıldız (1 + devam hakkı kullanmadıysan 1 + fındıkların ≥%60'ı 1), ödül `10 + 2L + (ilk kez 20) + yıldız*5`, "Yeni yolun açıldı: <şehir>", butonlar Sonraki Bölüm / Tekrar Oyna / Bölümler. Kayıt: `pbu_lvmax` (açık en yüksek bölüm), `pbu_lvs` (bölüm→yıldız). Eski oyuncular için `lvMax = maxReg+1`.
- Menü: BAŞLA (altında "Bölüm N · Şehir") + BÖLÜMLER (`#levels`, 3 sütun ızgara, kilitli/yıldızlı). HUD'da bölüm ilerleme çubuğu (`#lvBar`). Oyun sonu: "Bölüm N: x/len kapı". Görevler: 'win' (N bölüm bitir), 'star3'.
- **Müzik geri**: 9 şehrin her biri için elle yazılmış 32 adımlık ezgi (`MEL`), uzun notalar sonraki boşluğa kadar uzar, Konya ve Adıyaman'da ney/uzun hava titreşimi (`VIB`); ses biraz kısıldı. Menüde seçili bölümün şehrinin müziği. Ses düğmesi 3 durum: Ses Açık → Müzik Kapalı → Ses Kapalı.

## 36 bölüm, daha uzun (8 Kasım 2026)
- `LV_N = 36`, her şehrin 2 yolu var: `lvCity(L) = floor((L-1)/2) % 9`, `lvPart(L)` = 1/2. Gezgin 1–18, Usta 19–36 (`USTA = 19`, `isUsta`; gece başlar). 2. yol gün batımına yakın başlar.
- Uzunluk `lvLen(L) = 30 + floor((L-1)*.58)` → 30…50 kapı. Zorluk `dScore() = (L-1)*3 + score*.35` (hız Bölüm 1 ≈58 → Bölüm 36 ≈116–125).
- Kullanıcı isteğiyle bölüm ilerlemesi sıfırlandı: `pbu_lvv` 3 değilse `lvMax=1`, yıldızlar silinir (fındık, garaj, pasaport, kartpostallar korunur).
- Düzeltme: Bölümler ekranında 1'e basınca en son bölüme atlıyordu (`lvInit` bayrağı).

## Şehir lezzetleri + arka planda şehir adı (9 Kasım 2026)
- Arka planda (gökyüzünde, H*.3) saydam büyük harf şehir adı (`drawBackground` içinde, Pixelify 24px, gündüz %16 gece %10 opaklık, menüde daha soluk).
- Her şehre özel toplanabilir (`SPEC[reg]`, `SPEC_NAME`, item type 'spc', +3 fındık, ilk toplamada bilgi notu): Kapadokya üzüm, İstanbul simit, Sivas köftesi, Bursa kestane şekeri, Konya etli ekmek, Ankara armudu, Erzurum cağ kebabı, Adıyaman çiğ köfte, Antalya portakal. Olasılık %32 (İstanbul/Antalya %42). Görev 'spc' eklendi; simit/portakal görevleri hâlâ sayılıyor. Şehir ipuçları lezzeti söylüyor.

## Şehir sırası değişti (9 Kasım 2026)
- `LV_ORDER = [0,1,2,6,7,3,4,5,8]`: Kapadokya → İstanbul → Sivas → **Erzurum → Adıyaman** → Bursa → Konya → Ankara → Antalya. `lvCity(L)` bu sıradan okur. Şehir indeksleri (REG, CITY_NAME, CARDS…) değişmedi.
- `maxReg` (`pbu_reg`) artık şehir indeksi değil, bu sıradaki **pozisyon** (`cityPos(ci)`); pasaport görünürlüğü, görev ön koşulları ve "Gezilen şehir" buna göre. Pasaport şehirleri yeni sırada listeler.

## Garaj: sadece sincaplar, pahalı fiyatlar, yeni harcama yerleri (9 Kasım 2026)
- `CHARS` artık yalnız sincap türleri: Kızıl (0), Gri (80), Kar (160), Anadolu (260, 1 çarpmayı affeder), Kara (380, %25 çift fındık), Çizgili (520, 2x palamut, başta çizgi), Uçan (700, mıknatısla başlar, yan zar), Altın (1000, her 10 kapıda +5, parıltı). Tilki/Kirpi/Baykuş/Van Kedisi kaldırıldı (eski seçim `byId` ile Kızıl Sincap'a düşer).
- Fiyatlar ~3 kat: balonlar 60/140/240/390/660/1050, güç yükseltmeleri `UP_COST` [120,240,420,660,960].
- Yeni sekmeler (Sincap · Balon · Şapka · İz · Güç):
  - **Şapka** (`HATS`, `HATS_DRAW`, `pbu_own_hat`/`pbu_sel_hat`): Fes 150, Kar Beresi 220, Kasket 300, Çiçek Taç 400, Pilot Başlığı 550, Sikke 650, Altın Taç 900; `renderPlayer` `o.hat` ile çizer.
  - **İz** (`TRAILS`, `pbu_own_tr`/`pbu_sel_tr`): Bulut 120, Yıldız Tozu 260, Konfeti 380, Kalpler 480, Nazar 600, Gökkuşağı 850; oyunda balon arkasında parçacık izi.
  - **Güç** sekmesinde **Hazırlık** (tek kullanımlık, `inv`/`pbu_inv`, bölüm başında `useCons()` otomatik): Başlangıç Kalkanı 40 (5 sn), Mıknatıslı Başlangıç 35 (8 sn), Çift Fındık 90 (bölüm boyunca `dblNuts`).

## Oyunun adı "Uçan Sincap" (10 Kasım 2026)
- Başlık ve menüden "Kapadokya" kaldırıldı; alt yazı "Balonla Türkiye'yi gez: 9 şehir, 36 bölüm". GitHub deposu adı: `ucan-sincap` (kullanıcı açacak; sonra push + GitHub Pages).

## Taç Kapı (11 Kasım 2026)
- Bölümün son kapısı (Büyük Kapı) geçilince +15 fındık ve pul verilir ama kutlama artık başlamaz. 250 px sonra büyük bir **Taç Kapı** gelir (`finGate`, `drawCrownGate`): mermer kemer, 2x büyüklükte altın taç amblemi, flamalar, açıklıkta parıldayan ışık perdesi. Çarpışma yok (sadece süs). Görününce "Taç Kapı! İçinden geç, kutlama başlasın!" yazısı çıkar.
- Oyuncu Taç Kapı'dan geçince `startCeleb()` başlar (balonlar, konfeti, fanfar), 3.6 sn sonra `showWin()`. Büyük Kapı sonrası boşluk 320 px.
- Not: testte `shieldT = 999` verilince kalkan süre çubuğu ekran boyu çizgi olarak görünür; bu sadece test kopyasının yan etkisi.

## Tarihi kapı + Ankara + iki yol farklı (11 Kasım 2026 gece)
- Taç Kapı kaldırıldı → `drawGate(x)`: yere oturan, iki kuleli (mazgal + bayrak), çini ve yazı kuşaklı, kırmızı-beyaz ablak taşlı **sivri kemerli tarihi kapı**; kemer içinde mukarnas, kandiller, ışık. Kemerden geçince kutlama (`finGate`).
- Ankara 1. yol arka planı: Anıtkabir ve Atakule kaldırıldı → Ankara Kalesi tepesi + **Hacı Bayram Veli Camii** (piramit çatı, tuğla minare) + Augustus Tapınağı duvarı + evler. 2. yol (`drawAnk2`): **TBMM binası** (sütunlu, kuleli, bayraklı) + **Ulus Meydanı Zafer Anıtı** + güvercinler.
- **Her şehrin 2. yolu farklı** (`lvPart(level) === 2`): `drawRegion` 2. yolda `drawKap2…drawAnt2` çizer; `makeBottom` yol başına farklı yapı seti kullanır:
  - Kapadokya 1: peri bacaları · 2: kaya kaleler; arka plan Uçhisar, güvercinlikler, Kızılırmak, Avanos çömlekleri.
  - İstanbul 1: Galata, Kız Kulesi · 2: Saat Kulesi, **Dikilitaş** (`makeObelisk`); arka plan Sultanahmet & Ayasofya, Haliç, kırmızı tramvay.
  - Sivas 1: Çifte Minareli, kümbet · 2: Gök Medrese, **Divriği taç kapısı** (`makeDivrigi`); arka plan Divriği, Eğri Köprü, koyunlar.
  - Bursa 1: Yeşil Türbe + teleferik · 2: Tophane, Ulu Cami minaresi, üstte bulut; arka plan Cumalıkızık evleri, Irgandı Köprüsü.
  - Konya 1: Mevlâna · 2: İnce Minareli, Alaaddin kümbeti; arka plan Alaaddin Tepesi, Çatalhöyük.
  - Ankara 1: Ankara Kalesi, Hacı Bayram minaresi · 2: **TBMM** (`makeMeclis`), **Ulus Zafer Anıtı** (`makeUlus`), Atakule. (Anıtkabir sadece Büyük Kapı olarak kaldı.)
  - Erzurum 1: Üç Kümbetler · 2: Yakutiye, **Erzurum Kalesi** (`makeAnKale(...,'erzkale')`); arka plan kale + Tepsi Minare + Çifte Minareli.
  - Adıyaman 1: Nemrut başları · 2: Cendere, **Perre** (`makePerre`); arka plan Atatürk Barajı gölü, Cendere Köprüsü, kaya mezarları.
  - Antalya 1: Yivli Minare, Hadrian · 2: **Aspendos** (`makeAspendos`), palmiye; arka plan Aspendos tiyatrosu, Konyaaltı plajı ve şemsiyeler.
- Pasaporta yeni yapılar eklendi (`CITY_LM`, `LMK`, `LM_NAME`).

## Menü yazıları sadeleşti (11 Kasım 2026)
- Ana menüde `.ol` kalın kontur/gölge kaldırıldı (çizik gibi görünüyordu). Başlıkta hafif tek gölge; alt yazı, istatistikler ve ipucu yarı saydam koyu zeminli kutularda, gölgesiz.
- Ana menü başlığı: "UÇAN SİNCAP" ve alt yazı yarı saydam koyu, ince açık çerçeveli bir zemin kutusunda; başlık rengi açık altın (#ffe08a).
