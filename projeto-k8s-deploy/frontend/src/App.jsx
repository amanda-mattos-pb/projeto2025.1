import { useEffect, useState } from 'react'

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000"

function App() {
  const [mensagens, setMensagens] = useState([])
  const [novaMensagem, setNovaMensagem] = useState("")

  const carregarMensagens = () => {
    fetch(`${API_URL}/api/mensagens`)
      .then(res => res.json())
      .then(setMensagens)
  }

  const enviarMensagem = () => {
    fetch(`${API_URL}/api/mensagens`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ texto: novaMensagem })
    }).then(() => {
      setNovaMensagem("")
      carregarMensagens()
    })
  }

  useEffect(() => {
    carregarMensagens()
  }, [])

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Sistema de Mensagens - IFPB</h1>

      <input
        className="border px-2 py-1 mr-2"
        value={novaMensagem}
        onChange={(e) => setNovaMensagem(e.target.value)}
        placeholder="Digite uma mensagem"
      />
      <button className="bg-blue-500 text-white px-4 py-1" onClick={enviarMensagem}>
        Enviar
      </button>

      <ul className="mt-4">
        {mensagens.map((m) => (
          <li key={m.id} className="mb-1 border-b">{m.texto}</li>
        ))}
      </ul>
    </div>
  )
}

export default App
