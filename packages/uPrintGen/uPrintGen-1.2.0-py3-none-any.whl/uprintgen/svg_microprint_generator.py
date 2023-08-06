"""Module for svg microprint generation"""

import math
import logging
from tqdm import tqdm
import svgwrite
from .microprint_generator import MicroprintGenerator


class SVGMicroprintGenerator(MicroprintGenerator):
    """
    Microprint generator implementation that generates svg microprints
    """

    def _load_svg_fonts(self):
        """
        Embeds fonts into svg
        """
        additional_fonts = self.rules.get("additional_fonts",
                                          {"google_fonts": [],
                                           "truetype_fonts": []})

        google_fonts = additional_fonts.get("google_fonts", [])

        truetype_fonts = additional_fonts.get("truetype_fonts", [])

        for _count, google_font in enumerate(google_fonts):
            name = google_font["name"]
            url = google_font["google_font_url"]

            self.drawing.embed_google_web_font(name, url)

        for _count, truetype_font in enumerate(truetype_fonts):
            name = truetype_font["name"]
            truetype_file = truetype_font["truetype_file"]

            self.drawing.embed_font(name, truetype_file)

    def __init__(self, output_filename="microprint.svg", config_file_path="config.json", text=""):
        super().__init__(output_filename=output_filename,
                         config_file_path=config_file_path, text=text)

        self.drawing = svgwrite.Drawing(
            output_filename, (self.microprint_width, self.microprint_height), debug=False)

        self.font_family = self.rules.get("font-family", "monospace")

        self._load_svg_fonts()

    def render_microprint_column(self, first_line, last_line, x_with_gap, y_value, current_line):
        """
        Renders one column of the microprint
        """
        backgrounds = self.drawing.add(self.drawing.g())

        default_text_color = self.default_colors["text_color"]

        texts = self.drawing.add(self.drawing.g(
            font_size=self.scale, fill=default_text_color))

        attributes = {'xml:space': 'preserve',
                      "font-family": self.font_family}

        texts.update(attributes)

        text_lines = self.text_lines[first_line:last_line]

        for text_line in tqdm(text_lines, total=len(text_lines), desc="Generating rows"):
            background_color = self.check_color_line_rule(
                color_type="background_color", text_line=text_line)

            background_rect = self.drawing.rect(insert=(x_with_gap, y_value),
                                                size=(self.column_width,
                                                      self.scale + 0.3),
                                                rx=None, ry=None, fill=background_color)

            text_color = self.check_color_line_rule(
                color_type="text_color", text_line=text_line)

            text = self.drawing.text(text_line, insert=(x_with_gap, y_value),
                                     fill=text_color, dominant_baseline="hanging")

            text.update({"data-text-line": current_line})
            background_rect.update({"data-text-line": current_line})

            backgrounds.add(background_rect)
            texts.add(text)

            y_value += self.scale_with_spacing

            current_line += 1

    def render_microprint(self):
        logging.info('Generating svg microprint')

        default_background_color = self.default_colors["background_color"]

        self.drawing.add(self.drawing.rect(insert=(0, 0), size=('100%', '100%'),
                                           rx=None, ry=None, fill=default_background_color))

        current_line = 0

        for column in tqdm(range(self.number_of_columns),
                           total=self.number_of_columns, desc="Generating columns"):
            x_value = math.ceil(column * self.column_width)
            x_with_gap = x_value if column == 0 else x_value + self.column_gap_size

            self.drawing.add(self.drawing.rect(
                insert=(x_with_gap, 0), size=(self.column_width, '100%'),
                rx=None, ry=None, fill=default_background_color))

            if column != 0:
                self.drawing.add(self.drawing.rect(
                    insert=(x_value, 0), size=(self.column_gap_size, '100%'),
                    rx=None, ry=None, fill=self.column_gap_color))

            y_value = 0

            first_line = math.ceil(column * self.text_lines_per_column)

            last_line = min(
                math.ceil((column + 1) * self.text_lines_per_column), len(self.text_lines) - 1)

            if first_line >= len(self.text_lines):
                break

            self.render_microprint_column(
                first_line=first_line,
                last_line=last_line, x_with_gap=x_with_gap,
                y_value=y_value, current_line=current_line)

            current_line += self.text_lines_per_column

        self.drawing.save()

        logging.info("Microprint saved as '%s'", self.output_filename)
