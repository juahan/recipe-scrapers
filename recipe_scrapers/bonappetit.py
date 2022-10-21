# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback, schemaorg_fallback


class BonAppetit(AbstractScraper):
    @classmethod
    def host(cls):
        return "bonappetit.com"

    def title(self):
        return self.schema.title()

    @schemaorg_fallback
    def author(self):
        pass

    def total_time(self):
        return None

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    @opengraph_fallback
    @schemaorg_fallback
    def image(self):
        pass
