# Basement Poster Machine

A generative poster tool for [@basement.ldn](https://instagram.com/basement.ldn) parties. Type in the lineup once, shuffle until the vibe feels right, and download matching posters for print and Instagram.

**Try it:** https://posle-zavtra.github.io/basement-poster-machine/

## What it does

- **One set of party details, every format:** A4 print (PDF/PNG), Instagram post (1080×1350) and Instagram story (1080×1920), all matching.
- **Shuffle with a mood:** day ↔ night, soft ↔ harsh and clean ↔ chaos sliders steer 12 layouts, dozens of fonts, generative art and effects.
- **Lock what you like:** keep a section fixed while the rest reshuffles.
- **Like / dislike:** the shuffle learns what you like. Liked looks are saved so you can come back to them.
- **Poster codes:** copy a code to reuse a look later with a new lineup.
- **Your own photos and fonts:** drop them in. They stay in your browser.

## Two modes

- **For DJs** (default): the same panels as the designer mode, but the look arrives exactly as the designer sent it. Layout, fonts, vibe and art type are locked. DJs fill in the party, add their photo, pick colourways and move effects and sizes within a small range. **Shuffle** goes through the curated looks, **all looks** opens the full list, **♥ like** keeps favourites on that device.
- **For designers**: the full controls, shuffle, likes and fonts, behind a 4-digit code. Use **★ send to DJs** (sends the photo too) or ☆ on a liked look to add it to the DJ mode.

The curated looks are in `DJ_BUILTIN` in `src/src.html`. In designer mode, use "copy DJ looks file" to export them. The password is only a light gate to keep the full controls out of the way. It is not real security.

## Use

Open `index.html` in any browser, or use the link above. There's nothing to install. In designer mode, press **space** to shuffle, **L** to like and **X** to skip.

## Fonts

Only the open-licence fonts [Geist](https://github.com/vercel/geist-font) and [Space Mono](https://github.com/googlefonts/spacemono) are bundled (SIL OFL, see `fonts/`). The other built-in fonts load from Google Fonts. Please don't commit commercial fonts here: load them in the tool instead.

## Editing

The source is `src/src.html`. Run `python3 src/build.py` to rebuild `index.html` with the fonts embedded.
