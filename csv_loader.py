import os
import re

import folder_paths

# ARTISTS


class ArtistsCSVLoader:
    """
    Loads csv file with artists.
    """

    @staticmethod
    def load_artists_csv(artists_path: str):
        """Loads csv file with artists. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of artists. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        artists = {"Error loading artists.csv, check the console": ["", ""]}
        if not os.path.exists(artists_path):
            print(
                f"""Error. No artists.csv found. Put your artists.csv in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """
            )
            return artists
        try:
            with open(artists_path, "r", encoding="utf-8") as f:
                artists = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                artists = {x[0]: [x[1], x[2]] for x in artists}
        except Exception as e:
            print(
                f"""Error loading artists.csv. Make sure it is in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """
            )
        return artists

    @classmethod
    def INPUT_TYPES(cls):
        artists_csv_path = os.path.join(
            folder_paths.base_path,
            "custom_nodes",
            "ComfyUI-CSV-Loader",
            "CSV",
            "artists.csv",
        )
        cls.artists_csv = cls.load_artists_csv(artists_csv_path)
        return {
            "required": {
                "artists": (list(cls.artists_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, artists):
        return (self.artists_csv[artists][0], self.artists_csv[artists][1])


# ARTMOVEMENTS


class ArtmovementsCSVLoader:
    """
    Loads csv file with artmovements. For migration purposes from automatic11111 webui.
    """

    @staticmethod
    def load_artmovements_csv(artmovements_path: str):
        artmovements = {"Error loading artmovements.csv, check the console": ["", ""]}
        if not os.path.exists(artmovements_path):
            print(
                f"""Error. No artmovements.csv found. Put your artmovements.csv in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """
            )
            return artmovements
        try:
            with open(artmovements_path, "r", encoding="utf-8") as f:
                artmovements = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                artmovements = {x[0]: [x[1], x[2]] for x in artmovements}
        except Exception as e:
            print(
                f"""Error loading artmovements.csv. Make sure it is in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """
            )
        return artmovements

    @classmethod
    def INPUT_TYPES(cls):
        artmovements_csv_path = os.path.join(
            folder_paths.base_path,
            "custom_nodes",
            "ComfyUI-CSV-Loader",
            "CSV",
            "artmovements.csv",
        )
        cls.artmovements_csv = cls.load_artmovements_csv(artmovements_csv_path)
        return {
            "required": {
                "artmovements": (list(cls.artmovements_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, artmovements):
        return (
            self.artmovements_csv[artmovements][0],
            self.artmovements_csv[artmovements][1],
        )


# CHARACTERS


class CharactersCSVLoader:
    """
    Loads csv file with characters. For migration purposes from automatic11111 webui.
    """

    @staticmethod
    def load_characters_csv(characters_path: str):
        characters = {"Error loading characters.csv, check the console": ["", ""]}
        if not os.path.exists(characters_path):
            print(
                f"""Error. No characters.csv found. Put your characters.csv in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """
            )
            return characters
        try:
            with open(characters_path, "r", encoding="utf-8") as f:
                characters = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                characters = {x[0]: [x[1], x[2]] for x in characters}
        except Exception as e:
            print(
                f"""Error loading characters.csv. Make sure it is in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """
            )
        return characters

    @classmethod
    def INPUT_TYPES(cls):
        characters_csv_path = os.path.join(
            folder_paths.base_path,
            "custom_nodes",
            "ComfyUI-CSV-Loader",
            "CSV",
            "characters.csv",
        )
        cls.characters_csv = cls.load_characters_csv(characters_csv_path)
        return {
            "required": {
                "characters": (list(cls.characters_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, characters):
        return (self.characters_csv[characters][0], self.characters_csv[characters][1])


# COLORS


class ColorsCSVLoader:
    """
    Loads csv file with colors. For migration purposes from automatic11111 webui.
    """

    @staticmethod
    def load_colors_csv(colors_path: str):
        colors = {"Error loading colors.csv, check the console": ["", ""]}
        if not os.path.exists(colors_path):
            print(
                f"""Error. No colors.csv found. Put your colors.csv in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """
            )
            return colors
        try:
            with open(colors_path, "r", encoding="utf-8") as f:
                colors = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                colors = {x[0]: [x[1], x[2]] for x in colors}
        except Exception as e:
            print(
                f"""Error loading colors.csv. Make sure it is in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """
            )
        return colors

    @classmethod
    def INPUT_TYPES(cls):
        colors_csv_path = os.path.join(
            folder_paths.base_path,
            "custom_nodes",
            "ComfyUI-CSV-Loader",
            "CSV",
            "colors.csv",
        )
        cls.colors_csv = cls.load_colors_csv(colors_csv_path)
        return {
            "required": {
                "colors": (list(cls.colors_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, colors):
        return (self.colors_csv[colors][0], self.colors_csv[colors][1])


# COMPOSITION


class CompositionCSVLoader:
    """
    Loads csv file with composition. For migration purposes from automatic11111 webui.
    """

    @staticmethod
    def load_composition_csv(composition_path: str):
        composition = {"Error loading composition.csv, check the console": ["", ""]}
        if not os.path.exists(composition_path):
            print(
                f"""Error. No composition.csv found. Put your composition.csv in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """
            )
            return composition
        try:
            with open(composition_path, "r", encoding="utf-8") as f:
                composition = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                composition = {x[0]: [x[1], x[2]] for x in composition}
        except Exception as e:
            print(
                f"""Error loading composition.csv. Make sure it is in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """
            )
        return composition

    @classmethod
    def INPUT_TYPES(cls):
        composition_csv_path = os.path.join(
            folder_paths.base_path,
            "custom_nodes",
            "ComfyUI-CSV-Loader",
            "CSV",
            "composition.csv",
        )
        cls.composition_csv = cls.load_composition_csv(composition_csv_path)
        return {
            "required": {
                "composition": (list(cls.composition_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, composition):
        return (
            self.composition_csv[composition][0],
            self.composition_csv[composition][1],
        )


# LIGHTING


class LightingCSVLoader:
    """
    Loads csv file with lighting. For migration purposes from automatic11111 webui.
    """

    @staticmethod
    def load_lighting_csv(lighting_path: str):
        lighting = {"Error loading lighting.csv, check the console": ["", ""]}
        if not os.path.exists(lighting_path):
            print(
                f"""Error. No lighting.csv found. Put your lighting.csv in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """
            )

            return lighting
        try:
            with open(lighting_path, "r", encoding="utf-8") as f:
                lighting = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                lighting = {x[0]: [x[1], x[2]] for x in lighting}
        except Exception as e:
            print(
                f"""Error loading lighting.csv. Make sure it is in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """
            )
        return lighting

    @classmethod
    def INPUT_TYPES(cls):
        lighting_csv_path = os.path.join(
            folder_paths.base_path,
            "custom_nodes",
            "ComfyUI-CSV-Loader",
            "CSV",
            "lighting.csv",
        )
        cls.lighting_csv = cls.load_lighting_csv(lighting_csv_path)
        return {
            "required": {
                "lighting": (list(cls.lighting_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, lighting):
        return (self.lighting_csv[lighting][0], self.lighting_csv[lighting][1])


# SETTINGS


class SettingsCSVLoader:
    """
    Loads csv file with settings. For migration purposes from automatic11111 webui.
    """

    @staticmethod
    def load_settings_csv(settings_path: str):
        settings = {"Error loading settings.csv, check the console": ["", ""]}
        if not os.path.exists(settings_path):
            print(
                f"""Error. No settings.csv found. Put your settings.csv in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """
            )
            return settings
        try:
            with open(settings_path, "r", encoding="utf-8") as f:
                settings = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                settings = {x[0]: [x[1], x[2]] for x in settings}
        except Exception as e:
            print(
                f"""Error loading settings.csv. Make sure it is in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """
            )
        return settings

    @classmethod
    def INPUT_TYPES(cls):
        settings_csv_path = os.path.join(
            folder_paths.base_path,
            "custom_nodes",
            "ComfyUI-CSV-Loader",
            "CSV",
            "settings.csv",
        )
        cls.settings_csv = cls.load_settings_csv(settings_csv_path)
        return {
            "required": {
                "settings": (list(cls.settings_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, settings):
        return (self.settings_csv[settings][0], self.settings_csv[settings][1])


# STYLES


class StylesCSVLoader:
    """
    Loads csv file with styles. For migration purposes from automatic11111 webui.
    """

    @staticmethod
    def load_styles_csv(styles_path: str):
        styles = {"Error loading styles.csv, check the console": ["", ""]}
        if not os.path.exists(styles_path):
            print(
                f"""Error. No styles.csv found. Put your styles.csv in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """
            )
            return styles
        try:
            with open(styles_path, "r", encoding="utf-8") as f:
                styles = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                styles = {x[0]: [x[1], x[2]] for x in styles}
        except Exception as e:
            print(
                f"""Error loading styles.csv. Make sure it is in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """
            )
        return styles

    @classmethod
    def INPUT_TYPES(cls):
        styles_csv_path = os.path.join(
            folder_paths.base_path,
            "custom_nodes",
            "ComfyUI-CSV-Loader",
            "CSV",
            "styles.csv",
        )
        cls.styles_csv = cls.load_styles_csv(styles_csv_path)
        return {
            "required": {
                "styles": (list(cls.styles_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, styles):
        return (self.styles_csv[styles][0], self.styles_csv[styles][1])


# POSITIVE


class PositiveCSVLoader:
    """
    Loads csv file with positive. For migration purposes from automatic11111 webui.
    """

    @staticmethod
    def load_positive_csv(positive_path: str):
        positive = {"Error loading positive.csv, check the console": ["", ""]}
        if not os.path.exists(positive_path):
            print(
                f"""Error. No positive.csv found. Put your positive.csv in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """
            )
            return positive
        try:
            with open(positive_path, "r", encoding="utf-8") as f:
                positive = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                positive = {x[0]: [x[1], x[2]] for x in positive}
        except Exception as e:
            print(
                f"""Error loading positive.csv. Make sure it is in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """
            )
        return positive

    @classmethod
    def INPUT_TYPES(cls):
        positive_csv_path = os.path.join(
            folder_paths.base_path,
            "custom_nodes",
            "ComfyUI-CSV-Loader",
            "CSV",
            "positive.csv",
        )
        cls.positive_csv = cls.load_positive_csv(positive_csv_path)
        return {
            "required": {
                "positive": (list(cls.positive_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, positive):
        return (self.positive_csv[positive][0], self.positive_csv[positive][1])


# NEGATIVE


class NegativeCSVLoader:
    """
    Loads csv file with negative. For migration purposes from automatic11111 webui.
    """

    @staticmethod
    def load_negative_csv(negative_path: str):
        negative = {"Error loading negative.csv, check the console": ["", ""]}
        if not os.path.exists(negative_path):
            print(
                f"""Error. No negative.csv found. Put your negative.csv in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """
            )
            return negative
        try:
            with open(negative_path, "r", encoding="utf-8") as f:
                negative = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                negative = {x[0]: [x[1], x[2]] for x in negative}
        except Exception as e:
            print(
                f"""Error loading negative.csv. Make sure it is in the custom_nodes-ComfyUI_Loader-CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """
            )
        return negative

    @classmethod
    def INPUT_TYPES(cls):
        negative_csv_path = os.path.join(
            folder_paths.base_path,
            "custom_nodes",
            "ComfyUI-CSV-Loader",
            "CSV",
            "negative.csv",
        )
        cls.negative_csv = cls.load_negative_csv(negative_csv_path)
        return {
            "required": {
                "negative": (list(cls.negative_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, negative):
        return (self.negative_csv[negative][0], self.negative_csv[negative][1])


# NODE NAMING

NODE_CLASS_MAPPINGS = {
    "Load Artists CSV": ArtistsCSVLoader,
    "Load Artmovements CSV": ArtmovementsCSVLoader,
    "Load Characters CSV": CharactersCSVLoader,
    "Load Colors CSV": ColorsCSVLoader,
    "Load Composition CSV": CompositionCSVLoader,
    "Load Lighting CSV": LightingCSVLoader,
    "Load Settings CSV": SettingsCSVLoader,
    "Load Styles CSV": StylesCSVLoader,
    "Load Positive CSV": PositiveCSVLoader,
    "Load Negative CSV": NegativeCSVLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ArtistsCSVLoader": "Load Artists CSV Node",
    "ArtmovementsCSVLoader": "Load Art Movements CSV Node",
    "CharactersCSVLoader": "Load Characters CSV Node",
    "ColorsCSVLoader": "Load Colors CSV Node",
    "CompositionCSVLoader": "Load Composition CSV Node",
    "LightingCSVLoader": "Load Lighting CSV Node",
    "SettingsCSVLoader": "Load Settings CSV Node",
    "StylesCSVLoader": "Load Styles CSV Node",
    "PositiveCSVLoader": "Load Positive CSV Node",
    "NegativeCSVLoader": "Load Negative CSV Node",
}
