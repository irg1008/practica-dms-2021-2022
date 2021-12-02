import json
from typing import Dict, Optional, Tuple
from http import HTTPStatus
from flask.globals import current_app

from dms2122backend.service.auth.protected_endpoint_dec import protected_endpoint
from dms2122common.data.role import Role


@protected_endpoint(roles=[Role.Teacher])
def new(body: Dict, **kwargs) -> Tuple[int, Optional[int]]:
    """New question endpoint

    Roles: Teacher

    Returns:
        Tuple[str, Optional[int]]: Response message and status code
    """

    return (1, HTTPStatus.OK)


@protected_endpoint(roles=[Role.Teacher, Role.Student])
def getQ(id: int, **kwargs):
    return ({"id": id}, 200)


@protected_endpoint(roles=[Role.Teacher])
def editQ(id: int, **kwargs):
    return (id, 200)


@protected_endpoint(roles=[Role.Teacher])
def getAll(**kwargs):

    questions = json.loads(
        """
    [
	{
		"id": 0,
		"title": "Pregunta 1",
		"statment": "Saul Hudson (Slash) of the band Guns N' Roses is known for playing what type of guitar?",
		"correct_answer": "Les Paul Standard",
		"incorrect_answers": [
			"Fender Stratocaster",
			"LsL Mongrel",
			"Gretsch Falcon"
		],
		"user_answers": [],
		"image_url": "",
		"penalty": 0,
		"is_public": false,
		"score": 1
	},
	{
		"id": 1,
		"title": "Pregunta 2",
		"statment": "Irish musician Hozier released a music track in 2013 titled, \"Take Me to ______\"",
		"correct_answer": "Church",
		"incorrect_answers": ["Mosque", "Synagogue", "Temple"],
		"user_answers": [],
		"image_url": "",
		"penalty": 0,
		"is_public": false,
		"score": 1
	},
	{
		"id": 2,
		"title": "Pregunta 3",
		"statment": "Which song by Swedish electronic musician Avicii samples the song \"Something Got A Hold On Me\" by Etta James?",
		"correct_answer": "Levels",
		"incorrect_answers": ["Fade Into Darkness", "Silhouettes", "Seek Bromance"],
		"user_answers": [],
		"image_url": "",
		"penalty": 0,
		"is_public": false,
		"score": 1
	},
	{
		"id": 3,
		"title": "Pregunta 4",
		"statment": "What was the title of Sakamoto Kyu's song \"Ue o Muite Arukou\" (I Look Up As I Walk) changed to in the United States?",
		"correct_answer": "Sukiyaki",
		"incorrect_answers": ["Takoyaki", "Sushi", "Oden"],
		"user_answers": [],
		"image_url": "",
		"penalty": 0,
		"is_public": false,
		"score": 1
	},
	{
		"id": 4,
		"title": "Pregunta 5",
		"statment": "Who is the frontman of Muse?",
		"correct_answer": "Matt Bellamy",
		"incorrect_answers": ["Dominic Howard", "Thom Yorke", "Jonny Greenwood"],
		"user_answers": [],
		"image_url": "",
		"penalty": 0,
		"is_public": false,
		"score": 1
	},
	{
		"id": 5,
		"title": "Pregunta 6",
		"statment": "When did The Beatles release the LP \"Please Please Me\"?",
		"correct_answer": "1963",
		"incorrect_answers": ["1970", "1960", "1969"],
		"user_answers": [],
		"image_url": "",
		"penalty": 0,
		"is_public": false,
		"score": 1
	},
	{
		"id": 6,
		"title": "Pregunta 7",
		"statment": "Saul Hudson (Slash) of the band Guns N' Roses is known for playing what type of guitar?",
		"correct_answer": "Les Paul Standard",
		"incorrect_answers": [
			"Fender Stratocaster",
			"LsL Mongrel",
			"Gretsch Falcon"
		],
		"user_answers": [],
		"image_url": "",
		"penalty": 0,
		"is_public": false,
		"score": 1
	},
	{
		"id": 7,
		"title": "Pregunta 8",
		"statment": "In the Panic! At the Disco's song \"Nothern Downpour\", which lyric follows\"I know the world's a broken bone\".",
		"correct_answer": "So melt your headaches call it home",
		"incorrect_answers": [
			"So sing your song until you're home",
			"So let them know they're on their own",
			"So start a fire in their cold stone"
		],
		"user_answers": [],
		"image_url": "",
		"penalty": 0,
		"is_public": false,
		"score": 1
	},
	{
		"id": 8,
		"title": "Pregunta 9",
		"statment": "When was the 3rd album \"Notes from the Underground\" of the band \"Hollywood Undead\" released?",
		"correct_answer": "2013",
		"incorrect_answers": ["2011", "2014", "2009"],
		"user_answers": [],
		"image_url": "",
		"penalty": 75,
		"is_public": false,
		"score": 1
	},
	{
		"id": 9,
		"title": "Pregunta 10",
		"statment": "What date is referenced in the 1971 song \"September\" by Earth, Wind & Fire?",
		"correct_answer": "21st of September",
		"incorrect_answers": [
			"26th of September",
			"23rd of September",
			"24th of September"
		],
		"user_answers": [],
		"image_url": "",
		"penalty": 0,
		"is_public": false,
		"score": 1
	},
	{
		"id": 10,
		"title": "F1 Quiz",
		"statment": "¿Cuánto Mide Yuki Tsunoda?",
		"correct_answer": "159cm",
		"incorrect_answers": ["180cm", "190cm", "200cm", "170cm"],
		"user_answers": [],
		"image_url": "https://i.redd.it/6dfphxxis1q71.gif",
		"penalty": 25,
		"is_public": false,
		"score": 1
	},
	{
		"id": 11,
		"title": "F1 Quiz",
		"statment": "Seleccione el apodo correcto sobre el siguiente piloto",
		"correct_answer": "Padre",
		"incorrect_answers": ["Fernando Malonso", "Poleman", "Polero"],
		"user_answers": [],
		"image_url": "https://www.larazon.es/resizer/KdLnugN5E_TDZi7vtKR6AckOilI=/600x400/smart/filters:format(webp):quality(65)/cloudfront-eu-central-1.images.arcpublishing.com/larazon/M5HARXCHXVBY5IFZZQQXSDVE5Q.jpg",
		"penalty": 50,
		"is_public": false,
		"score": 1
	}
]

    """
    )

    return (questions, 200)
