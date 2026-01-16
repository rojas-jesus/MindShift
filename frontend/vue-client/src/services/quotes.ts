import axios from 'axios'

const QUOTES_API_BASE = 'https://zenquotes.io/api'

export interface Quote {
  q: string      // Quote text
  a: string      // Author
  h: string      // HTML formatted quote
}

export interface QuoteResponse {
  quotes: Quote[]
}

export const quotesService = {
  async getRandomQuote(): Promise<Quote> {
    try {
      const response = await axios.get(`${QUOTES_API_BASE}/random`)
      return response.data[0] // Returns single quote in array
    } catch (error) {
      console.error('Error fetching random quote:', error)
      // Fallback quote
      return {
        q: "The only way to do great work is to love what you do.",
        a: "Steve Jobs",
        h: "<blockquote>\"The only way to do great work is to love what you do.\" — <footer>Steve Jobs</footer></blockquote>"
      }
    }
  },

  async getTodayQuote(): Promise<Quote> {
    try {
      const response = await axios.get(`${QUOTES_API_BASE}/today`)
      return response.data[0]
    } catch (error) {
      console.error('Error fetching today quote:', error)
      // Fallback quote
      return {
        q: "Every moment is a fresh beginning.",
        a: "T.S. Eliot",
        h: "<blockquote>\"Every moment is a fresh beginning.\" — <footer>T.S. Eliot</footer></blockquote>"
      }
    }
  },

  async getMultipleQuotes(count: number = 5): Promise<Quote[]> {
    try {
      const response = await axios.get(`${QUOTES_API_BASE}/quotes`)
      return response.data.slice(0, count)
    } catch (error) {
      console.error('Error fetching multiple quotes:', error)
      // Fallback quotes
      return [
        {
          q: "The only way to do great work is to love what you do.",
          a: "Steve Jobs",
          h: "<blockquote>\"The only way to do great work is to love what you do.\" — <footer>Steve Jobs</footer></blockquote>"
        },
        {
          q: "Every moment is a fresh beginning.",
          a: "T.S. Eliot",
          h: "<blockquote>\"Every moment is a fresh beginning.\" — <footer>T.S. Eliot</footer></blockquote>"
        }
      ]
    }
  }
}
