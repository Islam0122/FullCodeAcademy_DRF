from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.shortcuts import get_object_or_404

class ListNotes(APIView):
     serializer_class = NoteSerializer
     queryset = Note.objects.all()

     def get(self, request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data)

     def post(self, request, format=None):
         serializer = NoteSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailNote(APIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get(self, request, pk, *args, **kwargs):
        notes = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(notes)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(instance=note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)