# Reza Badpa academic website

Personal academic website for Reza Badpa, a Ph.D. candidate in Physical Oceanography at Stony Brook University.

Live site: https://rezart1427.github.io

## Editing the website

Edit the biography, CV, manuscript, and presentation content in `build.py`, then run `python build.py` to regenerate the HTML. This uses only the Python standard library. Edit `assets/style.css` for styling and replace `assets/Reza-Badpa-CV.docx` when the downloadable CV changes. The public CV excludes phone numbers; keep them excluded in future updates.

The original profile photograph is preserved in `assets/reza-badpa-profile.png`. Its circular crop is controlled by `.profile-mark img` in the stylesheet.

## Preview

Run `python -m http.server 4173 --bind 127.0.0.1` from this folder, then visit http://127.0.0.1:4173.

## Publishing

GitHub Pages publishes the root of the `main` branch. In Settings > Pages, select Deploy from a branch, then main and /(root). Future pushes to main update the website automatically.

The website uses original code, with its academic layout inspired by https://mattluongo.github.io/.
