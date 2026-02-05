const API_URL = import.meta.env.PUBLIC_API_URL || 'http://127.0.0.1:8000';

export async function register(vet: any) {
  const res = await fetch(`${API_URL}/veterinarias/registro`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(vet),
  });
  return res;
}

export async function login(username: string, password: string) {
  const params = new URLSearchParams();
  params.append('username', username);
  params.append('password', password);
  const res = await fetch(`${API_URL}/veterinarias/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: params.toString(),
  });
  if (res.ok) {
    const data = await res.json();
    localStorage.setItem('token', data.access_token);
    return data;
  }
  throw new Error('Login failed');
}

export function getToken() {
  return localStorage.getItem('token');
}

export function logout() {
  localStorage.removeItem('token');
  localStorage.removeItem('vet_name');
}
