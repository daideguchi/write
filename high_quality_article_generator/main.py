import os
from dotenv import load_dotenv
from src.research import Research

def main():
    """メイン関数"""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("エラー: OPENAI_API_KEYが設定されていません。 .envファイルを確認してください。")
        return

    researcher = Research(api_key=api_key)

    theme = "AIと人間の協働の未来"
    keywords = researcher.suggest_keywords(theme)

    print(f"--- テーマ: {theme} ---")
    print("関連キーワード:")
    for keyword in keywords:
        print(f"- {keyword}")

if __name__ == "__main__":
    main()
