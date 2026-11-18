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

- **For DJs** (default): fill in the party details and press **shuffle** (or space) to go through the curated looks with new colours. ‹ › steps through them in order. Small safe tweaks: photo size and position, colourway, vibe sliders, grain, glitch, rgb split, glow, soft focus, photocopy, name and lineup size. **♥ like** keeps favourites in Likes on that device, and **all looks** opens the full list. Text always stays readable.
- **For designers**: the full controls, shuffle, likes and fonts, behind a 4-digit code. Star a liked look (☆) to send it to the DJ mode.

The curated looks are in `DJ_BUILTIN` in `src/src.html`. In designer mode, use "copy DJ looks file" to export them. The password is only a light gate to keep the full controls out of the way. It is not real security.

## Use

Open `index.html` in any browser, or use the link above. There's nothing to install. In designer mode, press **space** to shuffle, **L** to like and **X** to skip.

## Fonts

Only the open-licence fonts [Geist](https://github.com/vercel/geist-font) and [Space Mono](https://github.com/googlefonts/spacemono) are bundled (SIL OFL, see `fonts/`). The other built-in fonts load from Google Fonts. Please don't commit commercial fonts here: load them in the tool instead.

## Editing

The source is `src/src.html`. Run `python3 src/build.py` to rebuild `index.html` with the fonts embedded.
