from random import randint
import traceback
import json

from typing import List

from sqlalchemy.orm import session  # type: ignore

from dms2122backend.data.db.schema import Schema  # type: ignore
from dms2122backend.data.db.results.question import Question  # type: ignore


questions_json = '[\n\t{\n\t\t"id": 0,\n\t\t"title": "Pregunta 1",\n\t\t"statment": "Saul Hudson (Slash) of the band Guns N\' Roses is known for playing what type of guitar?",\n\t\t"correct_answer": "Les Paul Standard",\n\t\t"incorrect_answers": [\n\t\t\t"Fender Stratocaster",\n\t\t\t"LsL Mongrel",\n\t\t\t"Gretsch Falcon"\n\t\t],\n\t\t"user_answers": [],\n\t\t"image_url": "",\n\t\t"penalty": 0,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 1,\n\t\t"title": "Pregunta 2",\n\t\t"statment": "Irish musician Hozier released a music track in 2013 titled, \\"Take Me to ______\\"",\n\t\t"correct_answer": "Church",\n\t\t"incorrect_answers": ["Mosque", "Synagogue", "Temple"],\n\t\t"user_answers": [],\n\t\t"image_url": "",\n\t\t"penalty": 0,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 2,\n\t\t"title": "Pregunta 3",\n\t\t"statment": "Which song by Swedish electronic musician Avicii samples the song \\"Something Got A Hold On Me\\" by Etta James?",\n\t\t"correct_answer": "Levels",\n\t\t"incorrect_answers": ["Fade Into Darkness", "Silhouettes", "Seek Bromance"],\n\t\t"user_answers": [],\n\t\t"image_url": "",\n\t\t"penalty": 0,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 3,\n\t\t"title": "Pregunta 4",\n\t\t"statment": "What was the title of Sakamoto Kyu\'s song \\"Ue o Muite Arukou\\" (I Look Up As I Walk) changed to in the United States?",\n\t\t"correct_answer": "Sukiyaki",\n\t\t"incorrect_answers": ["Takoyaki", "Sushi", "Oden"],\n\t\t"user_answers": [],\n\t\t"image_url": "",\n\t\t"penalty": 0,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 4,\n\t\t"title": "Pregunta 5",\n\t\t"statment": "Who is the frontman of Muse?",\n\t\t"correct_answer": "Matt Bellamy",\n\t\t"incorrect_answers": ["Dominic Howard", "Thom Yorke", "Jonny Greenwood"],\n\t\t"user_answers": [],\n\t\t"image_url": "",\n\t\t"penalty": 0,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 5,\n\t\t"title": "Pregunta 6",\n\t\t"statment": "When did The Beatles release the LP \\"Please Please Me\\"?",\n\t\t"correct_answer": "1963",\n\t\t"incorrect_answers": ["1970", "1960", "1969"],\n\t\t"user_answers": [],\n\t\t"image_url": "",\n\t\t"penalty": 0,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 6,\n\t\t"title": "Pregunta 7",\n\t\t"statment": "Saul Hudson (Slash) of the band Guns N\' Roses is known for playing what type of guitar?",\n\t\t"correct_answer": "Les Paul Standard",\n\t\t"incorrect_answers": [\n\t\t\t"Fender Stratocaster",\n\t\t\t"LsL Mongrel",\n\t\t\t"Gretsch Falcon"\n\t\t],\n\t\t"user_answers": [],\n\t\t"image_url": "",\n\t\t"penalty": 0,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 7,\n\t\t"title": "Pregunta 8",\n\t\t"statment": "In the Panic! At the Disco\'s song \\"Nothern Downpour\\", which lyric follows\\"I know the world\'s a broken bone\\".",\n\t\t"correct_answer": "So melt your headaches call it home",\n\t\t"incorrect_answers": [\n\t\t\t"So sing your song until you\'re home",\n\t\t\t"So let them know they\'re on their own",\n\t\t\t"So start a fire in their cold stone"\n\t\t],\n\t\t"user_answers": [],\n\t\t"image_url": "",\n\t\t"penalty": 0,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 8,\n\t\t"title": "Pregunta 9",\n\t\t"statment": "When was the 3rd album \\"Notes from the Underground\\" of the band \\"Hollywood Undead\\" released?",\n\t\t"correct_answer": "2013",\n\t\t"incorrect_answers": ["2011", "2014", "2009"],\n\t\t"user_answers": [],\n\t\t"image_url": "",\n\t\t"penalty": 75,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 9,\n\t\t"title": "Pregunta 10",\n\t\t"statment": "What date is referenced in the 1971 song \\"September\\" by Earth, Wind & Fire?",\n\t\t"correct_answer": "21st of September",\n\t\t"incorrect_answers": [\n\t\t\t"26th of September",\n\t\t\t"23rd of September",\n\t\t\t"24th of September"\n\t\t],\n\t\t"user_answers": [],\n\t\t"image_url": "",\n\t\t"penalty": 0,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 10,\n\t\t"title": "F1 Quiz",\n\t\t"statment": "\u00bfCu\u00e1nto Mide Yuki Tsunoda?",\n\t\t"correct_answer": "159cm",\n\t\t"incorrect_answers": ["180cm", "190cm", "200cm", "170cm"],\n\t\t"user_answers": [],\n\t\t"image_url": "https:\/\/i.redd.it\/6dfphxxis1q71.gif",\n\t\t"penalty": 25,\n\t\t"is_public": false,\n\t\t"score": 1\n\t},\n\t{\n\t\t"id": 11,\n\t\t"title": "F1 Quiz",\n\t\t"statment": "Seleccione el apodo correcto sobre el siguiente piloto",\n\t\t"correct_answer": "Padre",\n\t\t"incorrect_answers": ["Fernando Malonso", "Poleman", "Polero"],\n\t\t"user_answers": [],\n\t\t"image_url": "https:\/\/www.larazon.es\/resizer\/KdLnugN5E_TDZi7vtKR6AckOilI=\/600x400\/smart\/filters:format(webp):quality(65)\/cloudfront-eu-central-1.images.arcpublishing.com\/larazon\/M5HARXCHXVBY5IFZZQQXSDVE5Q.jpg",\n\t\t"penalty": 50,\n\t\t"is_public": false,\n\t\t"score": 1\n\t}\n]\n'


def populate(db: Schema):

    session = db.new_session()
    count = session.query(Question).count()
    session.rollback()

    if count > 5:
        print(
            f"Skipping DB Initial populate as {count} items already exist", flush=True
        )
        return

    parsed = json.loads(questions_json)

    questions: List[Question] = []

    for q in parsed:
        questions.append(
            Question(
                q["title"],
                q["statment"],
                q["correct_answer"],
                q["incorrect_answers"],
                q["image_url"],
                float(q["score"]),
                float(q["penalty"]),
                mock_stats=not randint(0, 1),
            )
        )

    session = db.new_session()

    try:
        session.bulk_save_objects(questions)
        session.commit()
        print(f"Added {len(questions)} questions:", flush=True)
        for q in questions:
            print(q, flush=True)

    except Exception:
        session.rollback()
        print(traceback.format_exc(), flush=True)

