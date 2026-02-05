import { getToken } from './auth';

function authHeaders() {
  const token = getToken();
  return token ? { Authorization: `Bearer ${token}` } : {};
}

export async function fetchClientes() {
  const res = await fetch('http://127.0.0.1:8000/clientes', {
    headers: { ...authHeaders(), 'Content-Type': 'application/json' },
  });
  if (!res.ok) throw new Error('Error fetching clientes');
  return res.json();
}

export async function createCliente(cliente: any) {
  const res = await fetch('http://127.0.0.1:8000/clientes', {
    method: 'POST',
    headers: { ...authHeaders(), 'Content-Type': 'application/json' },
    body: JSON.stringify(cliente),
  });
  if (!res.ok) throw new Error('Error creating cliente');
  return res.json();
}

export async function updateCliente(id: number, cliente: any) {
  const res = await fetch(`http://127.0.0.1:8000/clientes/${id}`, {
    method: 'PUT',
    headers: { ...authHeaders(), 'Content-Type': 'application/json' },
    body: JSON.stringify(cliente),
  });
  if (!res.ok) throw new Error('Error updating cliente');
  return res.json();
}

export async function deleteCliente(id: number) {
  const res = await fetch(`http://127.0.0.1:8000/clientes/${id}`, {
    method: 'DELETE',
    headers: { ...authHeaders(), 'Content-Type': 'application/json' },
  });
  if (!res.ok) throw new Error('Error deleting cliente');
  return res.json();
}
