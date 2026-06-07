"""Generate DL notebooks cleanly — PyTorch/TF examples in markdown, runnable code only in code cells."""
import json, os
os.makedirs('notebooks', exist_ok=True)

def nb(*cells):
    return {"nbformat":4,"nbformat_minor":5,
            "metadata":{"kernelspec":{"display_name":"Python (Pyodide)","language":"python","name":"python"}},
            "cells":list(cells)}
def md(s): return {"cell_type":"markdown","metadata":{},"source":s}
def py(s): return {"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":s}
def save(name, notebook):
    with open(f"notebooks/{name}.ipynb","w") as f: json.dump(notebook,f,indent=1)
    print(f"  OK {name}.ipynb")

# ─────────────────────────────────────────────────────────────────────────────
# DL-01: Neural Networks — Diabetes/Breast Cancer Classification
# ─────────────────────────────────────────────────────────────────────────────
save("dl-01-neural-networks", nb(
    md("# Neural Network Basics\nLearn how a neural network learns by building one to predict disease risk."),
    py("import micropip\nawait micropip.install(['scikit-learn','matplotlib','numpy'])\nprint('Ready!')"),
    md("## Activation Functions\nEach neuron applies an activation function: `output = activation(W·x + b)`"),
    py("""import numpy as np, matplotlib.pyplot as plt
x = np.linspace(-5,5,200)
fig,axes = plt.subplots(1,3,figsize=(12,3))
for ax,fn,nm,c in zip(axes,
    [np.maximum(0,x), 1/(1+np.exp(-x)), np.tanh(x)],
    ['ReLU','Sigmoid','Tanh'], ['#6b21a8','#059669','#f59e0b']):
    ax.plot(x,fn,color=c,lw=2); ax.set_title(nm); ax.axhline(0,c='gray',lw=0.5)
plt.tight_layout(); plt.show()"""),
    md("## Load Data"),
    py("""from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
data = load_breast_cancer()
X = StandardScaler().fit_transform(data.data)
X_train,X_test,y_train,y_test = train_test_split(X,data.target,test_size=0.2,random_state=42)
print(f"Train: {X_train.shape}  |  Test: {X_test.shape}  |  Features: {X_train.shape[1]}")"""),
    md("## Train MLP (Multi-Layer Perceptron)\nArchitecture: 30 inputs → 64 neurons → 32 neurons → 1 output"),
    py("""from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score
mlp = MLPClassifier(hidden_layer_sizes=(64,32), activation='relu',
                    solver='adam', max_iter=500, random_state=42)
mlp.fit(X_train,y_train)
y_pred = mlp.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test,y_pred):.3f}")
print(classification_report(y_test,y_pred,target_names=data.target_names))"""),
    md("## Training Loss Curve"),
    py("""plt.figure(figsize=(8,4))
plt.plot(mlp.loss_curve_,color='#6b21a8')
plt.xlabel('Epoch'); plt.ylabel('Loss')
plt.title('Neural Network Training Loss')
plt.grid(alpha=0.3); plt.show()"""),
    md("## Effect of Architecture"),
    py("""for arch in [(16,),(64,32),(128,64,32)]:
    m = MLPClassifier(hidden_layer_sizes=arch,max_iter=300,random_state=42)
    m.fit(X_train,y_train)
    print(f"Arch {str(arch):<15} | train={m.score(X_train,y_train):.3f} | test={m.score(X_test,y_test):.3f}")"""),
    md("## L2 Regularisation (alpha)\nalpha controls weight decay — higher alpha = simpler model, lower variance"),
    py("""for alpha in [0.0001,0.001,0.01,0.1,1.0]:
    m = MLPClassifier(hidden_layer_sizes=(64,32),alpha=alpha,max_iter=300,random_state=42)
    m.fit(X_train,y_train)
    tr,te = m.score(X_train,y_train), m.score(X_test,y_test)
    print(f"alpha={alpha:<8} | train={tr:.3f} | test={te:.3f} | overfit={tr-te:.3f}")"""),
    md("---\n**Your turn:** Try `activation='tanh'`. Which gives better test accuracy?\n\n**Full deep learning:** Use PyTorch on Kaggle GPU for GPU-accelerated training."),
))

