#Ref: https://huggingface.co/lcw99/t5-large-korean-text-summary


print("Loading modules ....")
from time import time
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
nltk.download('punkt')

print("Loading models ....")
_model_dir = "lcw99/t5-large-korean-text-summary"
_tokenizer = AutoTokenizer.from_pretrained(_model_dir)
_model = AutoModelForSeq2SeqLM.from_pretrained(_model_dir)

print("Initializing ...")
_max_input_length = 512 + 256

def summary(text):
	inputs = ["summarize: " + text]
	inputs = _tokenizer(inputs, max_length=_max_input_length, truncation=True, return_tensors="pt")
	output = _model.generate(**inputs, num_beams=8, do_sample=True, min_length=30, max_length=1300)
	decoded_output = _tokenizer.batch_decode(output, skip_special_tokens=True)[0]
	predicted_title = nltk.sent_tokenize(decoded_output.strip())[0]
	return predicted_title



if __name__ == '__main__':
	print("Start API Server ...")
	from flask import Flask, request

	app = Flask(__name__)

	@app.route("/api/summary")
	def summary():
		start_time = time()
		text = request.args['text']
		print("---> input text")
		print(text);
		predicted_title = summary(text)
		print("---> summarized text")
		print(predicted_title)

		elapsed_time = time() - start_time
		return f"""<h1>요약</h1>
		<p>걸린시간: {round(elapsed_time, 2)}s</p>
		<p><b>{predicted_title}</b></p>
		<h2>원본 텍스트</h2>
		<p>{text}</p>"""
	app.run()