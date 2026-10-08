import moodle_docs_theme

project = "moodle-tool_participantscustomfilter"
copyright = "2026, Kelson da Costa Medeiros"
author = "Kelson da Costa Medeiros"
release = "1.0.3"

extensions = [
    "sphinx.ext.githubpages",
    "moodle_docs_theme",
]

templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

html_theme = "moodle_docs_theme"
html_theme_path = [moodle_docs_theme.get_html_theme_path()]

html_theme_options = {
    "project_name": "moodle-tool_participantscustomfilter",
    "tagline": "Filter by custom user profile fields in participants list",
    "github_url": "https://github.com/moodle-by-kelsoncm/tool_participantscustomfilter",
    "github_repo": "moodle-by-kelsoncm/tool_participantscustomfilter",
    "github_version": "main",
    "doc_path": "docs/en/",
    "show_edit_on_github": True,
    "enable_dark_mode": True,
    "enable_language_selector": True,
    "navigation_links": "Home|index, Installation|installation, Configuration|configuration, Usage|usage",
}

html_static_path = []