# ─────────────────────────────────────────────────────────────────────────────
# DL-02: CNNs — CIFAR-10 / MNIST Image Classification
# ─────────────────────────────────────────────────────────────────────────────
save("dl-02-cnns-cifar10", nb(
    md("# Convolutional Neural Networks — Image Classification\n\nLearn CNN concepts using MNIST digits. For full CIFAR-10/ImageNet, use Kaggle GPU."),
    py("import micropip\nawait micropip.install(['scikit-learn','matplotlib','numpy'])\nprint('Ready!')"),
    md("## Famous CNN Models\n\n| Model | Year | Params | Top-5 Error |\n|---|---|---|---|\n| LeNet | 1998 | 60K | N/A |\n| AlexNet | 2012 | 60M | 15.3% |\n| VGG-16 | 2014 | 138M | 7.4% |\n| ResNet-50 | 2015 | 25M | 5.25% |\n| EfficientNet-B0 | 2019 | 5M | 2.9% |\n\n**Key insight:** ResNet is smaller than VGG but more accurate — residual connections allow deeper training."),
    md("## CNN Architecture Intuition\n\n```\nInput image (32x32x3)\n    ↓\nConv Layer → Edge detectors\n    ↓\nConv Layer → Texture detectors  \n    ↓\nConv Layer → Object part detectors\n    ↓\nFlatten + FC → Classification\n```\n\nFilters are LEARNED — not hand-crafted."),
    py("""import numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits = load_digits()
X, y = digits.data/16.0, digits.target
fig,axes = plt.subplots(2,8,figsize=(14,3.5))
for i,ax in enumerate(axes.flat):
    ax.imshow(digits.images[i],cmap='gray'); ax.set_title(f'Label:{y[i]}',fontsize=7); ax.axis('off')
plt.suptitle('MNIST 8x8 Digits (same CNN concepts apply to 32x32 CIFAR-10)')
plt.tight_layout(); plt.show()
print(f"Shape: {digits.images.shape} | Classes: {len(set(y))}")"""),
    py("""from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, confusion_matrix
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
mlp = MLPClassifier(hidden_layer_sizes=(256,128),activation='relu',max_iter=500,random_state=42)
mlp.fit(X_train,y_train)
acc = accuracy_score(y_test,mlp.predict(X_test))
print(f"Accuracy: {acc:.3f}")"""),
    py("""cm = confusion_matrix(y_test,mlp.predict(X_test))
fig,ax = plt.subplots(figsize=(8,7))
ConfusionMatrixDisplay(cm,display_labels=list(range(10))).plot(ax=ax,colorbar=False)
plt.title('Digit Classification Confusion Matrix'); plt.show()"""),
    md("## Datasets at a Glance\n\n| Dataset | Images | Classes | Use |\n|---|---|---|---|\n| MNIST | 70K | 10 | Digit recognition |\n| CIFAR-10 | 60K | 10 | Basic objects |\n| CIFAR-100 | 60K | 100 | Fine-grained |\n| ImageNet | 1.2M | 1000 | CNN benchmarking |\n| COCO | 330K | 80 | Object detection |\n| Chest X-ray | 112K | 14 | Medical imaging |"),
    md("## HuggingFace Quick Start\n\n```python\n# Run on Kaggle/Colab — zero training needed\nfrom transformers import pipeline\nclassifier = pipeline('image-classification',\n                       model='google/vit-base-patch16-224')\nresult = classifier('my_image.jpg')\nprint(result)  # [{'label': 'tabby cat', 'score': 0.97}]\n```\n\n**Visit:** huggingface.co/models → filter by `image-classification`"),
    md("---\n**Your turn:** Visit [kaggle.com/code](https://kaggle.com/code), create a notebook with GPU, and run a ResNet50 on CIFAR-10."),
))

