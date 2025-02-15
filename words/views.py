from collections import Counter

from rest_framework.response import Response
from rest_framework.views import APIView

from words.models import Word

with open("words/dictionary.txt", 'r') as file:
    ALL_WORDS = set(file.read().splitlines())


class TodaysWord(APIView):
    def get(self, request):
        word = Word.objects.order_by('-id').first()
        if not word:
            return

        return Response({
            "id": word.pk,
            "word": word.word,
            "date": f'{word.created_at}'[0:10].replace('-', '/')
        })


class VerifyWord(APIView):
    def get(self, request, word: str):
        user_word = word.lower()

        if user_word not in ALL_WORDS:
            return Response({
                'success': False,
                'status': "invalid word"
            })

        word_object = Word.objects.order_by('-id').first()
        if word_object:
            today_word = word_object.word

        if user_word == today_word:
            return Response({
                'success': True,
                'status': [2 for _ in range(5)]
            })

        word_letters_validation = [0 for _ in range(5)]
        letters_counter = Counter(today_word)

        for i in range(len(user_word)):
            if user_word[i] == today_word[i]:
                word_letters_validation[i] = 2
                letters_counter[user_word[i]] -= 1

        for i in range(len(user_word)):
            if user_word[i] in today_word \
                and letters_counter[user_word[i]] > 0 \
                    and word_letters_validation[i] == 0:
                word_letters_validation[i] = 1
                letters_counter[user_word[i]] -= 1

        return Response({
            'success': False,
            'status': word_letters_validation
        })
