# Contributing

Thanks for helping improve `faker-ecommerce-provider`. This is a small,
data-focused package: most changes are catalog entries or a generation format,
and they should be easy to verify.

This file is the contributor-facing distillation of [`AGENTS.md`](AGENTS.md),
which holds the agent-specific and release rules. The two must not drift: when
you change a rule in one, change it in the other in the same commit.

## Supported versions

- **Python 3.10 – 3.14.** `requires-python` is `>=3.10` and the classifiers list
  3.10 through 3.14; CI runs the test suite on every one of them.
- **Faker >= 18.0.0**, the only runtime dependency. Keep it that way — new
  tooling belongs in the `dev` extra, not in `dependencies`.
- Anything you write must run on 3.10, so no syntax or stdlib API newer than
  that.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Optionally install the hooks: `pre-commit install`, then `pre-commit run
--all-files`. The hooks pin tool versions while CI installs the current release
from the `dev` extra; if the two ever disagree, CI is the authority.

## Checks

These four commands are exactly what CI runs. All must pass before a PR is
ready:

```bash
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m mypy --ignore-missing-imports --no-strict-optional .
```

## Seeded determinism

Consumers pin seeds so their own test fixtures stay stable. That constrains what
this package may do:

- **All randomness comes from the provider helpers** — `self.random_element`,
  `self.random_int`, `self.random_uppercase_letter`, and friends. Never import
  `random`, `secrets`, or `uuid`, and never read the clock. `Faker.seed(n)` must
  fully determine the output.
- **Same seed, same version, same call sequence, same output.** Nothing may
  depend on dict ordering, set iteration, the host locale, or the environment.
- **A method's draw count is part of its behavior.** For a given branch, a call
  should consume a stable sequence of draws; adding an extra draw to an existing
  branch reshuffles every later value for a seeded consumer.
- **Catalog edits do shift the seeded stream**, unavoidably: appending changes
  later draws once the new length changes the index arithmetic, and inserting or
  reordering changes them from the very first draw. That shift is expected for a
  data release — but prefer appending to the end of the tuple, and never reorder
  a catalog for cosmetic reasons.
- **Public shapes are API**: return types, string formats, and the `full_order()`
  keys. Adding a key is additive; renaming or removing one is a breaking change.

## Data rules

From `AGENTS.md`, and binding for every catalog change:

- **Additive by default.** Do not remove an existing entry in order to add a
  newer one. Removal is justified only when the maintainer asks for it, or for a
  duplicate, a typo, or a demonstrably invalid entry.
- **Rebrands add, they don't replace.** When a company changes its name, add the
  current name and keep the older one if that entity is still real, operating,
  or historically meaningful.
- **Real values only.** Real brands, real carriers, real payment methods, real
  status vocabulary. Verify anything you are unsure of against an official
  source before adding it; do not invent entries. Trademarked names appear here
  as plain catalog strings so the fake data reads as realistic — no logos, no
  marketing copy, and nothing implying affiliation or endorsement.
- **Tracking formats follow the carrier's documented format**, for example UPU
  S10 (two letters, nine digits, ISO country code) for postal operators. Match
  the real shape, not an approximation of it.
- **Historical and regional coverage is a feature.** Current, legacy, and
  regional entries can sit side by side.
- Catalogs stay plain tuples on `EcommerceProvider` in
  `faker_ecommerce/provider.py`. No data files, no network access, no import-time
  work.

## Tests for new data

Add focused tests to `tests/test_provider.py`:

- **Pin what you added.** Assert the new entries are present, the way
  `TestCatalogRefresh2026` does, so a later refactor cannot silently drop them.
  A brand-new catalog also goes into the `catalog_names` tuple of
  `test_catalogs_have_no_duplicates`.
- **Assert the shape of any new or changed format** — length, prefix or suffix,
  and character classes — as `test_royal_mail_tracking_format` does for S10,
  rather than only checking the type.
- **Correlated fields are asserted together.** Values derived from another field
  must stay consistent with it: `full_order()` must always emit a
  `tracking_number` that matches its own `carrier`, and `test_full_order` is
  where that is checked. Any new correlation you introduce needs the same
  treatment.
- **Locale coverage.** The provider is currently locale-independent: one global
  catalog set, no per-locale variants. If you add locale-specific behavior,
  cover every locale you claim with its own test and say in the PR which locales
  are covered. For global additions (Pix, iDEAL, UPI, SF Express, and the like),
  name the market the entry belongs to in the PR description.
- Tests stay fast and dependency-free — `pytest` and the package itself, nothing
  more.

## Provenance and licensing of catalog data

- **Cite a source for anything non-obvious**, in the PR description: the
  operator's own site, the standards document (UPU S10 for postal tracking), or
  the payment scheme's official documentation. "Seen somewhere" is not
  provenance.
- **No bulk imports.** Do not paste in a scraped dataset or a wholesale copy of
  someone else's catalogue. Entries are added individually and verified
  individually; names and documented formats are facts, and that is what belongs
  here.
- **Check the licence before reusing a compiled list.** A source under CC BY-SA,
  ODbL, or proprietary terms cannot be vendored into an MIT package. If some
  future catalogue genuinely needs external data, record the source and its
  licence in the PR before it is merged; terms incompatible with MIT are a
  blocker, not a footnote.
- **Never real personal or transactional data**: no real customer records, no
  real order or tracking numbers, no coupon codes that would actually redeem.

## Pull requests

- Keep changes small and focused. A mechanical reformat goes in its own commit,
  separate from substantive edits.
- Run the four checks above before opening the PR.
- Do not bump the version or create tags in a data PR. Releases are
  maintainer-driven and documented in [`AGENTS.md`](AGENTS.md).