# ─────────────────────────────────────────────────────────────────────────────
# DL-03: RNNs & LSTMs — Stock Price Trend
# ─────────────────────────────────────────────────────────────────────────────
save("dl-03-rnn-lstm-stock", nb(
    md("# RNNs & LSTMs — Stock Price Trend Prediction\n\nSequential models that learn from temporal patterns."),
    py("import micropip\nawait micropip.install(['scikit-learn','matplotlib','numpy'])\nprint('Ready!')"),
    md("## Why RNNs?\n\nStandard networks are memoryless — each input is processed independently.\nRNNs maintain **hidden state** — memory of past inputs.\n\n```\nRNN:  h(t) = tanh(Wh · h(t-1) + Wx · x(t))\nLSTM: adds 3 gates (forget, input, output) — solves vanishing gradient\nGRU:  2 gates, fewer parameters, often as good as LSTM\n```"),
    py("""import numpy as np, matplotlib.pyplot as plt
np.random.seed(42)
t = np.arange(500)
price = 100 + 0.08*t + 15*np.sin(2*np.pi*t/52) + np.random.randn(500)*5
plt.figure(figsize=(12,4))
plt.plot(price,color='#6b21a8',lw=0.8)
plt.xlabel('Trading Days'); plt.ylabel('Price ($)')
plt.title('Simulated Stock: Trend + Seasonality + Noise')
plt.grid(alpha=0.3); plt.show()"""),
    md("## Sliding Window Features"),
    py("""def make_sequences(series, window=20):
    X,y = [],[]
    for i in range(window,len(series)):
        X.append(series[i-window:i])
        y.append(series[i])
    return np.array(X), np.array(y)

window=20; X,y = make_sequences(price,window)
X_n=(X-X.mean())/X.std(); y_n=(y-y.mean())/y.std()
split=int(len(X)*0.8)
X_tr,X_te = X_n[:split], X_n[split:]
y_tr,y_te = y_n[:split], y_n[split:]
print(f"Each sample: {window} days of history → predict next day")
print(f"Train: {X_tr.shape}  |  Test: {X_te.shape}")"""),
    md("## Train & Evaluate"),
    py("""from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_percentage_error
mlp = MLPRegressor(hidden_layer_sizes=(128,64),activation='relu',max_iter=1000,random_state=42)
mlp.fit(X_tr,y_tr)
y_pred = mlp.predict(X_te)
y_test_d = y_te*y.std()+y.mean(); y_pred_d = y_pred*y.std()+y.mean()
mape = mean_absolute_percentage_error(y_test_d,y_pred_d)*100
print(f"MAPE: {mape:.2f}%")
plt.figure(figsize=(12,4))
plt.plot(y_test_d[:100],label='Actual',color='#059669')
plt.plot(y_pred_d[:100],label='Predicted',color='#6b21a8',alpha=0.7)
plt.legend(); plt.title('Actual vs Predicted (first 100 test days)')
plt.grid(alpha=0.3); plt.show()"""),
    md("## Full LSTM (PyTorch — Kaggle GPU)\n\n```python\nimport torch, torch.nn as nn\n\nclass StockLSTM(nn.Module):\n    def __init__(self, hidden=64, layers=2):\n        super().__init__()\n        self.lstm = nn.LSTM(1, hidden, layers, batch_first=True, dropout=0.2)\n        self.fc   = nn.Linear(hidden, 1)\n    def forward(self, x):\n        out, _ = self.lstm(x)         # (batch, seq, hidden)\n        return self.fc(out[:, -1, :]) # last timestep\n\nmodel = StockLSTM()\noptimizer = torch.optim.Adam(model.parameters(), lr=0.001)\ncriterion = nn.MSELoss()\n```"),
    md("## GRU vs LSTM\n\n| | LSTM | GRU |\n|---|---|---|\n| Gates | 3 | 2 |\n| Params | More | ~33% fewer |\n| Speed | Slower | Faster |\n| Performance | Often similar | Comparable |\n\n**Rule:** Try GRU first. Use LSTM if sequences are very long (>200 steps)."),
    md("---\n**Your turn:** Change `window=5` and `window=60`. How does MAPE change with shorter vs longer history?"),
))

