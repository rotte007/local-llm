from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset
from transformers import Trainer, TrainingArguments

# Load base model & tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-1b-it")
base = AutoModelForCausalLM.from_pretrained(
    "google/gemma-3-1b-it",
    load_in_4bit=True,
    device_map="auto",
    # low_cpu_mem_usage=True
)
base = prepare_model_for_kbit_training(base)
base.resize_token_embeddings(len(tokenizer))

# Configure LoRA
lora_cfg = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj","v_proj"],
    lora_dropout=0.05,
    bias="none"
)
model = get_peft_model(base, lora_cfg)

# Print trainable parameters
print(model.print_trainable_parameters())
print(model)

# # Dataset
# ds = load_dataset("json", data_files="data/faqs.json", split="train")
# def tokenize(ex): return tokenizer(ex["prompt"], truncation=True, max_length=512)
# ds = ds.map(tokenize, batched=True)

# # Train
# args = TrainingArguments(
#     output_dir="lora-output",
#     per_device_train_batch_size=4,
#     num_train_epochs=3,
#     logging_steps=10,
#     save_total_limit=2
# )
# trainer = Trainer(model=model, train_dataset=ds, args=args)
# trainer.train()
# model.save_pretrained("lora-output")
