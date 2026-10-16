# dhikr-profile-repo

Dhikr profiles for [weecounter](https://github.com/santarl/weecounter). The app downloads `index.json`
(one small file, at most once a week) and lists the profiles; a profile file is downloaded only when
someone taps it.

## Adding a profile

Put a `.dhikr` file in `profiles/` (open a pull request, or add it yourself). Start it with a header:

```
# Morning Adhkar
@id morning-adhkar
@version 1
@author Your Name
@desc One or two lines about the profile.
@desc More lines are joined with line breaks.

---1
# First slide
...
```

- `@id`: a short unique name made of letters, digits, `-`, `_`, `.`. Never change it afterwards.
- `@version`: a whole number. Raise it every time you change the file, so the app offers an update.
- `@author`, `@desc`: shown in the app. The description pops up once when the profile is first opened.

`index.json` is rebuilt by the **Build index** action on every push. Do not edit it by hand.
Translations and texts must be yours to share, or free to redistribute.
The full profile format is in `dhikr-profile-format.md`.