# ─────────────────────────────────────────────────────────────────────────────
# DL-04: Autoencoders & GANs — MNIST Compression + Face Generation
# ─────────────────────────────────────────────────────────────────────────────
save("dl-04-autoencoders-gans", nb(
    md("# Autoencoders & GANs\nMNIST Image Compression + Face Generation Concepts"),
    py("import micropip\nawait micropip.install(['scikit-learn','matplotlib','numpy'])\nprint('Ready!')"),
    md("## Autoencoder Architecture\n\n```\nInput → Encoder → Latent Code (bottleneck) → Decoder → Reconstruction\n  64       32→16         16 dims              16→32        64\n```\n\n**Uses:** Compression, denoising, anomaly detection, feature learning"),
    py("""import numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
digits = load_digits()
X = digits.data / 16.0
X_train,X_test = train_test_split(X,test_size=0.2,random_state=42)
print(f"Original: {X.shape[1]} dims | Bottleneck: 16 dims | Compression: 4x")"""),
    py("""ae = MLPRegressor(hidden_layer_sizes=(32,16,32),activation='relu',max_iter=500,random_state=42)
ae.fit(X_train,X_train)  # target = input
X_rec = ae.predict(X_test)
from sklearn.metrics import mean_squared_error
print(f"Reconstruction MSE: {mean_squared_error(X_test,X_rec):.4f}")
fig,axes = plt.subplots(2,10,figsize=(14,3))
for i in range(10):
    axes[0,i].imshow(X_test[i].reshape(8,8),cmap='gray'); axes[0,i].axis('off')
    axes[1,i].imshow(X_rec[i].reshape(8,8),cmap='gray');  axes[1,i].axis('off')
axes[0,0].set_ylabel('Original'); axes[1,0].set_ylabel('Reconstructed')
plt.suptitle('Autoencoder: Original vs Reconstructed'); plt.tight_layout(); plt.show()"""),
    md("## Denoising Autoencoder"),
    py("""noise = 0.3
X_noisy_tr = np.clip(X_train + noise*np.random.randn(*X_train.shape),0,1)
X_noisy_te = np.clip(X_test  + noise*np.random.randn(*X_test.shape),0,1)
denoiser = MLPRegressor(hidden_layer_sizes=(32,16,32),activation='relu',max_iter=500,random_state=42)
denoiser.fit(X_noisy_tr,X_train)
X_clean = denoiser.predict(X_noisy_te)
fig,axes = plt.subplots(3,8,figsize=(14,5))
for i in range(8):
    axes[0,i].imshow(X_test[i].reshape(8,8),cmap='gray');    axes[0,i].axis('off')
    axes[1,i].imshow(X_noisy_te[i].reshape(8,8),cmap='gray');axes[1,i].axis('off')
    axes[2,i].imshow(X_clean[i].reshape(8,8),cmap='gray');   axes[2,i].axis('off')
for label,ax in zip(['Clean','Noisy','Denoised'],axes[:,0]): ax.set_ylabel(label)
plt.suptitle('Denoising Autoencoder'); plt.tight_layout(); plt.show()"""),
    md("## GAN — Generator + Discriminator\n\nTwo networks competing:\n- **Generator (G):** Creates fake images from random noise z ~ N(0,1)\n- **Discriminator (D):** Classifies real vs fake\n\nTraining objective: G tries to fool D; D tries not to be fooled.\n\n```python\n# DCGAN for face generation (PyTorch — CelebA on Kaggle)\nclass Generator(nn.Module):\n    def __init__(self, z_dim=100):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.ConvTranspose2d(z_dim, 512, 4, 1, 0),  # 4x4\n            nn.BatchNorm2d(512), nn.ReLU(),\n            nn.ConvTranspose2d(512, 256, 4, 2, 1),    # 8x8\n            nn.BatchNorm2d(256), nn.ReLU(),\n            nn.ConvTranspose2d(256, 3, 4, 2, 1),      # 16x16 RGB\n            nn.Tanh()\n        )\n    def forward(self, z):\n        return self.net(z.view(-1, 100, 1, 1))\n```\n\n**Dataset for face generation:** CelebA (202K celebrity faces) on Kaggle."),
    md("## VAE vs GAN\n\n| | Autoencoder | VAE | GAN |\n|---|---|---|---|\n| Purpose | Compression | Smooth latent space | Realistic synthesis |\n| Training | MSE loss | ELBO | Adversarial |\n| Use | Anomaly detection | Drug discovery | Image/video gen |"),
    md("---\n**Your turn:** Increase noise to 0.5 and retrain. Can the denoiser still recover clean digits?"),
))

