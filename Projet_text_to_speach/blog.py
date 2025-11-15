from db import get_connection
from datetime import datetime
from translate import Translator
from gtts import gTTS
import os
import platform


class Blog:
    def __init__(self, title, content):
        self._title = title
        self._content = content
        self._id = None
        self._created_at = None
        self._updated_at = None

    def save(self):  
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO blogs (title, content, created_at, updated_at) VALUES (%s, %s, %s, %s) RETURNING id, created_at, updated_at",
            (self._title, self._content, self._created_at, self._updated_at)
        )
        row = cursor.fetchone()
        self._id = row["id"]
        self._created_at = row["created_at"]
        self._updated_at = row["updated_at"]
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, conn):
        self._updated_at = datetime.now()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE blogs SET title = %s, content = %s, updated_at = %s WHERE id = %s",
            (self._title, self._content, self._updated_at, self._id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, conn):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM blogs WHERE id = %s",
            (self._id,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def translate_and_speak(self):
        # Liste des langues disponibles
        language_names = {
            1: ("en", "English"),
            2: ("fr", "French"),
            3: ("es", "Spanish"),
            4: ("de", "German"),
            5: ("it", "Italian"),
            6: ("pt", "Portuguese"),
            7: ("ru", "Russian"),
        }

        # --------- FROM LANGUAGE ----------
        print("Choisissez la langue d'origine :")
        for num, (_, name) in language_names.items():
            print(f"{num}. {name}")

        from_choice = int(input("Entrez un numéro : "))
        from_lang_code, from_lang_name = language_names.get(from_choice, ("en", "English"))

        # --------- TO LANGUAGE ----------
        print("\nChoisissez la langue de traduction :")
        for num, (_, name) in language_names.items():
            print(f"{num}. {name}")

        to_choice = int(input("Entrez un numéro : "))
        to_lang_code, to_lang_name = language_names.get(to_choice, ("en", "English"))

        # Traduction
        translator = Translator(from_lang=from_lang_code, to_lang=to_lang_code)
        translated_content = translator.translate(self._content)

        # Génération audio
        tts = gTTS(text=translated_content, lang=to_lang_code)

        audio_file = f"blog_{self._id}_{to_lang_name}.mp3"
        tts.save(audio_file)

        print(f"\nTraduction ({from_lang_name} -> {to_lang_name}) :")
        print(translated_content)
        print(f"\nAudio généré : {audio_file}")

        # Lecture audio
        system = platform.system()

        if system == "Windows":
            os.startfile(audio_file)
        elif system == "Darwin":
            os.system(f"open \"{audio_file}\"")
        else:
            os.system(f"xdg-open \"{audio_file}\"")

    @classmethod
    def get_all(cls, conn):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, content, created_at, updated_at FROM blogs")
        rows = cursor.fetchall()
        blogs = []
        for row in rows:
            blog = cls(row[1], row[2])
            blog._id = row[0]
            blog._created_at = row[3]
            blog._updated_at = row[4]
            blogs.append(blog)
        cursor.close()
        conn.close()
        return blogs

    @classmethod
    def get_by_id(cls, conn, blog_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, content, created_at, updated_at FROM blogs WHERE id = %s",
            (blog_id,)
        )
        row = cursor.fetchone()
        if row:
            blog = cls(row[1], row[2])
            blog._id = row[0]
            blog._created_at = row[3]
            blog._updated_at = row[4]
            cursor.close()
            conn.close()
            return blog
        cursor.close()
        conn.close()
        return None

    def to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "content": self._content,
            "created_at": self._created_at,
            "updated_at": self._updated_at
        }

if __name__ == "__main__":
    from db import get_connection

    # Demander à l’utilisateur de saisir titre et contenu
    title = input("Entrez le titre du blog : ")
    content = input("Entrez le contenu du blog : ")

    # Créer le blog
    blog = Blog(title, content)

    # Sauvegarder dans la base
    blog.save()
    print("Blog sauvegardé avec ID :", blog._id)

    # Traduire et générer audio
    blog.translate_and_speak()
