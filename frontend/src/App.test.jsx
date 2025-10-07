import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from './App'

// Mock fetch
global.fetch = vi.fn()

describe('App Component', () => {
  beforeEach(() => {
    fetch.mockClear()
  })

  it('renders hello world heading', () => {
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ 
        message: 'Hello, World!', 
        timestamp: '2024-01-01T00:00:00Z' 
      })
    })

    render(<App />)
    expect(screen.getByText(/Hello World App/i)).toBeInTheDocument()
  })

  it('displays loading state initially', () => {
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ 
        message: 'Hello, World!', 
        timestamp: '2024-01-01T00:00:00Z' 
      })
    })

    render(<App />)
    expect(screen.getByText(/Loading/i)).toBeInTheDocument()
  })

  it('fetches and displays message from API', async () => {
    const mockData = {
      message: 'Hello, World!',
      timestamp: '2024-01-01T12:00:00Z'
    }

    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockData
    })

    render(<App />)

    await waitFor(() => {
      expect(screen.getByText('Hello, World!')).toBeInTheDocument()
    })
  })

  it('displays error message when API call fails', async () => {
    fetch.mockRejectedValueOnce(new Error('Network error'))

    render(<App />)

    await waitFor(() => {
      expect(screen.getByText(/Error/i)).toBeInTheDocument()
    })
  })

  it('displays retry button on error', async () => {
    fetch.mockRejectedValueOnce(new Error('Network error'))

    render(<App />)

    await waitFor(() => {
      expect(screen.getByText(/Retry/i)).toBeInTheDocument()
    })
  })

  it('calls API again when refresh button is clicked', async () => {
    const mockData = {
      message: 'Hello, World!',
      timestamp: '2024-01-01T12:00:00Z'
    }

    fetch.mockResolvedValue({
      ok: true,
      json: async () => mockData
    })

    render(<App />)

    await waitFor(() => {
      expect(screen.getByText('Hello, World!')).toBeInTheDocument()
    })

    const refreshButton = screen.getByText(/Refresh/i)
    await userEvent.click(refreshButton)

    await waitFor(() => {
      expect(fetch).toHaveBeenCalledTimes(2)
    })
  })

  it('displays timestamp', async () => {
    const mockData = {
      message: 'Hello, World!',
      timestamp: '2024-01-01T12:00:00Z'
    }

    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockData
    })

    render(<App />)

    await waitFor(() => {
      expect(screen.getByText(/Timestamp:/i)).toBeInTheDocument()
    })
  })
})