# ─────────────────────────────────────────────────────────────────────────────
# DL-05: Transformers — Sentiment + Summarisation
# ─────────────────────────────────────────────────────────────────────────────
save("dl-05-transformers-nlp", nb(
    md("# Transformers — Sentiment Analysis & Text Summarisation\n\nThe architecture behind GPT, BERT, Claude, and every modern LLM."),
    py("import micropip\nawait micropip.install(['scikit-learn','matplotlib','numpy'])\nprint('Ready!')"),
    md("## Self-Attention Intuition\n\nEvery token attends to every other token:\n```\nAttention(Q,K,V) = softmax(QK^T / sqrt(d_k)) * V\n```\n'Bank' in 'river bank' vs 'bank account' — context changes meaning.\nTransformers capture this via attention over the full sequence."),
    py("""import numpy as np, matplotlib.pyplot as plt
words = ['The','model','attended','to','every','word','context']
n = len(words)
np.random.seed(42)
attn = np.random.dirichlet(np.ones(n),size=n)
attn = (attn+attn.T)/2
plt.figure(figsize=(7,6))
plt.imshow(attn,cmap='Purples'); plt.colorbar()
plt.xticks(range(n),words,rotation=45,ha='right')
plt.yticks(range(n),words)
plt.title('Self-Attention Weights (simulated)'); plt.tight_layout(); plt.show()"""),
    md("## Sentiment Analysis (TF-IDF baseline)"),
    py("""from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
reviews = [
    "This movie was absolutely fantastic! Great acting.",
    "Terrible film. Complete waste of time. Very disappointed.",
    "An incredible journey. Moved me to tears. Must watch!",
    "Boring and predictable. Fell asleep halfway through.",
    "Brilliant performances. Gripping from start to finish.",
    "Awful script. Poor characters. Worst film I have seen.",
    "Heartwarming and beautiful. A modern masterpiece.",
    "Dreadful. Plot made no sense. Acting was wooden.",
    "Outstanding! Best film of the decade. Highly recommend.",
    "Disappointing. Had high hopes but execution was poor.",
]
labels = [1,0,1,0,1,0,1,0,1,0]
X_tr,X_te,y_tr,y_te = train_test_split(reviews,labels,test_size=0.3,random_state=42)
vec = TfidfVectorizer(ngram_range=(1,2))
clf = LogisticRegression().fit(vec.fit_transform(X_tr),y_tr)
print(classification_report(y_te,clf.predict(vec.transform(X_te)),target_names=['Neg','Pos']))"""),
    md("## HuggingFace Sentiment (Kaggle/Colab)\n\n```python\nfrom transformers import pipeline\nsentiment = pipeline('sentiment-analysis',\n    model='distilbert-base-uncased-finetuned-sst-2-english')\nresults = sentiment(['This course is amazing!', 'I wasted my money.'])\nfor r in results:\n    print(r)  # {'label': 'POSITIVE', 'score': 0.99}\n```"),
    md("## Extractive Summarisation"),
    py("""from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
def summarise(text, n=3):
    sents = [s.strip() for s in text.split('.') if len(s.strip())>20]
    if len(sents)<=n: return text
    mat = TfidfVectorizer(stop_words='english').fit_transform(sents)
    scores = mat.sum(axis=1).A1
    top = sorted(np.argsort(scores)[-n:])
    return '. '.join(sents[i] for i in top) + '.'
article = (
    "Machine learning enables systems to learn from data. "
    "Deep learning uses many layers to learn hierarchical representations. "
    "Transformers have revolutionised NLP since 2017. "
    "The attention mechanism allows models to focus on relevant parts. "
    "BERT and GPT are pre-trained models achieving state-of-the-art results. "
    "Transfer learning enables fine-tuning on specific tasks with limited data."
)
print("Original:", len(article.split()), "words")
summary = summarise(article, 2)
print("Summary: ", len(summary.split()), "words")
print(summary)"""),
    md("## BERT vs GPT vs T5\n\n| Model | Type | Best for |\n|---|---|---|\n| BERT | Encoder | Classification, NER, Q&A |\n| GPT | Decoder | Text generation |\n| T5 | Encoder-Decoder | Translation, summarisation |\n| DistilBERT | Encoder | Fast inference, mobile |\n| RoBERTa | Encoder | Better BERT training |"),
    md("---\n**Your turn:** Change `n=2` in the summariser. Does removing one sentence hurt quality?\n\n**HuggingFace:** huggingface.co/spaces — try 'summarization' demos live."),
))

