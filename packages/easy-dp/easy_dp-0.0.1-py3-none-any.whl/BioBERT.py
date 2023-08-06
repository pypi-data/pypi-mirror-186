import requests
from typing import List
import json
from pathlib import Path
import time

N_calls = 0

class Entity:
    '''
    A simple dataclass to store the information of a BioBERT entity.
    '''
    mesh_ids: List[str] # List of Unique identifier for the entity, e.g. MESH:D001234. (You can use the MESH ID to look up the name of the entity in the MESH database.)
    mention: str # The string that is associated with the entity in the text (e.g. "BRCA1").
    type: str # The type of the entity. Can be 'gene' or 'disease'.
    prob: float # The probability of the entity, it indicates the confidence of the model prediction.
    span_begin: int # The begin of the span of the entity.
    span_end: int # The end of the span of the entity.
    is_neural_normalized: bool # Whether the entity is normalized by neural network.
    mutationType: str # The type of mutation, if the entity is a gene.
    normalizedName: str # The normalized name of the entity, if the entity is a gene.

    def __init__(self, id: List[str], mention: str, obj: str, prob: float, span: dict, is_neural_normalized: bool, mutationType: str = '', normalizedName: str = ''):
        self.mesh_ids = id
        self.mention = mention
        self.type = obj
        self.prob = prob
        # text[span['begin']:span['end']] == mention
        self.span_begin = span['begin']
        self.span_end = span['end']
        self.is_neural_normalized = is_neural_normalized
        self.mutationType = mutationType
        self.normalizedName = normalizedName

    def __dict__(self):
        return {
            "id": self.mesh_ids,
            "mention": self.mention,
            "obj": self.type,
            "prob": self.prob,
            "span": {
                "begin": self.span_begin,
                "end": self.span_end
            },
            "is_neural_normalized": self.is_neural_normalized,
            "mutationType": self.mutationType,
            "normalizedName": self.normalizedName
        }

    def __eq__(self, other):
        if isinstance(other, Entity):
            # We say that two entities are equal if at least one of their mesh_ids is equal.
            return any([mesh_id in other.mesh_ids for mesh_id in self.mesh_ids])
        return False

    def __repr__(self):
        return f"Entity(mention={self.mention}, type={self.type}, prob={self.prob}, span_begin={self.span_begin}, span_end={self.span_end}, is_neural_normalized={self.is_neural_normalized}, mesh_ids={self.mesh_ids})"

def query_biobert(text: str, url="http://bern2.korea.ac.kr/plain") -> List[Entity]:
    """
    Query the BERN2 server for plain text.
    Args:
        text (str): the text to be annotated
        url (str): the url of the BERN2 server.
    """
    global N_calls
    N_calls += 1
    if N_calls % 100 == 0:
        print("Waiting 30 seconds to avoid being blocked by the server")
        # We are limited to 100 calls every 100 seconds, just to be safe we wait 30 seconds (avg 1 call every 1 sec anyway)
        time.sleep(30)
        N_calls = 0

    # Limit the text at 5000 characters
    if len(text) > 5000:
        print("Warning: text is too long, truncating to 5000 characters.")
        text = text[:5000]

    result = requests.post(url, json={'text': text})

    if result.status_code != 200:
        print("Error: {}".format(result.status_code))
        raise Exception("Error: {}".format(result.status_code))

    try:
        annotations = result.json()['annotations']
    except json.decoder.JSONDecodeError:
        print("Error while decoding the json")
        return []

    # annotiations[0] == {'id': ['mesh:D003404'], 'is_neural_normalized': False, 'mention': 'creatinine', 'obj': 'drug', 'prob': 0.9962512850761414, 'span': {'begin': 2282, 'end': 2292}}

    entities = [Entity(**annotation) for annotation in annotations]

    return entities

def load_or_extract_entities(texts: List[str], file_name: str = "training_entities.json") -> List[List[Entity]]:
    '''
    Extract the entities from the texts using BioBERT. If the entities have already been extracted, load them from file_name.
    '''
    def save(file_name, text_entities):
        print("Saving entities to file")
        # Create the directory to file_name if it does not exist
        Path(file_name).parent.mkdir(parents=True, exist_ok=True)

        with open(file_name, "w") as f:
            # Save the entities to json by converting them to dicts
            json.dump(list(map(lambda x: list(map(lambda y: y.__dict__(), x)), text_entities)), f)

    # For each sample we have a list of entities
    text_entities: List[List[Entity]] = []
    # Check if we had already extracted the entities, if so, load them; otherwise, extract them
    try:
        with open(file_name, "r") as f:
            text_entities = json.load(f)
            text_entities = [list(map(lambda x: Entity(**x), entities)) for entities in text_entities]
    except FileNotFoundError:
        # If not, extract them
        for i, text in enumerate(texts):
            print(f"Extracting entities for sample {i}/{len(texts)}")
            text_entities.append(query_biobert(text))
            if i % 100 == 0:
                save(file_name, text_entities)

        save(file_name, text_entities)
    finally:
        num_entities_cached = len(text_entities)
        # If we had already extracted the entities, check if we have enough
        if num_entities_cached < len(texts):
            for i, text in enumerate(texts[num_entities_cached:]):
                print(f"Extracting entities for sample {i + num_entities_cached}/{len(texts)}")
                text_entities.append(query_biobert(text))
                if i % 100 == 0:
                    save(file_name, text_entities)

            save(file_name, text_entities)

    return text_entities

def compute_similarity_score(entities1: List[Entity], entities2: List[Entity]) -> float:
    '''
    Returns a score between 0 and 1 that indicates how similar the two lists of entities are. This is given by the Jaccard index.
    '''
    # First we flatten the list of entities to a list of all the mesh_ids present in the text
    entities1_meshes_flat = set([mesh_id for entity in entities1 for mesh_id in entity.mesh_ids])
    entities2_meshes_flat = set([mesh_id for entity in entities2 for mesh_id in entity.mesh_ids])
    # Then we compute the Jaccard index, defined as the length of the intersection divided by the length of the union of the two sets
    return len(entities1_meshes_flat.intersection(entities2_meshes_flat)) / len(entities1_meshes_flat.union(entities2_meshes_flat))
