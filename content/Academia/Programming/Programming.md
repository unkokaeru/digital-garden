## Academic Projects

MATLAB: [[Computer Algebra and Technical Computing]]
Python: [[MTH1007 Professional Skills and Group Study]]

## Personal Projects

Also: [[Functional Programming]], [Uncensored LLMs](https://www.youtube.com/watch?v=GyllRd2E6fg), [7deadlysongs](https://github.com/bluegreengreen/7deadlysongs/blob/main/7deadlysongs.py), Python Project Template (with Cruft). [Eleven Labs](https://elevenlabs.io/speech-synthesis) is pretty cool, also.

### Sky (Voice Assistant)

**Git Repo**: ...
**Date Started**: ...

A GPT voice assistant with as much integration and usefulness as I can manage.

### Morning Briefing Generation (App)

**Git Repo**: morning-briefing-generation
**Date Started**: 11th November, 2023

This is my largest project thus far, using Python. It aims to generate a natural morning briefing, as if written by a human personal assistant. This is mostly complete and functional, but there are some routes I'd like to continue with, for example being able to run the project within Obsidian with a plugin - which I've now implemented with my obsidian-run-python project.

Next up, adding tests (with pytest, pytest-cov, and a CI/CD pipeline with GitHub), adding asynchronicity (with asyncio, httpx, asynci TaskGroups, etc.), and adding a GUI (PySimpleGUI, Streamlit, Tkinter, PyQT) to customise what's included in the briefing and when it is generated (automatically on a server and pushed with Git?).

After this, my final goal would be to call my phone and play an mp3 file generated with TTS, with a phone API (like Twilio).

### Chess Analysis (App)

**Git Repo**: ...
**Date Started**: ...

Similar to the Chess.com Review feature, give it a PGN (or Chess.com or Lichess link to a game) and it'll return a move-by-move analysis, as well as summary of the different qualities of move found in the game. At the end, it'll estimate the rating of both players and offer improvements and drills.

### Chess Mini-Me (Chess Engine)

**Git Repo**: chess-mini-me
**Date Started**: 24th December 2023

A chess bot that acts at the exact same level as me, with similar openings, etc. - just like the customised Chess.com bots, but it also develops alongside me. It would be quite cool if it could do similar with any Chess.com account, given its URL.

So far, it's a just simple chess engine with a proof-of-concept chess AI. I've utilised [[Python Classes (according to my brother)]], so I can learn a new important programming concept.

### Lingual Mini-Me (Chatbot)

**Git Repo**: ...
**Date Started**: ...

A chat bot that learns a language at the exact same rate as the user - maybe it could do this by simply using a dictionary of vocabulary that is the same as the user, and only generate sentences using grammar that the user has learned, or maybe something else (such as simply performing up to the last standardised test that the user has completed).

The end goal is to be able to talk to someone else naturally with the language the user already knows, for practice and "immersion" - maybe after this it could slowly introduce new vocabulary and grammar, although it might easier to implement that accidentally from the beginning.

### Obsidian Formatter (Obsidian Plugin)

**Git Repo**: obsidian-formatter
**Date Started**: 11th December, 2023

A simple plugin to clean-up the clipboard when you paste something into Obsidian, for example converting LaTeX style and converting grammar.

### Obsidian Assistant (Obsidian Plugin)

**Git Repo**: ...
**Date Started**: ...

[[this one]] describes integrating GPT-4 into an Obsidian Vault so that it can generate notes and manage the vault independently from the user. For example, at the minute I can generate notes and then manually paste them in (with the clipboard being formatted by my Obsidian Formatter plugin), but this plugin would do that all with a simple command typing in the topic name, and that's it.

### Building a GPT

https://www.youtube.com/watch?v=kCc8FmEb1nY.