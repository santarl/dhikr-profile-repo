# The quran folder

These files are used by the Quran screen of the weecounter app (https://github.com/santarl/weecounter). They are
not profiles: this folder is not listed in `index.json`, so Browse profiles never shows them. The app downloads them
directly from here.

| File | What it is |
|---|---|
| `quran-full.dhikr` | The whole Quran as a profile file: one slide per verse, the Arabic first and the English as a second view, a heading slide at the start of every surah. |
| `AmiriQuran-Regular.ttf` | The Amiri Quran font, used to show the Arabic. |
| `OFL.txt` | The licence of the font (SIL Open Font License 1.1). It has to travel with every copy of the font. |

## Sources and licences

- **Arabic text:** the Tanzil Project, Uthmani text, https://tanzil.net, licensed under Creative Commons Attribution 3.0.
  The Arabic is not modified. Tanzil's file has the basmala at the start of ayah 1 of surahs 2 to 114 (except 9),
  and it is left there; the app takes it off when it shows it (see the comment in `Qd.java` in the app, which says why).
- **Tables of pages, juz, ruku and sajda** (used by the app, kept in its code): Tanzil's metadata, Copyright (C)
  2008-2009 Tanzil.info, licensed under Creative Commons Attribution 3.0.
- **English:** Marmaduke Pickthall, *The Meaning of the Glorious Koran* (1930), public domain, lightly corrected.
- **Font:** Amiri Quran, Copyright 2010-2022 The Amiri Quran Project Authors (https://github.com/aliftype/amiri),
  licensed under the SIL Open Font License 1.1 (`OFL.txt`). The font file is not modified.
