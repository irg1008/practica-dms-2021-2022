import json
from typing import List
import os
from dms2122frontend.presentation.web.Question import Question


def getQuestionMocks():

    path = os.path.dirname(__file__)

    questions: List[Question] = []

    q_json = json.loads(
        """
    [
	{
		"id": 0,
		"title": "Pregunta 1",
		"statment": "Saul Hudson (Slash) of the band Guns N&#039; Roses is known for playing what type of guitar?",
		"correct_answer": "Les Paul Standard",
		"incorrect_answers": [
			"Fender Stratocaster",
			"LsL Mongrel",
			"Gretsch Falcon"
		],
		"imageUrl": "",
		"penalty": 0,
		"isPublic": false,
		"score": 1
	},
	{
		"id": 1,
		"title": "Pregunta 2",
		"statment": "Irish musician Hozier released a music track in 2013 titled, &quot;Take Me to ______&quot;",
		"correct_answer": "Church",
		"incorrect_answers": ["Mosque", "Synagogue", "Temple"],
		"imageUrl": "",
		"penalty": 0,
		"isPublic": false,
		"score": 1
	},
	{
		"id": 2,
		"title": "Pregunta 3",
		"statment": "Which song by Swedish electronic musician Avicii samples the song &quot;Something&#039;s Got A Hold On Me&quot; by Etta James?",
		"correct_answer": "Levels",
		"incorrect_answers": ["Fade Into Darkness", "Silhouettes", "Seek Bromance"],
		"imageUrl": "",
		"penalty": 0,
		"isPublic": false,
		"score": 1
	},
	{
		"id": 3,
		"title": "Pregunta 4",
		"statment": "What was the title of Sakamoto Kyu&#039;s song &quot;Ue o Muite Arukou&quot; (I Look Up As I Walk) changed to in the United States?",
		"correct_answer": "Sukiyaki",
		"incorrect_answers": ["Takoyaki", "Sushi", "Oden"],
		"imageUrl": "",
		"penalty": 0,
		"isPublic": false,
		"score": 1
	},
	{
		"id": 4,
		"title": "Pregunta 5",
		"statment": "Who is the frontman of Muse?",
		"correct_answer": "Matt Bellamy",
		"incorrect_answers": ["Dominic Howard", "Thom Yorke", "Jonny Greenwood"],
		"imageUrl": "",
		"penalty": 0,
		"isPublic": false,
		"score": 1
	},
	{
		"id": 5,
		"title": "Pregunta 6",
		"statment": "When did The Beatles release the LP &quot;Please Please Me&quot;?",
		"correct_answer": "1963",
		"incorrect_answers": ["1970", "1960", "1969"],
		"imageUrl": "",
		"penalty": 0,
		"isPublic": false,
		"score": 1
	},
	{
		"id": 6,
		"title": "Pregunta 7",
		"statment": "Saul Hudson (Slash) of the band Guns N&#039; Roses is known for playing what type of guitar?",
		"correct_answer": "Les Paul Standard",
		"incorrect_answers": [
			"Fender Stratocaster",
			"LsL Mongrel",
			"Gretsch Falcon"
		],
		"imageUrl": "",
		"penalty": 0,
		"isPublic": false,
		"score": 1
	},
	{
		"id": 7,
		"title": "Pregunta 8",
		"statment": "In the Panic! At the Disco&#039;s song &quot;Nothern Downpour&quot;, which lyric follows &#039;I know the world&#039;s a broken bone&#039;.",
		"correct_answer": "&quot;So melt your headaches call it home&quot;",
		"incorrect_answers": [
			"&quot;So sing your song until you&#039;re home&quot;",
			"&quot;So let them know they&#039;re on their own&quot;",
			"&quot;So start a fire in their cold stone&quot;"
		],
		"imageUrl": "",
		"penalty": 0,
		"isPublic": false,
		"score": 1
	},
	{
		"id": 8,
		"title": "Pregunta 9",
		"statment": "When was the 3rd album &quot;Notes from the Underground&quot; of the band &quot;Hollywood Undead&quot; released?",
		"correct_answer": "2013",
		"incorrect_answers": ["2011", "2014", "2009"],
		"imageUrl": "",
		"penalty": 0,
		"isPublic": false,
		"score": 1
	},
	{
		"id": 9,
		"title": "Pregunta 10",
		"statment": "What date is referenced in the 1971 song &quot;September&quot; by Earth, Wind &amp; Fire?",
		"correct_answer": "21st of September",
		"incorrect_answers": [
			"26th of September",
			"23rd of September",
			"24th of September"
		],
		"imageUrl": "",
		"penalty": 0,
		"isPublic": false,
		"score": 1
	}
]

    """
    )

    for q in q_json:
        questions.append(
            Question(
                q["id"],
                q["title"],
                q["statment"],
                q["correct_answer"],
                q["incorrect_answers"],
                q["imageUrl"],
                float(q["score"]),
                float(q["penalty"]),
                bool(q["isPublic"]),
            )
        )

    return questions
