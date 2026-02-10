import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

// Helper to safely extract the username from the JWT access token
const getUsernameFromToken = (): string | null => {
  try {
    const token = localStorage.getItem('access_token');
    if (!token) return null;

    const parts = token.split('.');
    if (parts.length !== 3) return null;

    const payload = JSON.parse(atob(parts[1]));
    if (typeof payload?.username === 'string' && payload.username.trim() !== '') {
      return payload.username;
    }

    return null;
  } catch {
    return null;
  }
};

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem('refresh_token');
        if (refreshToken) {
          const response = await axios.post(`${API_BASE_URL}/account/api/token/refresh/`, {
            refresh: refreshToken,
          });

          const { access } = response.data;
          localStorage.setItem('access_token', access);

          originalRequest.headers.Authorization = `Bearer ${access}`;
          return api(originalRequest);
        }
      } catch (refreshError) {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        window.location.href = '/login';
      }
    }

    return Promise.reject(error);
  }
);

export const authService = {
  async login(username: string, password: string) {
    try {
      console.log('Attempting login with:', { username, password: '***' });
      const response = await axios.post(`${API_BASE_URL}/account/api/token/`, {
        username,
        password,
      });

      console.log('Login response:', response.data);

      const { access, refresh, username: loggedUsername, email, id } = response.data;

      // Always persist a username, even if backend didn't include it explicitly
      const finalUsername =
        (typeof loggedUsername === 'string' && loggedUsername.trim() !== '')
          ? loggedUsername
          : username;

      localStorage.setItem('access_token', access);
      localStorage.setItem('refresh_token', refresh);
      localStorage.setItem('user_info', JSON.stringify({
        username: finalUsername,
        email,
        id
      }));

      return response.data;
    } catch (error: any) {
      console.error('Login error:', error);
      console.error('Error response:', error.response?.data);
      throw error;
    }
  },

  async register(username: string, email: string, password: string, password2: string) {
    const response = await axios.post(`${API_BASE_URL}/account/api/register/`, {
      username,
      email,
      password,
      password2,
    });

    return response.data;
  },

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_info');
  },

  isAuthenticated(): boolean {
    return !!localStorage.getItem('access_token');
  },

  getStoredUser() {
    const userInfo = localStorage.getItem('user_info');

    if (userInfo) {
      try {
        const parsed = JSON.parse(userInfo);

        // If username is missing in stored info, try to backfill it from token
        if (!parsed.username) {
          const tokenUsername = getUsernameFromToken();
          if (tokenUsername) {
            parsed.username = tokenUsername;
          }
        }

        return parsed;
      } catch {
        // If parsing fails, fall back to token
      }
    }

    // If we don't have valid stored user info, derive a minimal user from the token
    const tokenUsername = getUsernameFromToken();
    if (tokenUsername) {
      return { username: tokenUsername };
    }

    return null;
  },

  getCurrentUser() {
    return api.get('/account/api/user/me/');
  },
};

export default api;
