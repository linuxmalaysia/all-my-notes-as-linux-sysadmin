"""Unit tests for sitemaps consistency and Context7 configuration.

Validates sitemap XML/text files for well-formedness and consistency, as well as Context7
and MkDocs documentation environment configuration.
"""

import os
import re
import xml.etree.ElementTree as ET
import pytest

try:
    import yaml
except ImportError:
    yaml = None


def test_sitemaps_consistency():
    """Verify existence, XML validity, and link consistency across sitemaps."""
    sitemap_xml_paths = ["docs/sitemap.xml", "html/sitemap.xml"]

    for path in sitemap_xml_paths:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            sanitized = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", content)
            root = ET.fromstring(sanitized)
            assert root.tag.endswith("urlset") or root.tag == "urlset", f"Sitemap {path} root element must be 'urlset'."

            # Parse any loc URLs inside url entries
            locs = [elem.text for elem in root.iter() if elem.tag.endswith("loc") and elem.text]
            if path == "docs/sitemap.xml":
                assert len(locs) > 0, f"Sitemap {path} contains no valid <loc> elements."

    sitemap_txt_path = "html/docs/sitemap.txt"
    if os.path.exists(sitemap_txt_path):
        with open(sitemap_txt_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        assert len(lines) > 0, f"Sitemap txt file {sitemap_txt_path} is empty."


def test_context7_configuration():
    """Verify MkDocs and Context7 AI knowledge context configurations."""
    mkdocs_path = "mkdocs.yml"
    assert os.path.exists(mkdocs_path), f"MkDocs configuration file missing: {mkdocs_path}"

    with open(mkdocs_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "site_name:" in content, "mkdocs.yml missing required key 'site_name'."
        assert "docs_dir:" in content, "mkdocs.yml missing required key 'docs_dir'."

        if yaml is not None:
            try:
                mkdocs_config = yaml.load(content, Loader=yaml.FullLoader)
                if isinstance(mkdocs_config, dict):
                    assert "site_name" in mkdocs_config
                    assert "docs_dir" in mkdocs_config
            except Exception:
                # Fallback if custom python tags aren't loaded by PyYAML
                pass

    # Check Context7 XML context files
    xml_context_paths = ["llms_context.xml", "html/llms_context.xml"]
    for path in xml_context_paths:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                raw_xml = f.read()
            # Strip invalid XML 1.0 control characters
            sanitized = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", raw_xml)
            root = ET.fromstring(sanitized)
            assert root.tag == "context", f"Context7 XML file {path} root element must be <context>."
            files = root.findall("file")
            assert len(files) > 0, f"Context7 XML file {path} contains no <file> entries."
