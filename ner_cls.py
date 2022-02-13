import spacy
import argparse

def entity_recognizer(text, lang):
    nlp = spacy.load(f"{lang}_core_web_sm")
    doc = nlp(text)
    entity_list = []

    for ent in doc.ents:
        entity_list.append({"text": ent.text, "start-char": ent.start_char,"end-char": ent.end_char,"type": ent.label_})
    
    print(entity_list)
    return(entity_list)






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-t','--text', help='Description for foo argument', required=True)
    parser.add_argument('-l','--lang', help='Description for bar argument', required=True)
    args = vars(parser.parse_args())


    entity_recognizer(args["text"], args["lang"])