from transformers import BertConfig, BertForSequenceClassification, BertTokenizer


def get_encoder_model(pretrained_model, num_labels):
    print("load pretrained model/tokenizer for '{}'".format(pretrained_model))
    config_class, model_class, tokenizer_class = (BertConfig, BertForSequenceClassification, BertTokenizer)
    config = config_class.from_pretrained(pretrained_model, num_labels=num_labels,)
    tokenizer = tokenizer_class.from_pretrained(pretrained_model)
    model = model_class.from_pretrained(pretrained_model, config=config)

    return model, tokenizer
