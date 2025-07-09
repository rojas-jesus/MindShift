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
