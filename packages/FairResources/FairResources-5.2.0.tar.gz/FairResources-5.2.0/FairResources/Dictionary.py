from FairResources import FairResources
from F import DATE
from F.LOG import Log


def simple_word_lookup(word):
    dic = FairResources.load_json("english_dictionary")
    word_upper = str(word).upper()
    if word_upper in dic:
        return dic[word_upper]
    return "Word Not Found."


# def migrate_to_database():
#     from FM.DBDatabase import DBDatabase
#     # Load Resource
#     dic = FairResources.load_json("english_dictionary")
#     # Connect to MongoDB
#     db = DBDatabase().connect("192.168.1.180", 27017).database("brain")
#     collection = db.collection("dictionary")
#     # Add Records
#     records = []
#     for word in Log.ProgressBarYielder(dic, prefix="Preparing Records for Database..."):
#         record = { "word": word, "definition": dic[word], "updatedDate": DATE.TO_DATETIME(DATE.mongo_date_today_str()) }
#         records.append(record)
#     collection.add_records_field_match(records, fieldName="word")

if __name__ == '__main__':
    print(simple_word_lookup("rs"))