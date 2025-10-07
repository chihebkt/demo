import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState('')
  const [timestamp, setTimestamp] = useState('')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

  useEffect(() => {
    fetchHelloMessage()
  }, [])

  const fetchHelloMessage = async () => {
    try {
      setLoading(true)
      setError(null)
      
      const response = await fetch(`${API_URL}/hello`)
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      setMessage(data.message)
      setTimestamp(new Date(data.timestamp).toLocaleString())
    } catch (err) {
      console.error('Error fetching hello message:', err)
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>🌍 Hello World App</h1>
        
        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>Loading...</p>
          </div>
        )}
        
        {error && (
          <div className="error">
            <p>❌ Error: {error}</p>
            <button onClick={fetchHelloMessage} className="retry-button">
              🔄 Retry
            </button>
          </div>
        )}
        
        {!loading && !error && (
          <div className="message-container">
            <div className="message">
              <h2>{message}</h2>
              <p className="timestamp">
                <span className="label">Timestamp:</span> {timestamp}
              </p>
            </div>
            <button onClick={fetchHelloMessage} className="refresh-button">
              🔄 Refresh
            </button>
          </div>
        )}

        <div className="info">
          <p>React + FastAPI Hello World</p>
          <p className="small">Backend API: {API_URL}</p>
        </div>
      </header>
    </div>
  )
}

export default App