# ─────────────────────────────────────────────────────────────────────────────
# DL-06: Multimodal — Image Captioning + Visual Q&A
# ─────────────────────────────────────────────────────────────────────────────
save("dl-06-multimodal", nb(
    md("# Multimodal AI — Image Captioning & Visual Q&A\n\nModels that process images and text simultaneously."),
    py("import micropip\nawait micropip.install(['scikit-learn','matplotlib','numpy'])\nprint('Ready!')"),
    md("## Key Multimodal Models\n\n| Model | Type | Use |\n|---|---|---|\n| CLIP (OpenAI) | Image+Text Encoder | Zero-shot image search |\n| DALL-E 3 | Text→Image | Image generation |\n| LLaVA | Visual Chat | Image Q&A |\n| GPT-4V | Visual Chat | Complex visual understanding |\n| BLIP-2 | VQA + Captioning | Image captioning, VQA |\n| Gemini | Native multimodal | Video, audio, image, text |"),
    py("""import numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Image classification (digit = simulated object category)
digits = load_digits()
X = digits.data / 16.0; y = digits.target
X_tr,X_te,y_tr,y_te = train_test_split(X,y,test_size=0.2,random_state=42)
clf = MLPClassifier(hidden_layer_sizes=(256,128),max_iter=500,random_state=42)
clf.fit(X_tr,y_tr)
print(f"Image classification accuracy: {accuracy_score(y_te,clf.predict(X_te)):.3f}")"""),
    md("## Image Captioning — BLIP (Kaggle/Colab)\n\n```python\nfrom transformers import BlipProcessor, BlipForConditionalGeneration\nfrom PIL import Image\n\nprocessor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')\nmodel = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')\n\nimage = Image.open('cat.jpg')\ninputs = processor(image, return_tensors='pt')\nout = model.generate(**inputs, max_new_tokens=50)\nprint(processor.decode(out[0], skip_special_tokens=True))\n# Output: 'a tabby cat sitting on a wooden table'\n```"),
    md("## Visual Q&A — BLIP (Kaggle/Colab)\n\n```python\nfrom transformers import BlipProcessor, BlipForQuestionAnswering\n\nprocessor = BlipProcessor.from_pretrained('Salesforce/blip-vqa-base')\nmodel = BlipForQuestionAnswering.from_pretrained('Salesforce/blip-vqa-base')\n\nimage = Image.open('dog.jpg')\nfor question in ['What colour is the dog?', 'Is it indoors or outdoors?']:\n    inputs = processor(image, question, return_tensors='pt')\n    out = model.generate(**inputs)\n    answer = processor.decode(out[0], skip_special_tokens=True)\n    print(f'Q: {question}  ->  A: {answer}')\n```"),
    md("## CLIP Zero-Shot Classification (Kaggle/Colab)\n\n```python\nfrom transformers import CLIPProcessor, CLIPModel\nimport torch\n\nmodel = CLIPModel.from_pretrained('openai/clip-vit-base-patch32')\nprocessor = CLIPProcessor.from_pretrained('openai/clip-vit-base-patch32')\n\nimage = Image.open('animal.jpg')\nlabels = ['a cat', 'a dog', 'a bird', 'a fish']\ninputs = processor(text=labels, images=image, return_tensors='pt', padding=True)\nwith torch.no_grad():\n    probs = model(**inputs).logits_per_image.softmax(dim=1)[0]\nfor label, prob in zip(labels, probs):\n    print(f'{label}: {prob:.1%}')\n# No fine-tuning needed! CLIP works zero-shot.\n```"),
    py("""# Multimodal datasets reference
datasets = {
    'COCO Captions': '330K images + 5 captions each. Best for captioning.',
    'VQA v2': '1.1M visual questions and answers.',
    'Flickr30k': '31K images + 5 captions. Lighter alternative to COCO.',
    'CelebA': '202K celebrity face images. For GAN/face generation.',
    'Fashion Product': 'E-commerce images + product descriptions.',
}
print("Top multimodal datasets (all on Kaggle):")
for name, desc in datasets.items():
    print(f"  {name}: {desc}")"""),
    md("---\n**Your turn:** Visit [huggingface.co/spaces](https://huggingface.co/spaces) and search 'image captioning' — try it on your own photo."),
))

