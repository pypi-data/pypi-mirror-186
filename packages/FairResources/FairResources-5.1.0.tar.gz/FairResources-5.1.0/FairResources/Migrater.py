import FairResources
from FBrain.JModel import WordModel
from FNLP.Engines.Words import Analyzers
from F import DATE
from F.LOG import Log
from FM.DBDatabase import DBDatabase

# Connect to MongoDB
db = DBDatabase().connect("192.168.1.180", 27017).database("brain")
TODAY = DATE.TO_DATETIME(DATE.mongo_date_today_str())

collection = lambda name: db.collection(name)
resource = lambda name: FairResources.load_json(name)

# Models
DICTIONARY = lambda word, definition: { "word": word, "definition": definition, "updatedDate": TODAY }
ENGLISH_WORD = lambda word, first_letter, letter_count, isFirstCapital: \
    {
    "word": word,
    "first_letter": first_letter,
    "letter_count": letter_count,
    "isFirstCapital": isFirstCapital,
    "updatedDate": TODAY
    }

def migrate_dictionary_to_database():
    # Load Resource and Collection
    dic = resource("english_dictionary")
    # Add Records
    records = []
    for word in Log.ProgressBarYielder(dic, prefix="Preparing Records for Database..."):
        records.append(DICTIONARY(word, dic[word]))
    collection("dictionary").add_records_field_match(records, fieldName="word")

def migrate_word_list_to_database(name="english_words", collection_name=None):
    # Load Resource
    dic = FairResources.get_source(name)
    if not dic:
        return f"No Resource Found. {name}"
    # Add Records
    records = []
    for word in Log.ProgressBarYielder(dic, prefix="Preparing Records for Database..."):
        breakdown = Analyzers.analyze_word(word)
        record = ENGLISH_WORD(word, breakdown["firstLetter"], breakdown["letterCount"], breakdown["firstLetterCapital"])
        records.append(record)
    collection(collection_name if collection_name is not None else name).add_records_field_match(records, fieldName="word", ignoreExists=True)

def migrate_stop_list_to_database():
    # Load Resource
    dic = FairResources.get_stopwords()
    if not dic:
        return f"No Resource Found."
    # Add Records
    records = []
    for word in Log.ProgressBarYielder(dic, prefix="Preparing Records for Database..."):
        model = WordModel(word)
        j = model.toJson()
        records.append(j)
    print(records)
    # collection("stop_words").add_records_field_match(records, fieldName="word", ignoreExists=True)


if __name__ == '__main__':
    migrate_stop_list_to_database()
    # migrate_word_list_to_database("english_nouns")