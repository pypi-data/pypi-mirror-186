..
    Copyright (C) 2020-2022 TU Wien.

    Invenio-Theme-TUW is free software; you can redistribute it and/or
    modify it under the terms of the MIT License; see LICENSE file for more
    details.

Changes
=======

Version 2023.1 (released 2023-01-13, updated 2023-01-19)

- Display the record's first uploaders on the landing pages
- Fix the draft preview page failing with a 404 code


Version 2022.6 (released 2022-10-17, updated 2022-11-30)

- v10 compat: Replace direct 'elasticsearch' import
- v10 compat: Load and pass ``custom_fields`` in ``communities_new`` view function
- Override ``app.config`` to specially handle our ``SITE_{API,UI}_URL`` config items
- Remove the ``communities_new`` override
- Remove "under development" text in frontpage
- Render missing flashed messages
- Rework the initialization procedure used for some custom overrides
- Migrate from setup.py to setup.cfg
- Remove old documents
- Hide the privacy policy for now, until it is accepted and published centrally
- Move Flask config override from Invenio-Theme-TUW to Invenio-Config-TUW
- Disable Matomo integration by default
- Use fallback system font during initial page load
- Update footer logos, links and file links


Version 2022.5 (released 2022-09-06, updated 2022-10-11)

- Add surrounding element to the recent uploads on the frontpage
- Some styling fixes
- Add config variable for Matomo site ID
- Rework the staging warning into a more general customizable warning
- Make the input element sizing on the deposit page more uniform
- Update the contact page
- Self-serve Google fonts used for the TUW corporate design
- Fix missing search bar in results page
- Remove inline styling from templates
- Add total record count to the search bar placeholder
- Scale down hero images
- Add possibility to a render a warning box in the frontpage


Version 2022.4 (released 2022-07-19, updated 2022-08-25)

- v9 compat: Chase upstream changes in our overridden templates
- v9 compat: Add permission guard page for community creation
- Add config variable for the FAQ link
- Remove unnecessary/outdated template and JS overrides
- Refactor directory structure for remaining template overrides
- Add comments marking the changes and their reasons in remaining overrides
- UI enhancements for mobile (side bar and communities frontpage)
- Reverse contents of CHANGES.rst (recent changes are shown on top)
- Fix wrong route in deposit guard template
- Update description in frontpage
- Override the ``communities_new`` view function (to support ``LocalProxy`` objects as ``SITE_UI_URL``)


Version 2022.3 (released 2022-03-11, updated 2022-07-14)

- Make the theme compatible with the v8 release of InvenioRDM
- Fix some styling issues
- Fix race conditions regarding blueprint overrides during init phase
- Add layer of protection around the deposit pages
- Update text on frontpage and contact page
- Reformat jinja templates
- Add tombstone page for Florian
- Refactor the module to actually play nice with InvenioRDM v8


Version 2022.2 (released 2022-02-07)

- Rebrand to 'TU Data Repository'
- Adjust Recent Uploads
- 'More'-button added to frontpage


Version 2022.1 (released 2022-01-26)

- Frontpage lists recent uploads
- Display creators of records nicely on frontpage
- Restyled Records on frontpage


Version 2021.11 (released 2022-01-05)

- Make ready for InvenioRDM v7 and Flask 2.0.2+
- Fix upload deposit upload quota


Version 2021.10 (released 2021-09-27, updated 2021-11-09)

- Add THEME_SITENAME config variable
- Make site name configurable
- Override webpack configuration in order to enable webp image assets
- Fix Manifest file
- Improved Accessibility on frontpage
- Increase Link Contrast
- SEO improvements
- Remove left-over usage of removed config variable
- Removed unintended link on frontpage
- Tooltip added to filenames on record landingpages


Version 2021.9 (released 2021-08-16, updated 2021-09-20)

- Capsulated CSS into Semantic UI Theme
- Fixed UI bugs (sticky header and mobile menu)
- Fixed typos on frontpage
- Fixed button text color
- Fixed footer (footer should still stick to the bottom of the page on pages with small content)
- Fixed Dropdown element font
- Fixed Login/Logout Button
- Added `alt`-text to all images
- Compressed hero images
- Improved Accessibility
- Fix mobile bugs on mobile version
- TU Data renamed to TU Research Data
- Feature section headings renamed
- Fix display of licenses
- Use configured search settings rather than hard-coded values
- Use upstream implementation of "cite as"
- Improve translation support
- Fix checkboxes not having visible check marks


Version 2021.8 (released 2021-07-29, updated 2021-08-12)

- Added hero images.
- Fixed navigation.
- Fix build errors.
- Update module for InvenioRDM 6.0 release.


Version 2021.7 (released 2021-07-29)

- Fix PDF files not being previewed.
- Fix incorrect sources for images in footer.
- Housekeeping (removing old scripts, ...).


Version 2021.6 (released 2021-07-18)

-  Fixes to corporate design, e.g.

   -  login button
   -  flipping tiles
   -  spacing


Version 2021.5 (released 2021-07-16)

- Fix set of distributed files.


Version 2021.4 (released 2021-07-16)

- Implement new TUW corporate design.


Version 2021.3 (released 2021-07-16)

- Fix set of distributed files.


Version 2021.2 (released 2021-07-16)

- Rework caching of result for schemaorg metadata.


Version 2021.1 (released 2021-07-15)

- Initial public release.
