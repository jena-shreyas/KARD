import os
import os.path as osp
import json
from pprint import pprint

data_dir = "preprocessed_data/strategyqa-cot-wikipedia"

with open(osp.join(data_dir, "train.json"), 'r') as f:
    data = json.load(f)

template_ka = ""

qn_idxs = [0, 10, 20, 30, 40]
data_sample = [data[i] for i in qn_idxs]

for d in data_sample:
    qn = d["question"]
    reason = d["reasoning"]
    knowledge = d["knowledge"]

    question, options = qn.split("?")
    question = question + "?"
    knowledge = knowledge + "\n" + options

    prompt = "Question: " + question + "\nKnowledge: " + knowledge + "\nAnswer: " + reason
    template_ka += prompt + "\n"

with open('prompts/strategyqa/template_cot_knowledge_5shot.txt', 'w') as f:
    f.write(template_ka)
