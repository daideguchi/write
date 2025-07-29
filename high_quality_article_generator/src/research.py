import openai

class Research:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def suggest_keywords(self, theme):
        """
        与えられたテーマに基づいて、関連するキーワードを提案します。
        """
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "あなたは、SEOとコンテンツマーケティングに精通した専門家です。与えられたテーマに基づいて、読者の検索意図を網羅するような、関連キーワードを10個提案してください。"},
                {"role": "user", "content": f"テーマ: {theme}"}
            ],
            temperature=0.8,
        )
        return response.choices[0].message.content.strip().split('\n')
