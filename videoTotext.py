import speech_recognition as sr
import moviepy.editor as mp
import re
from collections import OrderedDict


def vidTotext1(video):   # for c lang
    vid1 = mp.VideoFileClip(video)
    vid1.audio.write_audiofile('clanguage.wav')
    r = sr.Recognizer()
    with sr.AudioFile('clanguage.wav') as source:
        audio = r.record(source)

    text = r.recognize_google(audio)
    return text


def vidTotext4(video):   # for os
    vid1 = mp.VideoFileClip(video)
    vid1.audio.write_audiofile('osvid.wav')
    r = sr.Recognizer()
    with sr.AudioFile('osvid.wav') as source:
        audio = r.record(source)

    text = r.recognize_google(audio)
    return text


def vidTotext0(video):   # for sorting
    vid1 = mp.VideoFileClip(video)
    vid1.audio.write_audiofile('sorting.wav')
    r = sr.Recognizer()
    with sr.AudioFile('sorting.wav') as source:
        audio = r.record(source)

    text = r.recognize_google(audio)
    return text


def vidTotext2(video):   # for english vid
    vid1 = mp.VideoFileClip(video)
    vid1.audio.write_audiofile('engvid.wav')
    r = sr.Recognizer()
    with sr.AudioFile('engvid.wav') as source:
        audio = r.record(source)

    text = r.recognize_google(audio)
    return text


def duplicate(doubt):
    res = list(OrderedDict.fromkeys(doubt))
    return res


def extract0(text):      # for sorting algo
    doubt = re.findall(r"\b\w{4,20}\ssort\b|\b\w{4,20}\salgorithms\b|\b\w{4,12}\s\w{9}y\b", text)
    list1 = duplicate(doubt)
    return list1


def extract1(text):      # for C language
    doubt = re.findall(r"\bm\w{5}\s\bl\w{6}e\b|\bm\w{2}\s\bl\w{3}l\b|\bk\w{5}s\b|\bs\w{5}\s\bp\w{9}g\b|\bp\w{8}\s\bo\w{6}d\b|\bs\w{9}\s\bp\w{9}g\b", text)
    list1 = duplicate(doubt)
    return list1


def extract2(text):      # for english
    doubt = re.findall(r'\bi\w{6}t\b|\bu\w{7}g\b|\bi\w{6}n\b|\bc\w{8}t\b|\bc\w{8}n\b|\bc\w{6}y\b|\bc\w{5}e\b', text)
    list1 = duplicate(doubt)
    return list1


def extract4(text):      # for OS
    doubt = re.findall(r'\bd\w{6}k\b|\bm\w{5}\s\w{9}|\bh\w{3}\s\w{3}\s\w{4}|\bc\w{7}\s\w{4}|\bp\w{8}n\b|\br\w{3}\s\w{4}'
                       , text)
    list1 = duplicate(doubt)
    return list1


