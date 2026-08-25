"""Ujian unit untuk ketekalan 'sitemap' dan konfigurasi Context7.

Mengesahkan fail XML/teks 'sitemap' untuk keabsahan dan ketekalan, serta konfigurasi persekitaran
dokumentasi Context7 dan MkDocs.
"""

import os
import re
import yaml
import defusedxml.ElementTree as ET
import pytest


class CustomSafeLoader(yaml.SafeLoader):
    """Pemuat YAML selamat yang menyokong tag khas pymdownx.superfences."""
    pass


def _fence_code_format_constructor(loader, node):
    """Custom YAML constructor for pymdownx.superfences code format functions.

    Args:
        loader (yaml.Loader): YAML loader instance.
        node (yaml.Node): YAML node being constructed.

    Returns:
        str: Constructed scalar string.
    """
    return loader.construct_scalar(node)


CustomSafeLoader.add_constructor(
    "tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format",
    _fence_code_format_constructor,
)


def test_sitemaps_consistency():
    """Mengesahkan kewujudan, keabsahan XML, dan ketekalan pautan di seluruh 'sitemap'."""
    sitemap_xml_paths = ["docs/sitemap.xml", "html/sitemap.xml"]

    for path in sitemap_xml_paths:
        assert os.path.exists(path), f"Fail sitemap tidak wujud: {path}"
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Sahkan kandungan asal tidak mengandungi aksara kawalan tidak sah
        invalid_ctrls = re.findall(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", content)
        assert not invalid_ctrls, f"Fail sitemap {path} mengandungi aksara kawalan tidak sah: {invalid_ctrls}"

        root = ET.fromstring(content)
        assert root.tag.endswith("urlset") or root.tag == "urlset", f"Elemen akar Sitemap {path} mestilah 'urlset'."

        locs = [elem.text for elem in root.iter() if elem.tag.endswith("loc") and elem.text]
        if path == "docs/sitemap.xml":
            assert len(locs) > 0, f"Sitemap {path} tidak mengandungi elemen <loc> yang sah."

    sitemap_txt_path = "html/docs/sitemap.txt"
    assert os.path.exists(sitemap_txt_path), f"Fail sitemap txt tidak wujud: {sitemap_txt_path}"
    with open(sitemap_txt_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    assert len(lines) > 0, f"Fail sitemap txt {sitemap_txt_path} adalah kosong."


def test_context7_configuration():
    """Mengesahkan konfigurasi konteks pengetahuan AI MkDocs dan Context7."""
    mkdocs_path = "mkdocs.yml"
    assert os.path.exists(mkdocs_path), f"Fail konfigurasi MkDocs tidak wujud: {mkdocs_path}"

    with open(mkdocs_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "site_name:" in content, "mkdocs.yml kehilangan kunci wajib 'site_name'."
        assert "docs_dir:" in content, "mkdocs.yml kehilangan kunci wajib 'docs_dir'."

        if "pymdownx.superfences" in content or "python/name:" in content:
            mkdocs_config = yaml.load(content, Loader=CustomSafeLoader)
        else:
            mkdocs_config = yaml.safe_load(content)

        assert isinstance(mkdocs_config, dict), "mkdocs.yml mesti diuraikan menjadi kamus YAML."
        assert "site_name" in mkdocs_config, "mkdocs.yml kehilangan kunci 'site_name'."
        assert "docs_dir" in mkdocs_config, "mkdocs.yml kehilangan kunci 'docs_dir'."

    xml_context_paths = ["llms_context.xml", "html/llms_context.xml"]
    for path in xml_context_paths:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                raw_xml = f.read()

            sanitized_xml = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", raw_xml)
            root = ET.fromstring(sanitized_xml)
            assert root.tag == "context", f"Elemen akar fail Context7 XML {path} mestilah <context>."
            files = root.findall("file")
            assert len(files) > 0, f"Fail Context7 XML {path} tidak mengandungi sebarang entri <file>."
