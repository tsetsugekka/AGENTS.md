# Frontend design

Use only for interface design, redesign, and frontend development involving an interface; do not read for backend-only, data, documentation, or other non-interface tasks. This file is the single detailed source of design preferences; do not duplicate it in the three skills.

## Skill responsibilities

- For new pages, prefer `finesse-ui`: first clarify the page purpose, desired style, and unwanted effects; briefly describe the design direction and implement after confirmation. Prefer localized adjustments for subsequent feedback.
- For redesigning existing pages, prefer the Taste suite's `redesign-existing-projects` (directory `redesign-skill`): first confirm what to retain, the target style, and the scope, then adjust layout, motion, and information density while preserving functionality not requested to change.
- After implementation, use `impeccable audit`, then apply `polish` as needed for actual issues. An audit does not authorize changes; avoid repeated audits or endless polishing.
- These are default responsibilities, not a pipeline requiring all three skills every time. Read only the skills and references needed for the current stage. Explicit user choices, existing project design systems, and the scope of localized changes take precedence; do not mechanically stack conflicting style rules.

## Information density

- Keep desktop and mobile interfaces as compact as practical: first tighten the page's whitespace, padding, margins, line heights, module sizes, and repetitive explanations. Increase information density while preserving readable text, clear hierarchy, and reliable click and touch targets. Keep similar modules consistent in size and spacing.
- Compact does not mean collapsing content or hiding it behind buttons. Optimize the default visible page first; decide whether to hide secondary content based on purpose, frequency of use, and importance. Keep core information and primary actions directly visible.
- App-style navigation does not replace compact design within sections. Tighten settings, filters, tables, options, and empty states as well. Avoid stacking padding, margins, and large empty cards to achieve touch-target height; verify visual dimensions and interaction areas together.

## Design mobile around app-like workflows

- Identify the most frequent mobile activities before organizing the first screen, navigation, and action paths. Reorganize content for the available mobile space rather than merely stacking desktop columns into a long page or scaling them down.
- On market-data pages, prioritize the current instrument, key values, common switches, and charts. Give management, settings, and infrequent explanations clear work areas according to their purpose. Use bottom navigation only when content and frequency justify it; do not mechanically reuse identical tabs or hide primary functionality.
- Make frequent switching directly usable on narrow screens. For a small number of instruments, equal-width symbol buttons may be used, with names, prices, and status grouped in the current instrument's details rather than repeated as large blocks in every switch item. Test the actual maximum count, not just one item.
- Preserve the desktop version's brand, fonts, colors, control language, and business meaning. Mobile may change content order, navigation, and action placement while maintaining selection and state continuity. A mobile-only redesign must not change desktop layout or data logic.
- At realistic narrow-screen sizes, verify core actions, long names, maximum list counts, empty states, loading/errors, scrolling, and fixed-bar occlusion. Do not claim interactions pass based only on CSS or screenshots. Also check desktop to confirm mobile changes do not spill over.
