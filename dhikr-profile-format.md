# .dhikr profile format

A `.dhikr` file is a plain UTF-8 text file that describes one weecounter profile: a list of slides, each with a repeat count and some text. Import it from the Profiles screen, or share it to weecounter from another app.

## Quick example

```
# Morning Adhkar

---1
# Ayat al-Kursi
[_]آية الكرسي | Ayat al-Kursi | The Throne Verse
[]

---33
# Subhanallah
[_]سُبْحَانَ اللهِ | Subhanallah | Glory be to Allah
[]
[10]Recite after each prayer

---
Ignored: this text sits outside any slide.
```

The first `# Name` line of the file is the profile name, so the file above is called "Morning Adhkar".

## Structure

A file is a list of slides. Each slide starts with a count line and ends at the next count line or the end of the file.

| Syntax | Meaning |
| --- | --- |
| `---N` | Starts a slide that is counted N times. Any positive number up to 100000 works. |
| `---0` | Starts a slide with a count of 0. It is skipped and never shown. |
| `---` (bare, on its own line) | Ends the text of the current slide. Anything after it, until the next `---N`, is ignored. |

Rules:
- Count lines are matched with optional spaces, so `--- 33` and `---33` both work.
- Text before the first `---N` line is ignored.
- Blank lines are dropped.
- Lines are trimmed, so leading and trailing spaces do not matter.
- Slides with a count of 0 are dropped completely.

## Header fields

Lines at the top of the file, before the first `---N`, can carry details about the profile:

| Line | Meaning |
| --- | --- |
| `# Name` | The first `# ` line is the profile's name when it is pasted as text. |
| `@id slug` | A unique short id (letters, digits, `-`, `_`, `.`). Links an installed profile to its entry in the profile repo, so never change it. |
| `@version N` | A whole number. Raise it for every change, so the app can offer an update. |
| `@author Name` | Shown with the profile. |
| `@desc text` | A description. Repeat the line for more lines, they are joined with line breaks. |

The description pops up once the first time a profile is opened. You can read it again by holding the profile in the profile list, or by tapping it in the browse screen. Author and version show with it.

All header lines are optional, and files without them work as before.

## Title

`# Title` names the slide. Only the first `#` line in a slide is used, and it has these effects:
- It is shown in the title element above the counter, and in the slide list.
- The rest of the slide's text never shows a `#` line.
- Any text line in the slide that exactly matches the title is hidden, so the title is not repeated.

Without a `# Title` line, the slide list shows the start of the slide's first text line (the first alternative, without its `[n]` prefix, cut at 28 characters). The title element stays empty.

Keep the `#` at the start of the line and write the title after it. `#Title` and `# Title` both work.

## Text lines

Each text line is one row of the slide, shown in the counting views.

### Size prefix: `[n]`

A line can begin with `[n]` to set its relative text size:

| Prefix | Meaning |
| --- | --- |
| `[n]` (a number) | Size n relative to the other lines. `[10]` is a little smaller than `[20]`. |
| `[_]` or `[*]` | Takes the remaining size, so the rest of the slide's text fills the space. |
| no prefix | Default size. Uses the same rule as an unnumbered line. |
| `[0]` or `[]` | The line is hidden. The text after it is not shown. |

`[n]` with no text after it is a blank gap of that size. For example, `[10]` on its own leaves a gap.

### Alternative views: `|`

A `|` on a line separates alternative views of the same line. Each position is one view, so a line of three parts (Arabic, transliteration, meaning) gives three views. Switch views with a swipe up or down.

```
[_]Arabic text | Transliteration | Meaning
```

A line without `|` appears in every view.

Each alternative can have its own `[n]` prefix. Blank alternatives are dropped.

```
[_]Arabic | [10]Transliteration | Meaning
```

Lines that are not part of a view (no `|`) show in every view. Views are numbered from 1, and the number of views is the largest number of alternatives on any single line.

## Checklist for a new profile

1. Start with `# Profile Name`.
2. For each slide, write `---N`, then `# Slide title`.
3. Put the text lines below the title. Use `|` for alternative views, and `[n]` if a line needs a size.
4. End each slide with `---` if you want anything after it to be ignored, or leave it out to run into the next slide.
5. Check that every count is above 0 unless you want the slide hidden.

## Version

Rules match weecounter after patch 0035 (header fields) and patch 0031 (title duplicates).
