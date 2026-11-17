# Basement Poster Machine

A one-page poster generator for [@basement.ldn](https://instagram.com/basement.ldn) parties. You type in the party details once, shuffle until the look feels right, and export everything:

- A4 print PDF (optionally with 3 mm bleed) and PNG
- Instagram post (1080×1350)
- Instagram story (1080×1920)
- all of them together as one zip

It's a single `index.html` with no build step and no server. Open it in a browser, or use the GitHub Pages link.

## How to use it

1. **Party:** fill in the kicker, name, date, time, venue and lineup.
2. **Vibe:** drag day ↔ night, soft ↔ harsh and clean ↔ chaos. Press **space** or **SHUFFLE** for new options in that mood.
3. **Lock** a section to keep it while the rest shuffles. **↻** on a section shuffles only that section.
4. **♥ like / ✕ not for me** (keys `L` / `X`): likes are saved, and future shuffles lean towards what you like.
5. **#** gives you a poster code. Paste a code to get that look back later. Party details aren't included in the code, so you can reuse a look with a new lineup.
6. **Your own fonts and photos:** drop them into the tool. They stay in your browser and are never uploaded anywhere.

## Fonts

Only open-licence fonts ship in this repo: [Geist](https://github.com/vercel/geist-font) and [Space Mono](https://github.com/googlefonts/spacemono), both under the SIL Open Font License (see `fonts/*/OFL.txt`). The other built-in fonts load from Google Fonts. Please don't commit commercial fonts to this repo. Load them locally in the tool instead.

## Editing

The editable source is `src/src.html`. To rebuild `index.html` with the fonts embedded:

```sh
python3 src/build.py
```

## Notes

- Likes and the short `BSMT-` codes are shared through a database only in the hosted Claude version of the tool. On GitHub Pages they're stored in each person's own browser. The long codes (`B2.…`) work anywhere.
