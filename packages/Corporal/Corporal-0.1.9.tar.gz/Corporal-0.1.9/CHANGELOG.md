
# Changelog
All notable changes to Corporal will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [0.1.9] - 2023-01-18
### Changed
- Use handler to build menus.
- Include sample config files in manifest.
- Tweak view config per upstream changes.
- Remove reference to `rattail[auth]` extra.
- Add support for new-style `corporal install` command.

## [0.1.8] - 2023-01-02
### Changed
- Register entry points for emails.
- Expose app setting for default grid pagesize.
- Add ASGI app wrapper.

## [0.1.7] - 2022-03-10
### Changed
- Remove DB config from web app startup.
- Move CORE-specific vendor catalog view logic to tailbone-corepos.
- Tweak how product lookup happens for vendor catalog batch.
- Rename routes for `poser_reports` per upstream changes.

## [0.1.6] - 2022-03-02
### Changed
- Add import/export views and menu link.
- Add views, menus for Poser Reports.

## [0.1.5] - 2021-11-04
### Changed
- Add menu entry for CORE Member Batches.

## [0.1.4] - 2021-08-02
### Changed
- Parse the Fannie config file to get lane definitions for rattail.conf (when deploying).
- Include email setting for CORE Office -> Lane export.
- Add CORE Office URL to deployed Corporal config.

## [0.1.3] - 2021-06-15
### Changed
- Just show default favicon and header image.

## [0.1.2] - 2021-06-15
### Changed
- More fabric tweaks for basic Corporal app install.
- Remove version restriction for mysql-connector-python.

## [0.1.1] - 2021-06-11
### Changed
- Freeze sqlalchemy version per pip issues

## [0.1.0] - 2021-06-11
### Added
- Initial release, to test install
