from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Thought

class UserThoughtsTextView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id

        # thoughts it is a list of thoughts 
        thoughts = Thought.objects.filter(user_id=user_id).values_list("description", flat=True)

        numbered_thoughts = []

        index = 1 

        for thought in thoughts:
            line = str(index) + ") " + thought
            numbered_thoughts.append(line)
            index += 1 

        # Join every element of the list into a single string with a visual separator "•"
        thoughts_text = " • ".join(numbered_thoughts)

        return Response({"thoughts_text": thoughts_text})


# AIMLAPI
from openai import OpenAI
import httpx
import os 

timeout_http_client = httpx.Client(timeout=60.0)

client = OpenAI(
    base_url = os.environ.get("AIMLAPI_URL"),
    api_key = os.environ.get("AIMLAPI_KEY"),
    http_client = timeout_http_client
)

class AIThoughtsAnalysisView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        # thoughts it is a list of thoughts 
        thoughts = Thought.objects.filter(user_id=user_id).values_list("description", flat=True)

        numbered_thoughts = []

        index = 1 

        for thought in thoughts:
            line = str(index) + ") " + thought
            numbered_thoughts.append(line)
            index += 1 

        # Join every element of the list into a single string with a visual separator "•"
        thoughts_text = " • ".join(numbered_thoughts)

        prompt = f"You are a mental wellness assistant. Analyze the user's thoughts: {thoughts_text}"

        try:
            response = client.chat.completions.create(
                model="google/gemma-3n-e4b-it",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )

            message = response.choices[0].message.content

            return Response({
                "prompt": prompt,
                "ai_response": message
            })

        except Exception as e:
            return Response({
                "prompt": prompt,
                "error": str(e)
            }, status=500)