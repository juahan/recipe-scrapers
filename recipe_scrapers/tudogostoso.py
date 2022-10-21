# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback, schemaorg_fallback
from ._utils import get_minutes, normalize_string


class TudoGostoso(AbstractScraper):
    @classmethod
    def host(cls):
        return "tudogostoso.com.br"

    def title(self):
        return normalize_string(self.soup.find("h1").get_text())

    @schemaorg_fallback
    def author(self):
        pass

    def total_time(self):
        return get_minutes(self.soup.find("time", {"class": "dt-duration"}))

    def ingredients(self):
        ingredients_html = self.soup.findAll("span", {"class": "p-ingredient"})

        return [
            normalize_string(ingredient.get_text()) for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.findAll(
            "div", {"class": "instructions e-instructions"}
        )

        return "\n".join(
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        )

    @opengraph_fallback
    def image(self):
        pass