# ─────────────────────────────────────────────────────────────────────────────
# DL-07: Transfer Learning — Dog Breed Classifier with ResNet50
# ─────────────────────────────────────────────────────────────────────────────
save("dl-07-transfer-learning", nb(
    md("# Transfer Learning — Dog Breed Classifier with ResNet50\n\nUse a model trained on 1.2M images to classify 120 dog breeds — with minimal data."),
    py("import micropip\nawait micropip.install(['scikit-learn','matplotlib','numpy'])\nprint('Ready!')"),
    md("## Why Transfer Learning?\n\nTraining ResNet50 from scratch requires:\n- 1.2M+ labelled images\n- Days of GPU compute\n\nTransfer learning reuses learned weights:\n- **Feature extraction:** freeze all layers, train only final classifier\n- **Fine-tuning:** unfreeze some layers, low learning rate\n\n| Strategy | Data needed | Time | Accuracy |\n|---|---|---|---|\n| From scratch | 100K+ | Hours | ~70% |\n| Feature extraction | 1K+ | Minutes | ~85% |\n| Fine-tuning (partial) | 5K+ | 30 min | ~92% |"),
    md("## ResNet50 Architecture\n\nKey innovation: **Skip connections** (residual blocks)\n\n```\nx → Conv → BN → ReLU → Conv → BN → (+x) → ReLU\n    ↑________________________________↑  skip!\n```\n\nWithout skip connections, training 50+ layer networks was nearly impossible.\nSkip connections provide a gradient highway — solving vanishing gradients.\n\n```\nStage 1: Conv 7x7, stride 2   (112x112)\nStage 2: 3 residual blocks    (56x56)\nStage 3: 4 residual blocks    (28x28)\nStage 4: 6 residual blocks    (14x14)\nStage 5: 3 residual blocks    (7x7)\nGlobal Average Pool → 2048 features\nFC → 1000 classes (ImageNet)\n```"),
    py("""# Simulate transfer learning on digit recognition
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

digits = load_digits()
X = digits.data/16.0; y = digits.target
X_tr,X_te,y_tr,y_te = train_test_split(X,y,test_size=0.2,random_state=42)

# 'Pre-trained' model on large dataset
pretrained = MLPClassifier(hidden_layer_sizes=(256,128),max_iter=500,random_state=42)
pretrained.fit(X_tr,y_tr)
print(f"Full dataset accuracy: {accuracy_score(y_te,pretrained.predict(X_te)):.3f}")

# Transfer scenario: only 10% of data available
X_small,_,y_small,_ = train_test_split(X_tr,y_tr,test_size=0.9,random_state=42)
from_scratch = MLPClassifier(hidden_layer_sizes=(256,128),max_iter=500,random_state=42)
from_scratch.fit(X_small,y_small)
print(f"From scratch (10% data): {accuracy_score(y_te,from_scratch.predict(X_te)):.3f}")
print(f"Transfer simulated gain: use pretrained features → ~{accuracy_score(y_te,pretrained.predict(X_te)):.3f}")"""),
    md("## PyTorch Transfer Learning (Kaggle GPU)\n\n```python\nimport torchvision.models as models\nimport torch.nn as nn\n\n# Load ResNet50 pre-trained on ImageNet\nmodel = models.resnet50(weights='IMAGENET1K_V2')\n\n# Freeze all layers\nfor param in model.parameters():\n    param.requires_grad = False\n\n# Replace head: 2048 -> 120 dog breeds\nmodel.fc = nn.Sequential(\n    nn.Dropout(0.3),\n    nn.Linear(2048, 120)\n)\n\n# Only the new head trains\noptimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)\n```\n\n**Dataset:** Stanford Dogs (20K images, 120 breeds) on Kaggle."),
    py("""# Popular pre-trained models
models = [
    ('ResNet-50',      '25M',  'Excellent baseline, easy to fine-tune'),
    ('EfficientNet-B0','5M',   'Best accuracy/size, recommended first choice'),
    ('VGG-16',         '138M', 'Simple architecture, easy to understand'),
    ('MobileNetV2',    '3.4M', 'Designed for mobile/edge devices'),
    ('ViT-B/16',       '86M',  'Vision Transformer — state of the art'),
]
print(f"{'Model':<18}|{'Params':<8}|Notes")
print("-"*60)
for m in models:
    print(f"{m[0]:<18}|{m[1]:<8}|{m[2]}")"""),
    md("## Fine-Tuning Strategy\n\n1. **Phase 1 (5 epochs):** Freeze all, train head only — lr=0.001\n2. **Phase 2 (10 epochs):** Unfreeze last block — lr=0.00001\n3. **Phase 3 (optional):** Unfreeze all — lr=0.000001\n\n**Never** unfreeze early layers with high learning rate — causes catastrophic forgetting."),
    md("---\n**Your turn:** What happens if you unfreeze ALL layers with lr=0.001? Research 'catastrophic forgetting'."),
))

