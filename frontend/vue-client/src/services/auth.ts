import axios from 'axios';

// FORCE LOCALHOST during development to ensure we hit the code we are actually editing.
// If you want to use Render, you would set this in your .env file, but for now we want local.
const API_BASE_URL = 'http://localhost:8000';

console.log('AUTH_SERVICE_LOADED: Developing against LOCAL backend at', API_BASE_URL);

/**
 * Helper to safely extract the username from the JWT access token payload.
 */
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

/**
 * Main axios instance for authenticated API calls.
 */
const api = axios.create({
  baseURL: API_BASE_URL.endsWith('/') ? API_BASE_URL : `${API_BASE_URL}/`,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

console.log('API_TRACE: Axios baseURL is', api.defaults.baseURL);

// Inject Bearer token into every request if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  // Diagnostic log for tracking network routing
  console.log(`API_TRACE: ${config.method?.toUpperCase()} ${config.baseURL}${config.url}`);
  return config;
});

// Handle global response errors
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
          }, { timeout: 10000 });

          const { access } = response.data;
          localStorage.setItem('access_token', access);

          originalRequest.headers.Authorization = `Bearer ${access}`;
          return api(originalRequest);
        }
      } catch (refreshError) {
        localStorage.clear();
        window.location.href = '/login';
      }
    }

    return Promise.reject(error);
  }
);

export const authService = {
  async login(username: string, password: string) {
    try {
      console.log('LOGIN_ATTEMPT: Starting...', { username, url: `${API_BASE_URL}/account/api/token//` });

      const response = await axios.post(`${API_BASE_URL}/account/api/token/`, {
        username,
        password,
      }, { timeout: 12000 });

      console.log('LOGIN_SUCCESS: Response received', response.status);

      const { access, refresh, username: loggedUsername, email, id } = response.data;
      const finalUsername = (typeof loggedUsername === 'string' && loggedUsername.trim() !== '') ? loggedUsername : username;

      localStorage.setItem('access_token', access);
      localStorage.setItem('refresh_token', refresh);
      localStorage.setItem('user_info', JSON.stringify({
        username: finalUsername,
        email,
        id
      }));

      return response.data;
    } catch (error: any) {
      console.error('LOGIN_ERROR:', error.message);
      throw error;
    }
  },

  async register(username: string, email: string, password: string, password2: string) {
    const response = await axios.post(`${API_BASE_URL}/account/api/register/`, {
      username,
      email,
      password,
      password2,
    }, { timeout: 15000 });

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
        if (!parsed.username) {
          const tokenUsername = getUsernameFromToken();
          if (tokenUsername) parsed.username = tokenUsername;
        }
        return parsed;
      } catch { }
    }
    const tokenUsername = getUsernameFromToken();
    if (tokenUsername) return { username: tokenUsername };
    return null;
  },

  getCurrentUser() {
    return api.get('account/api/user/me/');
  },
};

export default api;
