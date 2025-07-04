
  # 🧠 EmotionDetect - Detecção de Emoções com Transformers


> Um projeto simples e poderoso que utiliza modelos **Transformers** para identificar emoções em textos com **Python**. Ideal para experimentos em **NLP**, análise de sentimentos, chatbots, entre outros.

---

## 🚀 Sobre o Projeto

O **EmotionDetect** é um projeto de NLP que classifica emoções humanas com base em texto natural. Usando o poder de modelos pré-treinados como os da biblioteca 🤗 **Transformers**, o sistema é capaz de identificar emoções como:

- 😄 Positividade (`joy`)
- 😠 Negatividade (`anger`)

Este projeto pode ser integrado em aplicativos, assistentes virtuais, redes sociais e muito mais.

---

## 🛠️ Tecnologias Usadas

- Python 🐍
- Transformers (HuggingFace) 🤗
- PyTorch ou TensorFlow (como dependência da importação do modelo)
- FastAPI (opcional, para API REST)
- Jupyter Notebook (para testes e experimentos)

---

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/emotion-detect.git
cd emotion-detect
```

2. Crie uma venv

   ```bash
   python -m venv venv
   ```

3. instale os pacotes
   ```bash
   pip install -r requirements.txt
   ```
4. Rode o projeto
   ```python
   uvicorn app:app --port 4000 --host 0.0.0.0
   ```