# ─────────────────────────────────────────────────────────────────────────────
# DL-08: Model Compression — Pruning & Quantisation
# ─────────────────────────────────────────────────────────────────────────────
save("dl-08-model-compression", nb(
    md("# Model Compression — Pruning & Quantisation\n\nMake models smaller and faster for mobile/edge deployment."),
    py("import micropip\nawait micropip.install(['scikit-learn','matplotlib','numpy'])\nprint('Ready!')"),
    md("## Why Compress?\n\n| Challenge | Without | With |\n|---|---|---|\n| Model size | ResNet50=97MB | MobileNetV2=14MB |\n| Inference time | 100ms CPU | 10ms CPU |\n| Mobile RAM | Won't fit | Fits |\n\n**Techniques:** Pruning, Quantisation, Knowledge Distillation, Architecture Search"),
    py("""import numpy as np, matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = load_breast_cancer()
X_tr,X_te,y_tr,y_te = train_test_split(data.data,data.target,test_size=0.2,random_state=42)
ns = [100,50,25,10,5,2,1]
accs = []
for n in ns:
    rf = RandomForestClassifier(n_estimators=n,random_state=42)
    rf.fit(X_tr,y_tr); accs.append(accuracy_score(y_te,rf.predict(X_te)))
plt.plot(ns,accs,'o-',color='#6b21a8',lw=2)
plt.xlabel('Trees (model size proxy)'); plt.ylabel('Accuracy')
plt.title('Pruning: Model Size vs Accuracy Trade-off')
plt.grid(alpha=0.3); plt.show()
for n,a in zip(ns,accs): print(f"  {n:<4} trees: {a:.3f}")"""),
    md("## Quantisation\n\nReduce weight precision: float32 → int8\n\n```\nfloat32: 32 bits per weight  (0.347821...)\nint8:    8 bits per weight   (89, mapped to -128..127)\n\n4x smaller model  +  2-4x faster inference  +  ~1% accuracy loss\n\n# PyTorch dynamic quantisation:\nmodel_int8 = torch.quantization.quantize_dynamic(\n    model,\n    {torch.nn.Linear},\n    dtype=torch.qint8\n)\n```"),
    md("## Knowledge Distillation\n\nTrain a **small student** to mimic a **large teacher**:\n\n```\nTeacher (ResNet50, 25M params)  →  Student (MobileNet, 3.4M params)\n         Soft probability outputs       Learn from teacher, not hard labels\n```"),
    py("""from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
data = load_breast_cancer()
X_tr,X_te,y_tr,y_te = train_test_split(data.data,data.target,test_size=0.2,random_state=42)

# Teacher: large model
teacher = MLPClassifier(hidden_layer_sizes=(256,128,64),max_iter=500,random_state=42)
teacher.fit(X_tr,y_tr)
teacher_acc = accuracy_score(y_te,teacher.predict(X_te))

# Student without distillation
student = MLPClassifier(hidden_layer_sizes=(32,),max_iter=500,random_state=42)
student.fit(X_tr,y_tr)
student_acc = accuracy_score(y_te,student.predict(X_te))

# Student with distillation: train on teacher's soft probabilities
soft_targets = teacher.predict_proba(X_tr)[:,1]
distilled = MLPClassifier(hidden_layer_sizes=(32,),max_iter=1000,random_state=42)
distilled.fit(X_tr, soft_targets)
distilled_acc = accuracy_score(y_te,(distilled.predict(X_te)>0.5).astype(int))

print(f"Teacher (large):       {teacher_acc:.3f}")
print(f"Student (no distil):   {student_acc:.3f}")
print(f"Student (distilled):   {distilled_acc:.3f}  <- recovered {distilled_acc-student_acc:.3f}")"""),
    md("## Compression Summary\n\n| Technique | Speedup | Accuracy loss |\n|---|---|---|\n| Pruning | 1.5-3x | <1% |\n| Quantisation (int8) | 2-4x | ~1% |\n| Knowledge Distillation | 5-10x | ~2-3% |\n| MobileNet architecture | 5-10x | ~2-5% |\n| Neural Architecture Search | varies | varies |"),
    md("---\n**Your turn:** Change student to `(64,32)`. Does distillation still outperform no-distillation?"),
))

print(f"\nDone. DL notebooks: {len([f for f in os.listdir('notebooks') if f.startswith('dl-')])}")
