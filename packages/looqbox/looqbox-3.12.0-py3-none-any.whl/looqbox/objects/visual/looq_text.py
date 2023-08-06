from looqbox.objects.visual.abstract_visual_component import AbstractVisualComponent
from looqbox.objects.component_utility.css_option import CssOption as css
from looqbox.render.abstract_render import BaseRender
from multimethod import multimethod


class ObjText(AbstractVisualComponent):
    def __init__(self, text, **properties):
        super().__init__(**properties)
        self.text = text
        self._titles_options = {
            "h1": {
                   "fontSize": css.FontSize(24),
                   "fontWeight": css.FontWeight(700),
                   "color": css.Color("#1C1C1C")
                  },
            "h2": {
                "fontSize": css.FontSize(20),
                "fontWeight": css.FontWeight(600),
                "color": css.Color("#4F4F4F")
                  },
            "h3": {
                "fontSize": css.FontSize(16),
                "fontWeight": css.FontWeight(500),
                "color": css.Color("#808080")
                },
            "default": {
                "fontSize": css.FontSize(11),
                "fontWeight": css.FontWeight(300),
                "color": css.Color("#252626")
                }
        }

    def set_as_title(self, title_level: int | str):
        """
        Method to set a given text as title, using HTML's header tag properties.
        :param title_level: Header level, could be assigned as an integer or the tag name.
        Examples:
            example_title = ObjText("Report Title")
            example_title.set_as_title(1) #or
            example_title.set_as_title("H1")
        # in this case, both methods call will set the text property as an equivalent of <h1></h1> tag
        """

        title_properties = self._get_title_level_properties(title_level)

        self.css_options = css.add(self.css_options, title_properties.get("fontSize"))
        self.css_options = css.add(self.css_options, title_properties.get("fontWeight"))
        self.css_options = css.add(self.css_options, title_properties.get("color"))
        return self

    @multimethod
    def _get_title_level_properties(self, level: int) -> dict:

        level = "h" + str(level)
        properties = self._titles_options.get(level,
                                              self._titles_options["default"]
                                              )

        return properties

    @multimethod
    def _get_title_level_properties(self, level: str) -> dict:

        properties = self._titles_options.get(level.lower(),
                                              self._titles_options["default"]
                                              )

        return properties

    @property
    def set_text_alignment_left(self):
        self.css_options = css.add(self.css_options, css.TextAlign.left)
        return self

    @property
    def set_text_alignment_center(self):
        self.css_options = css.add(self.css_options, css.TextAlign.center)
        return self

    @property
    def set_text_alignment_right(self):
        self.css_options = css.add(self.css_options, css.TextAlign.right)
        return self

    def to_json_structure(self, visitor: BaseRender):
        return visitor.text_render(self)

    def __repr__(self):
        return f"{self.text}"
