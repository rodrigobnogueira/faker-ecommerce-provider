# Agent Guidance

This repository contains a Faker provider for generating realistic e-commerce
test data. Keep changes small, data-focused, and easy to verify.

## Project Conventions

- Use the existing provider API shape in `faker_ecommerce/provider.py`.
- Keep the data catalogs (categories, brands, product types, carriers, payment
  methods, statuses, and so on) as plain tuples on `EcommerceProvider`.
- Prefer adding focused tests in `tests/test_provider.py` when changing catalog
  behavior or generation formats.
- Run `python -m pytest` before opening a PR when dependencies are available.
- Do not include local environment files such as `.venv/`, `.pytest_cache/`, or
  editor files in commits.

## Catalog Updates

- Catalog updates should be additive by default.
- Do not remove an existing entry when adding newer ones unless the user clearly
  asks for removal, or unless there is a verified reason such as a duplicate,
  typo, or demonstrably invalid entry.
- When a company rebrands (for example a carrier changing its name), prefer
  adding the current name while keeping the older one if it is still a real,
  operating, or historically meaningful entity.
- Use realistic values only: real brands, real carriers, real payment methods,
  and real status vocabulary. Verify anything you are unsure of against
  official sources before adding it; do not invent entries.
- Carrier-specific tracking formats in `tracking_number()` should follow the
  carrier's real, documented format (for example UPU S10 for postal operators).
- Preserve useful historical coverage. This provider is for realistic fake
  data, so it may include current, legacy, and regional entries side by side.

## Publishing a Release

The primary path is automated: pushing a `vX.Y.Z` tag triggers `.github/workflows/release.yml`,
which runs the tests, builds fresh distributions, verifies the tag matches the `pyproject.toml`
version, and publishes to PyPI via **Trusted Publishing** (OIDC — no token or secret; the
publisher is registered on PyPI under project → Settings → Publishing for `release.yml`,
environment `pypi`). The workflow also supports `workflow_dispatch` to (re)run a release for an
already-pushed tag. The checklist below still applies — the workflow automates the build/upload
steps, not the judgment ones; the manual `twine upload` flow remains a valid fallback.

- Publish only from an up-to-date `main` branch after all intended PRs are merged.
- Check PyPI for the latest published `faker-ecommerce-provider` version before choosing the next version.
- Update both `pyproject.toml` and `faker_ecommerce/__init__.py` to the same release version.
- Run the test suite and build checks before uploading: `python -m pytest`, `python -m build`, and `python -m twine check dist/*`.
- Build fresh artifacts for the version being published. Do not upload stale files from an old `dist/` directory.
- Commit the version bump before publishing.
- Always create and push a matching git tag for every published version, using the format `vX.Y.Z`.
- Create the tag on a commit that already contains `.github/workflows/release.yml` (tag merged `main`, not a pre-merge commit), otherwise the tag push will not trigger the release workflow.
- Upload the checked wheel and source distribution to PyPI with Twine or the repository's configured trusted-publishing workflow.
- After publishing, verify the new version is visible on PyPI and that the git tag points at the release commit.
- Download the published package from PyPI into a fresh environment and run a smoke test against the installed package.
