from groq import Groq
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class GeminiChatService:
    def __init__(self):
        api_key = getattr(settings, "GROQ_API_KEY", None)
        
        print(f"🔑 API Key loaded: {'Yes' if api_key else 'No'}")
        
        if not api_key:
            print("❌ GROQ_API_KEY missing in settings")
            self.client = None
            return

        try:
            # Initialize Groq client
            self.client = Groq(api_key=api_key)
            print("✅ Groq initialized successfully")
        except Exception as e:
            print(f"❌ Groq init error: {e}")
            self.client = None

    def get_response(self, session, user_message):
        """Handle text-only messages"""
        if not self.client:
            return "⚠️ AI service not configured. Please check your API key configuration."

        try:
            if not user_message or not user_message.strip():
                return "Please enter a valid message."
            
            print(f"📩 User: {user_message}")

            # Make API call to Groq
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant. Provide clear, concise, and accurate responses."},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=500,
            )

            # Extract response
            if response and hasattr(response, "choices") and len(response.choices) > 0:
                reply = response.choices[0].message.content
                print(f"✅ AI: {reply[:100]}...")
                return reply

            return "⚠️ No response received from AI."

        except Exception as e:
            print(f"❌ Groq error: {e}")
            logger.error(f"Groq API error: {e}", exc_info=True)
            return f"⚠️ Error: {str(e)}"