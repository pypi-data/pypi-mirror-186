import io
import mimetypes
import os
from typing import List

from google.cloud import vision
from PIL import Image

from .pdfhandler import pdf_to_image


class BotCloudVisionPlugin:
    def __init__(self) -> None:
        """BotCloudVisionPlugin
        """
        self._render_rate = 72
        self._json_credentials = None
        self._to_uppercase = False
        self._to_lowercase = False
        self._threshold = None

        self._full_text = ""
        self._entries = []

    def render_rate(self) -> int:
        """The render resolution rate

        Returns:
            int: resolution rate
        """
        return self._render_rate

    def set_render_rate(self, rate: int) -> "BotCloudVisionPlugin":
        """Sets the render resolution rate.

        Args:
            rate (int): resolution rate
        """
        self._render_rate = rate
        return self

    def threshold(self) -> int:
        """The threshold to be applied before parsing the image.

        Returns:
            int: Threshold value. By default it is None which means no threshold.
        """
        return self._threshold

    def set_threshold(self, threshold: int) -> "BotCloudVisionPlugin":
        """Set the threshold level to be applied to the image before parsing.

        Args:
            threshold (int): Threshold value. Use `None` for no threshold.
        """
        self._threshold = threshold

    def credentials(self, credentials: str) -> "BotCloudVisionPlugin":
        """The Google Cloud Vision JSON credential file path.

        Args:
            credentials (str): Path to the JSON file.
        """
        self._json_credentials = credentials
        return self

    def full_text(self) -> str:
        """Get the full text from the image.

        Returns:
            str: The full text.
        """
        return self._full_text

    def entries(self) -> List[List]:
        """Get the list of entries after reading the file.

        Each element contains a list of values in which are:
        `text`, `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, `y4` and `page`.

        Returns:
            List[List]: List of entries.
        """
        return self._entries

    def reset_case(self) -> "BotCloudVisionPlugin":
        """Reset the configuration for upper/lower case.
        """
        self._to_uppercase = False
        self._to_lowercase = False
        return self

    def to_upper_case(self) -> "BotCloudVisionPlugin":
        """Convert the text to upper case when processing the file.
        """
        self._to_uppercase = True
        self._to_lowercase = False
        return self

    def to_lower_case(self) -> "BotCloudVisionPlugin":
        """Convert the text to lower case when processing the file.
        """
        self._to_uppercase = False
        self._to_lowercase = True
        return self

    def read(self, filepath: str, raise_on_error: bool = False) -> "BotCloudVisionPlugin":
        """Read the file and set the entries list.

        Args:
          filepath (str): The file path for the image or PDF to be read.
          raise_on_error (bool): Whether or not to raise an exception if it fails.

        Raises:
            ValueError: If file is not an image or PDF.
        """
        if not mimetypes.inited:
            mimetypes.init()
        file_type = mimetypes.guess_type(filepath)[0]

        images = []

        if "/pdf" in file_type:
            images.extend(pdf_to_image(filepath, resolution=self._render_rate))
        elif "image/" in file_type:
            images.append(Image.open(filepath))
        else:
            raise ValueError("Invalid file type. Only images and PDFs are accepted.")

        self._full_text = ""
        self._entries = []

        client = vision.ImageAnnotatorClient.from_service_account_file(self._json_credentials)

        for image in images:
            # TODO: Implement thresholding if needed.
            if self._threshold is not None:
                pass
                # image = threshold(image, threshold)

            buffer = io.BytesIO()
            image.save(buffer, format='PNG')
            try:
                vision_image = vision.Image()
                vision_image.content = buffer.getvalue()
            except TypeError:
                if raise_on_error:
                    raise
                continue
            response = client.text_detection(image=vision_image)

            if response.error.code != 0:
                if raise_on_error:
                    raise RuntimeError(f"Error: {response.error.message}")
                print(f"Error processing image: {response.error.message}")
                continue
            annotations = response.text_annotations
            if len(annotations) > 0:
                text = annotations[0].description.strip()
                self._full_text += os.linesep
                if self._to_lowercase:
                    text = text.lower()
                if self._to_uppercase:
                    text = text.upper()
                self._full_text += text

            start_y = 0

            for page_idx, page in enumerate(response.full_text_annotation.pages, start=1):
                for block in page.blocks:
                    for par in block.paragraphs:
                        for word in par.words:
                            start_y += page.height

                            offset_y = start_y
                            if page_idx == 1:
                                offset_y = 0

                            text = self._word_to_text(word)
                            bbox = word.bounding_box
                            entry = []
                            entry.append(text)
                            entry.append(bbox.vertices[0].x)
                            entry.append(bbox.vertices[0].y+offset_y)
                            entry.append(bbox.vertices[1].x)
                            entry.append(bbox.vertices[1].y+offset_y)
                            entry.append(bbox.vertices[2].x)
                            entry.append(bbox.vertices[2].y+offset_y)
                            entry.append(bbox.vertices[3].x)
                            entry.append(bbox.vertices[3].y+offset_y)
                            entry.append(page_idx)

                            self._entries.append(entry)

        return self

    def _word_to_text(self, word):
        ret = ""
        for s in word.symbols:
            ret += s.text
        return ret
