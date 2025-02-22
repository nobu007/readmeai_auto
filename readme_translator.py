import argparse
import logging
import os
import sys
from typing import List, Optional

import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai.types import generation_types

# 環境変数の読み込み
load_dotenv()

# ロギング設定
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# ツールのディレクトリ取得
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(TOOL_DIR, "prompts")

# サポートする言語（ISO 639-1コード）
# lang_code: lang_name
SUPPORTED_LANGUAGES = {
    "en": "English",
    "zh": "Chinese",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "ja": "Japanese",
    "ko": "Korean",
    "ru": "Russian",
}

# 再翻訳しない対象リスト
RETRANSLATION_EXCLUDED_FILES = []
for lang_code_ in SUPPORTED_LANGUAGES.keys():
    RETRANSLATION_EXCLUDED_FILES.append("_" + lang_code_.upper() + ".md")


# システムプロンプトの読み込み
def load_translation_prompt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


class ReadmeTranslator:
    def __init__(
        self,
        api_key: Optional[str] = None,
        system_prompt_file: str = os.path.join(PROMPTS_DIR, "SYSTEM_PROMPT.md"),
    ):
        """
        READMEトランスレーターの初期化

        Args:
            api_key (str, optional): Gemini API Key。環境変数から取得されます。
            prompt_file (str, optional): システムプロンプトのファイルパス
        """
        # API Keyの取得（優先順位: 引数 > 環境変数 > .env）
        api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("Gemini API Keyが設定されていません")

        self.system_prompt = load_translation_prompt(system_prompt_file)
        genai.configure(api_key=api_key)
        generation_config = generation_types.GenerationConfig()
        generation_config.temperature = 1.0  # 何度生成しても同じ結果になるように固定
        self.model = genai.GenerativeModel(
            "gemini-2.0-flash-exp", system_instruction=self.system_prompt, generation_config=generation_config
        )

    def translate_text(self, text: str, target_language: str) -> str:
        """
        テキストを指定言語に翻訳する

        Args:
            text (str): 翻訳元のテキスト
            target_language (str): ターゲット言語

        Returns:
            str: 翻訳されたテキスト
        """
        try:
            additional_prompt = "Notice: If the target language is the same as the original language, do not translate and output it as is.\n"
            prompt = f"<order>\nTranslate the following [original_text]. It is README.md.\n{additional_prompt}\nIMPORTANT ORDER: [target language]={target_language}\n</order>\n<original_text>\n{text}\n</original_text>"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"翻訳エラー: {e}")
            return ""

    def translate_readme(
        self,
        input_file: str = "README.md",
        languages: Optional[List[str]] = None,
        folder: Optional[str] = None,
        exclude: Optional[List[str]] = None,
    ) -> None:
        """
        READMEファイルを指定言語に翻訳

        Args:
            input_file (str): 翻訳元のREADMEファイルパス
            languages (List[str], optional): 翻訳先言語コード
            folder (str, optional): 翻訳対象のフォルダ
            exclude (List[str], optional): 翻訳から除外するファイルまたはフォルダ
        """
        try:
            # デフォルト言語設定
            if languages is None:
                languages = list(SUPPORTED_LANGUAGES.keys())

            # 翻訳対象ファイルのリスト
            files_to_translate = []

            # input_fileのファイル
            if input_file and os.path.isfile(input_file):
                files_to_translate.append(input_file)

            # folderのファイル
            if folder:
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # 再翻訳しないファイルのチェック
                        if any(excluded in file for excluded in RETRANSLATION_EXCLUDED_FILES):
                            continue
                        # 除外ファイルのチェック
                        if exclude and any(excluded in file_path for excluded in exclude):
                            continue
                        files_to_translate.append(file_path)

            # ファイルごとに翻訳と出力
            for file_path in files_to_translate:
                if not os.path.exists(file_path):
                    logger.error(f"ファイルが見つかりません: {file_path}")
                    continue

                with open(file_path, "r", encoding="utf-8") as file:
                    original_text = file.read()

                for lang_code in languages:
                    if lang_code not in SUPPORTED_LANGUAGES:
                        logger.warning(f"サポートされていない言語: {lang_code}")
                        continue

                    try:
                        lang_name = SUPPORTED_LANGUAGES[lang_code]
                        translated_text = self.translate_text(original_text, lang_name)

                        output_file = f"{os.path.splitext(file_path)[0]}_{lang_code.upper()}.md"
                        with open(output_file, "w", encoding="utf-8") as file:
                            file.write(translated_text)

                        logger.info(f"{output_file}に{lang_name}版を出力")

                    except Exception as lang_error:
                        logger.error(f"{lang_name}版への翻訳中にエラー: {lang_error}")

        except Exception as e:
            logger.error(f"翻訳処理中にエラー: {e}")


def cli():
    """
    コマンドラインインターフェース
    """
    parser = argparse.ArgumentParser(description="README多言語化ツール")
    parser.add_argument("-f", "--file", default="README.md", help="翻訳元READMEファイルパス")
    parser.add_argument("-l", "--languages", nargs="+", help="翻訳先言語コード（スペース区切り）")
    parser.add_argument("--folder", help="翻訳対象のフォルダ")
    parser.add_argument("--exclude", nargs="+", help="翻訳から除外するファイルまたはフォルダ")
    parser.add_argument("--list-languages", action="store_true", help="サポート言語一覧を表示")

    args = parser.parse_args()

    # サポート言語表示
    if args.list_languages:
        print("サポート言語一覧:")
        for code, name in SUPPORTED_LANGUAGES.items():
            print(f"{code}: {name}")
        sys.exit(0)

    try:
        translator = ReadmeTranslator()
        translator.translate_readme(
            input_file=args.file, languages=args.languages, folder=args.folder, exclude=args.exclude
        )
    except Exception as e:
        logger.error(f"エラー: {e}")
        sys.exit(1)


def main():
    """メイン実行関数"""
    cli()


if __name__ == "__main__":
    main()
