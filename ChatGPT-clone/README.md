# CHATGPT CLONE

A chatGPT clone hecho con Tyscript 

Inspirado en el chat de:  <a href="https://chat-gtp-clone.vercel.app/" target="_blank">Vercel App</a>

## How to run(?)

- Para correrlo tenemos que usar node (asegurarnos de que esté en una versión)
  ```bash
  node -v
  ```
  ```bash
    # OUTPUT: User versión v14.18.3 pero puede correr en cualquiera arriba de la mía
  ```
  
- Clona mi repo
  ```bash
  git clone https://github.com/innovatec-swe/API_ChatGPT.git
  ```
- Para correr el `backend/` folder
  ```bash
  cd API_ChatGPT
  cd ChatGPT-clone
  cd backend
  ```
  Carga las dependencias
  ```bash
  npm i
  ```
  Inicia el server
  ```bash
  npm run dev
  ```
  ```bash
  # Debe mostrar:
  Server running...
  ```
- Para correr en el server local ve a `frontend/` folder
  ```bash
  cd ../frontend
  ```
  Instala las dependencia
  ```bash
  npm i
  ```
  Y corre en el server 
  ```bash
  npm run dev
  ```
  ```bash
  #Output:

  VITE v4.0.3  ready in 375 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
  ```

## Tools
- Vite
- Typescript
- Open AI GPT-3 [`text-davinci-003`]
- Node JS
- Express

- Y así sale nuestra versión de Chat-GPT3 de cinco peso :') 
