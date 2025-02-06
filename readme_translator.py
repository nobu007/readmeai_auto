import os
import sys
import argparse
import logging
from typing import List, Optional
import google.generativeai as genai
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# ロギング設定
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

# サポートする言語（ISO 639-1コード）
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

# システムプロンプト
TRANSLATION_SYSTEM_PROMPT = """
You are a highly skilled technical translator specializing in README files. Your task is to accurately translate the following README into [target language].
Follow these detailed guidelines when translating:

1. **Preserve Markdown Structure**:
   - Ensure all headers, bullet points, code blocks, links, and formatting remain intact and consistent with the original.
   - Do not modify or remove any special formatting symbols (e.g., `**`, `#`, `[]()`).

2. **Accuracy and Technical Precision**:
   - For technical content (e.g., code examples, commands, or API documentation), ensure the instructions and terminology are translated with 100% accuracy.
   - Avoid interpreting code or altering technical details; keep all examples unchanged.

3. **Language Fluency and Naturalness**:
   - Translate into natural and fluent language while maintaining clarity and readability.
   - Ensure the text feels written by a native speaker of the target language.

4. **Style and Tone Consistency**:
   - Retain the original tone, whether it is formal, casual, persuasive, or technical.
   - Adapt idioms, cultural references, or expressions to make them more relatable to the target audience.

5. **Error-Free Output**:
   - Proofread the output to eliminate grammar, spelling, or punctuation mistakes.
   - Avoid introducing any ambiguity or inconsistency in the translation.

6. **Handling of Untranslatable Text**:
   - Leave proper nouns, brand names, and file names unchanged unless explicitly requested.
   - Clearly differentiate between translatable text and untranslatable sections like code snippets or commands.

7. **If the target language is the same as the original language, do not translate and output it as is.**

Your goal is to deliver an accurate, high-quality translation that retains the integrity of the original content while making it accessible and engaging for the target audience.
"""


class ReadmeTranslator:
    def __init__(self, api_key: Optional[str] = None):
        """
        READMEトランスレーターの初期化

        Args:
            api_key (str, optional): Gemini API Key。環境変数から取得されます。
        """
        # API Keyの取得（優先順位: 引数 > 環境変数 > .env）
        api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("Gemini API Keyが設定されていません")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            "gemini-2.0-flash-exp", system_instruction=TRANSLATION_SYSTEM_PROMPT
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
        self, input_file: str = "README.md", languages: Optional[List[str]] = None, folder: Optional[str] = None, exclude: Optional[List[str]] = None
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

            # フォルダ内のファイルを再帰的に読み込む
            files_to_translate = []
            if folder:
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if exclude and any(excluded in file_path for excluded in exclude):
                            continue
                        files_to_translate.append(file_path)
            else:
                files_to_translate.append(input_file)

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
    parser.add_argument(
        "-f", "--file", default="README.md", help="翻訳元READMEファイルパス"
    )
    parser.add_argument(
        "-l", "--languages", nargs="+", help="翻訳先言語コード（スペース区切り）"
    )
    parser.add_argument(
        "--folder", help="翻訳対象のフォルダ"
    )
    parser.add_argument(
        "--exclude", nargs="+", help="翻訳から除外するファイルまたはフォルダ"
    )
    parser.add_argument(
        "--list-languages", action="store_true", help="サポート言語一覧を表示"
    )

    args = parser.parse_args()

    # サポート言語表示
    if args.list_languages:
        print("サポート言語一覧:")
        for code, name in SUPPORTED_LANGUAGES.items():
            print(f"{code}: {name}")
        sys.exit(0)

    try:
        translator = ReadmeTranslator()
        translator.translate_readme(input_file=args.file, languages=args.languages, folder=args.folder, exclude=args.exclude)
    except Exception as e:
        logger.error(f"エラー: {e}")
        sys.exit(1)


def main():
    """メイン実行関数"""
    cli()


if __name__ == "__main__":
    main()
